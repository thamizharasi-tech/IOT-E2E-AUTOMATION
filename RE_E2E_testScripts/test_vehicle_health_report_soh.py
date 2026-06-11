import pytest
import random
import time, datetime

from C2CModules.vehicle_diagnostic import VehicleHealthReport_insertModel, VehicleHealthReport_updateModel, \
    VehicleHealthReport_updateModel_new, VehicleHealthReport_generate_vehicleHealthReport, \
    new_model_config_for_vehicle_health_report, update_model_config_for_vehicle_health_report, \
    generate_vehicle_health_report, update_model_config_for_vehicle_health_report_new
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

    def test_positive_generate_vehicle_health_report_battery_soh(self):

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

        # telemetry - SOC
        print("-------------Telemetry Update - Battery SOC & Battery SOH---------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Battery SOH attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soh_attribute, b2c_telemetry_battery_soh_attribute)

        if b2c_telemetry_battery_soh_attribute in str(ls[0]):
            print(f"Battery SOH attribute name printed in device log : ' {b2c_telemetry_battery_soh_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Battery SOH",
                       "Device logs contains the logs for Battery SOH, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery SOH logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Battery SOH",
                       "Device logs does not contain the logs for Battery SOH or failed to read the device log, pls refer device logs for detailed info")

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

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOH in curr value==================================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            # Flags to track validation
            soh_validated = False
            for j in range(dataList_len):
                signal = response_body["responseData"]["signals"][j]
                name = signal["name"]
                value = signal["value"]
                # Validate State of Health (SoH)
                if not soh_validated and name == telemetry_attribute_ev_battery_soh:
                    print("BATTERY SOH value configured in the stub:", b2c_telemetry_battery_soh_value1)
                    print("BATTERY SOH value stored in Cloud DB:", value)
                    if int(value) == int(float(b2c_telemetry_battery_soh_value1)):
                        testResult(self, "passed",
                                   "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                                   "BATTERY SOH value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
                    else:
                        testResult(self, "failed",
                                   "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                                   "BATTERY SOH value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
                    soh_validated = True
                # Exit loop if both are validated
                if soh_validated:
                    break
        except Exception as e:
            print("An error occurred while processing the response:", e)

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 40
        thresholdLow = 30
        areaId1 = 0
        thresholdHigh1 = 10
        thresholdLow1 = 1
        print("Model : ", modelId)
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Battery SOH - AttributeId : ", telemetry_attributeId_ev_battery_soh)
        print("Battery SOH - AttributeName : ", telemetry_attribute_ev_battery_soh)
        print("Battery SOH - AreaId : ", areaId)
        print("Battery SOH - ThresholdHigh : ", thresholdHigh)
        print("Battery SOH - ThresholdLow : ", thresholdLow)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc,
                                                   telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ev_battery_soh,
                                                   telemetry_attribute_ev_battery_soh, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 20
        thresholdLow = 1
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_new(self, modelId, telemetry_attributeId_ev_battery_soh,
                                                          telemetry_attribute_ev_battery_soh, areaId, thresholdHigh,
                                                          thresholdLow)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report(self, systemId, telemetry_attribute_ev_battery_soh, thresholdLow, thresholdHigh,
                                       b2c_telemetry_battery_soh_value1)


    def test_positive_generate_vehicle_health_report_battery_soh_exceed_limit(self):

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
        print("-------------Telemetry Update - Battery SOC & Battery SOH---------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Battery SOH attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soh_attribute, b2c_telemetry_battery_soh_attribute)

        if b2c_telemetry_battery_soh_attribute in str(ls[0]):
            print(f"Battery SOH attribute name printed in device log : ' {b2c_telemetry_battery_soh_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Battery SOH",
                       "Device logs contains the logs for Battery SOH, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery SOH logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Battery SOH",
                       "Device logs does not contain the logs for Battery SOH or failed to read the device log, pls refer device logs for detailed info")

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

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        value = ""

        # ==============================Validate Battery SOH in curr value==================================

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            # Flags to track validation
            soh_validated = False
            for j in range(dataList_len):
                signal = response_body["responseData"]["signals"][j]
                name = signal["name"]
                value = signal["value"]
                # Validate State of Health (SoH)
                if not soh_validated and name == telemetry_attribute_ev_battery_soh:
                    print("BATTERY SOH value configured in the stub:", b2c_telemetry_battery_soh_value2)
                    print("BATTERY SOH value stored in Cloud DB:", value)
                    if int(value) == int(float(b2c_telemetry_battery_soh_value2)):
                        testResult(self, "passed",
                                   "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                                   "BATTERY SOH value is stored in the Cloud DB and same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
                    else:
                        testResult(self, "failed",
                                   "BATTERY SOH value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                                   "BATTERY SOH value is not stored in the Cloud DB or same as that of configured in the stub running on device. Please refer to cloud logs for detailed info.")
                    soh_validated = True
                # Exit loop if both are validated
                if soh_validated:
                    break
        except Exception as e:
            print("An error occurred while processing the response:", e)

    def test_11(self):

        print("\n-------------------Vehicle Health Report----------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        modelId = fetch_vehicle_model_by_systemId(self, systemId)
        areaId = 0
        thresholdHigh = 40
        thresholdLow = 30
        areaId1 = 0
        thresholdHigh1 = 10
        thresholdLow1 = 1
        print("Model : ", modelId)
        print("Battery SOC - AttributeId : ", telemetry_attributeId_ev_battery_soc)
        print("Battery SOC - AttributeName : ", telemetry_attribute_ev_battery_soc)
        print("Battery SOC - AreaId : ", areaId)
        print("Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Battery SOC - ThresholdLow : ", thresholdLow)
        print("Battery SOH - AttributeId : ", telemetry_attributeId_ev_battery_soh)
        print("Battery SOH - AttributeName : ", telemetry_attribute_ev_battery_soh)
        print("Battery SOH - AreaId : ", areaId)
        print("Battery SOH - ThresholdHigh : ", thresholdHigh)
        print("Battery SOH - ThresholdLow : ", thresholdLow)

        new_model_config_for_vehicle_health_report(self, modelId, telemetry_attributeId_ev_battery_soc,
                                                   telemetry_attribute_ev_battery_soc, areaId, thresholdHigh,
                                                   thresholdLow, telemetry_attributeId_ev_battery_soh,
                                                   telemetry_attribute_ev_battery_soh, areaId1, thresholdHigh1,
                                                   thresholdLow1)

        # ---------------------------update model config--------------------------

        thresholdHigh = 20
        thresholdLow = 1
        print("Updated Battery SOC - ThresholdHigh : ", thresholdHigh)
        print("Updated Battery SOC - ThresholdLow : ", thresholdLow)

        update_model_config_for_vehicle_health_report_new(self, modelId, telemetry_attributeId_ev_battery_soh,
                                                          telemetry_attribute_ev_battery_soh, areaId, thresholdHigh,
                                                          thresholdLow)

        # ---------------------------Generate Vehicle Health Report--------------------------

        generate_vehicle_health_report(self, systemId, telemetry_attribute_ev_battery_soh, thresholdLow, thresholdHigh,
                                       b2c_telemetry_battery_soh_value2)