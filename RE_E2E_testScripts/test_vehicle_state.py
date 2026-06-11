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
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.telemetry_modules import telemetry_Curr
onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_vehicleState:

    def test_vehicle_state_current_state(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if currentState == "ACTIVE":
            testResult(self, "passed", "Vehicle should be up and running with cloud connection", "Vehicle is up and running with cloud connection")
            assert True
        elif currentState == "OFFLINE":
            testResult(self, "passed", "vehicle should not be active for more than 3 days to 30 days",
                       "vehicle is not active for more than 3 days to 30 days")
            assert True
        elif currentState == "INACTIVE":
            testResult(self, "passed", "vehicle should not be active for More than 30 mins and less than 3 days",
                       "vehicle is not active for More than 30 mins and less than 3 days")
            assert True
        elif currentState == "IDLE":
            testResult(self, "passed", "vehicle should not be communicating with cloud for 30 mins",
                       "vehicle is not communicating with cloud for 30 mins")
            assert True
        elif currentState == "DEAD":
            testResult(self, "passed", "vehicle should be Dead state when the vehicle is not communicated for last 30 days and primary battery is disabled",
                       "vehicle is Dead when the vehicle is not communicated for last 30 days and primary battery is disabled")
            assert True
        else:
            print(f"Unexpected vehicle state: {currentState}")
            assert False

    def test_vehicle_state_running_speed_greater_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_running_state")
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
        b2c_telemetry_speed_value = "0.9"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
            testResult(self, "passed", "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                       "vehicle is in Running state when the vehicle speed is above 3kmp and ignition is ON")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should be Running state when the vehicle speed is above 3kmp and ignition is ON",
                       f"vehicle is not in Running state when the vehicle speed is above 3kmp and ignition is ON. Rather than found: {speed}")
            assert False

    def test_vehicle_state_running_speed_equals_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_3km_ignition_on")
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
        b2c_telemetry_speed_value = "0.84"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "RUNNING" and ignition == "ON" and parkMode == "OFF":
            testResult(self, "passed", "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                       "vehicle is in Running state when the vehicle speed is equal to 3kmp and ignition is ON")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should be Running when the vehicle speed is equal to 3kmp and ignition is ON",
                       f"vehicle is not in Running state when the vehicle speed is equal to 3kmp and ignition is ON. Rather than found: {speed}")
            assert False

    def test_vehicle_state_halt_speed_0_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_halt_state")
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
        b2c_telemetry_speed_value = "0"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "HALT" and ignition == "ON" and parkMode == "OFF":
            testResult(self, "passed", "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                       "vehicle is in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should be Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON",
                       f"vehicle is not in Halt state when the vehicle speed is 0 to 3kmp but the ignition is ON. Rather than found: {speed}")
            assert False

    def test_vehicle_state_idle_speed_lesser_3km_ignition_on(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_less3km_ignition_on")
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
        b2c_telemetry_speed_value = "0.7"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "IDLE" and ignition == "ON" and parkMode == "OFF":
            testResult(self, "passed", "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                       "vehicle is in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should be IDLE state when the vehicle speed is less than 3kmp but the ignition is ON",
                       f"vehicle is not in IDLE state when the vehicle speed is less than 3kmp but the ignition is ON. Rather than found: {speed}")
            assert False

    def test_vehicle_state_halt_speed_lesserOr0_ignition_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "speed_0_ignition_off")
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
        b2c_telemetry_speed_value = "0"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
            testResult(self, "passed", "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                       "vehicle is not Running state when the vehicle speed is not above 3kmp and ignition is OFF")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                       f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
            assert False

    def test_vehicle_state_halt_speed_greater_3km_ignition_off(self):

        systemId = read_vehicleJsonFile(self, "system_id")

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
        b2c_telemetry_speed_value = "0.9"
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

        print("-------------------------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
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
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        #-------------------vehicle state------------------

        currentState, speed, vehicleMode, parkMode, ignition = vehicle_state_info(self, systemId, "regional")

        if speed == "HALT" and ignition == "OFF" and parkMode == "ON":
            testResult(self, "passed", "vehicle should not Halt when the vehicle the speed should not be 0 but the ignition should not be ON",
                       "vehicle is not Halt state when the vehicle speed is not above 3kmp and ignition is OFF")
            assert True
        else:
            testResult(self, "failed",
                       "vehicle should not be Running state when the vehicle speed is not above 3kmp and ignition is OFF",
                       f"vehicle is Running state when the vehicle speed is not above 3kmp and ignition is OFF.")
            assert False



class Test:

    def test_vehicle_state_gps_fix(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "gps_fix_1")
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
        b2c_telemetry_gps_fix_value = "1"
        telemetry_gps_fix_attribute = "gpsFix:"
        tele_gps_fix = telemetry_gps_fix_attribute + b2c_telemetry_gps_fix_value

        ls = verify_message_in_log(self, b2c_telemetry_gps_fix_value, tele_gps_fix)

        if tele_gps_fix in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_gps_fix} ' ")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_gps_fix_value} ",
                       f"Speed value is set to {b2c_telemetry_gps_fix_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_gps_fix_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed",
                       f"Speed value should be set to {b2c_telemetry_gps_fix_value} ",
                       f"Speed value is not set to {b2c_telemetry_gps_fix_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_lat_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "AL_GPS_FIX":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_gps_fix_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_gps_fix_value):
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

        #-------------------vehicle state------------------
        response = get_vehicle_state_details_regional(self, systemId, "regional")

        print("----------------------------------------------------------")

        # Validate response status code
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        result_data = response_body.get("result", [])
        if len(result_data) >= 1:
            for vehicle_data in result_data:
                # Extract fields from response
                systemId_actual = vehicle_data["systemId"]
                status = vehicle_data["status"]
                response_data = vehicle_data["responseData"]
                vehicle_state_data = response_data["vehicleStateData"]

                lastHeartBeatTime = response_data["lastHeartBeatTime"]
                currentState = vehicle_state_data["currentState"]
                parkMode = vehicle_state_data["parkMode"]
                ignition = vehicle_state_data["ignition"]
                speed = vehicle_state_data["speed"]
                ota = vehicle_state_data["ota"]
                command = vehicle_state_data["command"]
                gpsFix = vehicle_state_data["gpsFix"]
                primaryBatteryStatus = vehicle_state_data["primaryBatteryStatus"]
                vehicleMode = vehicle_state_data["vehicleMode"]

                # Validate and log details
                if systemId == systemId_actual and status == "Success":
                    print("Vehicle state details retrieved successfully.")
                    break
            else:
                testResult(self, "failed",
                           "Vehicle state details should be retrieved for the desired systemId.",
                           "Vehicle state details retrieval failed.")
                raise AssertionError("Vehicle state details could not be validated.")
        else:
            print("No vehicle state records exist in the cloud database.")
            raise AssertionError("No vehicle state records found.")

        # Print extracted vehicle state details
        print("----------------------------------------------------------")
        print(f"System ID: {systemId_actual}")
        print(f"Current State: {currentState}")
        print(f"Park Mode: {parkMode}")
        print(f"Ignition: {ignition}")
        print(f"Speed: {speed}")
        print(f"OTA: {ota}")
        print(f"Command: {command}")
        print(f"GPS Fix: {gpsFix}")
        print(f"Primary Battery Status: {primaryBatteryStatus}")
        print(f"Vehicle Mode: {vehicleMode}")
        print(f"Last Heart Beat Time: {lastHeartBeatTime}")
        print("----------------------------------------------------------")

        # testResult(self, "passed",
        # "Vehicle metadata details should be retrieved successfully for the desired systemId.",
        # "Vehicle metadata details retrieved successfully.")