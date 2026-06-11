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


class Test_R8S3_TelemetryEvent:
    @pytest.mark.regression
    # Validate telemetry - speed functionality.
    def test_positive_bikeSecuritySafety_telemetryUpdate_HA(self):
        print("----------------------------------------------------------")
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for HA on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ha")
        time.sleep(5)

        print("HA stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - HA

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify HA attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_ha_attribute, b2c_telemetry_ha_attribute)

        if b2c_telemetry_ha_attribute in str(ls[0]):
            print(f"HA attribute name printed in device log : ' {b2c_telemetry_ha_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for HA (constr_and_send_proto_msg success for 4446)",
                       "Device logs contains the logs for HA (constr_and_send_proto_msg success for 4446), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "HA logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for HA (constr_and_send_proto_msg success for 4446)",
                       "Device logs doesnot contain the logs for HA (constr_and_send_proto_msg success for 4446) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify HA value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        if cloudEnv in ["GCP-QA3"]:
            telemetry_attribute_HA = "VCU_Data__Harsh_Acc_Flg_RX_V"
            telemetry_HA_event_type = 69

        response = telemetry_Curr_eventType(self, telemetry_HA_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_HA:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("HARSH ACCELERATION value configured in the stub : ", telemetry_HA_value)
        print("HARSH ACCELERATION value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_HA_value) and int(reasonCode) == int(telemetry_HA_reason_code):
            testResult(self, "passed",
                       "HARSH ACCELERATION value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "HARSH ACCELERATION value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "HARSH ACCELERATION value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "HARSH ACCELERATION value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")

            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry - speed functionality.
    def test_positive_bikeSecuritySafety_telemetryUpdate_HB(self):
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
        print("Run stub for HB on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_hb")
        time.sleep(5)

        print("HB stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - HB

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify HB attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_hb_attribute, b2c_telemetry_hb_attribute)

        if b2c_telemetry_hb_attribute in str(ls[0]):
            print(f"HB attribute name printed in device log : ' {b2c_telemetry_hb_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for HB (constr_and_send_proto_msg success for 4447)",
                       "Device logs contains the logs for HB (constr_and_send_proto_msg success for 4447), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "HB logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for HB (constr_and_send_proto_msg success for 4447)",
                       "Device logs doesnot contain the logs for HB (constr_and_send_proto_msg success for 4447) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify HB value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_HB_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_HB:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("HARSH BRAKING value configured in the stub : ", telemetry_HB_value)
        print("HARSH BRAKING value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_HB_value) and int(reasonCode) == int(telemetry_HB_reason_code):
            testResult(self, "passed",
                       "HARSH BRAKING value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "HARSH BRAKING value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "HARSH BRAKING value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "HARSH BRAKING value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_positive_bikeSecuritySafety_telemetryUpdate_overSpeed(self):

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

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if float(value) == float(
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