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


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test:

    def test_positive_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
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

        #set vacation mode
        vehicle_mode_set_via_cloud(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time, end_time, "Vacation")

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in vacation mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6510",
            "constr_and_send_proto_msg success for 6517",
            "constr_and_send_proto_msg success for 2001",
            "constr_and_send_proto_msg success for 1001"
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
                testResult(self, "failed",
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
        vacationMode_Disabled = read_masterConfJsonFile_v2(self, "VacationMode_Enabled", "vacationMode")

        print(" Vacation Mode - Enabled :", vacationMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if vacationMode_Disabled == "false" or vacationMode_Disabled == False:
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
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")

                # Handle each mode
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False


    def test_positive_incognito_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.incognito_mode"
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

        #set vacation mode
        vehicle_mode_set_via_cloud(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time, end_time, "Incognito")

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in incognito mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6510",
            "constr_and_send_proto_msg success for 6517",
            "constr_and_send_proto_msg success for 1001",
            "constr_and_send_proto_msg success for 2001"
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
                testResult(self, "failed",
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
        incognitoMode_Disabled = read_masterConfJsonFile_v2(self, "IncognitoMode_Enabled", "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if incognitoMode_Disabled == "false" or incognitoMode_Disabled == False:
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
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")

                # Handle each mode
                if "incognito_mode" in vehicle_mode:
                    mode_config = vehicle_mode["incognito_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Incognito Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Incognito Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False


    def test_positive_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
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

        #set vacation mode
        vehicle_mode_set_via_cloud(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time, end_time, "Privacy")

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in privacy mode: ")
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
                testResult(self, "failed",
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
        print("Validate Privacy mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        privacyMode_Disabled = read_masterConfJsonFile_v2(self, "PrivacyMode_Enabled", "privacyMode")

        print(" Privacy Mode - Enabled :", privacyMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if privacyMode_Disabled == "false" or privacyMode_Disabled == False:
            testResult(self, "passed",
                       "Privacy Mode Flag should be set to False in master_conf.json file on device",
                       "Privacy Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       "Privacy Mode Flag should be set to False in master_conf.json file on device",
                           "Privacy Mode Flag is not set to False in master_conf.json file on device")
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
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")

                # Handle each mode
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["privacy_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Privacy Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Privacy Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False