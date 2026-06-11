import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random

from C2CModules.e2e_testData import *

from C2CModules.vehicle_configurations import *
from C2CModules.vehicle_state import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.telemetry_modules import telemetry_Curr

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
deviceSerialNo = b2c_ivi_adbSerialNo


def safe_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


class Test_vehicleState:

    def test_vehicle_state_update_telemetry_parameters(self):

        #oem = "RE"

        cloudEnv = read_cloud_env(self)
        dict = read_api_data_from_excel(self, "Env_Details", cloudEnv)
        #oem = str(dict["modelCode"])
        modelCode = str(dict["modelCode"])
        vehicle_type = "EV"

        if cloudEnv in ["RE-DM1"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ride_mode", "elementId": 557875296, "eventType": 6501, "unit": ""}
            parameter4 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_update_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3, parameter4, "valid")

        elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_update_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3,"", "valid")
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ride_mode", "elementId": 557875296, "eventType": 6501, "unit": ""}
            parameter4 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_update_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3, parameter4, "vehicle_type")

        else:
            raise ValueError(f"Unsupported cloud environment: {cloudEnv}")

        #Validate response status code
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        #Parse API response into JSON
        response_body = response.json()
        #Validate response body
        if cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
            if response_body["message"] == "Model code '1234' updated successfully.":
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be updated/configured successfully",
                           "Vehicle state telemetry parameters are updated/configured successfully")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be updated/configured successfully",
                           "Vehicle state telemetry parameters are not updated/configured successfully")
                assert False
                #self.result.set_result(TestResults.failed)
        else:

            if response_body["status"] == "Success":
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be updated/configured successfully",
                           "Vehicle state telemetry parameters are updated/configured successfully")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be updated/configured successfully",
                           "Vehicle state telemetry parameters are not updated/configured successfully")
                assert False
                #self.result.set_result(TestResults.failed)

            # get telemetry parameters
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "GCP-QA5"]:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "valid")
        else:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "vehicle_type")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)
            assert False
        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["status"] == "Success":
            actual_params = response_body["responseData"]

            if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
                expected_params = [parameter1, parameter2, parameter3, parameter4]
            elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
                expected_params = [parameter1, parameter2, parameter3]
            else:
                print("Unexpected Cloud Environment")
                assert False
                #self.result.set_result(TestResults.failed)
                return  # Exit early

            # Check if all expected parameters are present in actual response
            if all(param in actual_params for param in expected_params):
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be present in API response",
                           "All expected telemetry parameters found in API response")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be present in API response",
                           "Some expected telemetry parameters missing in API response")
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Response message is not Success. Rather than found: ", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

    def test_vehicle_state_delete_telemetry_parameters(self):

        #oem = "RE"

        cloudEnv = read_cloud_env(self)
        dict = read_api_data_from_excel(self, "Env_Details", cloudEnv)
        #oem = str(dict["modelCode"])
        modelCode = str(dict["modelCode"])
        vehicle_type = "EV"


        response = vehicle_state_delete_telemetry_parameters(self, cloudEnv, modelCode, "valid")

        #Validate response status code
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        #Parse API response into JSON
        response_body = response.json()
        #Validate response body
        if cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
            if response_body["message"] == "Model code '1234' deleted successfully.":
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be deleted successfully",
                           "Vehicle state telemetry parameters are deleted successfully")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be deleted successfully",
                           "Vehicle state telemetry parameters are not deleted successfully")
                assert False
                #self.result.set_result(TestResults.failed)
        else:

            if response_body["status"] == "Success":
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be deleted successfully",
                           "Vehicle state telemetry parameters are deleted successfully")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be deleted successfully",
                           "Vehicle state telemetry parameters are not deleted successfully")
                assert False
                #self.result.set_result(TestResults.failed)

            # get telemetry parameters
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "GCP-QA5"]:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "valid")
        else:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "vehicle_type")

        # Validate response status code
        if response.status_code == 204:
            testResult(self, "passed",
                           "Vehicle state telemetry parameters should not be present in API response",
                           "All expected telemetry parameters not found in API response")
            assert True
                #self.result.set_result(TestResults.passed)
        elif response.status_code == 400:
            response_body = response.json()
            if response_body["status"] == "Failed" and response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0]["message"] == "No data found for this model 1234 .":
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should not be present in API response",
                           "All expected telemetry parameters not found in API response")
                assert True
            else:
                assert False
        else:
            testResult(self, "failed",
                           "Vehicle state telemetry parameters should not be present in API response",
                           "Some expected telemetry parameters found in API response")
            assert False
                #self.result.set_result(TestResults.failed)

    def test_vehicle_state_save_telemetry_parameters(self):

        #oem = "RE"

        cloudEnv = read_cloud_env(self)
        dict = read_api_data_from_excel(self, "Env_Details", cloudEnv)
        #oem = str(dict["modelCode"])
        modelCode = str(dict["modelCode"])
        vehicle_type = "EV"

        if cloudEnv in ["RE-DM1"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ride_mode", "elementId": 557875296, "eventType": 6501, "unit": ""}
            parameter4 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_save_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3, parameter4, "valid")

        elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_save_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3,"", "valid")
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5"]:
            parameter1 = {"attributeName": "speed", "elementId": 557875288, "eventType": 6500, "unit": ""}
            parameter2 = {"attributeName": "gps_fix", "elementId": 559988762, "eventType": 3101, "unit": ""}
            parameter3 = {"attributeName": "ride_mode", "elementId": 557875296, "eventType": 6501, "unit": ""}
            parameter4 = {"attributeName": "ignition", "elementId": 557875730, "eventType": 2003, "unit": ""}
            response = vehicle_state_save_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, parameter1, parameter2,
                                                                 parameter3, parameter4, "vehicle_type")

        else:
            raise ValueError(f"Unsupported cloud environment: {cloudEnv}")

        #Validate response status code
        if response.status_code == 200:
            #Parse API response into JSON
            response_body = response.json()
            #Validate response body
            if cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
                if response_body["message"] == "Model code '1234' added successfully.":
                    testResult(self, "passed",
                               "Vehicle state telemetry parameters should be saved successfully",
                               "Vehicle state telemetry parameters are saved successfully")
                    assert True
                    #self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed",
                               "Vehicle state telemetry parameters should be saved successfully",
                               "Vehicle state telemetry parameters are not saved successfully")
                    assert False
                    #self.result.set_result(TestResults.failed)
            else:

                if response_body["status"] == "Success":
                    testResult(self, "passed",
                               "Vehicle state telemetry parameters should be saved successfully",
                               "Vehicle state telemetry parameters are saved successfully")
                    assert True
                    #self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed",
                               "Vehicle state telemetry parameters should be saved successfully",
                               "Vehicle state telemetry parameters are not saved successfully")
                    assert False
                    #self.result.set_result(TestResults.failed)

        elif response.status_code == 400:
            response_body = response.json()
            if response_body["errors"][0]["errorCode"] == "16003" and response_body["errors"][0]["message"] == "Already data present for this model 1234 .":
                assert True
            else:
                assert False
        else:
            print("Response status code is not expected.Rather than found: ", response.status_code)
            assert False


            # get telemetry parameters
        if cloudEnv not in ["GCP-QA3", "GCP-QA4", "GCP-QA5"]:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "valid")
        else:
            response = vehicle_state_get_telemetry_parameters(self, cloudEnv, modelCode, vehicle_type, "vehicle_type")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)
            assert False
        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["status"] == "Success":
            actual_params = response_body["responseData"]

            if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
                expected_params = [parameter1, parameter2, parameter3, parameter4]
            elif cloudEnv in ["GCP-QA2", "RE-UAT"]:
                expected_params = [parameter1, parameter2, parameter3]
            else:
                print("Unexpected Cloud Environment")
                assert False
                #self.result.set_result(TestResults.failed)
                return  # Exit early

            # Check if all expected parameters are present in actual response
            if all(param in actual_params for param in expected_params):
                testResult(self, "passed",
                           "Vehicle state telemetry parameters should be present in API response",
                           "All expected telemetry parameters found in API response")
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Vehicle state telemetry parameters should be present in API response",
                           "Some expected telemetry parameters missing in API response")
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Response message is not Success. Rather than found: ", response_body)
            assert False
            #self.result.set_result(TestResults.failed)


class Test_vehicleState_currentState:

    def test_vehicle_state_current_state(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if currentState == "ACTIVE":
            testResult(self, "passed", "Vehicle should be up and running with cloud connection",
                       "Vehicle is up and running with cloud connection")
            assert True
        elif currentState == "OFFLINE":
            testResult(self, "failed", "vehicle should not be active for more than 3 days to 30 days",
                       "vehicle is not active for more than 3 days to 30 days")
            assert True
        elif currentState == "INACTIVE":
            testResult(self, "failed", "vehicle should not be active for More than 30 mins and less than 3 days",
                       "vehicle is not active for More than 30 mins and less than 3 days")
            assert True
        elif currentState == "IDLE":
            testResult(self, "failed", "vehicle should not be communicating with cloud for 30 mins",
                       "vehicle is not communicating with cloud for 30 mins")
            assert True
        elif currentState == "DEAD":
            testResult(self, "failed",
                       "vehicle should be Dead state when the vehicle is not communicated for last 30 days and primary battery is disabled",
                       "vehicle is Dead when the vehicle is not communicated for last 30 days and primary battery is disabled")
            assert True
        else:
            print(f"Unexpected vehicle state: {currentState}")
            assert False

class Test_vehicleState_speedState:

    def test_vehicle_state_running_speed_greater_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed and ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state")
        time.sleep(5)
        print("Speed & Ignition stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            response_data = response_body.get("responseData", {})
            signals = response_data.get("dataList") or response_data.get("signals", [])
            dataList_len = len(signals)
            for i in range(dataList_len):
                if signals[i]["name"] == "SPEED" or signals[i]["name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = signals[i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except Exception:
            print("dataList is empty in api response")
            value = ""

        val_f = safe_float(value)
        exp_f = safe_float(b2c_telemetry_speed_value)

        if val_f is not None and exp_f is not None and val_f == exp_f:
            testResult(
                self,
                "verificationPassed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "verificationFailed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "RUNNING" and ignition == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_running_speed_greater_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed and ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state")
        time.sleep(5)
        print("Speed & Ignition stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "verificationPassed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "verificationFailed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "RUNNING" and ignition == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_running_speed_equals_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_3km_ignition_on")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "3"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.84"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value
        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : '{telemetry_ignition_attribute}'")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "RUNNING" and ignition == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is equal to 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is equal to 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is equal to 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is equal to 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_0_ignition_on_r8s14(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_halt_state")
        time.sleep(5)
        print("speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 6500
        elif cloudEnv in ["GCP-QA2"]:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 4445
        else:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if (response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V") and response_body["responseData"]["dataList"][i][
                            "eventType"] == "4445":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # Verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1","GCP-QA2"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value
        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : '{telemetry_ignition_attribute}'")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub :", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB :", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )

        print("Ignition State value configured in the stub :", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB :", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and ignition == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    "vehicle is in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    f"vehicle is not in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "HALT" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    "vehicle is in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    f"vehicle is not in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_idle_speed_lesser_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_less3km_ignition_on")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "1"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.7"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # Verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value
        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : '{telemetry_ignition_attribute}'")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub :", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB :", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "IDLE" and ignition == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    "vehicle is in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    f"vehicle is not in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "IDLE" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    "vehicle is in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    f"vehicle is not in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_lesserOr0_ignition_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_0_ignition_off")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # Verify Ignition Off attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "0"
        else:
            telemetry_ignition_value = "3"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value
        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : '{telemetry_ignition_attribute}'")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub :", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB :", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and ignition == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is not Running state when the vehicle speed is not above 3kmp and ignition is OFF"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF."
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is not Running state when the vehicle speed is not above 3kmp and ignition is OFF"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF."
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_greater_3km_ignition_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_valid_ignition_off")
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

        # telemetry - Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_speed_value} ",
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
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "0"
        else:
            telemetry_ignition_value = "3"
        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs contains the logs for Ignition Off, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(self, "passed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
                testResult(self, "passed",
                           "vehicle should not Halt when the vehicle the speed should not be 0 but the ignition should not be ON",
                           "vehicle is not Halt state when the vehicle speed is not above 3kmp and ignition is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                           f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
                assert False
        else:
            if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
                testResult(self, "passed", "vehicle should not Halt when the vehicle the speed should not be 0 but the ignition should not be ON",
                           "vehicle is not Halt state when the vehicle speed is not above 3kmp and ignition is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                           f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
                assert False

class Test_vehicleState_speedState_v2:

    def test_vehicle_state_running_speed_greater_3km_not_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed and ignition on device:")
        if cloudEnv not in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state_v2")
        time.sleep(5)
        print("Speed & Ignition stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1", "GCP-QA4"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "verificationPassed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "verificationFailed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Device-side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0

        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_0)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_0):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "RUNNING" and rideMode != "PARK":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_running_speed_equals_3km_not_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        if cloudEnv in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_3km_ignition_on")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_3km_not_in_parkMode")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "3"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.84"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0

        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_0)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_0):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "RUNNING" and rideMode != "PARK":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is equal to 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is equal to 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    "vehicle is in Running state when the vehicle speed is equal to 3kmp and ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                    f"vehicle is not in Running state when the vehicle speed is equal to 3kmp and ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_0_not_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        if cloudEnv in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_halt_state")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_halt_state_v2")
        time.sleep(5)
        print("speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0

        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_0)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_0):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and rideMode != "PARK":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    "vehicle is in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    f"vehicle is not in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "HALT" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    "vehicle is in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                    f"vehicle is not in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_idle_speed_lesser_3km_not_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        if cloudEnv in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_less3km_ignition_on")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_less3km_not_in_parkMode")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "1"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.7"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0
        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ride mode attribute found in device log: '{telemetry_attribute_ridemode}'")
            testResult(
                self, "passed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs contain Ride Mode telemetry. Refer to device logs for details."
            )
            print("c2c logs line data : =>", ls[0])
        elif str(ls[0]) == "Error":
            print("Ride Mode logs not found or device logs not updated.")
            testResult(
                self, "verificationFailed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs missing Ride Mode telemetry or failed to read logs. Refer to device logs for details."
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud-side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        telemetry_speed_event_type = 6500
        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride Mode value configured in the stub:", telemetry_ridemode_value_0)
        print("Ride Mode value stored in Cloud DB:", value)

        if int(value) == int(telemetry_ridemode_value_0):
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

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "IDLE" and rideMode != "PARK":
                testResult(
                    self,
                    "passed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    "vehicle is in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    f"vehicle is not in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "IDLE" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self,
                    "passed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    "vehicle is in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                    f"vehicle is not in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_lesserOr0_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        if cloudEnv not in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_0_ignition_off")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_0_in_parkMode")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_12
        ls = verify_message_in_log(self, telemetry_ridemode_value_12, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ride mode attribute found in device log: '{telemetry_attribute_ridemode}'")
            testResult(
                self, "passed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs contain Ride Mode telemetry. Refer to device logs for details."
            )
            print("c2c logs line data : =>", ls[0])
        elif str(ls[0]) == "Error":
            print("Ride Mode logs not found or device logs not updated.")
            testResult(
                self, "verificationFailed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs missing Ride Mode telemetry or failed to read logs. Refer to device logs for details."
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud-side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        telemetry_speed_event_type = 6500
        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

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

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and rideMode == "PARK":
                testResult(
                    self,
                    "passed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is not Running state when the vehicle speed is not above 3kmp and ignition is OFF"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF."
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
                testResult(
                    self,
                    "passed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is not Running state when the vehicle speed is not above 3kmp and ignition is OFF"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                    "vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF."
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_halt_speed_greater_3km_in_parkMode(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")
        if cloudEnv not in ["GCP-QA3", "DM1"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_valid_ignition_off")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_valid_in_parkMode")
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

        # telemetry - Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "DM1"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_speed_value} ",
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
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                        response_body["responseData"]["dataList"][i][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_12
        ls = verify_message_in_log(self, telemetry_ridemode_value_12, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ride mode attribute found in device log: '{telemetry_attribute_ridemode}'")
            testResult(
                self, "passed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs contain Ride Mode telemetry. Refer to device logs for details."
            )
            print("c2c logs line data : =>", ls[0])
        elif str(ls[0]) == "Error":
            print("Ride Mode logs not found or device logs not updated.")
            testResult(
                self, "verificationFailed",
                "Device logs should contain the logs for Ride Mode",
                "Device logs missing Ride Mode telemetry or failed to read logs. Refer to device logs for details."
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud-side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        telemetry_speed_event_type = 6500
        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        value = reasonCode = ""

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

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

        #-------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if speed == "HALT" and rideMode == "PARK":
                testResult(self, "passed",
                           "vehicle should not Halt when the vehicle the speed should not be 0 but the ignition should not be ON",
                           "vehicle is not Halt state when the vehicle speed is not above 3kmp and ignition is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                           f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
                assert False
        else:
            if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
                testResult(self, "passed", "vehicle should not Halt when the vehicle the speed should not be 0 but the ignition should not be ON",
                           "vehicle is not Halt state when the vehicle speed is not above 3kmp and ignition is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                           f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
                assert False

class Test_vehicleState_speedState_v3:

    def test_vehicle_state_running_speed_greater_3km_not_in_parkMode_r8s14(self):

        # Read system ID and cloud environment
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed and parkMode on device:")
        if cloudEnv in ["GCP-QA", "GCP-DEMO2"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state")
        elif cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state_v2")
        elif cloudEnv in ["GCP-QA8", "RE-UAT", "GCP-QA2"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state_v3")
        else:
            print("Invalid cloudEnv")
        time.sleep(5)
        print("Speed & parkMode stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "RE-UAT","GCP-QA2"]:
            b2c_telemetry_speed_value = "4"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0.9"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationFailed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations :")
        print("-----------------------------")

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if (response_body["responseData"]["dataList"][i]["name"] == "SPEED" or \
                    response_body["responseData"]["dataList"][i][
                        "name"] == "Display_info__Display_Vehicle_Speed_RX_V") and \
                        response_body["responseData"]["dataList"][i]["eventType"] == telemetry_speed_event_type:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Device-side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # Verify rideMode attribute in the device
        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0
        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(
                self, "passed",
                "Device logs should contain the logs for ridemode",
                "Device logs contains the logs for ridemode, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self, "verificationFailed",
                "Device logs should contain the logs for ridemode",
                "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Verify rideMode value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_0)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_0):
            testResult(
                self, "passed",
                "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.passed)
        else:
            testResult(
                self, "failed",
                "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(
            self, cloudEnv, systemId, "regional"
        )

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5", "GCP-QA8", "RE-UAT", "GCP-QA2"]:
            if speed == "RUNNING" and rideMode != "PARK":
                testResult(
                    self, "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and driveMode is not in park",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and driveMode is not in park"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self, "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and driveMode is not in park",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and driveMode is not in park. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
                testResult(
                    self, "passed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and driveMode is not in park",
                    "vehicle is in Running state when the vehicle speed is above 3kmp and driveMode is not in park"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self, "failed",
                    "vehicle should be Running state when the vehicle speed is above 3kmp and driveMode is not in park",
                    f"vehicle is not in Running state when the vehicle speed is above 3kmp and driveMode is not in park. Rather than found: {speed}"
                )
                assert False
                #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_vehicle_state_connection_state_disconnected(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # Command to disable Wi-Fi
        print("---------------------------")
        print("TURN OFF WIFI ON THE DEVICE")
        print("---------------------------")
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        print("---------------------------")
        print("TURN ON WIFI ON THE DEVICE")
        print("---------------------------")
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(60)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "DISCONNECTED":
            testResult(self, "passed", "Connection state should be disconnected when there is no cloud connection on the device",
                       "Connection state is disconnected when there is no cloud connection on the device")
            assert True
        else:
            testResult(self, "failed", "Connection state should be disconnected when there is no cloud connection on the device",
                       "Connection state is not disconnected when there is no cloud connection on the device")
            print(f"Unexpected vehicle state: {connectionState}")
            assert False

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(20)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if connectionState == "CONNECTED":
            testResult(self, "passed", "Connection state should be connected when the device has proper cloud connection on the device",
                       "Connection state is connected when the device has proper cloud connection on the device")
            assert True
        else:
            testResult(self, "failed", "Connection state should be connected when the device has proper cloud connection on the device",
                       "Connection state is not connected when the device has proper cloud connection on the device")
            print(f"Unexpected vehicle state: {connectionState}")
            assert False

class Test_vehicleState_ignitionState:

    def test_vehicle_state_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOn_simulation")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs contains the logs for Ignition Off, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(self, "passed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if ignition == "ON":
                testResult(self, "passed",
                           "Ignition state should be ON",
                           "Ignition state is ON")
                assert True
            else:
                testResult(self, "failed",
                           "Ignition state should be ON",
                           f"Ignition state is not ON")
                assert False
        else:
            if ignition == "ON" and parkMode == "OFF":
                testResult(self, "passed",
                           "Ignition state should be ON and park mode should be OFF",
                           "Ignition state is ON and park mode is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "Ignition state should be ON and park mode should be OFF",
                           f"Ignition state is not ON and park mode is not OFF")
                assert False

    def test_vehicle_state_ignition_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOff_simulation")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "DM1"]:
            telemetry_ignition_value = "0"
        else:
            telemetry_ignition_value = "3"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs contains the logs for Ignition Off, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(self, "passed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self, cloudEnv, systemId, "regional")
        if cloudEnv in ["GCP-QA3", "DM1"]:
            if ignition == "OFF":
                testResult(self, "passed",
                           "Ignition state should be OFF",
                           "Ignition state is OFF")
                assert True
            else:
                testResult(self, "failed",
                           "Ignition state should be OFF",
                           f"Ignition state is not OFF")
                assert False
        else:
            if ignition == "OFF" and parkMode == "ON":
                testResult(self, "passed",
                           "Ignition state should be OFF and park mode should be ON",
                           "Ignition state is OFF and park mode is ON")
                assert True
            else:
                testResult(self, "failed",
                           "Ignition state should be OFF and park mode should be ON",
                           f"Ignition state is not OFF and park mode is not ON")
                assert False

class Test_vehicleState_rideMode:

    def test_vehicle_state_ridemode_sna(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_sna")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_0

        ls = verify_message_in_log(self, telemetry_ridemode_value_0, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_0)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_0):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "SNA":
                testResult(self, "passed",
                           "Ride mode should be updated as SNA",
                           "Ride mode  is updated as SNA")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as SNA",
                           f"Ride mode is not updated as SNA")
                assert False

    def test_vehicle_state_ridemode_sleep(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_sleep")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_1

        ls = verify_message_in_log(self, telemetry_ridemode_value_1, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_1)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_1):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")
        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "SLEEP":
                testResult(self, "passed",
                           "Ride mode should be updated as sleep",
                           "Ride mode  is updated as sleep")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as sleep",
                           f"Ride mode is not updated as sleep")
                assert False

    def test_vehicle_state_ridemode_deep_sleep(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_deep_sleep")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_2

        ls = verify_message_in_log(self, telemetry_ridemode_value_2, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_2)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_2):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "DEEP_SLEEP":
                testResult(self, "passed",
                           "Ride mode should be updated as deep sleep",
                           "Ride mode  is updated as deep sleep")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as deep sleep",
                           f"Ride mode is not updated as deep sleep")
                assert False

    def test_vehicle_state_ridemode_vacation(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_vacation")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_3

        ls = verify_message_in_log(self, telemetry_ridemode_value_3, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_3)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_3):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "VACATION":
                testResult(self, "passed",
                           "Ride mode should be updated as vacation",
                           "Ride mode  is updated as vacation")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as vacation",
                           f"Ride mode is not updated as vacation")
                assert False

    def test_vehicle_state_ridemode_shut_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_shut_off")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_4

        ls = verify_message_in_log(self, telemetry_ridemode_value_4, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_4)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_4):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "SHUT_OFF":
                testResult(self, "passed",
                           "Ride mode should be updated as shut off",
                           "Ride mode  is updated as shut off")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as shut off",
                           f"Ride mode is not updated as shut off")
                assert False

    def test_vehicle_state_ridemode_forced_ota(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_forced_ota")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_5

        ls = verify_message_in_log(self, telemetry_ridemode_value_5, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_5)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_5):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "SHUT_OFF":
                testResult(self, "passed",
                           "Ride mode should be updated as forced ota",
                           "Ride mode  is updated as forced ota")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as forced ota",
                           f"Ride mode is not updated as forced ota")
                assert False

    def test_vehicle_state_ridemode_power_up(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_power_up")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_6

        ls = verify_message_in_log(self, telemetry_ridemode_value_6, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_6)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_6):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "POWER_UP":
                testResult(self, "passed",
                           "Ride mode should be updated as power up",
                           "Ride mode  is updated as power up")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as power up",
                           f"Ride mode is not updated as power up")
                assert False

    def test_vehicle_state_ridemode_boot_up(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_boot_up")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_7

        ls = verify_message_in_log(self, telemetry_ridemode_value_7, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_7)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_7):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "BOOTUP":
                testResult(self, "passed",
                           "Ride mode should be updated as boot up",
                           "Ride mode  is updated as boot up")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as boot up",
                           f"Ride mode is not updated as boot up")
                assert False

    def test_vehicle_state_ridemode_diagnostics(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_diagnostics")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_8

        ls = verify_message_in_log(self, telemetry_ridemode_value_8, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_8)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_8):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "DIAGNOSTICS":
                testResult(self, "passed",
                           "Ride mode should be updated as diagnostics",
                           "Ride mode  is updated as diagnostics")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as diagnostics",
                           f"Ride mode is not updated as diagnostics")
                assert False

    def test_vehicle_state_ridemode_charge_idle(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_charge_idle")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_9

        ls = verify_message_in_log(self, telemetry_ridemode_value_9, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_9)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_9):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "CHARGE_IDLE":
                testResult(self, "passed",
                           "Ride mode should be updated as charge idle",
                           "Ride mode  is updated as charge idle")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as charge idle",
                           f"Ride mode is not updated as charge idle")
                assert False

    def test_vehicle_state_ridemode_charge_fault(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_charge_fault")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_10

        ls = verify_message_in_log(self, telemetry_ridemode_value_10, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_10)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_10):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "CHARGE_FAULT":
                testResult(self, "passed",
                           "Ride mode should be updated as charge fault",
                           "Ride mode  is updated as charge fault")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as charge fault",
                           f"Ride mode is not updated as charge fault")
                assert False

    def test_vehicle_state_ridemode_ota(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_ota")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_11

        ls = verify_message_in_log(self, telemetry_ridemode_value_11, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_11)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_11):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "OTA":
                testResult(self, "passed",
                           "Ride mode should be updated as ota",
                           "Ride mode  is updated as ota")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as ota",
                           f"Ride mode is not updated as ota")
                assert False

    def test_vehicle_state_ridemode_park(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_park")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_12

        ls = verify_message_in_log(self, telemetry_ridemode_value_12, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_12)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_12):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "PARK":
                testResult(self, "passed",
                           "Ride mode should be updated as park",
                           "Ride mode  is updated as park")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as park",
                           f"Ride mode is not updated as park")
                assert False

    def test_vehicle_state_ridemode_slow_mode(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_slow_mode")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_13

        ls = verify_message_in_log(self, telemetry_ridemode_value_13, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_13)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_13):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "SLOW_MODE":
                testResult(self, "passed",
                           "Ride mode should be updated as slow mode",
                           "Ride mode  is updated as slow mode")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as slow mode",
                           f"Ride mode is not updated as slow mode")
                assert False

    def test_vehicle_state_ridemode_riding(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_riding")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_14

        ls = verify_message_in_log(self, telemetry_ridemode_value_14, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_14)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_14):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "RIDING":
                testResult(self, "passed",
                           "Ride mode should be updated as riding",
                           "Ride mode  is updated as slow riding")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as riding",
                           f"Ride mode is not updated as slow riding")
                assert False

    def test_vehicle_state_ridemode_onboard_fast(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_onboard_fast")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_15

        ls = verify_message_in_log(self, telemetry_ridemode_value_15, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_15)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_15):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "ON_BOARD_FAST":
                testResult(self, "passed",
                           "Ride mode should be updated as onboard fast",
                           "Ride mode  is updated as slow onboard fast")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as onboard fast",
                           f"Ride mode is not updated as slow onboard fast")
                assert False

    def test_vehicle_state_ridemode_onboard_slow(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_onboard_slow")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_16

        ls = verify_message_in_log(self, telemetry_ridemode_value_16, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_16)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_16):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "ON_BOARD_SLOW":
                testResult(self, "passed",
                           "Ride mode should be updated as onboard slow",
                           "Ride mode  is updated as onboard slow")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as onboard slow",
                           f"Ride mode is not updated as onboard slow")
                assert False

    def test_vehicle_state_ridemode_alarm(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicleState_rideMode_alarm")
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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device

        tele_ridemode = telemetry_attribute_ridemode + telemetry_ridemode_value_17

        ls = verify_message_in_log(self, telemetry_ridemode_value_17, tele_ridemode)

        if telemetry_attribute_ridemode in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ridemode} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs contains the logs for ridemode, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride mode logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for ridemode",
                       "Device logs doesnot contain the logs for ride mode or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""
        telemetry_speed_event_type = 6500

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ridemode:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ride mode value configured in the stub : ", telemetry_ridemode_value_17)
        print("Ride mode value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ridemode_value_17):
            testResult(self, "passed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ride mode value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ride mode value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # -------------------vehicle state------------------

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition = vehicle_state_info(self,
                                                                                                             cloudEnv,
                                                                                                             systemId,
                                                                                                             "regional")

        if cloudEnv in ["GCP-QA3", "DM1"]:
            if rideMode == "ALARM":
                testResult(self, "passed",
                           "Ride mode should be updated as alarm",
                           "Ride mode  is updated as alarm")
                assert True
            else:
                testResult(self, "failed",
                           "Ride mode should be updated as alarm",
                           f"Ride mode is not updated as alarm")
                assert False

class Test_vehicleState_deviceActivationState:

    def test_vehicle_state_device_activation_state(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState = vehicle_state_info(self, cloudEnv, systemId, "regional")

        if deviceActivationState == "REGIONAL_ACTIVE":
            testResult(self, "passed", "Device Activation State should be updated as REGIONAL_ACTIVE",
                       "Device Activation State is updated as REGIONAL_ACTIVE")
            assert True
        else:
            testResult(self, "passed", "Device Activation State should be updated as REGIONAL_ACTIVE",
                       f"Device Activation State is not updated as REGIONAL_ACTIVE. Unexpected vehicle state: {currentState}")
            assert False

class Test_vehicleState_rideState:

    def test_vehicle_state_ride_state_atReset_speed_0(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "rideState_atRest_speed_0")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if any(cloudEnv in lst for lst in
               (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "0"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data: =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations for preconditions:")
        print("-----------------------------")

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for i in range(dataList_len):
                if (response_body["responseData"]["signals"][i]["name"] == "SPEED" or \
                    response_body["responseData"]["signals"][i][
                        "name"] == "Display_info__Display_Vehicle_Speed_RX_V") and \
                        response_body["responseData"]["signals"][i]["eventType"] == telemetry_speed_event_type:
                    value = response_body["responseData"]["signals"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB:", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "verificationPassed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "verificationFailed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in r8_patch4_sp17_envs:
            if rideState == "AT_REST":
                testResult(
                    self,
                    "passed",
                    "Ride State should be AT_REST when vehicle speed is 0",
                    "Ride State is AT_REST when vehicle speed is 0"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "Ride State should be AT_REST when vehicle speed is 0",
                    f"Ride State is not AT_REST when vehicle speed is 0. Rather than found: {rideState}"
                )
                #self.result.set_result(TestResults.failed)
                assert False

        print("----------------------------------------------------------")

    def test_vehicle_state_ride_state_inMotion_speed_greater_than_0(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for speed & ignition on device:")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "rideState_inMotion_speed_10")
        time.sleep(5)
        print("Speed stub run process is completed, verify logs for telemetry details:")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation:")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================
        print("-----------------------------")
        print("Device Side Validations:")
        print("-----------------------------")

        # Verify Over Speed attribute in the device logs
        if any(cloudEnv in lst for lst in
               (r8_envs, r8_patch1_envs, r8_patch2_envs, r8_patch3_envs, r8_patch_envs_hmac)):
            b2c_telemetry_speed_value = "10"
            telemetry_speed_event_type = 6500
        else:
            b2c_telemetry_speed_value = "10"
            telemetry_speed_event_type = 2001

        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log: '{tele_speed}'")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info"
            )
            print("c2c logs line data : =>", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(
                self,
                "verificationPassed",
                f"Speed value should be set to {b2c_telemetry_speed_value}",
                f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================
        print("-----------------------------")
        print("Cloud Side Validations:")
        print("-----------------------------")

        response_body = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")


        dataList_len = len(response_body["responseData"]["signals"])
        for i in range(dataList_len):
            if (response_body["responseData"]["signals"][i]["name"] == "SPEED" or \
                response_body["responseData"]["signals"][i][
                    "name"] == "Display_info__Display_Vehicle_Speed_RX_V") and \
                    response_body["responseData"]["signals"][i]["eventType"] == telemetry_speed_event_type:
                value = response_body["responseData"]["signals"][i]["value"]
                break

        print("Speed value configured in the telemetry stub:", b2c_telemetry_speed_value)
        print("Speed value stored in Cloud DB:", value)

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(
                self,
                "passed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device. pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # ------------------- Vehicle state -------------------
        currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rideState = vehicle_state_info(
            self,
            cloudEnv,
            systemId,
            "regional")

        if cloudEnv in r8_patch4_sp17_envs:
            if rideState == "IN_MOTION":
                testResult(
                    self,
                    "passed",
                    "Ride State should be IN_MOTION when vehicle speed is greater than 0",
                    "Ride State is IN_MOTION when vehicle speed is greater than 0"
                )
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                testResult(
                    self,
                    "failed",
                    "Ride State should be IN_MOTION when vehicle speed is greater than 0",
                    f"Ride State is not IN_MOTION when vehicle speed is greater than 0. Rather than found: {rideState}"
                )
                #self.result.set_result(TestResults.failed)
                assert False

        print("----------------------------------------------------------")
