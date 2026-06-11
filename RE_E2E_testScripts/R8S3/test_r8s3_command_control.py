import pytest
import time

from C2CModules.commandControl_modules import *
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from C2CModules.vehicle_state import *
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_command_precondition_r8s3:

    def test_pos_r8s3_save_command_precondition_vehicle_lock(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        cloudEnv = read_cloud_env(self)
        isCritical = True
        action = "VEHICLE_LOCK"

        if cloudEnv in ["GCP-QA3", "DM1"]:
            statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "rideMode", "operator": "in", "value": ["PARK"]}
            #statePreconditions4 = {"attribute": "ignition", "operator": "in", "value": ["ON"]}

        elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
            statePreconditions1 = {"attribute": "ignition", "operator": "eq", "value": ["OFF"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "parkMode", "operator": "eq", "value": ["ON"]}

        else:
            raise ValueError(f"Unsupported cloud environment: {cloudEnv}")

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action:", action)
        print("isCritical:", isCritical)
        print("Precondition-1:", statePreconditions1)
        print("Precondition-2:", statePreconditions2)
        print("Precondition-3:", statePreconditions3)
        print("----------------------------------------------------------")

        command_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, isCritical, "save_precondition")

    def test_pos_r8s3_save_command_precondition_vehicle_honk(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        cloudEnv = read_cloud_env(self)
        isCritical = True
        action = "VEHICLE_HONK"

        if cloudEnv in ["GCP-QA3", "DM1"]:
            statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "rideMode", "operator": "in", "value": ["PARK"]}

        elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
            statePreconditions1 = {"attribute": "ignition", "operator": "eq", "value": ["OFF"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "parkMode", "operator": "eq", "value": ["ON"]}

        else:
            raise ValueError(f"Unsupported cloud environment: {cloudEnv}")

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action:", action)
        print("isCritical:", isCritical)
        print("Precondition-1:", statePreconditions1)
        print("Precondition-2:", statePreconditions2)
        print("Precondition-3:", statePreconditions3)
        print("----------------------------------------------------------")

        command_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, isCritical, "save_precondition")

    def test_pos_r8s3_save_command_precondition_vehicle_head_light(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        cloudEnv = read_cloud_env(self)
        isCritical = True
        action = "VEHICLE_HEADLIGHT"

        if cloudEnv in ["GCP-QA3", "DM1"]:
            statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "rideMode", "operator": "in", "value": ["PARK"]}

        elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
            statePreconditions1 = {"attribute": "ignition", "operator": "eq", "value": ["OFF"]}
            statePreconditions2 = {"attribute": "vehicleMode", "operator": "in",
                                   "value": ["PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"]}
            statePreconditions3 = {"attribute": "parkMode", "operator": "eq", "value": ["ON"]}

        else:
            raise ValueError(f"Unsupported cloud environment: {cloudEnv}")

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action:", action)
        print("isCritical:", isCritical)
        print("Precondition-1:", statePreconditions1)
        print("Precondition-2:", statePreconditions2)
        print("Precondition-3:", statePreconditions3)
        print("----------------------------------------------------------")

        command_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2,
                             statePreconditions3, isCritical, "save_precondition")

class Test_RE8S3_Command_Control:

    def test1_positive_bikeSecuritySafety_command_remote_vehicleLock(self):

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
            #self.result.set_result(TestResults.passed)
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            #self.result.set_result(TestResults.failed)

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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

    def test2_positive_bikeSecuritySafety_command_remote_vehicleUnlock(self):

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
            #self.result.set_result(TestResults.passed)
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            #self.result.set_result(TestResults.failed)

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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
        value = command_value_0
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

    def test2_positive_bikeSecuritySafety_command_remote_vehicleHonkOn(self):

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
            #self.result.set_result(TestResults.passed)
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            #self.result.set_result(TestResults.failed)

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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
        print("5. Initiate Command - VEHICLE HONK via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleHonk
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

    def test1_positive_bikeSecuritySafety_command_remote_vehicleHonkOff(self):

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
            #self.result.set_result(TestResults.passed)
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride Mode value should be stored in the Cloud DB and match the stub configuration",
                "Ride Mode value is not stored in the Cloud DB or does not match the stub configuration. Refer to cloud logs for details."
            )
            #self.result.set_result(TestResults.failed)

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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
        print("5. Initiate Command - VEHICLE HONK via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleHonk
        time_value = command_time
        area = command_area
        value = command_value_0
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

    def test2_positive_bikeSecuritySafety_command_remote_vehicleHeadlightOn(self):

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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
        print("5. Initiate Command - VEHICLE HEADLIGHT via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleHeadLight
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

    def test1_positive_bikeSecuritySafety_command_remote_vehicleHeadlightOff(self):

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

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
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
        print("5. Initiate Command - VEHICLE HEADLIGHT via API")
        print("------------------------------------------")

        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleHeadLight
        time_value = command_time
        area = command_area
        value = command_value_0
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