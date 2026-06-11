import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.e2e_testData import *
from C2CModules.vehicle_metadata import *
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.telemetry_modules import telemetry_Curr

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
deviceSerialNo = b2c_ivi_adbSerialNo
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

class Test_certificate_revoke:

    # Device Revoke
    def test_positive_eol_onboarding_device_certificate_revoke(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        systemId = read_vehicleJsonFile(self, "system_id")

        print("SystemId: ", systemId)

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER CERTIFICATE REVOKE API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceRevoke(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Certificate revoked successfully":
            testResult(self, "passed", "Certificate Revoke API should be triggered successfully",
                       "Successfully triggered Certificate Revoke request")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Certificate revoked successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Certificate Revoke API should be triggered successfully",
                       "Failed to trigger certificate revoke API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False
        time.sleep(600)

    def test_positive_certificate_revoke_network_down_after_15_mins(self):

        print("-------------------------------------------------------------------------")

        print("=============================================================")
        try:
            print("Read VIN & System Id from device for validations")
            systemId = get_SystemId(self, onboardingType, chipsetType)
            vin = getVIN(self, onboardingType, chipsetType)
            print(f"VIN : =>  {vin}")
            print(f"SystemId : =>  {systemId}")
            pageNo, pageSize = "1", "10"

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")
            response = vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, "regional")
            response_body = response.json()

            print("Validate Life Cycle State @ Cloud post certificate revoke")
            state = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]

            if state in {"REVOKED"}:
                testResult(
                    self,
                    "passed",
                    "Life Cycle State should be set to REVOKED",
                    f"Life Cycle State is set to REVOKED, Rather than found: {state}"
                )
            else:
                testResult(
                    self,
                    "failed",
                    "Life Cycle State should be set to REVOKED",
                    f"Life Cycle State is not set to REVOKED, Rather than found: {state}"
                )

        except Exception as e:
            print(f"Exception occurred: {e}")
            testResult(self, "failed", "Cloud Validation", "Cloud validation failed, refer logs for more details")


        print("=============================================================")

        # Paths
        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\c2clogs.txt"
        ivi_files_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DeviceOnboarding_backup\ivi_files\c2c"

        # Step 1: Capture lifecycle start time
        lifecycle_start_time = datetime.now().replace(microsecond=0)
        print("Waiting before network toggle...")
        time.sleep(300)

        # Step 2: Toggle Wi-Fi
        print("Disabling Wi-Fi...")
        run_command_on_primary_IVI_device(self, deviceSerialNo, "shell cmd -w wifi set-wifi-enabled disabled")
        time.sleep(10)

        print("Enabling Wi-Fi...")
        run_command_on_primary_IVI_device(self, deviceSerialNo, "shell cmd -w wifi set-wifi-enabled enabled")
        time.sleep(10)

        # Step 3: First log pull – check for failure messages
        print("Pulling logs from device...")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        failure_keywords = [
            "MQTTClient_connect5 failed with error: -1",
            "Cloud MQTT connect failed",
            "c2c_edge_cloud_mqtt_init failed",
            "Reconnection failed with cloud",
            "INTERNET IS DOWN ADDING TO LOCAL PRIO QUEUE"
        ]

        failures_found = {}
        try:
            with open(log_file_path, "r", encoding="latin-1", errors="replace") as log_file:
                for line_number, line in enumerate(log_file, 1):
                    for keyword in failure_keywords:
                        if keyword in line:
                            failures_found.setdefault(keyword, []).append((line_number, line.strip()))

            if failures_found:
                print("\nFailure messages found:")
                for keyword, entries in failures_found.items():
                    print(f"\n'{keyword}' occurred {len(entries)} time(s):")
                    for line_number, log_line in entries:
                        print(f"  Line {line_number}: {log_line}")
            else:
                print("No failure messages found.")
        except Exception as e:
            print(f"Error reading log file: {e}")

        # Step 4: Wait before second log pull
        time.sleep(5)

        # Step 5: Second log pull – check for lifecycle messages
        print("Pulling logs from device (second pass)...")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        lifecycle_keywords = {
            "Assumption is certs revoked",
            "Switching to REG_COMMON",
            "cloud_connection_on : 1",
            "constr_and_send_prov_proto_msg success",  # new cert request
            "SV:Message type: 7",  # csr request
            "SV:Message type: 12"
        }

        lifecycle_found = {msg: False for msg in lifecycle_keywords}
        try:
            with open(log_file_path, "r", encoding="latin-1", errors="replace") as log_file:
                for line in log_file:
                    for keyword in lifecycle_keywords:
                        if keyword in line:
                            lifecycle_found[keyword] = True

            print("\nLifecycle message summary:")
            for keyword, found in lifecycle_found.items():
                status = "Found" if found else "✗ Missing"
                print(f"  {status}: {keyword}")
        except Exception as e:
            print(f"Error reading log file: {e}")

        # Step 6: Pull certificate files
        print("\nPulling certificate files...")
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")

        # Step 7: Check certificate timestamps
        print("\nChecking certificate file timestamps...")
        expected_cert_files = [
            "clientcert_reg.pem.crt",
            "clientcert_reg_dev_1.pem.crt",
            "cacert_reg.pem"
        ]

        cert_timestamp_confirmed = False
        for cert_file in expected_cert_files:
            full_path = os.path.join(ivi_files_path, cert_file)
            if os.path.exists(full_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(full_path)).replace(microsecond=0)
                print(f" {cert_file} found with timestamp: {file_time}")
                if file_time >= lifecycle_start_time:
                    cert_timestamp_confirmed = True
            else:
                print(f" {cert_file} not found.")

        # Step 8: Final validation
        print("\nFinal Validation Result:")
        if all(lifecycle_found.values()) and cert_timestamp_confirmed:
            print("Certificate lifecycle validation passed.")
            testResult(self, "passed",
                       "Device should revoke certificate, re-register, reconnect, and resume secure messaging",
                       "Lifecycle completed and certificate timestamp confirmed.")
        else:
            print("Certificate lifecycle validation failed.")
            if not cert_timestamp_confirmed:
                print("Certificate timestamp not confirmed.")
            for keyword, found in lifecycle_found.items():
                if not found:
                    print(f"Missing lifecycle log: {keyword}")
            testResult(self, "verificationFailed",
                       "Device should revoke certificate, re-register, reconnect, and resume secure messaging",
                       "Missing lifecycle logs or certificate timestamp confirmation.")

        time.sleep(10)

        print("=============================================================")
        try:
            print("Read VIN & System Id from device for validations")
            systemId = get_SystemId(self, onboardingType, chipsetType)
            vin = getVIN(self, onboardingType, chipsetType)
            print(f"VIN : =>  {vin}")
            print(f"SystemId : =>  {systemId}")
            pageNo, pageSize = "1", "10"

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")
            response = vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, "regional")
            response_body = response.json()

            print("Validate Life Cycle State @ Cloud post certificate revocation")
            state = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]

            if state in {"REGIONAL_ACTIVE"}:
                testResult(
                    self,
                    "passed",
                    "Life Cycle State should be set to REGIONAL_ACTIVE",
                    f"Life Cycle State is set to REGIONAL_ACTIVE, Rather than found: {state}"
                )
            else:
                testResult(
                    self,
                    "failed",
                    "Life Cycle State should be set to REGIONAL_ACTIVE",
                    f"Life Cycle State is not set to REGIONAL_ACTIVE, Rather than found: {state}"
                )
        except Exception as e:
            print(f"Exception occurred: {e}")
        testResult(self, "failed", "Cloud Validation", "Cloud validation failed, refer logs for more details")

        print("=============================================================")

        print("----------------------------------------------------------")

        print("Validate telemetry after certificate revoke")

        print("----------------------------------------------------------")
        print("Run Telemetry-Odometer stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_odo")
        time.sleep(5)

        print("Telemetry-Odometer stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # Telemetry-Odometer

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute1, telemetry_odo_attribute1)

        if telemetry_odo_attribute1 in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute1} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for odometer",
                       "Device logs contains the logs for odometer, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odometer logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Odometer",
                       "Device logs doesnot contain the logs for Odometer or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odometer value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value):
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")
