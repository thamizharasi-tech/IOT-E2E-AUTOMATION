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

class Test_Vehicle_Modes_R8_PATCH2:

    def test_positive_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

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

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5"]:
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

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA2","GCP-QA8"]:
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
        vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                   start_time,
                                   end_time, "Vacation")

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "VACATION_MODE":
            testResult(self, "passed", "vehicle mode should be in vacation_mode",
                       f"vehicle mode is in vacation mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in vacation_mode",
                       f"vehicle mode is not in vacation mode")
            assert False
            # self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in vacation mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6500",
            "constr_and_send_proto_msg success for 6501",
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
                if cloudEnv not in r8_patch2_envs:
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

    def test_positive_incognito_mode(self):

        # getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        # time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud side precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if any(cloudEnv in lst for lst in
               (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                #self.result.set_result(TestResults.failed)
                assert False
        elif cloudEnv in r5_envs:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                #self.result.set_result(TestResults.failed)
                assert False
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            # self.result.set_result(TestResults.failed)

        print("--------------------------------------------------------------------------------------")

        print("Run C2C_test_app to accept cloud request")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")
        # Test Data*

        action = "EDIT"
        # path = "vehicle_settings.vehicle_mode.incognito_mode"
        if any(cloudEnv in lst for lst in
               (r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
            path = "vehicle_settings.user_settings.vehicle_mode.incognito_mode"
        else:
            path = "vehicle_settings.vehicle_mode.incognito_mode"
        if cloudEnv in r8_patch_envs_hmac:
            enabled = 1
            disabled = 0
        else:
            enabled = True
            disabled = 0
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
        if cloudEnv in r8_patch4_sp17_envs:
            vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                          start_time,
                                          end_time, "incognitoMode_without_startEndTime")
        else:
            vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                       start_time,
                                       end_time, "Incognito")

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "INCOGNITO_MODE":
            testResult(self, "passed", "vehicle mode should be in incognito_mode",
                       f"vehicle is in incognito mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in incognito_mode",
                       f"vehicle is not in incognito mode")
            #self.result.set_result(TestResults.failed)
            assert False

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in incognito mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        if cloudEnv in r8_patch4_sp17_envs:
            telemetry_msgs = [
                "constr_and_send_proto_msg success for 3101",
                "constr_and_send_proto_msg success for 6500",
                "constr_and_send_proto_msg success for 6501",
                "constr_and_send_proto_msg success for 6506"
            ]
        else:
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

        if cloudEnv in r8_patch4_sp17_envs:

            print(
                "Due to mode disable won't happen automatically , initiating mode switching to normal mode via cluster ( cloud will restrict to trigger the request during incognito mode ) ..")
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "switching_normal_mode_from_cluster")
            time.sleep(10)

            # pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
            # time.sleep(30)
        else:
            pass

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        # Read master_conf.json file
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Validate Incognito mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        incognitoMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled",
                                                            "incognitoMode")

        print(" Incognito Mode - Enabled :", incognitoMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if ((isinstance(incognitoMode_Disabled, str) and incognitoMode_Disabled.strip().lower() in ("false", "0"))
                or incognitoMode_Disabled is False
                or incognitoMode_Disabled == 0):
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
                if any(cloudEnv in lst for lst in
                       (r3_envs, r5_envs, r7_envs, r8_envs, r8_patch1_envs)):
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
                        print("Vacation Mode Disable validation failed")
                        print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=False")
                        #self.result.set_result(TestResults.failed)
                        assert False
                else:
                    print("Invalid or unsupported vehicle mode.")
                    #self.result.set_result(TestResults.failed)
                    assert False

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode",
                       f"vehicle is not in normal mode")

            #self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    def test_positive_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud Side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)
        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            #self.result.set_result(TestResults.failed)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        action = "EDIT"
        # path = "vehicle_settings.vehicle_mode.privacy_mode"
        if cloudEnv in ["GCP-QA4", "GCP-QA2", "GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"
            enabled = 1
        else:
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

        # set vacation mode
        vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                                   end_time, "Privacy")

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "PRIVACY_MODE":
            testResult(self, "passed", "vehicle mode should be in privacy_mode",
                       f"vehicle is in privacy mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in privacy_mode",
                       f"vehicle mode is not in privacy mode")
            assert False
            #self.result.set_result(TestResults.failed)

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
        print("Validate Privacy mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        privacyMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")

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
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")

                # Handle each mode
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["privacy_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Privacy Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Privacy Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    #self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle should be in normal_mode",
                       f"vehicle is not in normal mode")
            assert False
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_positive_vehicle_mode_future_date(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("===================Cloud side precondition================")
        print("----------------------------------------------------------")

        # currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "VACATION_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)
        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "VACATION_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, vacation_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            #self.result.set_result(TestResults.failed)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("--------------------------------------------------------------------------------------")
        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4"]:
            path = "vehicle_settings.vehicle_mode.privacy_mode"
            enabled = True
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"
            enabled = 1
        #enabled = True
        # Get the current start time in milliseconds
        current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        start_time = current_time + 60000  # 1 min

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
        vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                                   end_time, "Privacy")

        time.sleep(60)
        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "PRIVACY_MODE":
            testResult(self, "passed", "vehicle mode should be in privacy_mode",
                       f"vehicle is in privacy mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in privacy_mode",
                       f"vehicle mode is not in privacy mode")
            assert False
            #self.result.set_result(TestResults.failed)

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
        print("Validate Privacy mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        privacyMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "PrivacyMode_Enabled", "privacyMode")

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
                if cloudEnv not in r8_patch2_envs:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")

                # Handle each mode
                if "privacy_mode" in vehicle_mode:
                    mode_config = vehicle_mode["privacy_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Privacy Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Privacy Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        #self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    #self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle is in normal mode")
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle should be in normal_mode",
                       f"vehicle is not in normal mode")
            assert False
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

class Test_Vehicle_Modes_R8_PATCH4S14:

    def test_positive_vacation_mode_r8p4s14(self):

        #getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #time.sleep(20)

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

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA5"]:
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

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA2","GCP-QA8"]:
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
        if cloudEnv in ["GCP-QA2"]:
            vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                          start_time,
                                          end_time, "vacationMode_without_startEndTime")
        else:
            vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                       start_time,
                                       end_time, "Vacation")

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "VACATION_MODE":
            testResult(self, "passed", "vehicle mode should be in vacation_mode",
                       f"vehicle mode is in vacation mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in vacation_mode",
                       f"vehicle mode is not in vacation mode")
            assert False
            # self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in vacation mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6500",
            "constr_and_send_proto_msg success for 6501",
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

        print("Due to mode disable won't happen automatically , initiating mode switching to normal mode..")

        #run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.normal_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA2","GCP-QA8"]:
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

        #pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        #time.sleep(30)

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
                        #self.result.set_result(TestResults.passed)
                    else:
                        print("Vacation Mode Disable validation failed")
                        print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=False")
                        assert False
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

class Test_vehicle_modes:

    def test_vacation_mode_enable(self):

        cloudEnv = read_cloud_env(self)

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        #time.sleep(20)


        if cloudEnv not in ["GCP-QA2"]:
            print("----------------------------------------------------------")
            print("Run Vehicle Mode A2A Test on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

            print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")
        else:
            print("Set vehicle mode precondition on device for speed and lvl2 property")
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("----------------------------------------------------------")



        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
        else:
            path = "vehicle_settings.vehicle_mode.vacation_mode"

        if cloudEnv in ["GCP-QA5","GCP-QA2","GCP-QA8"]:
            enabled = 1
            disabled = 0
        else:
            enabled = True
            disabled = False
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
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "vacationMode_without_startEndTime")

    def test_vacation_mode_disable(self):

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        if cloudEnv in ["GCP-REPL2", "GCP-DEMO2"]:
            getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
            #vehicle_conf_factory_reset(self, systemId)
            #time.sleep(20)

            # Read system id from c2c_vehicle.json file
            systemId = read_vehicleJsonFile(self, "system_id")

            # Test Data*

            action = "EDIT"
            if cloudEnv in ["GCP-QA4", "GCP-QA5","GCP-QA2","GCP-QA8"]:
                path = "vehicle_settings.user_settings.vehicle_mode.vacation_mode"
            else:
                path = "vehicle_settings.vehicle_mode.vacation_mode"

            if cloudEnv in ["GCP-QA5","GCP-QA2","GCP-QA8"]:
                enabled = 1
                disabled = 0
            else:
                enabled = True
                disabled = False
            # Get the current start time in milliseconds
            start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

            # Calculate end time for 5 minutes later
            #end_time = start_time + 300000  # 5 minutes in milliseconds

            print("----------------------------------------------------------")
            print("System Id :", systemId)
            print("Action :", action)
            print("Path :", path)
            print("Start Time :", start_time)
            print("End Time :", end_time)
            print("----------------------------------------------------------")

            # set vacation mode
            vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                           end_time, "vacationMode_without_startEndTime")
        else:

            print("Set vehicle mode precondition on device for speed and lvl2 property")
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vacation_mode_disable")

            print("--------------------------------------------------------------------------------------")

            pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
            time.sleep(30)
            print("# # # # # # # # # # # # # # # # # # # # # # # # ")
            print("Validate Vacation mode is disabled in master_conf.json : ")
            print("# # # # # # # # # # # # # # # # # # # # # # # # ")

            # Read master_conf.json file
            vacationMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "VacationMode_Enabled", "vacationMode")

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
                    if cloudEnv not in ["GCP-QA4", "GCP-QA5"]:
                        vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")
                    else:
                        vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get(
                            "vehicle_mode")

                    # Handle each mode
                    if "vacation_mode" in vehicle_mode:
                        mode_config = vehicle_mode["vacation_mode"]
                        if mode_config["enabled"] == "false" or mode_config["enabled"] == False or mode_config["enabled"] == 0:
                            testResult(self, "passed",
                                       "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                       "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                            assert True
                            # self.result.set_result(TestResults.passed)
                    else:
                        print("Invalid or unsupported vehicle mode.")
                        assert False
                        # self.result.set_result(TestResults.failed)

    def test_privacy_mode_enable(self):

        cloudEnv = read_cloud_env(self)
        if cloudEnv in ["GCP-QA2","GCP-QA8"]:
            print("----------------------------------------------------------")
            print("Run Vehicle Mode A2A Test on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

            print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA2", "GCP-QA8"]:
            path = "vehicle_settings.vehicle_mode.privacy_mode"
            enabled = True
            disabled = False
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"
            enabled = 1
            disabled = 0

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
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "privacyMode_without_startEndTime")

    def test_privacy_mode_disable(self):

        cloudEnv = read_cloud_env(self)

        if cloudEnv not in ["GCP-QA2", "GCP-QA8"]:
            print("----------------------------------------------------------")
            print("Run Vehicle Mode A2A Test on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

            print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA2", "GCP-QA8"]:
            path = "vehicle_settings.vehicle_mode.privacy_mode"
            enabled = True
            disabled = False
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.privacy_mode"
            enabled = 1
            disabled = 0

        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "privacyMode_without_startEndTime")

    def test_incognito_mode_enable(self):

        cloudEnv = read_cloud_env(self)

        if cloudEnv not in ["GCP-QA2","GCP-QA8"]:
            print("----------------------------------------------------------")
            print("Run Vehicle Mode A2A Test on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

            print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.vehicle_mode.incognito_mode"
            enabled = True
            disabled = False
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.incognito_mode"
            enabled = 1
            disabled = 0

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
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "incognitoMode_without_startEndTime")

    def test_incognito_mode_disable(self):

        cloudEnv = read_cloud_env(self)
        if cloudEnv not in ["GCP-QA2", "GCP-QA8"]:
            print("----------------------------------------------------------")
            print("Run Vehicle Mode A2A Test on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

            print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vm_delta_change")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        if cloudEnv not in ["GCP-QA2"]:
            action = "EDIT"
            if cloudEnv not in r8_patch2_envs:
                path = "vehicle_settings.vehicle_mode.incognito_mode"
            else:
                path = "vehicle_settings.user_settings.vehicle_mode.incognito_mode"
            enabled = True
            disabled = False
            # Get the current start time in milliseconds
            start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

            # Calculate end time for 5 minutes later
            #end_time = start_time + 300000  # 5 minutes in milliseconds

            print("----------------------------------------------------------")
            print("System Id :", systemId)
            print("Action :", action)
            print("Path :", path)
            print("Start Time :", start_time)
            print("End Time :", end_time)
            print("----------------------------------------------------------")

            # set vacation mode
            vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                           end_time, "incognitoMode_without_startEndTime")
        else:
            print("Due to mode disable won't happen automatically , initiating mode switching to normal mode via cluster..")
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "switching_normal_mode_from_cluster")
            time.sleep(10)

            pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
            time.sleep(30)

            print("# # # # # # # # # # # # # # # # # # # # # # # # ")
            print("Validate Vacation mode is disabled in master_conf.json : ")
            print("# # # # # # # # # # # # # # # # # # # # # # # # ")

            # Read master_conf.json file
            print("# # # # # # # # # # # # # # # # # # # # # # # # ")
            print("Validate Incognito mode is disabled in master_conf.json : ")
            print("# # # # # # # # # # # # # # # # # # # # # # # # ")

            # Read master_conf.json file
            incognitoMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "IncognitoMode_Enabled",
                                                                "incognitoMode")

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
                    if cloudEnv not in ["GCP-QA2"]:
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
                            print("Vacation Mode Disable validation failed")
                            print(f"Enabled mismatch: actual={mode_config['enabled']}, expected=False")
                            #self.result.set_result(TestResults.failed)
                            assert False
                    else:
                        print("Invalid or unsupported vehicle mode.")
                        #self.result.set_result(TestResults.failed)
                        assert False

            # Validate vehicle mode in vehicle state API

            currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
                self,
                cloudEnv,
                systemId,
                "regional")

            if vehicleMode == "NORMAL_MODE":
                testResult(self, "passed", "vehicle mode should be in normal_mode",
                           f"vehicle is in normal mode")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "vehicle mode should be in normal_mode",
                           f"vehicle is not in normal mode")

                #self.result.set_result(TestResults.failed)
                assert False

            print("----------------------------------------------------------")

class Test_vehConf_normalMode:

    def test_telemetry_conf_normal(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemetry_push_frequency_update(self, onboardingType, chipsetType, "normal_mode")

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 15000
        time.sleep(60)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_normal(self):

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run cstub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("CSTUB - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("Command - Device Precondition")
        print("----------------------------------------------------------")

        # Setup precondition on device
        systemId = read_vehicleJsonFile(self, "system_id")
        dt = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        print(f"Current date & time: {dt}")
        print("Set preconditions on device by running paho commands")
        print("----------------------------------------------------------")

        # Run ignition stub
        print("--> Run Telemetry-Ignition LVL1 stub on device")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType,
                                        "command_precondition_ignition_lvl1")
        time.sleep(5)
        print("Telemetry-Ignition LVL1 stub completed. Verifying logs...")
        print("----------------------------------------------------------")

        # Pull logs from device
        print("Pull/Fetch device logs for validation")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs fetched to host machine")
        print("----------------------------------------------------------")

        # Device-side validation: Ignition
        print("Device Side Validations")
        ls = verify_message_in_log(self, Command_ignition_lvl1_attribute, Command_ignition_lvl1_attribute)

        if Command_ignition_lvl1_attribute in str(ls[0]):
            print(f"Ignition Off attribute found: '{Command_ignition_lvl1_attribute}'")
            testResult(self, "passed", "Device logs should contain Ignition Off",
                       "Device logs verified for Ignition Off")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("Ignition Off logs missing or unreadable")
            testResult(self, "verificationFailed", "Device logs should contain Ignition Off",
                       "Device logs missing or unreadable")

        print("----------------------------------------------------------")

        # Cloud-side validation: Ignition
        print("Cloud Side Validations")
        telemetry_ignition_event_type = 6502
        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""
        try:
            for signal in response_body["responseData"]["signals"]:
                if signal["name"] == Command_ignition_lvl1_attribute:
                    value = signal["value"]
                    reasonCode = signal["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("Signal list empty in API response")

        print("Ignition Lvl-1 value configured in the stub:", Command_ignition_lvl1_value)
        print("Ignition Lvl-1 value stored in Cloud DB:", value)

        if int(value) == int(Command_ignition_lvl1_value):
            testResult(
                self, "passed",
                "Ignition Lvl-1 value should be stored in the Cloud DB and match the stub configuration",
                "Ignition Lvl-1 value is stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ignition Lvl-1 value should be stored in the Cloud DB and match the stub configuration",
                "Ignition Lvl-1 value is not stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
        print("-------------------------------------------------------------------------")
        time.sleep(5)

        print("----------------------------------------------------------")
        print("2. Run stub for Ride Mode PARK")
        print("----------------------------------------------------------")

        # Run Ride Mode stub
        print("Run stub for Ride Mode PARK simulation")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_park")
        time.sleep(5)
        print("Stub execution completed. Verifying logs...")
        print("----------------------------------------------------------")

        # Pull logs again
        print("Pull/Fetch device logs for validation")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs fetched to host machine")
        print("----------------------------------------------------------")

        # Device-side validation: Ride Mode
        print("Device Side Validations")
        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_12
        ls = verify_message_in_log(self, telemetry_ridemode_value_12, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ride Mode attribute found: '{telemetry_attribute_ridemode}'")
            testResult(self, "passed", "Device logs should contain Ride Mode",
                       "Ride Mode telemetry verified in device logs")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("Ride Mode logs missing or unreadable")
            testResult(self, "verificationFailed", "Device logs should contain Ride Mode",
                       "Ride Mode telemetry missing or unreadable")

        print("----------------------------------------------------------")

        # Cloud-side validation: Ride Mode
        print("Cloud Side Validations")
        telemetry_speed_event_type = 6500
        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""
        try:
            for signal in response_body["responseData"]["signals"]:
                if signal["name"] == telemetry_attribute_ridemode:
                    value = signal["value"]
                    reasonCode = signal["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("Signal list empty in API response")

        print("Ride Mode value configured in the stub:", telemetry_ridemode_value_12)
        print("Ride Mode value stored in Cloud DB:", value)

        if int(value) == int(telemetry_ridemode_value_12):
            testResult(
                self, "passed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        print("----------------------------------------------------------")
        print("3. Run stub on device: DTC")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)
        print("Stub run completed. Verify logs for alert details.")
        print("----------------------------------------------------------")

        print("-----------------------------------------------------------")
        print("4. Command - Cloud Precondition")
        print("-----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if (connectionState == "CONNECTED" and rideMode == "PARK" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE",
                                                                                      "INCOGNITO_MODE"] and currentState == "ACTIVE"):
            testResult(self, "passed", "Cloud precondition should satisfy to publish the command",
                       "Cloud precondition is satisfied to publish the geofence")
            assert True
        else:
            testResult(self, "failed", "Cloud precondition should satisfy to publish the command",
                       "Cloud precondition is not satisfied to publish the command")
            assert False

        print("------------------------------------------")
        print("5. Initiate Command - VEHICLE LOCK via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print(f"Name: {name}")
        print(f"System Id: {systemId}")
        print(f"APP Id: {appId}")
        print(f"Time: {time_value}")
        print(f"Area: {area}")
        print(f"Value: {value}")
        print(f"Timeout: {timeout}")

        response = commandControl_Service_Request(self, name, systemId, appId, area, value, timeout, "valid")

        print("------------------------------------------")
        print("Device Validations for initiated command")
        print("------------------------------------------")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response")
        print("------------------------------------------")

        actual_status = ""
        expected_status = expected_success_status

        try:
            response = response.json()
            trackingId = read_commandCtrl_trackingId(self, response)
            response = commandControl_Service_Tracking(self, trackingId, "valid")
            response = response.json()
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed", f"The Command status should be {expected_status}",
                           f"The Command status is {actual_status}")
            else:
                testResult(self, "failed", f"The Command status should be {expected_status}",
                           f"The Command status is not {expected_status}, rather it is '{actual_status}' or something went wrong. Refer to API response.")
        except:
            testResult(self, "failed", f"The Command status should be {expected_status}",
                       f"The Command status is not {expected_status} or something went wrong. Refer to API response.")

        print("-------------------------------------------------------------------------")

    def test_cmd_precondition_normal_invalid(self):

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run cstub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("CSTUB - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("Command - Device Precondition")
        print("----------------------------------------------------------")

        # Setup precondition on device
        systemId = read_vehicleJsonFile(self, "system_id")
        dt = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        print(f"Current date & time: {dt}")
        print("Set preconditions on device by running paho commands")
        print("----------------------------------------------------------")

        # Run ignition stub
        print("--> Run Telemetry-Ignition LVL1 stub on device")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType,
                                        "command_precondition_ignition_lvl1_invalid")
        time.sleep(5)
        print("Telemetry-Ignition LVL1 stub completed. Verifying logs...")
        print("----------------------------------------------------------")

        # Pull logs from device
        print("Pull/Fetch device logs for validation")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs fetched to host machine")
        print("----------------------------------------------------------")

        # Device-side validation: Ignition
        print("Device Side Validations")
        ls = verify_message_in_log(self, Command_ignition_lvl1_attribute, Command_ignition_lvl1_attribute)

        if Command_ignition_lvl1_attribute in str(ls[0]):
            print(f"Ignition Off attribute found: '{Command_ignition_lvl1_attribute}'")
            testResult(self, "passed", "Device logs should contain Ignition Off",
                       "Device logs verified for Ignition Off")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("Ignition Off logs missing or unreadable")
            testResult(self, "verificationFailed", "Device logs should contain Ignition Off",
                       "Device logs missing or unreadable")

        print("----------------------------------------------------------")

        # Cloud-side validation: Ignition
        print("Cloud Side Validations")
        telemetry_ignition_event_type = 6502
        Command_ignition_lvl1_value = "11"
        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""
        try:
            for signal in response_body["responseData"]["signals"]:
                if signal["name"] == Command_ignition_lvl1_attribute:
                    value = signal["value"]
                    reasonCode = signal["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("Signal list empty in API response")

        print("Ignition Lvl-1 value configured in the stub:", Command_ignition_lvl1_value)
        print("Ignition Lvl-1 value stored in Cloud DB:", value)

        if int(value) == int(Command_ignition_lvl1_value):
            testResult(
                self, "passed",
                "Ignition Lvl-1 value should be stored in the Cloud DB and match the stub configuration",
                "Ignition Lvl-1 value is stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ignition Lvl-1 value should be stored in the Cloud DB and match the stub configuration",
                "Ignition Lvl-1 value is not stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
        print("-------------------------------------------------------------------------")
        time.sleep(5)

        print("----------------------------------------------------------")
        print("2. Run stub for Ride Mode PARK")
        print("----------------------------------------------------------")

        # Run Ride Mode stub
        print("Run stub for Ride Mode PARK simulation")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_park")
        time.sleep(5)
        print("Stub execution completed. Verifying logs...")
        print("----------------------------------------------------------")

        # Pull logs again
        print("Pull/Fetch device logs for validation")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs fetched to host machine")
        print("----------------------------------------------------------")

        # Device-side validation: Ride Mode
        print("Device Side Validations")
        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_12
        ls = verify_message_in_log(self, telemetry_ridemode_value_12, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ride Mode attribute found: '{telemetry_attribute_ridemode}'")
            testResult(self, "passed", "Device logs should contain Ride Mode",
                       "Ride Mode telemetry verified in device logs")
            print("c2c logs line data:", ls[0])
        elif str(ls[0]) == "Error":
            print("Ride Mode logs missing or unreadable")
            testResult(self, "verificationFailed", "Device logs should contain Ride Mode",
                       "Ride Mode telemetry missing or unreadable")

        print("----------------------------------------------------------")

        # Cloud-side validation: Ride Mode
        print("Cloud Side Validations")
        telemetry_speed_event_type = 6500
        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""
        try:
            for signal in response_body["responseData"]["signals"]:
                if signal["name"] == telemetry_attribute_ridemode:
                    value = signal["value"]
                    reasonCode = signal["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("Signal list empty in API response")

        print("Ride Mode value configured in the stub:", telemetry_ridemode_value_12)
        print("Ride Mode value stored in Cloud DB:", value)

        if int(value) == int(telemetry_ridemode_value_12):
            testResult(
                self, "passed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is stored in the Cloud DB and matches the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        print("----------------------------------------------------------")
        print("3. Run stub on device: DTC")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)
        print("Stub run completed. Verify logs for alert details.")
        print("----------------------------------------------------------")

        print("-----------------------------------------------------------")
        print("4. Command - Cloud Precondition")
        print("-----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if (connectionState == "CONNECTED" and rideMode == "PARK" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE",
                                                                                      "INCOGNITO_MODE"] and currentState == "ACTIVE"):
            testResult(self, "passed", "Cloud precondition should satisfy to publish the command",
                       "Cloud precondition is satisfied to publish the geofence")
            assert True
        else:
            testResult(self, "failed", "Cloud precondition should satisfy to publish the command",
                       "Cloud precondition is not satisfied to publish the command")
            assert False

        print("------------------------------------------")
        print("5. Initiate Command - VEHICLE LOCK via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print(f"Name: {name}")
        print(f"System Id: {systemId}")
        print(f"APP Id: {appId}")
        print(f"Time: {time_value}")
        print(f"Area: {area}")
        print(f"Value: {value}")
        print(f"Timeout: {timeout}")

        response = commandControl_Service_Request(self, name, systemId, appId, area, value, timeout, "valid")

        print("------------------------------------------")
        print("Device Validations for initiated command")
        print("------------------------------------------")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response")
        print("------------------------------------------")

        actual_status = ""
        expected_status = "FAILED"

        try:
            response = response.json()
            trackingId = read_commandCtrl_trackingId(self, response)
            response = commandControl_Service_Tracking(self, trackingId, "valid")
            response = response.json()
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed", f"The Command status should be {expected_status}",
                           f"The Command status is {actual_status}")
            else:
                testResult(self, "failed", f"The Command status should be {expected_status}",
                           f"The Command status is not {expected_status}, rather it is '{actual_status}' or something went wrong. Refer to API response.")
        except:
            testResult(self, "failed", f"The Command status should be {expected_status}",
                       f"The Command status is not {expected_status} or something went wrong. Refer to API response.")

        print("-------------------------------------------------------------------------")

    def test_over_speed_alert_normal(self):

        #systemId = read_vehicleJsonFile(self, "system_id")
        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "normal_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "normal_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_vacationMode:

    def test_telemetry_conf_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemetry_push_frequency_update(self, onboardingType, chipsetType, "vacation_mode")
        time.sleep(120)

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 20000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_vacation(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "vacation_mode")

    def test_alert_over_speed_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "vacation_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "vacation_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "vacation_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_privacyMode:

    def test_telemetry_conf_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        cloudEnv = read_cloud_env(self)

        vehicle_conf_telemetry_push_frequency_update(self, onboardingType, chipsetType, "privacy_mode")
        time.sleep(120)

        if cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "RE-DEV", "RE-DM1"]:
            telemetry_msgs = ["constr_and_send_proto_msg success for 6500"]
            event_id = 6500
            push_freq = 11000
        else:
            telemetry_msgs = ["constr_and_send_proto_msg success for 1001"]
            event_id = 1001
            push_freq = 11000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_privacy(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_alert_over_speed_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "privacy_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "privacy_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_incognitoMode:

    def test_cmd_precondition_incognito(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_alert_over_speed_incognito(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "incognito_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "incognito_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_periodic_syncup:

    def test_vacation_mode_enable_periodic_syncup(self):

        # 1.Insert tyre pressure in master conf file in local folder
        print("==> 1.Adding tyre pressure in local folder")
        systemId = read_vehicleJsonFile(self, "system_id")

        update_master_conf(self, "insert_tyrePressure")

        # --------------------------------
        # update factory conf
        # --------------------------------

        model = fetch_vehicle_model_by_systemId(self, systemId)
        # model = "Cruiser"

        # 2.update factory conf on the cloud
        print("==> 2. Updating Factory Conf")
        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            # self.result.set_result(TestResults.failed)

        # 3. Do the factory reset to reflect updated factory conf on the cloud
        print("==> 3. Factory Reset")
        vehicle_conf_factory_reset(self, systemId)

        # trigger vacation mode
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("==> 4. Trigger Vacation Mode vai Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 180000  # 1 min

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

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
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should be triggered successfully",
                           "Vacation Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vacation Mode - Configuration update should be triggered successfully",
                       "Vacation Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationFailed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 400:
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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "FAILED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert False
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("==>5. Validating file upload during periodic syncUp")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2clogs\c2clogs.txt"  # Update with actual path

        pattern = r'CM_FU:recieved file name :(\S+\.json)'  # Regex pattern to capture filename

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_data = file.read()

        match = re.search(pattern, log_data)
        if match:
            filename = match.group(1)
            print(f"Extracted filename: {filename}")
        else:
            print("No matching filename found.")

        print("==>6. Get Presigned Url")
        response = ddl_get_presigned_url(self, systemId, filename, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            download_link = response_body["fileMetadata"]["downloadLink"]
            fileName = response_body["fileMetadata"]["fileName"]
            expirationDate = response_body["fileMetadata"]["expirationDate"]

            print(" Download link: ", download_link)
            print("File Name: ", fileName)
            print("Expiration Date: ", expirationDate)

            testResult(self, "verificationPassed", "File should Uploaded successfully on the cloud",
                       "File successfully uploaded on the cloud")
        else:
            testResult(self, "verificationFailed", "File should Uploaded successfully on the cloud",
                       "File not uploaded on the cloud or filename not found in the device log")

        print("==> Trigger vacation Mode request after periodic syncup")

        # set vacation mode
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
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should be triggered successfully",
                           "Vacation Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vacation Mode - Configuration update should be triggered successfully",
                       "Vacation Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    def test_vacation_mode_enable_periodic_syncup_v2(self):

        # 1.Insert tyre pressure in master conf file in local folder
        print("==> 1.Adding tyre pressure in local folder")
        systemId = read_vehicleJsonFile(self, "system_id")

        update_master_conf(self, "insert_tyrePressure")

        # --------------------------------
        # update factory conf
        # --------------------------------

        model = fetch_vehicle_model_by_systemId(self, systemId)
        # model = "Cruiser"

        # 2.update factory conf on the cloud
        print("==> 2. Updating Factory Conf")
        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            # self.result.set_result(TestResults.failed)

        # 3. Do the factory reset to reflect updated factory conf on the cloud
        print("==> 3. Factory Reset")
        vehicle_conf_factory_reset(self, systemId)

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")
        # trigger vacation mode
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("==> 4. Trigger Vacation Mode vai Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 180000  # 1 min

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

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
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should be triggered successfully",
                           "Vacation Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vacation Mode - Configuration update should be triggered successfully",
                       "Vacation Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationFailed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 400:
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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "FAILED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert False
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("==>5. Validating file upload during periodic syncUp")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Extract filename from logs
        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2clogs\c2clogs.txt"
        pattern = r'CM_FU:recieved file name :(\S+\.json)'

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_data = file.read()

        match = re.search(pattern, log_data)
        if match:
            filename = match.group(1).strip().lower()
            print(f"[DEBUG] Extracted filename from logs: '{filename}'")
        else:
            print("No matching filename found in logs.")
            assert False

        print("==>6. Get file metadata")

        offset = 1
        limit = 100
        match_found = False

        while True:
            response = ddl_get_file_metadata(self, str(offset), str(limit), systemId, "systemId")

            if response.status_code == 200:
                response_body = response.json()

                if response_body["message"] == "Data Fetched Successfully":
                    pageNo = response_body["pageNo"]
                    pageSize = response_body["pageSize"]
                    totalPages = response_body["totalPages"]
                    totalRecords = response_body["totalRecords"]

                    print("Page No: ", pageNo)
                    print("Page Size: ", pageSize)
                    print("Total Pages: ", totalPages)
                    print("Total Records: ", totalRecords)

                    data_len = len(response_body["metaData"])
                    print("[DEBUG] Available filenames in metadata:")
                    for i in range(data_len):
                        file_name = response_body["metaData"][i]["file-name"].strip().lower()
                        print(f"  - {file_name}")

                    if data_len >= 1:
                        for i in range(data_len):
                            uploadId = response_body["metaData"][i]["uploadId"]
                            system_id = response_body["metaData"][i]["system_id"]
                            file_upload_time = response_body["metaData"][i]["file-upload-time"]
                            file_name = response_body["metaData"][i]["file-name"].strip().lower()

                            print(
                                f"[DEBUG] Comparing metadata filename: '{file_name}' with extracted filename: '{filename}'")

                            if file_name == filename:
                                print("Upload Id: ", uploadId)
                                print("System Id: ", system_id)
                                print("file_upload_time: ", file_upload_time)
                                print("file_name: ", file_name)
                                testResult(self, "passed",
                                           "File metadata details should be fetched successfully for the respective vehicle",
                                           "File metadata details are fetched successfully for the vehicle")
                                match_found = True
                                break

                    if match_found or offset >= response_body["totalPages"]:
                        break

                    offset += 1

                else:
                    print("Response message is not expected. Rather than found: ", response_body["message"])
                    assert False

            elif response.status_code == 204:
                print("No data available")
                assert False
            else:
                print("Response status code is not expected. Rather than found: ", response.status_code)
                assert False

        if not match_found:
            print(f"[ERROR] Matching filename '{filename}' not found in metadata records")
            assert False

        print("==> Trigger vacation Mode request after periodic syncup")

        # set vacation mode
        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")
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
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "Vacation Mode - Configuration update should be triggered successfully",
                           "Vacation Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vacation Mode - Configuration update should be triggered successfully",
                       "Vacation Mode - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")


class Test_Remote_Diagnostic_Mode:

    def test_positive_remote_diagnostic_mode(self):

        #getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud Side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                assert True
                # self.result.set_result(TestResults.passed)
        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                assert True
                # self.result.set_result(TestResults.passed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            assert False
            # self.result.set_result(TestResults.failed)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        action = "EDIT"
        # path = "vehicle_settings.vehicle_mode.privacy_mode"
        if cloudEnv in ["GCP-QA4", "GCP-QA5"]:
            path = "vehicle_settings.user_settings.vehicle_mode.remote_diagnostic_mode"
        else:
            path = "vehicle_settings.vehicle_mode.remote_diagnostic_mode"
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
        vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                   start_time,
                                   end_time, "RemoteDiagnostic")

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "REMOTE_DIAGNOSTIC":
            testResult(self, "passed", "vehicle mode should be in remote_diagnostic_mode",
                       f"vehicle is in remote diagnostic mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle mode should be in remote_diagnostic_mode",
                       f"vehicle mode is not in remote diagnostic mode")
            assert False
            # self.result.set_result(TestResults.failed)

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in remote diagnostic mode: ")
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
        print("Validate Privacy mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        remoteDiagnosticMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_Enabled",
                                                                   "remoteDiagnosticMode")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if remoteDiagnosticMode_Disabled == "false" or remoteDiagnosticMode_Disabled == False:
            testResult(self, "passed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is not set to False in master_conf.json file on device")
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
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")

                # Handle each mode
                if "remote_diagnostic_mode" in vehicle_mode:
                    mode_config = vehicle_mode["remote_diagnostic_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Remote Diagnostic Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Remote Diagnostic Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                        # self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    assert False
                    # self.result.set_result(TestResults.failed)

        # Validate vehicle mode in vehicle state API

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "vehicle mode should be in normal_mode",
                       f"vehicle is in normal mode")
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "vehicle should be in normal_mode",
                       f"vehicle is not in normal mode")
            assert False
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_remote_diagnostic_mode_enable(self):


        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in r8_patch2_envs:
            path = "vehicle_settings.vehicle_mode.remote_diagnostic_mode"
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.remote_diagnostic_mode"
        enabled = True
        disabled = False
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
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "remoteDiagnosticMode_without_startEndTime")

    def test_remote_diagnostic_mode_file_upload_1002(self):

        print("Remote Diagnostic file upload will happen every 5 mins during the remote diagnostic mode")

        print("Waiting for 5 minutes....")

        #time.sleep(300)
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        successful_filenames = get_and_download_ddl_file_v2(self, systemId,"REMOTE_DIAGNOSTIC_FILE", "ROLE_MASKED")
        # decompress_downloaded_files_from_folder_v2(self, "ROLE_MASKED", successful_filenames)
        #decompress_downloaded_files_from_folder_v3(self, "REMOTE_DIAGNOSTIC_FILE", successful_filenames, onboardingType,
         #                                          chipsetType)
        validate_telemetry_data_from_decompressed_file_v2(self, cloudEnv, "REMOTE_DIAGNOSTIC_FILE","ROLE_MASKED")

    def test_ddl_file_upload_15(self):

        print("Remote Diagnostic file upload will happen every 5 mins during the remote diagnostic mode")

        print("Waiting for 5 minutes....")

        #time.sleep(300)
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        successful_filenames = get_and_download_ddl_file_v2(self, systemId,"DDL_FILE", "ROLE_UNMASKED")
        # decompress_downloaded_files_from_folder_v2(self, "ROLE_MASKED", successful_filenames)
        #decompress_downloaded_files_from_folder_v3(self, "DDL_FILE", successful_filenames, onboardingType,chipsetType)
        validate_telemetry_data_from_decompressed_file_v2(self, cloudEnv, "DDL_FILE","ROLE_UNMASKED")

    def test_remote_diagnostic_mode_disable(self):

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in r8_patch2_envs:
            path = "vehicle_settings.vehicle_mode.remote_diagnostic_mode"
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.remote_diagnostic_mode"
        enabled = True
        disabled = False
        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "remoteDiagnosticMode_without_startEndTime")

class Test_Remote_Diagnostic_Mode_R8P14:

    def test_positive_remote_diagnostic_mode_r8p4s14(self):

        # Now file sync up will happan during the onboarding process and no need to set the configuration files, thus commented
        # getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        # time.sleep(20)
        # getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        # time.sleep(20)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud Side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in r8_patch4_sp17_envs:
            if rideState == "AT_REST" and vehicleMode in ["NORMAL_MODE", "SERVICE_MODE"] and rideMode == "PARK":
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                           f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("invalid cloudEnv")

        #model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger EDIT FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        if cloudEnv in r8_patch4_sp17_envs:
            path = "vehicle_settings.user_settings.remote_diagnostic"
        value = 1
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Value :", value)
        print("----------------------------------------------------------")

        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 600000  # 10 minutes in milliseconds

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, "", value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            #self.result.set_result(TestResults.failed)
            assert False

        # Validate response body - Extract and verify timestamp
        print("----------------------------------------------------------")
        print("TIMESTAMP VALIDATION FROM RESPONSE BODY")
        print("----------------------------------------------------------")
        
        # Try to extract timestamp from various possible attributes
        response_timestamp = (response_body.get("timestamp") or 
                             response_body.get("createdAt") or 
                             response_body.get("updatedAt") or 
                             response_body.get("requestTime") or
                             response_body.get("updateTime"))
        
        print(f"Current time: {current_time} ms")
        print(f"End time: {end_time} ms")
        print(f"Response timestamp: {response_timestamp}")
        
        if response_timestamp:
            # Verify timestamp is within the valid time window
            if current_time <= response_timestamp <= end_time:
                testResult(self, "passed",
                          "Response timestamp should be within current and end time range",
                          f"Response timestamp {response_timestamp} is between {current_time} and {end_time}")
                print(f" => Timestamp validation passed: {response_timestamp} is within range")
            else:
                testResult(self, "verificationFailed",
                          "Response timestamp should be within current and end time range",
                          f"Response timestamp {response_timestamp} is NOT between {current_time} and {end_time}")
                print(f" => Timestamp validation failed: {response_timestamp} is outside range")
        else:
            print("Warning: No timestamp attribute found in response body")
            print("Available attributes:", list(response_body.keys()))

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "EDIT Feature - Configuration update should be triggered successfully",
                           "EDIT Feature - Configuration update is triggered successfully")
                assert True
                #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is not triggered successfully")
            #self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation - Configuration status by trackingId: ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed", "EDIT Feature - Configuration update should  be 'PROGRESSING'",
                           "EDIT Feature - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "EDIT Feature- Configuration update should success/completed",
                       "EDIT Feature - Configuration update is success/completed")
            assert True
            #self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "EDIT Feature - Configuration update should success/completed",
                       "EDIT Feature - Configuration update is not success/completed")
            #self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("VALIDATE UPDATED CONFIGURATION IN MASTER_CONF.JSON")

        # Read master_conf.json file
        remoteDiagnostic_value = read_masterConfJsonFile_v2(self, cloudEnv, "remote_diagnostic", "remote_diagnostic")

        status = ""

        if remoteDiagnostic_value == value:
            testResult(self, "passed", "Remote Diagnostic value should be updated in master_conf.json file on device",
                       "Remote Diagnostic feature value is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Remote Diagnostic feature value should be updated in master_conf.json file on device",
                       "Remote Diagnostic feature value is not updated in master_conf.json file on device")
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

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv in r8_patch4_sp17_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["user_settings"]

                # Check for 'tyre_pressure' feature
                if "remote_diagnostic" in vehicle_features:
                    if vehicle_features["remote_diagnostic"] == value:
                        testResult(self, "passed",
                                   "Remote Diagnostic Feature and value should be present in the vehicle configuration",
                                   "Remote Diagnostic Feature and value is present in the vehicle configuration.")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        print("Remote Diagnostic value does not match the expected value.")

                        #self.result.set_result(TestResults.failed)
                        assert False
                else:
                    # Log an error if 'tyre_pressure' feature is missing
                    print("Remote Diagnostic feature is not found in vehicle features.")
                    testResult(self, "failed",
                               "Remote Diagnostic Feature should be present in the vehicle configuration",
                               "'Remote Diagnostic' feature is missing in the vehicle configuration.")
                    #self.result.set_result(TestResults.failed)
                    assert False
            else:
                print("Unexpected response message:", response_body["message"])
                #self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            #self.result.set_result(TestResults.failed)
            assert False

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in remote diagnostic mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 6504",
            "constr_and_send_proto_msg success for 6505",
            "constr_and_send_proto_msg success for 6506"
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
                testResult(self, "Passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs.\n")
                testResult(self, "verificationFailed",
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

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odometer value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response1 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type1, systemId, "valid")
        response2 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type2, systemId, "valid")
        response3 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type3, systemId, "valid")

        if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
            testResult(self, "passed", "Should send telemetry block 6504, 6505 and 6506 during remote diagnostic mode", "Telemetry block 6504, 6505 and 6506 is sending during remote dianostic")
        else:
            testResult(self, "failed", "Should send telemetry block 6504, 6505 and 6506 during remote diagnostic mode",
                       "Telemetry block 6504, 6505 and 6506 is not sending during remote dianostic")

        # Parse API response into JSON
        response1_body = response1.json()
        response2_body = response2.json()
        response3_body = response3.json()

        responses = [response1_body, response2_body, response3_body]

        valid = []  # Track validity of each response
        timestamps = []

        try:
            for idx, resp in enumerate(responses, 1):
                signals = resp.get("responseData", {}).get("signals", [])
                updated_time = None

                if signals and isinstance(signals, list):
                    first_signal = signals[0]
                    if isinstance(first_signal, dict):
                        updated_time = first_signal.get("updatedTime")

                timestamps.append(updated_time)
                print(f"Response {idx} updatedTime: {updated_time}")

                if updated_time is None:
                    print(f"  => Response {idx} has no updatedTime available in the first signal. Validation cannot be completed for this response.")
                    valid.append(False)
                else:
                    if start_time <= updated_time <= end_time:
                        print(f"  => Response {idx} updatedTime {updated_time} is inside the expected window [{start_time}, {end_time}].")
                        valid.append(True)
                    else:
                        print(f"  => Response {idx} updatedTime {updated_time} is outside the expected window [{start_time}, {end_time}].")
                        valid.append(False)

        except KeyError as e:
            print(f"Missing key in response: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("\n----- SUMMARY -----")
        print(f"Collected updatedTime values: {timestamps}")

        if all(valid):
            print("All timestamps are valid")
            testResult(
                self, "passed",
                "All telemetry messages received during remote diagnostic mode with valid timestamps",
                "All 3 telemetry blocks (6504, 6505, 6506) received within remote diagnostic time window"
            )
        else:
            print("Some timestamps are invalid")
            testResult(
                self, "verificationFailed",
                "Some telemetry messages missing or have invalid timestamps",
                "Some telemetry messages missing or have invalid timestamps"
            )

        print("\n" + "=" * 80)
        print("REMOTE DIAGNOSTIC MODE MESSAGE RECEIPT SUMMARY")
        print("=" * 80)
        print(f"Remote Diagnostic Window: {start_time} to {end_time}")
        print("Telemetry Blocks Expected: 6504, 6505, 6506")

        print("\nMessage Receipt Status:")
        for idx, is_valid in enumerate(valid, 1):
            status = "VALID" if is_valid else "INVALID"
            print(f"  Response {idx}: {status}")

        print("=" * 80)

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
        remoteDiagnosticMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "remote_diagnostic",
                                                                   "remote_diagnostic")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if remoteDiagnosticMode_Disabled == "false" or remoteDiagnosticMode_Disabled == False or remoteDiagnosticMode_Disabled == 0:
            testResult(self, "passed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is not set to False in master_conf.json file on device")
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
                if cloudEnv in r8_patch4_sp17_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["user_settings"]

                # Handle each mode
                if "remote_diagnostic" in vehicle_features:
                    mode_config = vehicle_features["remote_diagnostic"]
                    if mode_config == 0:
                        testResult(self, "passed",
                                   "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on cloud",
                                   "Remote Diagnostic Mode Flag is set to False in master_conf.json file on cloud")
                        assert True
                        # self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    # self.result.set_result(TestResults.failed)
                    assert False


    def test_positive_remote_diagnostic_mode_r8p4s14_wrong(self):

        #getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud Side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if any(cloudEnv in lst for lst in
               (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and connection state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)
        elif cloudEnv in r8_patch4_sp17_envs:
            if rideState == "AT_REST" and vehicleMode in ["NORMAL_MODE", "SERVICE_MODE"] and rideMode == "PARK":
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)
        elif cloudEnv in r5_envs:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                assert True
                #self.result.set_result(TestResults.passed)

        else:
            testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                       f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
            #self.result.set_result(TestResults.failed)
            assert False

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        action = "EDIT"
        # path = "vehicle_settings.vehicle_mode.privacy_mode"
        if any(cloudEnv in lst for lst in
               (r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)) and cloudEnv not in r8_patch4_sp17_envs:
            path = "vehicle_settings.user_settings.vehicle_mode.remote_diagnostic_mode"
        elif cloudEnv in r8_patch4_sp17_envs:
            path = "vehicle_settings.user_settings.remote_diagnostic"
        else:
            path = "vehicle_settings.vehicle_mode.remote_diagnostic_mode"

        if cloudEnv in r8_patch_envs_hmac:
            enabled = 1
        else:
            enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 600000  # 10 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        if cloudEnv in r8_patch4_sp17_envs:
            vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                          start_time,
                                          end_time, "remote_diagnostic")
        else:
            vehicle_mode_set_via_cloud(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled,
                                       start_time,
                                       end_time, "RemoteDiagnostic")

        # Validate vehicle mode in vehicle state API

        if cloudEnv not in r8_patch4_sp17_envs:
            currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
                self,
                cloudEnv,
                systemId,
                "regional")

            if vehicleMode == "REMOTE_DIAGNOSTIC":
                testResult(self, "passed", "vehicle mode should be in remote_diagnostic_mode",
                           f"vehicle is in remote diagnostic mode")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "vehicle mode should be in remote_diagnostic_mode",
                           f"vehicle mode is not in remote diagnostic mode")
                #self.result.set_result(TestResults.failed)
                assert False
        else:
            pass

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in remote diagnostic mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 6504",
            "constr_and_send_proto_msg success for 6505"
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

        # Cloud side telemetry timestamp validation
        response1 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type1, systemId, "valid")
        response2 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type2, systemId, "valid")
        response3 = telemetry_Curr_eventType(self, telemetry_remote_diagnostic_event_type3, systemId, "valid")

        if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
            testResult(self, "passed", "Should send telemetry block 6504, 6505 and 6506 during remote diagnostic mode", "Telemetry block 6504, 6505 and 6506 is sending during remote dianostic")
        else:
            testResult(self, "failed", "Should send telemetry block 6504, 6505 and 6506 during remote diagnostic mode",
                       "Telemetry block 6504, 6505 and 6506 is not sending during remote dianostic")

        response_body1 = response1.json()
        response_body2 = response2.json()
        response_body3 = response3.json()

        response_bodies = [response_body1, response_body2, response_body3]

        print("----- TIMESTAMP VALIDATION -----")

        valid = []

        for i, body in enumerate(response_bodies, 1):
            updated_time = None

            # directly check inside signals
            for item in body.get("signals", []):
                if "updatedTime" in item:
                    updated_time = item["updatedTime"]
                    break

            print(f"\nResponse {i}: {updated_time}")

            if not updated_time:
                print("❌ No updatedTime")
                valid.append(False)
                continue

            if current_time <= updated_time <= end_time:
                print("✅ Valid timestamp")
                valid.append(True)
            else:
                print("❌ Invalid timestamp")
                valid.append(False)

        print("\n----- SUMMARY -----")

        if all(valid):
            print("✅ All timestamps are valid")
            testResult(self, "passed",
                       "All telemetry messages received during remote diagnostic mode with valid timestamps",
                       f"All 3 telemetry blocks (6504, 6505, 6506) received within remote diagnostic time window")
        else:
            print("❌ Some timestamps are invalid")
            testResult(self, "verificationFailed",
                       "Some telemetry messages missing or have invalid timestamps",
                       f"Not all messages received within remote diagnostic time window")

        print("\n" + "="*80)
        print("REMOTE DIAGNOSTIC MODE MESSAGE RECEIPT SUMMARY")
        print("="*80)
        print(f"Remote Diagnostic Window: {current_time} ms to {end_time} ms")
        print(f"Telemetry Blocks Expected: 6504, 6505, 6506")
        print(f"\nMessage Receipt Status:")
        for idx, is_valid in enumerate(valid, 1):
            status = "VALID" if is_valid else "INVALID"
            print(f"  Response {idx}: {status}")
        print("="*80)

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
        remoteDiagnosticMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "RemoteDiagnosticMode_Enabled",
                                                                   "remoteDiagnosticMode")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if remoteDiagnosticMode_Disabled == "false" or remoteDiagnosticMode_Disabled == False or remoteDiagnosticMode_Disabled == 0:
            testResult(self, "passed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is not set to False in master_conf.json file on device")
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
                if cloudEnv in r8_patch4_sp17_envs:
                    mode_config = response_body["configurations"]["vehicle_settings"]["user_settings"].get("remote_diagnostic")
                else:
                    vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode") or {}
                    mode_config = vehicle_mode.get("remote_diagnostic") if isinstance(vehicle_mode, dict) else None

                if mode_config in ("false", False, 0):
                    testResult(self, "passed",
                               "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on cloud",
                               "Remote Diagnostic Mode Flag is set to False in master_conf.json file on cloud")
                    assert True
                else:
                    print("Remote Diagnostic Mode Flag validation failed on cloud.")
                    print("mode_config:", mode_config)
                    assert False
            else:
                print("Unexpected response message:", response_body.get("message"))
                assert False


class Test_Service_Mode:

    def test_positive_service_mode(self):
        # ----------------------------------------------------------
        # 1) Initialize and verify preconditions
        # ----------------------------------------------------------
        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("======== 1) Cloud-side precheck before enabling Service Mode ========")
        print("Preparing to validate vehicle mode and connection state prerequisites...")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA8"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(
                    self, "passed",
                    "Precondition: connection must be CONNECTED and mode must be NORMAL/PRIVACY/INCOGNITO",
                    f"Precondition satisfied: connection={connectionState}, mode={vehicleMode}"
                )
                assert True
            else:
                # As per original logic: do not fail here
                print(
                    f"[Info] Precondition not strictly met, but continuing. connection={connectionState}, mode={vehicleMode}")
                assert True

        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(
                    self, "passed",
                    "Precondition: currentState must be ACTIVE and mode must be NORMAL/PRIVACY/INCOGNITO",
                    f"Precondition satisfied: currentState={currentState}, mode={vehicleMode}"
                )
                assert True
            else:
                # As per original logic: do not fail here
                print(
                    f"[Info] Precondition not strictly met, but continuing. currentState={currentState}, mode={vehicleMode}")
                assert True

        else:
            testResult(
                self, "failed",
                "Precondition failed: mode should be NORMAL/PRIVACY/INCOGNITO",
                f"Found vehicle mode: {vehicleMode}"
            )
            assert False

        # ----------------------------------------------------------
        # 2) Device-side precondition (Remote Diagnostic prerequisites)
        # ----------------------------------------------------------
        print("======== 2) Setting device-side preconditions for Service Mode ========")
        print("Applying device preconditions (speed and level-2 property) via PAHO script...")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")
        print("Device preconditions applied.")

        # ----------------------------------------------------------
        # 3) Enable service_mode_rdm on device (before cluster trigger)
        # ----------------------------------------------------------
        print("======== 3) Enabling service_rdm on device (pre-requisite) ========")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_rdm_enable")
        print("service_rdm enabled on device.")


        enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled, "Service_rdm")
        print("service_rdm applied via cluster update.")

        # ----------------------------------------------------------
        # 4) Trigger Service Mode via cloud API (with start/end time)
        # ----------------------------------------------------------
        print("======== 4) Triggering Service Mode via cloud API (time-bound) ========")

        action = "EDIT"
        if cloudEnv in ["GCP-QA4", "GCP-QA5", "GCP-QA8"]:
            path = "vehicle_settings.user_settings.vehicle_mode.service_mode"
        else:
            path = "vehicle_settings.vehicle_mode.service_mode"

        if cloudEnv not in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "PRE-PROD"]:
            enabled = True
        else:
            enabled = 1

        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 10 minutes later
        end_time = start_time + 600000  # 10 minutes in milliseconds

        print("---------- Request Parameters ----------")
        print(f"System ID  : {systemId}")
        print(f"Action     : {action}")
        print(f"Path       : {path}")
        print(f"Start Time : {start_time}")
        print(f"End Time   : {end_time}")
        print("---------------------------------------")

        vehicle_mode_set_via_cloud(
            self, cloudEnv, onboardingType, chipsetType,
            systemId, action, path, enabled, start_time, end_time, "Service"
        )
        print("Service Mode enable request submitted to cloud.")

        # ----------------------------------------------------------
        # 5) Validate Service Mode via Vehicle State API
        # ----------------------------------------------------------
        print("======== 5) Validating Service Mode via Vehicle State API ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if vehicleMode == "SERVICE_MODE":
            testResult(self, "passed", "Vehicle mode should be SERVICE_MODE", "Vehicle is in SERVICE_MODE")
            assert True
        else:
            testResult(self, "failed", "Vehicle mode should be SERVICE_MODE", "Vehicle is not in SERVICE_MODE")
            assert False

        # ----------------------------------------------------------
        # 6) Pull logs and verify vehicle.json shows ACTIVE
        # ----------------------------------------------------------
        print("======== 6) Verifying vehicle.json shows service_mode=ACTIVE ========")
        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Fetching updated files from device...")
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)  # Allow time for device to persist updates

        service_mode_status = read_vehicleJsonFile(self, "service_mode")

        if service_mode_status == "ACTIVE":
            testResult(self, "passed", "vehicle.json should show service_mode=ACTIVE", "vehicle.json shows ACTIVE")
        else:
            testResult(self, "failed", "vehicle.json should show service_mode=ACTIVE",
                       f"vehicle.json shows {service_mode_status}")

        # ----------------------------------------------------------
        # 7) Validate connection state becomes DISCONNECTED (Vehicle State API)
        # ----------------------------------------------------------
        print("======== 7) Validating connection state becomes DISCONNECTED ========")
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

        # ----------------------------------------------------------
        # 8) Wait until end_time (mode window expiry)
        # ----------------------------------------------------------
        print("======== 8) Waiting for Service Mode window to expire ========")
        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # seconds
            print(f"Waiting for end_time... Remaining: {remaining_time:.2f} seconds")
            time.sleep(10)
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        print("end_time reached. Proceeding with Service Mode cleanup...")
        time.sleep(10)

        # ----------------------------------------------------------
        # 9) Disable service_mode_rdm (device + cluster)
        # ----------------------------------------------------------
        print("======== 9) Disabling service_rdm (device + cluster) ========")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_rdm_disable")
        print("service_rdm disabled on device.")


        disabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, disabled, "Service_rdm")
        print("service_rdm disabled in cluster configuration.")

        # ----------------------------------------------------------
        # 10) Validate master_conf.json on device shows service_mode disabled
        # ----------------------------------------------------------
        print("======== 10) Validating device master_conf.json shows service_mode disabled ========")
        print("Reading Service Mode flag from device master_conf.json...")

        serviceMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "ServiceMode_Enabled", "serviceMode")
        print(f"Service Mode - Enabled : {serviceMode_Disabled}")

        status = ""

        if serviceMode_Disabled == "false" or serviceMode_Disabled is False or serviceMode_Disabled == 0:
            testResult(
                self, "passed",
                "Device master_conf.json should show service_mode enabled = False",
                "Device master_conf.json shows enabled=False"
            )
        else:
            testResult(
                self, "failed",
                "Device master_conf.json should show service_mode enabled = False",
                f"Device master_conf.json shows enabled={serviceMode_Disabled}"
            )
            status = "FAIL"
            print("Status:", status)

        if status != "FAIL":
            assert True
        else:
            assert False

        # ----------------------------------------------------------
        # 11) Validate vehicle.json shows INACTIVE after disabling
        # ----------------------------------------------------------
        print("======== 11) Validating vehicle.json shows service_mode=INACTIVE ========")
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        service_mode_status = read_vehicleJsonFile(self, "service_mode")

        if service_mode_status == "INACTIVE":
            testResult(self, "passed", "vehicle.json should show service_mode=INACTIVE", "vehicle.json shows INACTIVE")
        else:
            testResult(self, "failed", "vehicle.json should show service_mode=INACTIVE",
                       f"vehicle.json shows {service_mode_status}")

        # ----------------------------------------------------------
        # 12) Validate cloud configuration reflects service_mode disabled
        # ----------------------------------------------------------
        print("======== 12) Validating cloud master_conf.json shows service_mode disabled ========")
        print("Fetching cloud configuration via Vehicle Configuration API...")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()

        if response.status_code == 200:
            if response_body.get("message") == "Success":
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")
                if "service_mode" in vehicle_mode:
                    mode_config = vehicle_mode["service_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] is False:
                        testResult(
                            self, "passed",
                            "Cloud master_conf.json should show service_mode enabled = False",
                            "Cloud master_conf.json shows enabled=False"
                        )
                        assert True
                else:
                    print("[Error] 'service_mode' not found under vehicle_mode in cloud configuration.")
                    assert False

        # ----------------------------------------------------------
        # 13) Validate vehicle mode returns to NORMAL_MODE
        # ----------------------------------------------------------
        print("======== 13) Validating mode returns to NORMAL_MODE after Service Mode ========")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "Vehicle mode should return to NORMAL_MODE", "Vehicle is in NORMAL_MODE")
            assert True
        else:
            testResult(self, "failed", "Vehicle should return to NORMAL_MODE", f"Vehicle is in {vehicleMode}")
            assert False

        print("======== Service Mode positive flow validation complete ========")

    def test_positive_service_mode_enable(self):


        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA2", "RE-UAT", "GCP-QA4", "GCP-QA8"]:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(
                    self, "passed",
                    "Precondition: connection must be CONNECTED and mode must be NORMAL/PRIVACY/INCOGNITO",
                    f"Precondition satisfied: connection={connectionState}, mode={vehicleMode}"
                )
                assert True
            else:
                # As per original logic: do not fail here
                print(
                    f"[Info] Precondition not strictly met, but continuing. connection={connectionState}, mode={vehicleMode}")
                assert True

        elif cloudEnv in ["GCP-QA"]:
            if currentState == "ACTIVE" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE"]:
                testResult(
                    self, "passed",
                    "Precondition: currentState must be ACTIVE and mode must be NORMAL/PRIVACY/INCOGNITO",
                    f"Precondition satisfied: currentState={currentState}, mode={vehicleMode}"
                )
                assert True
            else:
                # As per original logic: do not fail here
                print(
                    f"[Info] Precondition not strictly met, but continuing. currentState={currentState}, mode={vehicleMode}")
                assert True

        else:
            testResult(
                self, "failed",
                "Precondition failed: mode should be NORMAL/PRIVACY/INCOGNITO",
                f"Found vehicle mode: {vehicleMode}"
            )
            assert False

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("----------------------------------------------------------")

        print("Enabling service mode rdm.....")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_rdm_enable")
        print("service_rdm enabled on device.")

        enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled, "Service_rdm")
        print("service_rdm applied via cluster update.")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA5", "GCP-QA8"]:
            path = "vehicle_settings.vehicle_mode.service_mode"
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.service_mode"

        if cloudEnv not in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "PRE-PROD"]:
            enabled = True
            disabled = False
        else:
            enabled = 1
            disabled = 0
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
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "serviceMode_without_startEndTime")

        # ----------------------------------------------------------
        # 5) Validate Service Mode via Vehicle State API
        # ----------------------------------------------------------
        print("======== Validating Service Mode via Vehicle State API ========")
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if vehicleMode == "SERVICE_MODE":
            testResult(self, "passed", "Vehicle mode should be SERVICE_MODE", "Vehicle is in SERVICE_MODE")
            assert True
        else:
            testResult(self, "failed", "Vehicle mode should be SERVICE_MODE", "Vehicle is not in SERVICE_MODE")
            assert False

        # ----------------------------------------------------------
        # 6) Pull logs and verify vehicle.json shows ACTIVE
        # ----------------------------------------------------------
        print("======== Verifying vehicle.json shows service_mode=ACTIVE ========")
        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Fetching updated files from device...")
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)  # Allow time for device to persist updates

        service_mode_status = read_vehicleJsonFile(self, "service_mode")

        if service_mode_status == "ACTIVE":
            testResult(self, "passed", "vehicle.json should show service_mode=ACTIVE", "vehicle.json shows ACTIVE")
        else:
            testResult(self, "failed", "vehicle.json should show service_mode=ACTIVE",
                       f"vehicle.json shows {service_mode_status}")

        # ----------------------------------------------------------
        # 7) Validate connection state becomes DISCONNECTED (Vehicle State API)
        # ----------------------------------------------------------
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

    def test_positive_service_mode_disable(self):

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("======== 9) Disabling service_rdm (device + cluster) ========")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_rdm_disable")
        print("service_rdm disabled on device.")

        disabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, disabled, "Service_rdm")
        print("service_rdm disabled in cluster configuration.")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA5", "GCP-QA8"]:
            path = "vehicle_settings.vehicle_mode.service_mode"
        else:
            path = "vehicle_settings.user_settings.vehicle_mode.service_mode"

        if cloudEnv not in ["GCP-QA4", "GCP-QA5", "GCP-QA8", "PRE-PROD"]:
            enabled = True
            disabled = False
        else:
            enabled = 1
            disabled = 0

        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, cloudEnv, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "serviceMode_without_startEndTime")

        # ----------------------------------------------------------
        # 11) Validate vehicle.json shows INACTIVE after disabling
        # ----------------------------------------------------------
        print("======== Validating vehicle.json shows service_mode=INACTIVE ========")
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        service_mode_status = read_vehicleJsonFile(self, "service_mode")

        if service_mode_status == "INACTIVE":
            testResult(self, "passed", "vehicle.json should show service_mode=INACTIVE", "vehicle.json shows INACTIVE")
        else:
            testResult(self, "failed", "vehicle.json should show service_mode=INACTIVE",
                       f"vehicle.json shows {service_mode_status}")

        # ----------------------------------------------------------
        # 12) Validate cloud configuration reflects service_mode disabled
        # ----------------------------------------------------------
        print("======== Validating cloud master_conf.json shows service_mode disabled ========")
        print("Fetching cloud configuration via Vehicle Configuration API...")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()

        if response.status_code == 200:
            if response_body.get("message") == "Success":
                vehicle_mode = response_body["configurations"]["vehicle_settings"]["user_settings"].get("vehicle_mode")
                if "service_mode" in vehicle_mode:
                    mode_config = vehicle_mode["service_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] is False:
                        testResult(
                            self, "passed",
                            "Cloud master_conf.json should show service_mode enabled = False",
                            "Cloud master_conf.json shows enabled=False"
                        )
                        assert True
                else:
                    print("[Error] 'service_mode' not found under vehicle_mode in cloud configuration.")
                    assert False

        # ----------------------------------------------------------
        # 13) Validate vehicle mode returns to NORMAL_MODE
        # ----------------------------------------------------------
        print("======== Validating mode returns to NORMAL_MODE after Service Mode ========")

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if vehicleMode == "NORMAL_MODE":
            testResult(self, "passed", "Vehicle mode should return to NORMAL_MODE", "Vehicle is in NORMAL_MODE")
            assert True
        else:
            testResult(self, "failed", "Vehicle should return to NORMAL_MODE", f"Vehicle is in {vehicleMode}")
            assert False

        print("======== Service Mode positive flow validation complete ========")


class Test_service_Mode_R8P14:

    def test_positive_service_mode_r8p4s14(self):

        # Now file sync up will happan during the onboarding process and no need to set the configuration files, thus commented
        # getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        # time.sleep(20)
        # getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        # time.sleep(20)

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        print("----------------------------------------------------------")
        print("===================Cloud Side Precondition================")
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in r8_patch4_sp17_envs:
            if connectionState == "CONNECTED" and vehicleMode in ["NORMAL_MODE"]:
                testResult(self, "passed", "vehicle mode and current state precondition should be satisfy",
                           f"vehicle mode is in {vehicleMode}")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "vehicle mode should be in normal_mode or privacy_mode or incognito_mode",
                           f"vehicle mode is not in normal_mode, privacy_mode and incognito_mode. Rather than found: {vehicleMode}")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("invalid cloudEnv")

        # model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger EDIT FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        if cloudEnv in r8_patch4_sp17_envs:
            path = "vehicle_settings.user_settings.vehicle_mode.service_mode"
        value = 1
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Value :", value)
        print("----------------------------------------------------------")

        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 600000  # 10 minutes in milliseconds

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, "", value, systemId,
                                                                    updateScope, modelCode, country,
                                                                    "EDIT")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Validate response body - Extract and verify timestamp
        print("----------------------------------------------------------")
        print("TIMESTAMP VALIDATION FROM RESPONSE BODY")
        print("----------------------------------------------------------")

        # Try to extract timestamp from various possible attributes
        response_timestamp = (response_body.get("timestamp") or
                              response_body.get("createdAt") or
                              response_body.get("updatedAt") or
                              response_body.get("requestTime") or
                              response_body.get("updateTime"))

        print(f"Current time: {current_time} ms")
        print(f"End time: {end_time} ms")
        print(f"Response timestamp: {response_timestamp}")

        if response_timestamp:
            # Verify timestamp is within the valid time window
            if current_time <= response_timestamp <= end_time:
                testResult(self, "passed",
                           "Response timestamp should be within current and end time range",
                           f"Response timestamp {response_timestamp} is between {current_time} and {end_time}")
                print(f" => Timestamp validation passed: {response_timestamp} is within range")
            else:
                testResult(self, "verificationFailed",
                           "Response timestamp should be within current and end time range",
                           f"Response timestamp {response_timestamp} is NOT between {current_time} and {end_time}")
                print(f" => Timestamp validation failed: {response_timestamp} is outside range")
        else:
            print("Warning: No timestamp attribute found in response body")
            print("Available attributes:", list(response_body.keys()))

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "EDIT Feature - Configuration update should be triggered successfully",
                           "EDIT Feature - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation - Configuration status by trackingId: ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

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
                testResult(self, "verificationPassed", "EDIT Feature - Configuration update should  be 'PROGRESSING'",
                           "EDIT Feature - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "EDIT Feature- Configuration update should success/completed",
                       "EDIT Feature - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "EDIT Feature - Configuration update should success/completed",
                       "EDIT Feature - Configuration update is not success/completed")
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("VALIDATE UPDATED CONFIGURATION IN MASTER_CONF.JSON")

        # Read master_conf.json file
        remoteDiagnostic_value = read_masterConfJsonFile_v2(self, cloudEnv, "remote_diagnostic", "remote_diagnostic")

        status = ""

        if remoteDiagnostic_value == value:
            testResult(self, "passed", "Remote Diagnostic value should be updated in master_conf.json file on device",
                       "Remote Diagnostic feature value is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Remote Diagnostic feature value should be updated in master_conf.json file on device",
                       "Remote Diagnostic feature value is not updated in master_conf.json file on device")
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

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv in r8_patch4_sp17_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["user_settings"]

                # Check for 'tyre_pressure' feature
                if "remote_diagnostic" in vehicle_features:
                    if vehicle_features["remote_diagnostic"] == value:
                        testResult(self, "passed",
                                   "Remote Diagnostic Feature and value should be present in the vehicle configuration",
                                   "Remote Diagnostic Feature and value is present in the vehicle configuration.")
                        assert True
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Remote Diagnostic value does not match the expected value.")

                        # self.result.set_result(TestResults.failed)
                        assert False
                else:
                    # Log an error if 'tyre_pressure' feature is missing
                    print("Remote Diagnostic feature is not found in vehicle features.")
                    testResult(self, "failed",
                               "Remote Diagnostic Feature should be present in the vehicle configuration",
                               "'Remote Diagnostic' feature is missing in the vehicle configuration.")
                    # self.result.set_result(TestResults.failed)
                    assert False
            else:
                print("Unexpected response message:", response_body["message"])
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

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
        remoteDiagnosticMode_Disabled = read_masterConfJsonFile_v2(self, cloudEnv, "remote_diagnostic",
                                                                   "remote_diagnostic")

        print(" Remote Diagnostic Mode - Enabled :", remoteDiagnosticMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if remoteDiagnosticMode_Disabled == "false" or remoteDiagnosticMode_Disabled == False or remoteDiagnosticMode_Disabled == 0:
            testResult(self, "passed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "failed",
                       "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on device",
                       "Remote Diagnostic Mode Flag is not set to False in master_conf.json file on device")
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
                if cloudEnv in r8_patch4_sp17_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["user_settings"]

                # Handle each mode
                if "remote_diagnostic" in vehicle_features:
                    mode_config = vehicle_features["remote_diagnostic"]
                    if mode_config == 0:
                        testResult(self, "passed",
                                   "Remote Diagnostic Mode Flag should be set to False in master_conf.json file on cloud",
                                   "Remote Diagnostic Mode Flag is set to False in master_conf.json file on cloud")
                        assert True
                        # self.result.set_result(TestResults.passed)
                else:
                    print("Invalid or unsupported vehicle mode.")
                    # self.result.set_result(TestResults.failed)
                    assert False
