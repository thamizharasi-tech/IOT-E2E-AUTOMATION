def test_positive_vacation_mode_sms_wakeup_r8p4s14(self):
    """
    Test Vacation Mode configuration with network outage recovery.
    Validates that vehicle handles mode updates correctly when experiencing disconnection.
    """

    # -----------------------------------------------------------
    # STEP 2: SET VEHICLE MODE PRECONDITIONS ON IVI
    # -----------------------------------------------------------
    print("\n================ STEP 2: SET VEHICLE MODE PRECONDITION ================\n")
    print("Setting Level-2 speed & vehicle mode preconditions on device...")
    run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")
    print("Vehicle mode precondition applied")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 3: RUN VEHICLE MODE A2A TEST
    # -----------------------------------------------------------
    print("\n================ STEP 3: RUN VEHICLE MODE A2A TEST ================\n")
    print("Running A2A test for vehicle mode on IVI...")
    run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")
    print("Vehicle Mode A2A Test execution completed")
    print("Please verify logs for detailed alert information.")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 4: FETCH SYSTEM ID
    # -----------------------------------------------------------
    print("\n================ STEP 4: FETCH SYSTEM ID ================\n")
    systemId = read_vehicleJsonFile(self, "system_id")
    print(f"System ID Retrieved: {systemId}")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 5: CLOUD PRECONDITION VALIDATION
    # -----------------------------------------------------------
    print("\n================ STEP 5: CLOUD PRECONDITION VALIDATION ================\n")
    cloudEnv = read_cloud_env(self)
    print("Fetching current vehicle state from cloud...")
    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
        vehicle_state_info(self, cloudEnv, systemId, "regional")
    print(f"Current Cloud Environment: {cloudEnv}")
    print(f"Vehicle Mode: {vehicleMode}")
    print(f"Connection State: {connectionState}")
    print("------------------------------------------------------------------")

    # Validate preconditions based on cloud environment
    if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5", "GCP-QA8"]:
        print("Validating for CONNECTED state + valid vehicle mode...")
        if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
            testResult(self, "passed",
                       "Vehicle mode & connection state must satisfy precondition",
                       f"Vehicle mode is {vehicleMode}")
            assert True
        else:
            testResult(self, "failed",
                       "Vehicle mode & connection state must satisfy precondition",
                       f"Expected CONNECTED state with valid mode. Got: {connectionState}, {vehicleMode}")
            assert False

    elif cloudEnv in ["GCP-QA"]:
        print("Validating for ACTIVE state + valid vehicle mode...")
        if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
            testResult(self, "passed",
                       "Vehicle mode & current state must satisfy precondition",
                       f"Vehicle mode is {vehicleMode}")
            assert True
        else:
            testResult(self, "failed",
                       "Vehicle mode & current state must satisfy precondition",
                       f"Expected ACTIVE state with valid mode. Got: {currentState}, {vehicleMode}")
            assert False
    else:
        testResult(self, "failed",
                   "Vehicle mode should be normal | privacy | incognito",
                   f"Cloud environment '{cloudEnv}' not recognized")
        assert False

    print("Cloud-side preconditions validated successfully")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 6: TURN OFF WI-FI TO SIMULATE NETWORK LOSS
    # -----------------------------------------------------------
    print("\n================ STEP 6: DISABLE WI-FI ON DEVICE ================\n")
    
    # NOTE: deviceSerialNo must be defined and passed to this test method
    # or retrieved from a fixture/config. It is used here to disable network.
    if not hasattr(self, 'deviceSerialNo') or not self.deviceSerialNo:
        print("WARNING: deviceSerialNo not defined. Network disable command will fail.")
        testResult(self, "verificationFailed",
                   "Device Serial Number must be configured",
                   "deviceSerialNo not found in test context")
        assert False

    disable_network = "shell cmd -w wifi set-wifi-enabled disabled"
    print("Turning OFF Wi-Fi on the IVI device...")
    run_command_on_primary_IVI_device(self, self.deviceSerialNo, disable_network)

    print("Waiting 60 seconds for disconnect to reflect on cloud...")
    time.sleep(60)

    print("Validating cloud connection state becomes DISCONNECTED...")
    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
        vehicle_state_info(self, cloudEnv, systemId, "regional")

    if connectionState == "DISCONNECTED":
        testResult(self, "passed",
                   "Connection must be DISCONNECTED during network outage",
                   "Connection is DISCONNECTED")
        assert True
    else:
        testResult(self, "failed",
                   "Connection must be DISCONNECTED during network outage",
                   f"Connection is {connectionState}, expected DISCONNECTED")
        assert False

    print("Device successfully transitioned to DISCONNECTED state")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 7: TRIGGER VACATION MODE CONFIG UPDATE (DURING OUTAGE)
    # -----------------------------------------------------------
    print("\n================ STEP 7: TRIGGER VACATION MODE CONFIG UPDATE ================\n")

    action = "EDIT"

    # Determine the correct path based on cloud environment
    if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
        path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
    else:
        path = "vehicle_settings.vehicle_mode.vacation_mode"

    # Determine enabled value format based on cloud environment
    if cloudEnv in ["GCP-QA5", "GCP-QA8", "GCP-QA2"]:
        enabled_value = 1  # These environments expect integer
    else:
        enabled_value = True  # These environments expect boolean

    # Calculate time window for vacation mode (10 minutes)
    start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    end_time = start_time + 600000  # 10 minutes in milliseconds

    print("Configuration Payload:")
    print(f"   System ID : {systemId}")
    print(f"   Action    : {action}")
    print(f"   Path      : {path}")
    print(f"   Start Time: {start_time}")
    print(f"   End Time  : {end_time}")
    print("------------------------------------------------------------------")

    print("Sending Vacation Mode request via Vehicle Configuration API...")
    response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(
        self, action, path, enabled_value, start_time, end_time, systemId, "without_start_end_time"
    )

    # Validate API response status code
    if response.status_code != 200:
        print(f"ERROR: API returned unexpected status code: {response.status_code}")
        testResult(self, "failed",
                   "Vacation Mode API should return 200 OK",
                   f"Got status code {response.status_code}")
        assert False

    print("Vacation Mode update request accepted (200 OK)")

    # Extract tracking ID from response
    try:
        response_body = response.json()
        api_status = response_body.get("status", "").upper()
        trackingId = response_body.get("trackingId", "")

        if api_status == "PROGRESSING" and trackingId:
            print(f"Tracking ID received: {trackingId}")
            testResult(self, "passed",
                       "Vacation Mode update should trigger successfully",
                       "Update triggered successfully with PROGRESSING status")
            assert True
        else:
            testResult(self, "failed",
                       "Vacation Mode configuration update should return PROGRESSING status",
                       f"Status: {api_status}, TrackingId: {trackingId}")
            assert False
    except (KeyError, ValueError) as e:
        print(f"ERROR: Failed to parse API response: {e}")
        testResult(self, "failed",
                   "Vacation Mode API response must contain valid status and trackingId",
                   f"Parse error: {e}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 8: TRACKING API VALIDATION DURING OUTAGE (EXPECT ONHOLD)
    # -----------------------------------------------------------
    print("\n================ STEP 8: TRACKING API VALIDATION DURING OUTAGE ================\n")

    final_api_status = None
    for i in range(5):
        print(f"Polling Tracking API... Attempt {i + 1}/5")

        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")
        print(f"Tracking API HTTP Status: {response.status_code}")
        print("------------------------------------------------------------------")

        if response.status_code not in [200, 207]:
            print(f"ERROR: Tracking API returned unexpected status: {response.status_code}")
            assert False

        try:
            response_body = response.json()
            api_status = response_body.get("results", [{}])[0].get("status", "")
            print(f"Configuration Status: {api_status}")

            if api_status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode update should be PROGRESSING",
                           "Status is PROGRESSING")
            elif api_status == "COMPLETED":
                print("Update completed. Exiting polling loop.")
                final_api_status = api_status
                break
            elif api_status == "ONHOLD":
                print("Update is ONHOLD (expected during outage)")
                final_api_status = api_status
                break

            time.sleep(10)
        except (KeyError, IndexError, ValueError) as e:
            print(f"ERROR: Failed to parse tracking response: {e}")
            assert False

    # Evaluate expected ONHOLD state during outage
    if final_api_status == "ONHOLD":
        try:
            error_code = response_body["results"][0].get("results", [{}])[0].get("errorCode", "")
            error_message = response_body["results"][0].get("results", [{}])[0].get("errorMessage", "")
            success_flag = response_body["results"][0].get("results", [{}])[0].get("success", True)

            print(f"Error Code   : {error_code}")
            print(f"Error Message: {error_message}")
            print(f"Success Flag : {success_flag}")

            # Expected error codes during network disconnection
            if (error_code in [16075, 16074]) and (success_flag == False):
                testResult(self, "passed",
                           "Vacation Mode update should be ONHOLD during network outage",
                           "Configuration correctly ONHOLD with appropriate error code")
                assert True
            else:
                testResult(self, "failed",
                           "Vacation Mode update should be ONHOLD with proper error code",
                           f"Got error code {error_code}, success={success_flag}")
                assert False
        except (KeyError, IndexError) as e:
            print(f"ERROR: Failed to extract error details: {e}")
            testResult(self, "failed",
                       "Tracking response must contain error details in ONHOLD state",
                       f"Parse error: {e}")
            assert False

    elif final_api_status == "FAILED":
        testResult(self, "failed",
                   "Vacation Mode update should be ONHOLD (not FAILED) during outage",
                   "Configuration status is FAILED")
        assert False
    else:
        print("ERROR: Update did not transition to ONHOLD or COMPLETED during outage")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 9: ENABLE WI-FI ON DEVICE (RECOVERY)
    # -----------------------------------------------------------
    print("\n================ STEP 9: ENABLE WI-FI ON DEVICE ================\n")

    print("Turning ON Wi-Fi on the IVI device...")
    enable_network = "shell cmd -w wifi set-wifi-enabled enabled"
    run_command_on_primary_IVI_device(self, self.deviceSerialNo, enable_network)

    print("Waiting 30 seconds for connection to recover...")
    time.sleep(30)

    print("Validating cloud connection state becomes CONNECTED...")
    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
        vehicle_state_info(self, cloudEnv, systemId, "regional")

    if connectionState == "CONNECTED":
        testResult(self, "passed",
                   "Connection state must be CONNECTED after network recovery",
                   "Connection state is CONNECTED")
        assert True
    else:
        testResult(self, "failed",
                   "Connection state must be CONNECTED after network recovery",
                   f"Connection state is {connectionState}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 10: CLOUD TRACKING API VALIDATION AFTER RECONNECT
    # -----------------------------------------------------------
    print("\n================ STEP 10: CLOUD TRACKING API VALIDATION AFTER RECONNECT ================\n")

    final_status = None
    for i in range(5):
        print(f"Polling Tracking API... Attempt {i + 1}/5")
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        print(f"HTTP Status: {response.status_code}")
        print("------------------------------------------------------------------")

        if response.status_code not in [200, 207]:
            print(f"ERROR: Tracking API returned unexpected status: {response.status_code}")
            assert False

        try:
            response_body = response.json()
            status = response_body.get("results", [{}])[0].get("status", "")

            if status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode update should be PROGRESSING",
                           "Update is PROGRESSING")
            elif status == "COMPLETED":
                print("Update completed successfully.")
                final_status = status
                break
            elif status == "FAILED":
                print("ERROR: Update failed after reconnection.")
                final_status = status
                break

            time.sleep(10)
        except (KeyError, IndexError, ValueError) as e:
            print(f"ERROR: Failed to parse tracking response: {e}")
            assert False

    # Validate final status
    if final_status == "COMPLETED":
        testResult(self, "passed",
                   "Vacation Mode configuration should complete successfully",
                   "Configuration completed successfully after reconnection")
        assert True
    elif final_status == "FAILED":
        testResult(self, "failed",
                   "Vacation Mode configuration should complete (not fail)",
                   "Configuration failed after reconnection")
        assert False
    else:
        print("ERROR: Configuration did not reach COMPLETED state within polling attempts")
        testResult(self, "failed",
                   "Vacation Mode configuration should complete within time limit",
                   f"Final status: {final_status}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 11: VALIDATE DEVICE master_conf.json (VACATION MODE ENABLED)
    # -----------------------------------------------------------
    print("\n================ STEP 11: VALIDATE DEVICE master_conf.json (VACATION MODE ENABLED) ================\n")

    pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
    time.sleep(30)

    print("Reading Vacation Mode fields from master_conf.json...")
    try:
        vacation_mode_enabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        print(f"Vacation Mode - Enabled: {vacation_mode_enabled}")
        print("------------------------------------------------------------------")

        # Normalize comparison: convert to boolean/int for reliable comparison
        is_enabled = vacation_mode_enabled in [True, 1, "1", "true", "True"]
        expected_enabled = enabled_value in [True, 1, "1", "true", "True"]

        if is_enabled == expected_enabled:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is correctly set to True")
            assert True
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       f"Expected enabled={expected_enabled}, got {vacation_mode_enabled}")
            assert False

    except Exception as e:
        print(f"ERROR: Failed to read master_conf.json: {e}")
        testResult(self, "verificationFailed",
                   "Device master_conf.json must be accessible",
                   f"Read error: {e}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 12: VALIDATE CLOUD CONFIGURATION (ENABLED)
    # -----------------------------------------------------------
    print("\n================ STEP 12: VALIDATE CLOUD CONFIGURATION (VACATION MODE ENABLED) ================\n")

    try:
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        
        if response.status_code != 200:
            print(f"ERROR: Configuration API returned status {response.status_code}")
            assert False

        response_body = response.json()
        if response_body.get("message") != "Success":
            print(f"ERROR: API response message is not Success: {response_body.get('message')}")
            assert False

        # Extract vehicle_mode based on cloud environment
        if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
            vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode", {})
        else:
            vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode", {})

        # Validate vacation_mode configuration
        if "vacation_mode" not in vehicle_mode:
            print("ERROR: vacation_mode not found in cloud configuration")
            assert False

        mode_config = vehicle_mode["vacation_mode"]
        is_enabled_cloud = mode_config.get("enabled") in [True, 1, "1", "true", "True"]

        if is_enabled_cloud:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to True in cloud configuration",
                       "Vacation Mode Flag is correctly set to True on cloud")
            assert True
        else:
            testResult(self, "failed",
                       "Vacation Mode Flag should be set to True in cloud configuration",
                       f"Enabled value: {mode_config.get('enabled')}")
            assert False

    except (KeyError, ValueError, Exception) as e:
        print(f"ERROR: Failed to validate cloud configuration: {e}")
        testResult(self, "failed",
                   "Cloud configuration must be accessible and valid",
                   f"Error: {e}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE)
    # -----------------------------------------------------------
    print("\n================ STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE) ================\n")

    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
        vehicle_state_info(self, cloudEnv, systemId, "regional")

    if vehicleMode == "VACATION_MODE":
        testResult(self, "passed",
                   "Vehicle mode should be VACATION_MODE",
                   "Vehicle mode is correctly set to VACATION_MODE")
        assert True
    else:
        testResult(self, "failed",
                   "Vehicle mode should be VACATION_MODE",
                   f"Vehicle mode is {vehicleMode}")
        assert False

    time.sleep(120)
    pull_logs_from_IVI_device(self, onboardingType, chipsetType)

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 14: VALIDATE TELEMETRY BEHAVIOR DURING VACATION MODE
    # -----------------------------------------------------------
    print("\n================ STEP 14: VALIDATE TELEMETRY DURING VACATION MODE ================\n")

    # List of telemetry messages that should NOT be present during vacation mode
    # (Telemetry publishing should be stopped/reduced)
    telemetry_msgs = [
        "constr_and_send_proto_msg success for 3101",
        "constr_and_send_proto_msg success for 6510",
        "constr_and_send_proto_msg success for 6517",
        "constr_and_send_proto_msg success for 2001",
        "constr_and_send_proto_msg success for 1001",
        "constr_and_send_proto_msg success for 6500",
        "constr_and_send_proto_msg success for 6501"
    ]

    results = []
    for msg in telemetry_msgs:
        result, frequency = verify_message_in_log(self, msg, msg)

        if result != "Error":
            # Message FOUND in logs (should NOT be there during vacation mode)
            print(f" => WARNING: Found telemetry message '{msg}' in logs (should be suppressed).")
            print(f"    Matching line: {result.strip()}")
            testResult(self, "failed",  # Changed from "verificationFailed" to "failed"
                       f"Telemetry '{msg}' should be suppressed during vacation mode",
                       f"Telemetry is still publishing to cloud (should be stopped)")
            results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
        else:
            # Message NOT found (expected - telemetry is suppressed)
            print(f" => OK: Telemetry message '{msg}' not found in logs (as expected).")
            testResult(self, "passed",
                       f"Telemetry '{msg}' should be suppressed during vacation mode",
                       f"Telemetry is correctly suppressed")
            results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

    print("\n[TELEMETRY VALIDATION SUMMARY]")
    for result in results:
        print(f"Message: {result['message']} - Status: {result['status']}")
        if result['details']:
            print(f"  Matching Line: {result['details']}")
            print(f"  Frequency: {result['frequency']}")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 15: WAIT UNTIL VACATION MODE END TIME
    # -----------------------------------------------------------
    print("\n================ STEP 15: WAIT UNTIL VACATION MODE END TIME ================\n")

    current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    while current_time < end_time:
        remaining_time = (end_time - current_time) / 1000  # Convert to seconds
        print(f"Waiting until vacation mode expires... Remaining: {remaining_time:.2f} seconds")
        time.sleep(10)
        current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

    print("Vacation mode end_time reached. Proceeding with mode transition...")
    time.sleep(10)

    print("Initiating transition to NORMAL_MODE (vacation mode will expire)...")
    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 16: DISABLE VACATION MODE (SET TO NORMAL MODE)
    # -----------------------------------------------------------
    print("\n================ STEP 16: DISABLE VACATION MODE ================\n")

    # Determine the correct path to disable vacation mode (set to normal mode)
    # NOTE: The previous code had a bug here - it was setting vacation_mode path instead of normal_mode
    if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA2", "GCP-QA8"]:
        path_disable = "vehicle_settings.user_settings.vehicle_mode.normal_mode"  # FIXED: Use normal_mode path
    else:
        path_disable = "vehicle_settings.vehicle_mode.normal_mode"  # FIXED: Use normal_mode path

    # Determine enabled value format for normal mode transition
    if cloudEnv in ["GCP-QA5", "GCP-QA2", "GCP-QA8"]:
        disabled_value = 0  # Disable vacation mode
    else:
        disabled_value = False  # Disable vacation mode

    # Get current timestamp for mode transition
    transition_start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
    transition_end_time = transition_start_time + 300000  # 5 minutes window

    print("Mode Transition Payload:")
    print(f"   System ID : {systemId}")
    print(f"   Action    : {action}")
    print(f"   Path      : {path_disable}")
    print(f"   Start Time: {transition_start_time}")
    print(f"   End Time  : {transition_end_time}")
    print("------------------------------------------------------------------")

    # Send mode transition request (disable vacation mode)
    vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action,
                                  path_disable, disabled_value, transition_start_time,
                                  transition_end_time, "normalMode_without_startEndTime")

    print("Mode transition request sent. Waiting for device update...")
    time.sleep(30)

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 17: VALIDATE VACATION MODE IS DISABLED IN master_conf.json
    # -----------------------------------------------------------
    print("\n================ STEP 17: VALIDATE VACATION MODE DISABLED ================\n")

    try:
        vacation_mode_status = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        print(f"Vacation Mode - Enabled: {vacation_mode_status}")

        # Normalize comparison
        is_disabled = vacation_mode_status in [False, 0, "0", "false", "False"]
        
        if is_disabled:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is correctly set to False")
            assert True
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       f"Expected False, got {vacation_mode_status}")
            assert False

    except Exception as e:
        print(f"ERROR: Failed to read master_conf.json: {e}")
        testResult(self, "verificationFailed",
                   "Device master_conf.json must be accessible",
                   f"Read error: {e}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 18: VALIDATE CLOUD CONFIGURATION (VACATION MODE DISABLED)
    # -----------------------------------------------------------
    print("\n================ STEP 18: VALIDATE CLOUD CONFIGURATION (DISABLED) ================\n")

    try:
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        
        if response.status_code != 200:
            print(f"ERROR: Configuration API returned status {response.status_code}")
            assert False

        response_body = response.json()
        if response_body.get("message") != "Success":
            print(f"ERROR: API response message is not Success: {response_body.get('message')}")
            assert False

        # Extract vehicle_mode based on cloud environment
        if cloudEnv not in ["GCP-QA2"]:
            vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode", {})
        else:
            vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode", {})

        # Validate vacation_mode is disabled
        if "vacation_mode" not in vehicle_mode:
            print("WARNING: vacation_mode not found in cloud configuration (might indicate disabled state)")
            testResult(self, "passed",
                       "Vacation Mode should be absent or disabled in cloud configuration",
                       "Vacation Mode not present in configuration")
            assert True

        mode_config = vehicle_mode.get("vacation_mode", {})
        is_disabled_cloud = mode_config.get("enabled") in [False, 0, "0", "false", "False"]

        if is_disabled_cloud:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to False in cloud configuration",
                       "Vacation Mode is correctly disabled on cloud")
            assert True
        else:
            testResult(self, "failed",
                       "Vacation Mode Flag should be set to False in cloud configuration",
                       f"Enabled value: {mode_config.get('enabled')}")
            assert False

    except (KeyError, ValueError, Exception) as e:
        print(f"ERROR: Failed to validate cloud configuration: {e}")
        testResult(self, "failed",
                   "Cloud configuration must be accessible and valid",
                   f"Error: {e}")
        assert False

    print("------------------------------------------------------------------")

    # -----------------------------------------------------------
    # STEP 19: VALIDATE VEHICLE STATE API (NORMAL_MODE)
    # -----------------------------------------------------------
    print("\n================ STEP 19: VALIDATE VEHICLE STATE API (NORMAL_MODE) ================\n")

    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
        vehicle_state_info(self, cloudEnv, systemId, "regional")

    if vehicleMode == "NORMAL_MODE":
        testResult(self, "passed",
                   "Vehicle mode should be NORMAL_MODE",
                   "Vehicle mode successfully transitioned to NORMAL_MODE")
        assert True
    else:
        testResult(self, "failed",
                   "Vehicle mode should be NORMAL_MODE",
                   f"Vehicle mode is {vehicleMode}")
        assert False

    print("------------------------------------------------------------------")
    print("\n================ TEST COMPLETED SUCCESSFULLY ================\n")
