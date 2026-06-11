import json
import time
from datetime import timezone
import random

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.vehicle_state import *
from C2CModules.telemetry_modules import *
from C2CModules.commandControl_modules import *
from C2CModules.ddl import *


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_SMS_WakeUp:

    def test_positive_vacation_mode_sms_wakeup(self):

        # -----------------------------------------------------------
        # STEP 1: SET MASTER CONFIG ON DEVICE
        # -----------------------------------------------------------
        print("\n================ STEP 1: APPLY MASTER CONFIGURATION ================\n")
        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)
        print("Master configuration applied successfully")
        print("------------------------------------------------------------------")

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
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")
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

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5", "GCP-QA8"]:
            print("Validating for CONNECTED state + valid vehicle mode...")
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed",
                           "Vehicle mode & connection state must satisfy precondition",
                           f"Vehicle mode is {vehicleMode}")
                assert True
            else:
                assert False

        elif cloudEnv in ["GCP-QA"]:
            print("Validating for ACTIVE state + valid vehicle mode...")
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed",
                           "Vehicle mode & current state must satisfy precondition",
                           f"Vehicle mode is {vehicleMode}")
                assert True
            else:
                assert False
        else:
            testResult(self, "failed",
                       "Vehicle mode should be normal | privacy | incognito",
                       f"Found: {vehicleMode}")
            assert False

        print("Cloud-side preconditions validated")
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 6: TURN OFF WI-FI TO SIMULATE NETWORK LOSS
        # -----------------------------------------------------------
        print("\n================ STEP 6: DISABLE WI-FI ON DEVICE ================\n")
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"
        print("Turning OFF Wi-Fi on the IVI device...")
        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        print("Waiting 60 seconds for disconnect to reflect on cloud...")
        time.sleep(60)

        print("Validating cloud connection state becomes DISCONNECTED...")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "DISCONNECTED":
            testResult(self, "passed",
                       "Connection must be DISCONNECTED during Service Mode",
                       "Connection is DISCONNECTED")
            assert True
        else:
            testResult(self, "failed",
                       "Connection must be DISCONNECTED during Service Mode",
                       f"Connection is {connectionState}")
            assert False

        print("Device successfully transitioned to DISCONNECTED state")
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 7: TRIGGER VACATION MODE CONFIG UPDATE (OUTAGE)
        # -----------------------------------------------------------
        print("\n================ STEP 7: TRIGGER VACATION MODE CONFIG UPDATE ================\n")

        action = "EDIT"

        if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
            path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5", "GCP-QA8", "GCP-QA2"]:
            enabled = 1
        else:
            enabled = True

        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 600000  # 10 minutes

        print("Configuration Payload:")
        print(f"   System ID : {systemId}")
        print(f"   Action    : {action}")
        print(f"   Path      : {path}")
        print(f"   Start Time: {start_time}")
        print(f"   End Time  : {end_time}")
        print("------------------------------------------------------------------")

        print("Sending Vacation Mode request via Vehicle Configuration API...")
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(
            self, action, path, enabled, start_time, end_time, systemId, "valid"
        )

        response_body = response.json()
        if response.status_code == 200:
            print("Vacation Mode update request accepted (200 OK)")
        else:
            print("API returned unexpected status code: ", response.status_code)
            assert False

        trackingId = ""
        if response_body["status"].upper() == "PROGRESSING" and response_body.get("trackingId"):
            trackingId = response_body["trackingId"]
            print(f"Tracking ID received: {trackingId}")
            testResult(self, "verificationPassed",
                       "Vacation Mode update should trigger successfully",
                       "Update triggered successfully")
            assert True
        else:
            testResult(self, "failed",
                       "Vacation Mode configuration update failed to trigger",
                       "Status not PROGRESSING")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 8: TRACKING API VALIDATION DURING OUTAGE (EXPECT ONHOLD / FAILED HANDLING)
        # -----------------------------------------------------------
        print("\n================ STEP 8: TRACKING API VALIDATION DURING OUTAGE ================\n")

        for i in range(5):
            print(f"Polling Tracking API... Attempt {i + 1}/5")

            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")
            print(f"Tracking API HTTP Status: {response.status_code}")
            print("------------------------------------------------------------------")

            if response.status_code not in [200, 207]:
                print("Tracking API returned unexpected status. Check logs.")
                assert False

            response_body = response.json()
            api_status = response_body["results"][0]["status"]

            if api_status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            elif api_status == "COMPLETED":
                break

            time.sleep(10)

        # Evaluate expected ONHOLD/FAILED/other states during outage
        if response_body["results"][0]["status"] == "ONHOLD":
            errorCode = response_body["results"][0]["results"][0]["errorCode"]
            errorMessage = response_body["results"][0]["results"][0]["errorMessage"]
            success = response_body["results"][0]["results"][0]["success"]
            print(f"Error Code   : {errorCode}")
            print(f"Error Message: {errorMessage}")
            print(f"Success Flag : {success}")
            if (errorCode == 16075 or errorCode == 16074) and success == False and (errorMessage == \
                    "The vehicle is currently in Deep Sleep mode, and since the request ('vehicle_settings.user_settings.vehicle_mode.vacation_mode') is critical, an SMSWakeUp request is being triggered." or errorMessage == "The vehicle is currently disconnected, and the request is critical. So holding this request for now."):
                testResult(self, "passed",
                           "Vacation Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                           "Vacation Mode - Configuration update is ONHOLD during network outage/losting cloud connection")
                assert True
            else:
                assert False

        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed",
                       "Vacation Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                       "Vacation Mode - Configuration update is not in ONHOLD during outage")
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 9: ENABLE WI-FI ON DEVICE (RECOVERY)
        # -----------------------------------------------------------
        print("\n================ STEP 9: ENABLE WI-FI ON DEVICE ================\n")

        print("Turning ON Wi-Fi on the IVI device...")
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"
        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        print("Waiting 30 seconds for connection to recover...")
        time.sleep(30)

        print("\n======== Validating connection state becomes CONNECTED ========\n")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "CONNECTED":
            testResult(self, "passed", "Connection state must be CONNECTED",
                       "Connection state is CONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection state must be CONNECTED",
                       f"Connection state is {connectionState}")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 10: CLOUD TRACKING API VALIDATION AFTER RECONNECT
        # -----------------------------------------------------------
        print("\n================ STEP 10: CLOUD TRACKING API VALIDATION ================\n")

        for i in range(5):
            print(f"Polling Tracking API... Attempt {i + 1}/5")
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(f"HTTP Status: {response.status_code}")
            print("------------------------------------------------------------------")

            if response.status_code not in [200, 207]:
                print("Unexpected API response. Check logs.")
                assert False

            response_body = response.json()
            status = response_body["results"][0]["status"]

            if status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode update should be 'PROGRESSING'",
                           "Vacation Mode update is PROGRESSING")
            elif status == "COMPLETED":
                break

            time.sleep(10)

        final_status = response_body["results"][0]["status"]
        if final_status == "COMPLETED":
            testResult(self, "passed",
                       "Vacation Mode configuration should success/completed",
                       "Vacation Mode configuration update is success/completed")
            assert True
        elif final_status == "FAILED":
            testResult(self, "failed",
                       "Vacation Mode configuration should success/completed",
                       "Vacation Mode configuration update is not success/completed")
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 11: VALIDATE DEVICE master_conf.json (VACATION MODE ENABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 11: VALIDATE DEVICE master_conf.json (ENABLED) ================\n")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("Reading Vacation Mode fields from master_conf.json...")
        vacationMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        vacationMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_StartTime", "vacationMode")
        vacationMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_EndTime", "vacationMode")

        print(f" Vacation Mode - Enabled    : {vacationMode_Enabled}")
        print(f" Vacation Mode - Start Time : {vacationMode_StartTime}")
        print(f" Vacation Mode - End Time   : {vacationMode_EndTime}")
        print("------------------------------------------------------------------")

        status = ""

        if str(vacationMode_Enabled) == enabled or bool(vacationMode_Enabled) == enabled:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("------------------------------------------------------------------")

        if vacationMode_StartTime == start_time:
            testResult(self, "passed",
                       "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("------------------------------------------------------------------")

        if vacationMode_EndTime == end_time:
            testResult(self, "passed",
                       "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("------------------------------------------------------------------")

        if status != "FAIL":
            assert True
        else:
            assert False
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 12: VALIDATE CLOUD CONFIGURATION (ENABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 12: VALIDATE CLOUD CONFIGURATION (ENABLED) ================\n")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()

        if response.status_code == 200:
            if response_body.get("message") == "Success":
                if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    if (mode_config["enabled"] == "true" or mode_config["enabled"] == True) and \
                            mode_config["start_time"] == start_time and \
                            mode_config["end_time"] == end_time:
                        testResult(self, "passed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        testResult(self, "failed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert False
                        #self.result.set_result(TestResults.failed)

        # -----------------------------------------------------------
        # STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE)
        # -----------------------------------------------------------
        print("\n================ STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE) ================\n")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if vehicleMode == "VACATION_MODE":
            testResult(self, "passed", "vehicle mode should be in vacation_mode",
                       "vehicle mode is in vacation mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in vacation_mode",
                       "vehicle mode is not in vacation mode")
            assert False
            #self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 14: VALIDATE TELEMETRY BEHAVIOR DURING VACATION MODE
        # -----------------------------------------------------------
        print("\n================ STEP 14: VALIDATE TELEMETRY DURING VACATION MODE ================\n")

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
                print(f" => Found telemetry message '{msg}' in logs.")
                print(f"    Matching line: {result.strip()}")
                testResult(self, "verificationFailed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. See device logs for details.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs (expected).")
                testResult(self, "passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is not publishing to the cloud.")
                results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

        print("\n[SUMMARY]")
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

        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # seconds
            print(f"Waiting until end_time... Remaining time: {remaining_time:.2f} seconds")
            time.sleep(10)
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        print("end_time reached. Proceeding with the operation...")
        time.sleep(10)

        # -----------------------------------------------------------
        # STEP 16: VALIDATE DEVICE master_conf.json (VACATION MODE DISABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 16: VALIDATE DEVICE master_conf.json (DISABLED) ================\n")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("Validate Vacation mode is disabled in master_conf.json:")
        vacationMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        print(f" Vacation Mode - Enabled : {vacationMode_Disabled}")
        print("------------------------------------------------------------------")

        status = ""
        if vacationMode_Disabled == "false" or vacationMode_Disabled == False or vacationMode_Disabled == 0:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is not set to False in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("------------------------------------------------------------------")

        if status != "FAIL":
            assert True
        else:
            assert False
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 17: VALIDATE CLOUD CONFIGURATION (DISABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 17: VALIDATE CLOUD CONFIGURATION (DISABLED) ================\n")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()

        if response.status_code == 200:
            print("Vehicle Configuration API returned 200 OK")

            if response_body.get("message") == "Success":
                print("API message indicates Success")
                print(f"Active Cloud Environment: {cloudEnv}")

                # Choose path for vehicle_mode based on environment
                if cloudEnv not in ["GCP-QA2", "GCP-QA8", "GCP-QA5"]:
                    print("Reading vehicle_mode from: configurations.vehicle_settings.vehicle_mode")
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    print("Reading vehicle_mode from: configurations.vehicle_settings.user_settings.vehicle_mode")
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Validate vacation_mode presence and disabled state
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    print(f"Vacation Mode - enabled field value: {mode_config.get('enabled')}")

                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False or mode_config[
                        "enabled"] == 0:
                        testResult(
                            self,
                            "passed",
                            "Vacation Mode Flag should be set to False in master_conf.json file on cloud",
                            "Vacation Mode Flag is set to False in master_conf.json file on cloud"
                        )
                        print("Cloud shows Vacation Mode DISABLED as expected")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        testResult(
                            self,
                            "failed",
                            "Vacation Mode Flag should be set to False in master_conf.json file on cloud",
                            "Vacation Mode Flag is not set to False in master_conf.json file on cloud"
                        )
                        print("Cloud shows Vacation Mode still ENABLED (unexpected)")
                        assert False
                        #self.result.set_result(TestResults.failed)
                else:
                    print("Invalid or unsupported vehicle_mode structure: 'vacation_mode' key not found")
                    assert False
                    #self.result.set_result(TestResults.failed)

            else:
                print(f"API message unexpected: {response_body.get('message')}")
                assert False
                #self.result.set_result(TestResults.failed)

        else:
            print(f"Vehicle Configuration API returned non-200 status: {response.status_code}")
            assert False
            #self.result.set_result(TestResults.failed)

        # -----------------------------------------------------------
        # STEP 18: VALIDATE VEHICLE STATE RETURNS NORMAL_MODE
        # -----------------------------------------------------------
        print("\n================ STEP 18: VALIDATE VEHICLE STATE RETURNS NORMAL_MODE ================\n")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       "vehicle mode is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode",
                       "vehicle mode is not in normal mode")
            assert False
            #self.result.set_result(TestResults.failed)

        print("------------------------------------------------------------------")

    def test_positive_privacy_mode_sms_wakeup(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # -------------------vehicle state------------------

        print("----------------------------------------------------------")
        print("===================Cloud side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5", "GCP-QA8"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)
        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

        # Command to disable Wi-Fi
        print("---------------------------")
        print("TURN OFF WIFI ON THE DEVICE")
        print("---------------------------")
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(60)

        print("======== Validating connection state becomes DISCONNECTED ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if connectionState == "DISCONNECTED":
            testResult(self, "passed", "Connection must be DISCONNECTED during Service Mode",
                       "Connection is DISCONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection must be DISCONNECTED during Service Mode",
                       f"Connection is {connectionState}")
            assert False
        # Test Data*

        print("------Trigger Vehicle Mode Update Request-------")

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA8","GCP-QA2"]:
            path = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"
        else:
            path = "vehicle_settings.vehicle_mode.privacy_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA8","GCP-QA2"]:
            enabled = 1
        else:
            enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 600000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print(f"Trigger Privacy Mode via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

        print("----------------------------------------------------------")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False
            # self.result.set_result(TestResults.failed)

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           f"Privacy Mode - Configuration update should be triggered successfully",
                           f"Privacy Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", f"Privacy Mode - Configuration update should be triggered successfully",
                       f"Privacy Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation via Tracking API : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           f"Privacy Mode - Configuration update should  be 'PROGRESSING'",
                           f"Privacy Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "ONHOLD":
            errorCode = response_body["results"][0]["results"][0]["errorCode"]
            errorMessage = response_body["results"][0]["results"][0]["errorMessage"]
            success = response_body["results"][0]["results"][0]["success"]
            print("Error Code: ", errorCode)
            print("Error Message: ", errorMessage)
            print("Success: ", success)
            if errorCode == 16075 and success == False and errorMessage == "The vehicle is currently in Deep Sleep mode, and since the request ('vehicle_settings.user_settings.vehicle_mode.privacy_mode') is critical, an SMSWakeUp request is being triggered.":
                testResult(self, "passed", f"Privacy Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                           f"Privacy Mode - Configuration update is ONHOLD during network outage/losting cloud connection")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", f"Privacy Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                       f"Privacy Mode - Configuration update is not in ONHOLD during network outage/losting cloud connection. Rather than found: ", response_body["results"][0]["status"])
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        # Command to enable Wi-Fi
        print("---------------------------")
        print("TURN ON WIFI ON THE DEVICE")
        print("---------------------------")
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(30)

        print("======== Validating connection state becomes CONNECTED ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if connectionState == "CONNECTED":
            testResult(self, "passed", "Connection state must be CONNECTED",
                       "Connection state is CONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection state must be CONNECTED",
                       f"Connection state is {connectionState}")
            assert False

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation via Tracking API : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           f"Privacy Mode - Configuration update should  be 'PROGRESSING'",
                           f"Privacy Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", f"Privacy Mode - Configuration update should success/completed",
                       f"Privacy Mode - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", f"Privacy Mode - Configuration update should success/completed",
                       f"Privacy Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print(f"Validate Privacy mode is enabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        # Read master_conf.json file
        privacyMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")
        privacyMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_StartTime", "privacyMode")
        privacyMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_EndTime", "privacyMode")

        print(" Privacy Mode - Enabled :", privacyMode_Enabled)
        print(" Privacy Mode - Start Time :", privacyMode_StartTime)
        print(" Privacy Mode - End Time :", privacyMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(privacyMode_Enabled) == enabled or bool(privacyMode_Enabled) == enabled:
            testResult(self, "passed", "Privacy Mode Flag should be set to True in master_conf.json file on device",
                       "Privacy Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode Flag should be set to True in master_conf.json file on device",
                       "Privacy Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if privacyMode_StartTime == start_time:
            testResult(self, "passed", "Privacy Mode Start time should be updated in master_conf.json file on device",
                       "Privacy Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode Start time should be updated in master_conf.json file on device",
                       "Privacy Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if privacyMode_EndTime == end_time:
            testResult(self, "passed", "Privacy Mode End time should be updated in master_conf.json file on device",
                       "Privacy Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode End time should be updated in master_conf.json file on device",
                       "Privacy Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Handle each mode
                if "privacy_mode" in vehicle_mode:
                    mode_config = vehicle_mode["privacy_mode"]
                    if (mode_config["enabled"] == "true" or mode_config["enabled"] == True) and mode_config[
                        "start_time"] == start_time and mode_config[
                        "end_time"] == end_time:
                        testResult(self, "passed",
                                   "Privacy Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Privacy Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                    else:
                        assert False

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "PRIVACY_MODE":
            testResult(self, "passed", "vehicle mode should be in privacy_mode",
                       f"vehicle mode is in privacy_mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in privacy_mode",
                       f"vehicle mode is not in privacy_mode")
            assert False
            # self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in vacation mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101"
        ]

        # Initialize result aggregation for a summary at the end
        results = []

        # Verify each message using verify_message_in_log
        for msg in telemetry_msgs:
            # Call the verify_message_in_log function to check if the message exists in the log
            result, frequency = verify_message_in_log(self, msg,
                                                      msg)  # Pass message1 and message2 (or the same message)

            # Handle the results
            if result != "Error":
                print(f" => Found telemetry message '{msg}' in logs.")
                print(f"Matching log line for '{msg}': {result.strip()}")
                testResult(self, "verificationFailed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs.\n")
                testResult(self, "passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is not publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

        # Summary Output
        print("\n[SUMMARY]")
        for result in results:
            print(f"Message: {result['message']} - Status: {result['status']}")
            if result['details']:
                print(f"  Matching Line: {result['details']}")
                print(f"  Frequency: {result['frequency']}")

        print("----------------------------------------------------------")

        # Wait until the end_time
        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # Convert remaining time to seconds
            print(f"Waiting until end_time... Remaining time: {remaining_time:.2f} seconds")
            time.sleep(10)  # Check every 10 seconds
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # After end_time is reached
        print("end_time reached. Proceeding with the operation...")
        time.sleep(10)

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Validate Vacation mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        privacyMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")

        print(" Privacy Mode - Enabled :", privacyMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if privacyMode_Disabled == "false" or privacyMode_Disabled == False or privacyMode_Disabled == 0:
            testResult(self, "passed",
                       "Privacy Mode Flag should be set to False in master_conf.json file on device",
                       "Privacy Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Privacy Mode Flag should be set to False in master_conf.json file on device",
                       "Privacy Mode Flag is not set to False in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                if cloudEnv not in ["GCP-QA2","GCP-QA8","GCP-QA5"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Handle each mode
                if "privacy_mode" in vehicle_mode:
                    mode_config = vehicle_mode["privacy_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False or mode_config[
                        "enabled"] == 0:
                        testResult(self, "passed",
                                   "Privacy Mode Flag should be set to False in master_conf.json file on cloud",
                                   "Privacy Mode Flag is set to False in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    #self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is not in normal mode")
            assert False
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_positive_incognito_mode_sms_wakeup(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # -------------------vehicle state------------------

        print("----------------------------------------------------------")
        print("===================Cloud side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5", "GCP-QA8"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)
        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

        # Command to disable Wi-Fi
        print("---------------------------")
        print("TURN OFF WIFI ON THE DEVICE")
        print("---------------------------")
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(60)

        print("======== Validating connection state becomes DISCONNECTED ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if connectionState == "DISCONNECTED":
            testResult(self, "passed", "Connection must be DISCONNECTED during Service Mode",
                       "Connection is DISCONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection must be DISCONNECTED during Service Mode",
                       f"Connection is {connectionState}")
            assert False
        # Test Data*

        print("------Trigger Vehicle Mode Update Request-------")

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA8","GCP-QA2"]:
            path = "vehicle_settings.user_settings.vehicle_mode.incognito_mode"
        else:
            path = "vehicle_settings.vehicle_mode.incognito_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA8","GCP-QA2"]:
            enabled = 1
        else:
            enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 600000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print(f"Trigger Incognito Mode via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

        print("----------------------------------------------------------")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False
            # self.result.set_result(TestResults.failed)

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           f"Incognito Mode - Configuration update should be triggered successfully",
                           f"Incognito Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", f"Incognito Mode - Configuration update should be triggered successfully",
                       f"Incognito Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation via Tracking API : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           f"Incognito Mode - Configuration update should  be 'PROGRESSING'",
                           f"Incognito Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "ONHOLD":
            errorCode = response_body["results"][0]["results"][0]["errorCode"]
            errorMessage = response_body["results"][0]["results"][0]["errorMessage"]
            success = response_body["results"][0]["results"][0]["success"]
            print("Error Code: ", errorCode)
            print("Error Message: ", errorMessage)
            print("Success: ", success)
            if errorCode == 16075 and success == False and errorMessage == "The vehicle is currently in Deep Sleep mode, and since the request ('vehicle_settings.user_settings.vehicle_mode.incognito_mode') is critical, an SMSWakeUp request is being triggered.":
                testResult(self, "passed", f"Incognito Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                           f"Incognito Mode - Configuration update is ONHOLD during network outage/losting cloud connection")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                assert False
                #self.result.set_result(TestResults.failed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", f"Incognito Mode - Configuration update should be ONHOLD during network outage/losting cloud connection",
                       f"Incognito Mode - Configuration update is not in ONHOLD during network outage/losting cloud connection. Rather than found: ", response_body["results"][0]["status"])
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        # Command to enable Wi-Fi
        print("---------------------------")
        print("TURN ON WIFI ON THE DEVICE")
        print("---------------------------")
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(30)

        print("======== Validating connection state becomes CONNECTED ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if connectionState == "CONNECTED":
            testResult(self, "passed", "Connection state must be CONNECTED",
                       "Connection state is CONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection state must be CONNECTED",
                       f"Connection state is {connectionState}")
            assert False

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation via Tracking API : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           f"Incognito Mode - Configuration update should  be 'PROGRESSING'",
                           f"Incognito Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", f"Incognito Mode - Configuration update should success/completed",
                       f"Incognito Mode - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", f"Incognito Mode - Configuration update should success/completed",
                       f"Incognito Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print(f"Validate Incognito mode is enabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        # Read master_conf.json file
        incognitoMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled", "incognitoMode")
        incognitoMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_StartTime", "incognitoMode")
        incognitoMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_EndTime", "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Enabled)
        print(" Incognito Mode - Start Time :", incognitoMode_StartTime)
        print(" Incognito Mode - End Time :", incognitoMode_EndTime)

        print("----------------------------------------------------------")
        status = ""

        if str(incognitoMode_Enabled) == enabled or bool(incognitoMode_Enabled) == enabled:
            testResult(self, "passed",
                       "Incognito Mode Flag should be set to True in master_conf.json file on device",
                       "Incognito Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode Flag should be set to True in master_conf.json file on device",
                       "Incognito Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if incognitoMode_StartTime == start_time:
            testResult(self, "passed",
                       "Incognito Mode Start time should be updated in master_conf.json file on device",
                       "Incognito Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode Start time should be updated in master_conf.json file on device",
                       "Incognito Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if incognitoMode_EndTime == end_time:
            testResult(self, "passed",
                       "Incognito Mode End time should be updated in master_conf.json file on device",
                       "Incognito Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode End time should be updated in master_conf.json file on device",
                       "Incognito Mode End time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Handle each mode
                if "incognito_mode" in vehicle_mode:
                    mode_config = vehicle_mode["incognito_mode"]
                    if (mode_config["enabled"] == "true" or mode_config["enabled"] == True) and mode_config[
                        "start_time"] == start_time and mode_config[
                        "end_time"] == end_time:
                        testResult(self, "passed",
                                   "Incognito Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Incognito Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                    else:
                        assert False

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "INCOGNITO_MODE":
            testResult(self, "passed", "vehicle mode should be in incognito_mode",
                       f"vehicle mode is in incognito_mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in incognito_mode",
                       f"vehicle mode is not in incognito_mode")
            assert False
            # self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in incognito mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6500",
            "constr_and_send_proto_msg success for 6501"
        ]

        # Initialize result aggregation for a summary at the end
        results = []

        # Verify each message using verify_message_in_log
        for msg in telemetry_msgs:
            # Call the verify_message_in_log function to check if the message exists in the log
            result, frequency = verify_message_in_log(self, msg,
                                                      msg)  # Pass message1 and message2 (or the same message)

            # Handle the results
            if result != "Error":
                print(f" => Found telemetry message '{msg}' in logs.")
                print(f"Matching log line for '{msg}': {result.strip()}")
                testResult(self, "verificationFailed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs.\n")
                testResult(self, "passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is not publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

        # Summary Output
        print("\n[SUMMARY]")
        for result in results:
            print(f"Message: {result['message']} - Status: {result['status']}")
            if result['details']:
                print(f"  Matching Line: {result['details']}")
                print(f"  Frequency: {result['frequency']}")

        print("----------------------------------------------------------")

        # Wait until the end_time
        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # Convert remaining time to seconds
            print(f"Waiting until end_time... Remaining time: {remaining_time:.2f} seconds")
            time.sleep(10)  # Check every 10 seconds
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # After end_time is reached
        print("end_time reached. Proceeding with the operation...")
        time.sleep(10)

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Validate Incognito mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        incognitoMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled", "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if incognitoMode_Disabled == "false" or incognitoMode_Disabled == False or incognitoMode_Disabled == 0:
            testResult(self, "passed",
                       "Incognito Mode Flag should be set to False in master_conf.json file on device",
                       "Incognito Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Incognito Mode Flag should be set to False in master_conf.json file on device",
                       "Incognito Mode Flag is not set to False in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                if cloudEnv not in ["GCP-QA2","GCP-QA8","GCP-QA5"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Handle each mode
                if "incognito_mode" in vehicle_mode:
                    mode_config = vehicle_mode["incognito_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False or mode_config[
                        "enabled"] == 0:
                        testResult(self, "passed",
                                   "Incognito Mode Flag should be set to False in master_conf.json file on cloud",
                                   "Incognito Mode Flag is set to False in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    #self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is not in normal mode")
            assert False
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

class Test_SMS_WakeUp_1:

    def test_positive_vacation_mode_sms_wakeup_r8p4s14(self):

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

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5", "GCP-QA8"]:
            print("Validating for CONNECTED state + valid vehicle mode...")
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed",
                           "Vehicle mode & connection state must satisfy precondition",
                           f"Vehicle mode is {vehicleMode}")
                assert True
            else:
                assert False

        elif cloudEnv in ["GCP-QA"]:
            print("Validating for ACTIVE state + valid vehicle mode...")
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed",
                           "Vehicle mode & current state must satisfy precondition",
                           f"Vehicle mode is {vehicleMode}")
                assert True
            else:
                assert False
        else:
            testResult(self, "failed",
                       "Vehicle mode should be normal | privacy | incognito",
                       f"Found: {vehicleMode}")
            assert False

        print("Cloud-side preconditions validated")
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 6: TURN OFF WI-FI TO SIMULATE NETWORK LOSS
        # -----------------------------------------------------------
        print("\n================ STEP 6: DISABLE WI-FI ON DEVICE ================\n")
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"
        print("Turning OFF Wi-Fi on the IVI device...")
        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        print("Waiting 60 seconds for disconnect to reflect on cloud...")
        time.sleep(60)

        print("Validating cloud connection state becomes DISCONNECTED...")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "DISCONNECTED":
            testResult(self, "passed",
                       "Connection must be DISCONNECTED during Service Mode",
                       "Connection is DISCONNECTED")
            assert True
        else:
            testResult(self, "failed",
                       "Connection must be DISCONNECTED during Service Mode",
                       f"Connection is {connectionState}")
            assert False

        print("Device successfully transitioned to DISCONNECTED state")
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 7: TRIGGER VACATION MODE CONFIG UPDATE (OUTAGE)
        # -----------------------------------------------------------
        print("\n================ STEP 7: TRIGGER VACATION MODE CONFIG UPDATE ================\n")

        action = "EDIT"

        if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
            path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5", "GCP-QA8", "GCP-QA2"]:
            enabled = 1
        else:
            enabled = True

        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 600000  # 10 minutes

        print("Configuration Payload:")
        print(f"   System ID : {systemId}")
        print(f"   Action    : {action}")
        print(f"   Path      : {path}")
        print(f"   Start Time: {start_time}")
        print(f"   End Time  : {end_time}")
        print("------------------------------------------------------------------")

        print("Sending Vacation Mode request via Vehicle Configuration API...")
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(
            self, action, path, enabled, start_time, end_time, systemId, "without_start_end_time"
        )

        response_body = response.json()
        if response.status_code == 200:
            print("Vacation Mode update request accepted (200 OK)")
        else:
            print("API returned unexpected status code: ", response.status_code)
            assert False

        trackingId = ""
        if response_body["status"].upper() == "PROGRESSING" and response_body.get("trackingId"):
            trackingId = response_body["trackingId"]
            print(f"Tracking ID received: {trackingId}")
            testResult(self, "verificationPassed",
                       "Vacation Mode update should trigger successfully",
                       "Update triggered successfully")
            assert True
        else:
            testResult(self, "failed",
                       "Vacation Mode configuration update failed to trigger",
                       "Status not PROGRESSING")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 8: TRACKING API VALIDATION DURING OUTAGE
        # Expected result: the update should be held (ONHOLD) while the vehicle is disconnected.
        # Poll the tracking API up to 5 times and verify the final outage state.
        # -----------------------------------------------------------
        print("\n================ STEP 8: TRACKING API VALIDATION DURING OUTAGE ================\n")

        for i in range(5):
            print(f"Polling Tracking API... Attempt {i + 1}/5")
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")
            print(f"Tracking API HTTP Status: {response.status_code}")

            if response.status_code not in [200, 207]:
                print("Tracking API returned unexpected status code. Check logs.")
                assert False

            response_body = response.json()
            api_status = response_body["results"][0]["status"]
            print(f"Tracking API Status: {api_status}")
            print("------------------------------------------------------------------")

            if api_status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should be 'PROGRESSING' while the request is being held",
                           "Vacation Mode - Configuration update is PROGRESSING")
            elif api_status in ["ONHOLD", "COMPLETED"]:
                break

            time.sleep(10)

        # Evaluate final tracking status after polling
        api_status = response_body["results"][0]["status"]
        if api_status == "ONHOLD":
            errorCode = response_body["results"][0]["results"][0].get("errorCode")
            errorMessage = response_body["results"][0]["results"][0].get("errorMessage", "")
            success = response_body["results"][0]["results"][0].get("success")
            print(f"Error Code   : {errorCode}")
            print(f"Error Message: {errorMessage}")
            print(f"Success Flag : {success}")

            if errorCode in [16074, 16075] and success is False and "vehicle is currently disconnected" in errorMessage.lower():
                testResult(self, "passed",
                           "Vacation Mode - Configuration update should be ONHOLD during network outage",
                           "Vacation Mode - Configuration update is ONHOLD during network outage")
                assert True
            else:
                print("Unexpected ONHOLD response details. Check tracking API response.")
                print(f"Actual ONHOLD details: code={errorCode}, success={success}, message={errorMessage}")
                assert False

        elif api_status == "FAILED":
            testResult(self, "failed",
                       "Vacation Mode - Configuration update should be ONHOLD during network outage",
                       "Vacation Mode - Configuration update is FAILED during outage")
            assert False
        else:
            print("Unexpected Tracking API status after polling. Expected ONHOLD during outage.")
            print(f"Tracking API returned final status: {api_status}")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 9: ENABLE WI-FI ON DEVICE (RECOVERY)
        # -----------------------------------------------------------
        print("\n================ STEP 9: ENABLE WI-FI ON DEVICE ================\n")

        print("Turning ON Wi-Fi on the IVI device...")
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"
        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        print("Waiting 30 seconds for connection to recover...")
        time.sleep(30)

        print("\n======== Validating connection state becomes CONNECTED ========\n")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "CONNECTED":
            testResult(self, "passed", "Connection state must be CONNECTED",
                       "Connection state is CONNECTED")
            assert True
        else:
            testResult(self, "failed", "Connection state must be CONNECTED",
                       f"Connection state is {connectionState}")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 10: CLOUD TRACKING API VALIDATION AFTER RECONNECT
        # -----------------------------------------------------------
        print("\n================ STEP 10: CLOUD TRACKING API VALIDATION ================\n")

        for i in range(5):
            print(f"Polling Tracking API... Attempt {i + 1}/5")
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(f"HTTP Status: {response.status_code}")
            print("------------------------------------------------------------------")

            if response.status_code not in [200, 207]:
                print("Unexpected API response. Check logs.")
                assert False

            response_body = response.json()
            status = response_body["results"][0]["status"]

            if status == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Vacation Mode update should be 'PROGRESSING'",
                           "Vacation Mode update is PROGRESSING")
            elif status == "COMPLETED":
                break

            time.sleep(10)

        final_status = response_body["results"][0]["status"]
        if final_status == "COMPLETED":
            testResult(self, "passed",
                       "Vacation Mode configuration should success/completed",
                       "Vacation Mode configuration update is success/completed")
            assert True
        elif final_status == "FAILED":
            testResult(self, "failed",
                       "Vacation Mode configuration should success/completed",
                       "Vacation Mode configuration update is not success/completed")
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            assert False

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 11: VALIDATE DEVICE master_conf.json (VACATION MODE ENABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 11: VALIDATE DEVICE master_conf.json (ENABLED) ================\n")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("Reading Vacation Mode fields from master_conf.json...")
        vacationMode_Enabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")
        #vacationMode_StartTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_StartTime", "vacationMode")
        #vacationMode_EndTime = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_EndTime", "vacationMode")

        print(f" Vacation Mode - Enabled    : {vacationMode_Enabled}")
        #print(f" Vacation Mode - Start Time : {vacationMode_StartTime}")
        #print(f" Vacation Mode - End Time   : {vacationMode_EndTime}")
        print("------------------------------------------------------------------")

        status = ""

        if str(vacationMode_Enabled) == enabled or bool(vacationMode_Enabled) == enabled:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("------------------------------------------------------------------")

        #if vacationMode_StartTime == start_time:
         #   testResult(self, "passed",
          #             "Vacation Mode Start time should be updated in master_conf.json file on device",
           #            "Vacation Mode Start time is updated in master_conf.json file on device")
        #else:
         #   testResult(self, "verificationFailed",
          #             "Vacation Mode Start time should be updated in master_conf.json file on device",
           #            "Vacation Mode Start time is not updated in master_conf.json file on device")
            #status = "FAIL"
            #print("Status", status)
        #print("------------------------------------------------------------------")

        #if vacationMode_EndTime == end_time:
         #   testResult(self, "passed",
          #             "Vacation Mode End time should be updated in master_conf.json file on device",
           #            "Vacation Mode End time is updated in master_conf.json file on device")
        #else:
         #   testResult(self, "verificationFailed",
          #             "Vacation Mode End time should be updated in master_conf.json file on device",
           #            "Vacation Mode End time is not updated in master_conf.json file on device")
           # status = "FAIL"
            #print("Status", status)
        #print("------------------------------------------------------------------")

        if status != "FAIL":
            assert True
        else:
            assert False
        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 12: VALIDATE CLOUD CONFIGURATION (ENABLED)
        # -----------------------------------------------------------
        print("\n================ STEP 12: VALIDATE CLOUD CONFIGURATION (ENABLED) ================\n")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()

        if response.status_code == 200:
            if response_body.get("message") == "Success":
                if cloudEnv not in ["RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    if (mode_config["enabled"] == "true" or mode_config["enabled"] == True):
                        testResult(self, "passed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        testResult(self, "failed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert False
                        #self.result.set_result(TestResults.failed)

        # -----------------------------------------------------------
        # STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE)
        # -----------------------------------------------------------
        print("\n================ STEP 13: VALIDATE VEHICLE STATE API (VACATION_MODE) ================\n")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = \
            vehicle_state_info(self, cloudEnv, systemId, "regional")

        if vehicleMode == "VACATION_MODE":
            testResult(self, "passed", "vehicle mode should be in vacation_mode",
                       "vehicle mode is in vacation mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in vacation_mode",
                       "vehicle mode is not in vacation mode")
            assert False
            #self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("------------------------------------------------------------------")

        # -----------------------------------------------------------
        # STEP 14: VALIDATE TELEMETRY BEHAVIOR DURING VACATION MODE
        # -----------------------------------------------------------
        print("\n================ STEP 14: VALIDATE TELEMETRY DURING VACATION MODE ================\n")

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
                print(f" => Found telemetry message '{msg}' in logs.")
                print(f"    Matching line: {result.strip()}")
                testResult(self, "verificationFailed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. See device logs for details.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs (expected).")
                testResult(self, "passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is not publishing to the cloud.")
                results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

        print("\n[SUMMARY]")
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

        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # seconds
            print(f"Waiting until end_time... Remaining time: {remaining_time:.2f} seconds")
            time.sleep(10)
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        print("end_time reached. Proceeding with the operation...")
        time.sleep(10)

        print("Due to mode disable won't happen automatically , initiating mode switching to normal mode..")

        # run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA2", "GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.normal_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5", "GCP-QA2", "GCP-QA8"]:
            enabled = 1
        else:
            enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                      start_time,
                                      end_time, "normalMode_without_startEndTime")

        # pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        # time.sleep(30)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Validate Vacation mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        vacationMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")

        print(" Vacation Mode - Enabled :", vacationMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if vacationMode_Disabled == "false" or vacationMode_Disabled == False or vacationMode_Disabled == 0:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is not set to False in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                if cloudEnv not in ["GCP-QA2"]:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                        "vehicle_mode")

                # Handle each mode
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False or mode_config[
                        "enabled"] == 0:
                        testResult(self, "passed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Vacation Mode Disable validation failed")
                        print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=False")
                        assert False
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    # self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is in normal mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode",
                       f"vehicle mode is not in normal mode")
            assert False
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")