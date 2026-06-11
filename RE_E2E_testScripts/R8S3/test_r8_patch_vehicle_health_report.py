import pytest
import random
import time, datetime

from C2CModules.vehicle_configurations import update_priority_in_dtcConf
from C2CModules.vehicle_diagnostic import *
from C2CModules.vehicle_metadata import vehicle_get_vehicle_metadata_new, fetch_vehicle_model_by_systemId
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile, run_paho_command_on_primary_IVI, \
    pull_logs_from_IVI_device
from C2CModules.e2e_testData import *
from C2CModules.testResults import testResult
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_VHR_Telemetry_result:

    def test_positive_generate_vehicle_health_report_battery_soc_new(self):

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
        time.sleep(5)

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
        print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_battery_soc")
        time.sleep(5)

        print("Vehicle health report stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - SOC

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        b2c_telemetry_battery_soc_attribute = "Batt_Sts_Info__Display_SoC_RX_V"

        # verify Battery SOC attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soc_attribute, b2c_telemetry_battery_soc_attribute)

        if b2c_telemetry_battery_soc_attribute in str(ls[0]):
            print(f"Battery SOC attribute name printed in device log : ' {b2c_telemetry_battery_soc_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for SOC",
                       "Device logs contains the logs for SOC, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOC logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for SOC",
                       "Device logs does not contain the logs for SOC or failed to read the device log, pls refer device logs for detailed info")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify battery soc value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soc1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Battery SOC value configured in the stub : ", b2c_telemetry_battery_soc_value1)
        print("Battery SOC value stored in Cloud DB : ", value)

        if float(value) == float(b2c_telemetry_battery_soc_value1):
            testResult(self, "passed",
                       "BATTERY SOC value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOC value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "BATTERY SOC value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOC value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition_off")
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
        ls = verify_message_in_log(self, telemetry_attribute_ignition1, telemetry_attribute_ignition1)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ignition1} ' ")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value) or int(value1) == int(telemetry_ignition_off_value):
            testResult(self, "passed",
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 40
        thresholdLow = 30
        areaId1 = 0
        thresholdHigh1 = 3
        thresholdLow1 = 0
        print("Model : ", modelId)
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc2)
        print("Battery SOC - Event Type : ", telemetry_battery_eventType1)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc1)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition1)
        print("Ignition - Event Type : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition1)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc2,
                                                      telemetry_battery_eventType1,
                                                      telemetry_attribute_ev_battery_soc1, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition1,
                                                      telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc2,
                                                         telemetry_battery_eventType1,
                                                         telemetry_attribute_ev_battery_soc1, areaId, thresholdHigh,
                                                         thresholdLow, telemetry_attributeId_ignition1,
                                                         telemetry_ignition_event_type,
                                                         telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                         thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v5(self, systemId, telemetry_attribute_ev_battery_soc1, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_soc_new_exceed_threshold_limit(self):

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
        time.sleep(5)

        print("----------------------------------------------------------")
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ==========================================================================================

        print("----------------------------------------------------------")
        print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_battery_soc_exceed_limit")
        time.sleep(5)

        print("Vehicle health report stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - SOC

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        b2c_telemetry_battery_soc_attribute = "Batt_Sts_Info__Display_SoC_RX_V"

        # verify Battery SOC attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soc_attribute, b2c_telemetry_battery_soc_attribute)

        if b2c_telemetry_battery_soc_attribute in str(ls[0]):
            print(f"Battery SOC attribute name printed in device log : ' {b2c_telemetry_battery_soc_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for SOC",
                       "Device logs contains the logs for SOC, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOC logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for SOC",
                       "Device logs does not contain the logs for SOC or failed to read the device log, pls refer device logs for detailed info")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify battery soc value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soc1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Battery SOC value configured in the stub : ", b2c_telemetry_battery_soc_value2)
        print("Battery SOC value stored in Cloud DB : ", value)

        if float(value) == float(b2c_telemetry_battery_soc_value2):
            testResult(self, "passed",
                       "BATTERY SOC value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOC value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "BATTERY SOC value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOC value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition_off")
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
        ls = verify_message_in_log(self, telemetry_attribute_ignition1, telemetry_attribute_ignition1)

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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value) or int(value1) == int(telemetry_ignition_off_value):
            testResult(self, "passed",
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 40
        thresholdLow = 30
        areaId1 = 0
        thresholdHigh1 = 3
        thresholdLow1 = 0
        print("Model : ", modelId)
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc2)
        print("Battery SOC - Event Type : ", telemetry_battery_eventType1)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc1)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition1)
        print("Ignition - Event Type : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition1)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc2,
                                                      telemetry_battery_eventType1,
                                                      telemetry_attribute_ev_battery_soc1, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition1,
                                                      telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc2,
                                                         telemetry_battery_eventType1,
                                                         telemetry_attribute_ev_battery_soc1, areaId, thresholdHigh,
                                                         thresholdLow, telemetry_attributeId_ignition1,
                                                         telemetry_ignition_event_type,
                                                         telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                         thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v5(self, systemId, telemetry_attribute_ev_battery_soc1, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_odo_new(self):

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
        time.sleep(5)

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
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition_off")
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
        ls = verify_message_in_log(self, telemetry_attribute_ignition1, telemetry_attribute_ignition1)

        if telemetry_attribute_ignition1 in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ignition1} ' ")
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
        value1 = reasonCode = ""

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
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value) or int(value1) == int(telemetry_ignition_off_value):
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

        print("-------------------------------------------------------------------------")

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 5500
        thresholdLow = 5000
        areaId1 = 0
        thresholdHigh1 = 3
        thresholdLow1 = 0
        print("Model : ", modelId)
        print("Telemetry Odo - AttributeId : ", telemetry_attributeId_odo)
        print("Telemetry Odo - Event Type : ", telemetry_odo_event_type1)
        print("Telemetry Odo - AttributeName : ", telemetry_attribute_odo)
        print("Telemetry Odo - AreaId : ", areaId)
        print("Telemetry Odo - ThresholdHigh : ", thresholdHigh)
        print("Telemetry Odo - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition1)
        print("Ignition - Event Type : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition1)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo,
                                                      telemetry_odo_event_type1,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition1,
                                                      telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo,
                                                         telemetry_odo_event_type1,
                                                         telemetry_attribute_odo, areaId, thresholdHigh,
                                                         thresholdLow, telemetry_attributeId_ignition1,
                                                         telemetry_ignition_event_type,
                                                         telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                         thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v5(self, systemId, telemetry_attribute_odo, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_odo_new_exceed_limit(self):

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
        time.sleep(5)

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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_odo_exceed_limit")
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

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    print("Value: ", value)
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value1)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value1):
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition_off")
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
        ls = verify_message_in_log(self, telemetry_attribute_ignition1, telemetry_attribute_ignition1)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_ignition1} ' ")
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
        value1 = reasonCode = ""

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
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value) or int(value1) == int(telemetry_ignition_off_value):
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

        print("-------------------------------------------------------------------------")

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 5500
        thresholdLow = 5000
        areaId1 = 0
        thresholdHigh1 = 3
        thresholdLow1 = 0
        print("Model : ", modelId)
        print("Telemetry Odo - AttributeId : ", telemetry_attributeId_odo)
        print("Telemetry Odo - EventType : ", telemetry_odo_event_type1)
        print("Telemetry Odo - AttributeName : ", telemetry_attribute_odo)
        print("Telemetry Odo - AreaId : ", areaId)
        print("Telemetry Odo - ThresholdHigh : ", thresholdHigh)
        print("Telemetry Odo - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition1)
        print("Ignition - EventType : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition1)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo,
                                                      telemetry_odo_event_type1,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition1,
                                                      telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo,
                                                         telemetry_odo_event_type1,
                                                         telemetry_attribute_odo, areaId, thresholdHigh,
                                                         thresholdLow, telemetry_attributeId_ignition1,
                                                         telemetry_ignition_event_type,
                                                         telemetry_attribute_ignition1, areaId1, thresholdHigh1,
                                                         thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v5(self, systemId, telemetry_attribute_odo, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)


class Test_VHR_Vehicle_status:

    def test_positive_generate_vehicle_health_report_status_priority_3_good(self):

        priority_value = 3
        cloudEnv = read_cloud_env(self)
        update_priority_in_dtcConf(self, cloudEnv, onboardingType, chipsetType, priority_value)

        # Generate DTC Alert
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "diagnostic_event1")

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        startDate = datetime.now() - timedelta(days=1)
        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

        offset = "0"
        limit = "10"
        details = "true"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)
        print("----------------------------------------------------------")

        # Call DTC reusable module
        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        #issuedTime = ""
        dtc_priority = None

        if response_body["message"] == "Data Saved Successfully":
            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:
                for i in range(dtc_len):
                    status = response_body["responseData"]["DTCs"][i]["status"]
                    if status == 'Unresolved':
                        dtc_priority = response_body["responseData"]["DTCs"][i]["priority"]
                        #issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]
                        break

            print("----------------------------------------------------------")
            if dtc_priority:
                print('DTC Priority : ', dtc_priority)
            else:
                print('No unresolved DTC found.')
            print("----------------------------------------------------------")

            testResult(self, "passed", "DTC details should be saved & fetched successfully",
                       "DTC details are saved & fetched successfully ")
            #self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "DTC details should be saved & fetched successfully",
                       "Failed to save/fetch the dtc details. Reason for failure: " + str(response_body))
            assert False
            #self.result.set_result(TestResults.failed)

        else:
            print("Something went wrong")
            #self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # Validate priority
        if str(priority_value) == str(dtc_priority):
            testResult(self, "passed", "Priority level matches", "Configured and dtc details priority are same")
        else:
            testResult(self, "verificationFailed", "Priority level mismatch", "Configured and dtc details priority differ")

        print("----------------------------------------------------------")
        print("Generate Vehicle Health Report")
        print("----------------------------------------------------------")

        # Fetch Vehicle Health Report
        response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        if response_body.get("message") != "Vehicle Health Report Generated Successfully":
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))
            return
        try:
            report = response_body["vehicleHealthReport"]
            model = report.get("model")
            dateOfInspection = report.get("dateOfInspection")
            kilometers = report.get("kilometers")
            ignitionStatus = report.get("ignitionStatus")
            activeDTCs = report.get("activeDTCs")
            actual_vehicle_status = report.get("vehicleStatus")

            print("Report Details:")
            print(f"-> Model              : {model}")
            print(f"-> Date of Inspection : {dateOfInspection}")
            print(f"-> Kilometers         : {kilometers}")
            print(f"-> System ID          : {systemId}")
            print(f"-> Report ID          : {report.get('reportId')}")
            print(f"-> Ignition Status    : {ignitionStatus}")
            print(f"-> Active DTCs        : {activeDTCs}")
            print(f"-> Vehicle Status     : {actual_vehicle_status}")
            print("----------------------------------------------------------")

            # Compute Expected Vehicle Status
            if activeDTCs == 0 or (activeDTCs == 1 and priority_value == 3):
                expected_vehicle_status = "Good"
            else:
                print("something went wrong")

            # Validate Overall Vehicle Status
            print("\nVehicle Status Evaluation")
            print(f"-> Expected Status : {expected_vehicle_status}")
            print(f"-> Reported Status : {actual_vehicle_status}")

            if expected_vehicle_status == actual_vehicle_status:
                testResult(self, "passed", "Overall status should reflect vehicle health",
                           "Overall status matches expected")
            else:
                testResult(self, "failed", "Overall status should reflect vehicle health",
                           "Overall status does not match expected")



            print("=============================================================")

        except KeyError as e:
            print(f"KeyError: Missing expected field — {e}")
        except ValueError as e:
            print(f"ValueError: Invalid data type — {e}")

        #DTC Clear

        dtc_clear(self, onboardingType, chipsetType)

    def test_positive_generate_vehicle_health_report_status_priority_1_warning(self):

        priority_value = 1
        cloudEnv = read_cloud_env(self)
        update_priority_in_dtcConf(self, cloudEnv, onboardingType, chipsetType, priority_value)

        # Generate DTC Alert
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "diagnostic_event1")
        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        startDate = datetime.now() - timedelta(days=1)
        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

        offset = "0"
        limit = "10"
        details = "true"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)
        print("----------------------------------------------------------")

        # Call DTC reusable module
        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # issuedTime = ""
        dtc_priority = None

        if response_body["message"] == "Data Saved Successfully":
            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:
                for i in range(dtc_len):
                    status = response_body["responseData"]["DTCs"][i]["status"]
                    if status == 'Unresolved':
                        dtc_priority = response_body["responseData"]["DTCs"][i]["priority"]
                        # issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]
                        break

            print("----------------------------------------------------------")
            if dtc_priority:
                print('DTC Priority : ', dtc_priority)
            else:
                print('No unresolved DTC found.')
            print("----------------------------------------------------------")

            testResult(self, "passed", "DTC details should be saved & fetched successfully",
                       "DTC details are saved & fetched successfully ")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "DTC details should be saved & fetched successfully",
                       "Failed to save/fetch the dtc details. Reason for failure: " + str(response_body))
            assert False
            # self.result.set_result(TestResults.failed)

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # Validate priority
        if str(priority_value) == str(dtc_priority):
            testResult(self, "passed", "Priority level matches", "Configured and dtc details priority are same")
        else:
            testResult(self, "verificationFailed", "Priority level mismatch", "Configured and dtc details priority differ")

        print("----------------------------------------------------------")
        print("Generate Vehicle Health Report")
        print("----------------------------------------------------------")

        # Fetch Vehicle Health Report
        response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        if response_body.get("message") != "Vehicle Health Report Generated Successfully":
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))
            return
        try:
            report = response_body["vehicleHealthReport"]
            model = report.get("model")
            dateOfInspection = report.get("dateOfInspection")
            kilometers = report.get("kilometers")
            ignitionStatus = report.get("ignitionStatus")
            activeDTCs = report.get("activeDTCs")
            actual_vehicle_status = report.get("vehicleStatus")

            print("Report Details:")
            print(f"-> Model              : {model}")
            print(f"-> Date of Inspection : {dateOfInspection}")
            print(f"-> Kilometers         : {kilometers}")
            print(f"-> System ID          : {systemId}")
            print(f"-> Report ID          : {report.get('reportId')}")
            print(f"-> Ignition Status    : {ignitionStatus}")
            print(f"-> Active DTCs        : {activeDTCs}")
            print(f"-> Vehicle Status     : {actual_vehicle_status}")
            print("----------------------------------------------------------")

            # Compute Expected Vehicle Status
            if activeDTCs == 1 and priority_value in [1, 2]:
                expected_vehicle_status = "Warning"
            else:
                print("something went wrong")

            # Validate Overall Vehicle Status
            print("\nVehicle Status Evaluation")
            print(f"-> Expected Status : {expected_vehicle_status}")
            print(f"-> Reported Status : {actual_vehicle_status}")

            if expected_vehicle_status == actual_vehicle_status:
                testResult(self, "passed", "Overall status should reflect vehicle health",
                           "Overall status matches expected")
            else:
                testResult(self, "failed", "Overall status should reflect vehicle health",
                           "Overall status does not match expected")

            print("=============================================================")

        except KeyError as e:
            print(f"KeyError: Missing expected field — {e}")
        except ValueError as e:
            print(f"ValueError: Invalid data type — {e}")

        #DTC Clear

        dtc_clear(self, onboardingType, chipsetType)

    def test_positive_generate_vehicle_health_report_status_priority_2_warning(self):

        priority_value = 2

        cloudEnv = read_cloud_env(self)
        update_priority_in_dtcConf(self, cloudEnv, onboardingType, chipsetType, priority_value)

        # Generate DTC Alert
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "diagnostic_event1")
        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        startDate = datetime.now() - timedelta(days=1)
        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

        offset = "0"
        limit = "10"
        details = "true"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)
        print("----------------------------------------------------------")

        # Call DTC reusable module
        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # issuedTime = ""
        dtc_priority = None

        if response_body["message"] == "Data Saved Successfully":
            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:
                for i in range(dtc_len):
                    status = response_body["responseData"]["DTCs"][i]["status"]
                    if status == 'Unresolved':
                        dtc_priority = response_body["responseData"]["DTCs"][i]["priority"]
                        # issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]
                        break

            print("----------------------------------------------------------")
            if dtc_priority:
                print('DTC Priority : ', dtc_priority)
            else:
                print('No unresolved DTC found.')
            print("----------------------------------------------------------")

            testResult(self, "passed", "DTC details should be saved & fetched successfully",
                       "DTC details are saved & fetched successfully ")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "DTC details should be saved & fetched successfully",
                       "Failed to save/fetch the dtc details. Reason for failure: " + str(response_body))
            assert False
            # self.result.set_result(TestResults.failed)

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # Validate priority
        if str(priority_value) == str(dtc_priority):
            testResult(self, "passed", "Priority level matches", "Configured and dtc details priority are same")
        else:
            testResult(self, "verificationFailed", "Priority level mismatch", "Configured and dtc details priority differ")

        print("----------------------------------------------------------")
        print("Generate Vehicle Health Report")
        print("----------------------------------------------------------")

        # Fetch Vehicle Health Report
        response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        if response_body.get("message") != "Vehicle Health Report Generated Successfully":
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))
            return
        try:
            report = response_body["vehicleHealthReport"]
            model = report.get("model")
            dateOfInspection = report.get("dateOfInspection")
            kilometers = report.get("kilometers")
            ignitionStatus = report.get("ignitionStatus")
            activeDTCs = report.get("activeDTCs")
            actual_vehicle_status = report.get("vehicleStatus")

            print("Report Details:")
            print(f"-> Model              : {model}")
            print(f"-> Date of Inspection : {dateOfInspection}")
            print(f"-> Kilometers         : {kilometers}")
            print(f"-> System ID          : {systemId}")
            print(f"-> Report ID          : {report.get('reportId')}")
            print(f"-> Ignition Status    : {ignitionStatus}")
            print(f"-> Active DTCs        : {activeDTCs}")
            print(f"-> Vehicle Status     : {actual_vehicle_status}")
            print("----------------------------------------------------------")

            # Compute Expected Vehicle Status
            if activeDTCs == 1 and priority_value in [1, 2]:
                expected_vehicle_status = "Warning"
            else:
                print("something went wrong")

            # Validate Overall Vehicle Status
            print("\nVehicle Status Evaluation")
            print(f"-> Expected Status : {expected_vehicle_status}")
            print(f"-> Reported Status : {actual_vehicle_status}")

            if expected_vehicle_status == actual_vehicle_status:
                testResult(self, "passed", "Overall status should reflect vehicle health",
                           "Overall status matches expected")
            else:
                testResult(self, "failed", "Overall status should reflect vehicle health",
                           "Overall status does not match expected")

            print("=============================================================")

        except KeyError as e:
            print(f"KeyError: Missing expected field — {e}")
        except ValueError as e:
            print(f"ValueError: Invalid data type — {e}")

        dtc_clear(self, onboardingType, chipsetType)

    def test_positive_generate_vehicle_health_report_status_priority_0_critical(self):

        priority_value = 0

        cloudEnv = read_cloud_env(self)
        update_priority_in_dtcConf(self, cloudEnv, onboardingType, chipsetType, priority_value)

        # Generate DTC Alert
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "diagnostic_event1")
        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        startDate = datetime.now() - timedelta(days=1)
        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")

        offset = "0"
        limit = "10"
        details = "true"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)
        print("----------------------------------------------------------")

        # Call DTC reusable module
        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        # issuedTime = ""
        dtc_priority = None

        if response_body["message"] == "Data Saved Successfully":
            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:
                for i in range(dtc_len):
                    status = response_body["responseData"]["DTCs"][i]["status"]
                    if status == 'Unresolved':
                        dtc_priority = response_body["responseData"]["DTCs"][i]["priority"]
                        # issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]
                        break

            print("----------------------------------------------------------")
            if dtc_priority:
                print('DTC Priority : ', dtc_priority)
            else:
                print('No unresolved DTC found.')
            print("----------------------------------------------------------")

            testResult(self, "passed", "DTC details should be saved & fetched successfully",
                       "DTC details are saved & fetched successfully ")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "DTC details should be saved & fetched successfully",
                       "Failed to save/fetch the dtc details. Reason for failure: " + str(response_body))
            assert False
            # self.result.set_result(TestResults.failed)

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # Validate priority
        if str(priority_value) == str(dtc_priority):
            testResult(self, "passed", "Priority level matches", "Configured and dtc details priority are same")
        else:
            testResult(self, "verificationFailed", "Priority level mismatch", "Configured and dtc details priority differ")

        print("----------------------------------------------------------")
        print("Generate Vehicle Health Report")
        print("----------------------------------------------------------")

        # Fetch Vehicle Health Report
        response = VehicleHealthReport_generate_vehicleHealthReport(self, systemId, "valid")
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        if response_body.get("message") != "Vehicle Health Report Generated Successfully":
            print("Vehicle health report was not generated successfully.")
            print("Reason:", response_body.get("message", "Unknown error"))
            return
        try:
            report = response_body["vehicleHealthReport"]
            model = report.get("model")
            dateOfInspection = report.get("dateOfInspection")
            kilometers = report.get("kilometers")
            ignitionStatus = report.get("ignitionStatus")
            activeDTCs = report.get("activeDTCs")
            actual_vehicle_status = report.get("vehicleStatus")

            print("Report Details:")
            print(f"-> Model              : {model}")
            print(f"-> Date of Inspection : {dateOfInspection}")
            print(f"-> Kilometers         : {kilometers}")
            print(f"-> System ID          : {systemId}")
            print(f"-> Report ID          : {report.get('reportId')}")
            print(f"-> Ignition Status    : {ignitionStatus}")
            print(f"-> Active DTCs        : {activeDTCs}")
            print(f"-> Vehicle Status     : {actual_vehicle_status}")
            print("----------------------------------------------------------")

            # Compute Expected Vehicle Status
            if activeDTCs == 1 and priority_value == 0:
                expected_vehicle_status = "Critical"
            else:
                print("something went wrong")

            # Validate Overall Vehicle Status
            print("\nVehicle Status Evaluation")
            print(f"-> Expected Status : {expected_vehicle_status}")
            print(f"-> Reported Status : {actual_vehicle_status}")

            if expected_vehicle_status == actual_vehicle_status:
                testResult(self, "passed", "Overall status should reflect vehicle health",
                           "Overall status matches expected")
            else:
                testResult(self, "failed", "Overall status should reflect vehicle health",
                           "Overall status does not match expected")

            print("=============================================================")

        except KeyError as e:
            print(f"KeyError: Missing expected field — {e}")
        except ValueError as e:
            print(f"ValueError: Invalid data type — {e}")

        dtc_clear(self, onboardingType, chipsetType)

class Test_try:

    def test_clear_dtc(self):

        dtc_clear(self, onboardingType, chipsetType)