import pytest
import time

from C2CModules.commandControl_modules import commandControl_Service_Request, \
    read_commandCtrl_trackingId, \
    commandControl_Service_Tracking, verify_commandCtrl_status
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_RE_SP2_Remote:
    @pytest.mark.regression
    # Validate  the VEHICLE_LOCK Command should be successful and return tracking id for the command
    def test1_positive_bikeSecuritySafety_command_remote_vehicleLock(self):
        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================
        print("----------------------------------------------------------")
        # Get systemId from device
        systemId = read_vehicleJsonFile(self, "system_id")
        print("----------------------------------------------------------")

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "commandControl_precondition_speedZero")
        time.sleep(40)

        print("precondition commands have been run on device, verify logs for detailed information")
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
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

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

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value_0):
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

    @pytest.mark.regression
    # Validate  the VEHICLE_LOCK Command should be successful and return tracking id for the command
    def test2_positive_bikeSecuritySafety_command_remote_vehicleUnLock(self):
        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================
        print("----------------------------------------------------------")
        # Get systemId from device
        systemId = read_vehicleJsonFile(self, "system_id")
        print("----------------------------------------------------------")

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "commandControl_precondition_speedZero")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

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

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value_0):
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

        name = command_vehicleUnLock
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

class Test_RE_R5_Remote:

    @pytest.mark.regression
    # Validate  the VEHICLE_HONK Command should be successful and return tracking id for the command
    def test1_positive_bikeSecuritySafety_command_remote_HONK(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

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

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        name = command_vehicleHonk
        time_value = command_time
        area = command_area
        value = command_value_0
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, area, value, timeout, "valid")


        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        # time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId, "valid")

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
                #self.result.set_result(TestResults.failed)
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    # Validate  the VEHICLE_HEADLIGHT Command should be successful and return tracking id for the command
    def test2_positive_bikeSecuritySafety_command_remote_whizz_bike(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

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

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        name = command_vehicleHeadLight
        time_value = command_time
        area = command_area
        value = command_value_0
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, area, value, timeout, "valid")

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
        # time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId, "valid")

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
                #self.result.set_result(TestResults.failed)
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

