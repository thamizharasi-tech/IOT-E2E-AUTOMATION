import time
import pytest
from datetime import datetime, timedelta

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file
from C2CModules.telemetry_modules import *
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import vehicle_update_metadata
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_R8S3_TelemetryUpdate:
    @pytest.mark.regression
    # Validate telemetry - speed functionality.
    def test_positive_bikeSecuritySafety_telemetryUpdate_gpsSpeed(self):
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

        response = telemetry_Curr_eventType(self, telemetry_vel_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            # dataList_len = len(response_body["responseData"]["dataList"])
            dataList_len = len(response_body["responseData"]["signals"])
            # print(dataList_len)
            for j in range(dataList_len):
                # print(response_body["responseData"]["dataList"][j]["name"])
                # print(response_body["responseData"]["dataList"][j]["value"])
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_gps_speed or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_gps_speed1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    break
        except:
            print("dataList is empty in api response")

        print("GPS Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
        print("GPS Speed value stored in Cloud DB : ", value)

        if float(value) == float(b2c_telemetry_speed_value):
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

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry - speed functionality.
    def test_positive_bikeSecuritySafety_telemetryUpdate_ignitionState(self):
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
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignition_off")
        time.sleep(5)

        print("Telemetry-Ignition Off stub run process is completed, verify logs for telemetry details : ")
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

        # Telemetry-Ignition Off

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off attribute in the device
        ls = verify_message_in_log(self, telemetry_ignition_attribute, telemetry_ignition_attribute)

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
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1 or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value) or int(value) == int(telemetry_ignition_off_value):
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

    def test_positive_telemetry_odo(self):

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

