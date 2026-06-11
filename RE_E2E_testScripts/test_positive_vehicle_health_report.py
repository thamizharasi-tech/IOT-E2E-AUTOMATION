import pytest
import random
import time, datetime

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


class Test:

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

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soc:
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc1)
        print("Battery SOC - Event Type : ", telemetry_battery_eventType)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - Event Type : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc1,
                                                      telemetry_battery_eventType,
                                                      telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition,
                                                      telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_ev_battery_soc1,
                                                         telemetry_battery_eventType,
                                                         telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                         thresholdLow, telemetry_attributeId_ignition,
                                                         telemetry_ignition_event_type,
                                                         telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                         thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_ev_battery_soc, thresholdLow,
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

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soc:
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "BATTERY SOC value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOC value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            #self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc1)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc,
                                                   telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc1,
                                                          telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                          thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)


        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_ev_battery_soc, thresholdLow, thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_soh_new(self):

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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_battery_soh")
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

        # telemetry - SOH

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Battery SOC attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soh_attribute, b2c_telemetry_battery_soh_attribute)

        if b2c_telemetry_battery_soh_attribute in str(ls[0]):
            print(f"Battery SOH attribute name printed in device log : ' {b2c_telemetry_battery_soh_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for SOC",
                       "Device logs contains the logs for SOC, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery SOH logs is not present or device logs are not updated. pls refer device logs in detail")
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

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soh:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Battery SOH value configured in the stub : ", b2c_telemetry_battery_soh_value1)
        print("Battery SOH value stored in Cloud DB : ", value)

        if float(value) == float(b2c_telemetry_battery_soc_value1):
            testResult(self, "passed",
                       "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOH value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOH value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        thresholdHigh = 40
        thresholdLow = 30
        areaId1 = 0
        thresholdHigh1 = 3
        thresholdLow1 = 0
        print("Model : ", modelId)
        print("Battery SOH - AttributeId : ", telemetry_attributeId_ev_battery_soh1)
        print("Battery SOH - AttributeName : ", telemetry_attribute_ev_battery_soh)
        print("Battery SOH - AreaId : ", areaId)
        print("Battery SOH - ThresholdHigh : ", thresholdHigh)
        print("Battery SOH - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc,
                                                   telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc1,
                                                      telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_ev_battery_soc, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_soh_new_exceed_threshold_limit(self):

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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_battery_soh_exceed_limit")
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

        # verify Battery SOC attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soh_attribute, b2c_telemetry_battery_soh_attribute)

        if b2c_telemetry_battery_soh_attribute in str(ls[0]):
            print(f"Battery SOC attribute name printed in device log : ' {b2c_telemetry_battery_soh_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for SOC",
                       "Device logs contains the logs for SOC, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOH logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for SOH",
                       "Device logs does not contain the logs for SOH or failed to read the device log, pls refer device logs for detailed info")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify battery soc value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOC in curr value===============================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ev_battery_soh:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Battery SOH value configured in the stub : ", b2c_telemetry_battery_soh_value2)
        print("Battery SOH value stored in Cloud DB : ", value)

        if float(value) == float(b2c_telemetry_battery_soh_value2):
            testResult(self, "passed",
                       "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOH value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "BATTERY SOH value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
            # self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Battery SOH - AttributeId : ", telemetry_attributeId_ev_battery_soh1)
        print("Battery SOH - AttributeName : ", telemetry_attribute_ev_battery_soh)
        print("Battery SOH - AreaId : ", areaId)
        print("Battery SOH - ThresholdHigh : ", thresholdHigh)
        print("Battery SOH - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc,
                                                   telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 50
        thresholdLow = 20
        print("Updated Battery SOH - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOH - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc1,
                                                      telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_ev_battery_soc, thresholdLow,
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

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type, systemId, "valid")

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Telemetry Odo - AttributeName : ", telemetry_attribute_odo)
        print("Telemetry Odo - AreaId : ", areaId)
        print("Telemetry Odo - ThresholdHigh : ", thresholdHigh)
        print("Telemetry Odo - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_odo,
                                                   telemetry_attribute_odo, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_odo,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_odo, thresholdLow,
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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - EventType : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo, telemetry_odo_event_type1,
                                                   telemetry_attribute_odo, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition, telemetry_ignition_event_type,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo, telemetry_odo_event_type1,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition, telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_odo, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_tire_pressure_front_new(self):

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
        print("Run Telemetry-Tire Pressure stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_tire_pressure_front")
        time.sleep(5)

        print("Telemetry-Tire Pressure stub run process is completed, verify logs for telemetry details : ")
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

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type, systemId, "valid")

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Telemetry Odo - AttributeName : ", telemetry_attribute_odo)
        print("Telemetry Odo - AreaId : ", areaId)
        print("Telemetry Odo - ThresholdHigh : ", thresholdHigh)
        print("Telemetry Odo - ThresholdLow : ", thresholdLow)
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_odo,
                                                   telemetry_attribute_odo, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_odo,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_odo, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)

    def test_positive_generate_vehicle_health_report_battery_tire_pressure_exceed_limit(self):

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
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_ignition")
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
        value1 = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev1:
                    value1 = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value1 = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value1) == int(telemetry_ignition_value):
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
        print("Ignition - AttributeId : ", telemetry_attributeId_ignition)
        print("Ignition - EventType : ", telemetry_ignition_event_type)
        print("Ignition - AttributeName : ", telemetry_attribute_ignition)
        print("Ignition - AreaId : ", areaId1)
        print("Ignition - ThresholdHigh : ", thresholdHigh1)
        print("Ignition - ThresholdLow : ", thresholdLow1)

        new_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo, telemetry_odo_event_type1,
                                                   telemetry_attribute_odo, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ignition, telemetry_ignition_event_type,
                                                   telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 6500
        thresholdLow = 5500
        print("Updated Odo - ThresholdHigh : ", thresholdHigh)
        print("Updated Odo - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_v2(self, modelId, telemetry_attributeId_odo, telemetry_odo_event_type1,
                                                      telemetry_attribute_odo, areaId, thresholdHigh,
                                                      thresholdLow, telemetry_attributeId_ignition, telemetry_ignition_event_type,
                                                      telemetry_attribute_ignition, areaId1, thresholdHigh1,
                                                      thresholdLow1)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report_v3(self, systemId, telemetry_attribute_odo, thresholdLow,
                                          thresholdHigh, value, thresholdLow1, thresholdHigh1, value1)