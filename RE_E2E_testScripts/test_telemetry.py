import time
import pytest
from datetime import datetime, timedelta

from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file
from C2CModules.telemetry_modules import telemetry_Curr_eventType_global
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_Telemetry_global:

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test1_positive_telemetry_update_global_gps_speed(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        print("----------------------------------------------------------")
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "gps_speed2")
        time.sleep(5)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - odo

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_gps_speed_attribute, b2c_telemetry_gps_speed_attribute)

        if b2c_telemetry_gps_speed_attribute in str(ls[0]):
            print(f"GPS Speed attribute name printed in device log : ' {b2c_telemetry_gps_speed_attribute} ' ")
            testResult(self, "passed", "GPS Speed attribute should be present in telemetry data",
                       "GPS Speed attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "GPS Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "GPS Speed attribute should be present in telemetry data ",
                       "GPS Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_speed = b2c_telemetry_gps_speed_attribute + b2c_telemetry_gps_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_gps_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"GPS Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "passed", "GPS Speed value should be published to cloud ",
                       "GPS Speed value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "GPS Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "GPS Speed value should be published to cloud ",
                       "GPS Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

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
        value = ""

        response = telemetry_Curr_eventType_global(self, telemetry_vel_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            # dataList_len = len(response_body["responseData"]["dataList"])
            dataList_len = len(response_body["responseData"]["signals"])
            # print(dataList_len)
            for j in range(dataList_len):
                # print(response_body["responseData"]["dataList"][j]["name"])
                # print(response_body["responseData"]["dataList"][j]["value"])
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_gps_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    break
        except:
            print("dataList is empty in api response")

        print("GPS Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
        print("GPS Speed value stored in Cloud DB : ", value)

        if int(value) == int(b2c_telemetry_speed_value):
            testResult(self, "passed",
                       "GPS Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "GPS Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "GPS Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "GPS Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

            #self.result.set_result(TestResults.failed)

    def test2_positive_telemetry_update_global_odometer(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Start c2c services
        # ===========================================================================================
        print("----------------------------------------------------------")
        # run_c2cServices_on_primary_IVI(self, onboardingType, chipsetType)

        print("----------------------------------------------------------")
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
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
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
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

        response = telemetry_Curr_eventType_global(self, telemetry_odo_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_odometer_value):
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