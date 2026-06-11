import time
import pytest

from C2CModules.c2c_modules import testResult
from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, \
    run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, get_SystemId, decode_msg_body
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr, telemetry_Curr_eventType, telemetry_Curr_remainingCharge

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test1_telemetry:

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test0_telemetry_location(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_location")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test1_telemetry_odometer(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_odo")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - odo

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odo meter attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
            testResult(self, "passed", "Odo-meter attribute should be present in telemetry data",
                       "Odo-meter attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odo-meter attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Odo-meter attribute should be present in telemetry data ",
                       "Odo-meter attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_odo = telemetry_odo_attribute + b2c_telemetry_odo_value
        ls = verify_message_in_log(self, b2c_telemetry_odo_value, tele_odo)

        if tele_odo in str(ls[0]):
            print(f"Odo meter value printed in device log : ' {tele_odo} ' ")
            testResult(self, "passed", "Odo-meter value should be published to cloud ",
                       "Odo-meter value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odo-meter value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Odo-meter value should be published to cloud ",
                       "Odo-meter value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odo meter value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_odo_event_type, systemId)
        print(response_body)
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Odo meter value configured in the telemetry stub : ", b2c_telemetry_odo_value)
            print("Odo meter value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_odo_value):
            testResult(self, "passed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test2_telemetry_fuelLevel(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_fuel")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - fuel level

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify fuel level attribute in the device logs
        ls = verify_message_in_log(self, telemetry_fuel_level_attribute, telemetry_fuel_level_attribute)

        if telemetry_fuel_level_attribute in str(ls[0]):
            print(f"Fuel level attribute name printed in device log : ' {telemetry_fuel_level_attribute} ' ")
            testResult(self, "passed", "Fuel level attribute should be present in telemetry data",
                       "Fuel level attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Fuel level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Fuel level attribute should be present in telemetry data ",
                       "Fuel levl attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        telemetry_fuel_level_value1 = telemetry_fuel_level_attribute + b2c_telemetry_fuel_level_value
        ls = verify_message_in_log(self, telemetry_fuel_level_value1, telemetry_fuel_level_value1)

        if telemetry_fuel_level_value1 in str(ls[0]):
            print(f"Fuel level value printed in device log : ' {telemetry_fuel_level_value1} ' ")
            testResult(self, "passed", "Fuel level value should be published to cloud ",
                       "Fuel level value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Fuel level value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Fuel level value should be published to cloud ",
                       "Fuel levl value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify fuel level value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_fuel_level_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            # print(dataList_len)
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Fuel:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = None

        if value == b2c_telemetry_fuel_level_value:
            print("Fuel level value configured in the telemetry stub : ", b2c_telemetry_fuel_level_value)
            print("Fuel level value stored in Cloud DB : ", value)
            testResult(self, "passed",
                       "Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Fuel level value is not stored in the Cloud DB  or not same as that of configured in the telemetry stub running on device . pls refer "
                       "device logs for detailed info")
        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry - EV BATTERY LEVEL functionality.
    def test3_telemetry_ev_battery_level(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_battery_level")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - ev battery level

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify fuel level attribute in the device logs
        ls = verify_message_in_log(self, telemetry_ev_battery_level_attribute, telemetry_ev_battery_level_attribute)

        if telemetry_fuel_level_attribute in str(ls[0]):
            print(
                f"Telemetry_ev_battery_level attribute name printed in device log : ' {telemetry_ev_battery_level_attribute} ' ")
            testResult(self, "passed", "Telemetry_ev_battery_level attribute should be present in telemetry data",
                       "Telemetry_ev_battery_level attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Telemetry_ev_battery_level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Telemetry_ev_battery_level attribute should be present in telemetry data ",
                       "Telemetry_ev_battery_level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify battery level value in the device logs
        telemetry_ev_battery_level_value1 = telemetry_ev_battery_level_attribute + b2c_telemetry_ev_battery_level_value
        ls = verify_message_in_log(self, telemetry_ev_battery_level_value1, telemetry_ev_battery_level_value1)

        if telemetry_ev_battery_level_value1 in str(ls[0]):
            print(f"Telemetry_ev_battery_level value printed in device log : ' {telemetry_ev_battery_level_value1} ' ")
            testResult(self, "passed", "Telemetry_ev_battery_level value should be published to cloud ",
                       "Telemetry_ev_battery_level value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Telemetry_ev_battery_level value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry_ev_battery_level value should be published to cloud ",
                       "Telemetry_ev_battery_level value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify battery level value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_ev_battery_level_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            # print(dataList_len)
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_ev_battery_level:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = None

        if value == b2c_telemetry_ev_battery_level_value:
            print("telemetry_ev_battery_level value configured in the telemetry stub : ",
                  b2c_telemetry_ev_battery_level_value)
            print("telemetry_ev_battery_level value stored in Cloud DB : ", value)
            testResult(self, "passed",
                       "Telemetry_ev_battery_level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Telemetry_ev_battery_level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Telemetry_ev_battery_level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Telemetry_ev_battery_level value is not stored in the Cloud DB  or not same as that of configured in the telemetry stub running on device . pls refer "
                       "device logs for detailed info")
        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry - speed functionality.
    def test4_telemetry_speed(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_speed")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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
        ls = verify_message_in_log(self, telemetry_speed_attribute, telemetry_speed_attribute)

        if telemetry_speed_attribute in str(ls[0]):
            print(f"Speed attribute name printed in device log : ' {telemetry_speed_attribute} ' ")
            testResult(self, "passed", "Speed attribute should be present in telemetry data",
                       "Speed attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Speed attribute should be present in telemetry data ",
                       "Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Spped value printed in device log : ' {tele_speed} ' ")
            testResult(self, "passed", "Speed value should be published to cloud ",
                       "Speed value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Speed value should be published to cloud ",
                       "Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value):
            testResult(self, "passed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

            # self.result.set_result(TestResults.failed)

    @pytest.mark.regression
    # Validate telemetry-battery temperature functionality.
    def test5_telemetry_battery_temp(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_normal_battery_temp")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_temp_attribute, b2c_telemetry_battery_temp_attribute)

        if b2c_telemetry_battery_temp_attribute in str(ls[0]):
            print(
                f"Battery temperature attribute name printed in device log : ' {b2c_telemetry_battery_temp_attribute} ' ")
            testResult(self, "passed", "Battery temperature attribute should be present in telemetry data",
                       "Battery temperature attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery temperature attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Battery temperature attribute should be present in telemetry data ",
                       "Battery temperature attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_temp = b2c_telemetry_battery_temp_attribute + b2c_telemetry_normal_battery_temp_value
        ls = verify_message_in_log(self, b2c_telemetry_battery_temp_attribute, tele_temp)

        if tele_temp in str(ls[0]):
            print(f"Battery Temperature value printed in device log : ' {tele_temp} ' ")
            testResult(self, "passed", "Battery temperature value should be published to cloud ",
                       "Battery temperature value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery temperature value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Battery temperature value should be published to cloud ",
                       "Battery temperature value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_current_battery_temp:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Headlight value configured in the telemetry stub : ", tele_temp)
            print("Headlight value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_normal_battery_temp_value):
            testResult(self, "passed",
                       "Battery temperature value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery temperature value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Battery temperature value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery temperature value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-battery range/charge remaining functionality.
    def test6_telemetry_remaining_battery_charge(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "remaining_battery_charge")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_range_remaining_attribute,
                                   b2c_telemetry_range_remaining_attribute)

        if b2c_telemetry_battery_temp_attribute in str(ls[0]):
            print(
                f"Battery temperature attribute name printed in device log : ' {b2c_telemetry_range_remaining_attribute} ' ")
            testResult(self, "passed", "Battery remaining charge attribute should be present in telemetry data",
                       "Battery remaining charge attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery remaining charge attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Battery remaining charge attribute should be present in telemetry data ",
                       "Battery remaining charge attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_temp = b2c_telemetry_range_remaining_attribute + b2c_telemetry_range_remaining_value
        ls = verify_message_in_log(self, b2c_telemetry_range_remaining_attribute, tele_temp)

        if tele_temp in str(ls[0]):
            print(f"Battery remaining charge value printed in device log : ' {tele_temp} ' ")
            testResult(self, "passed", "Battery remaining charge value should be published to cloud ",
                       "Battery remaining charge value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery remaining charge value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Battery remaining charge value should be published to cloud ",
                       "Battery remaining charge value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_range_remaining:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Battery remaining charge value configured in the telemetry stub : ", tele_temp)
            print("Battery remaining charge value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_range_remaining_value):
            testResult(self, "passed",
                       "Battery remaining charge value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery remaining charge value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Battery remaining charge value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery remaining charge value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-battery range/charge remaining functionality.
    def test7_telemetry_remaining_battery_charge_in_percentage(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_battery_level")
        time.sleep(15)
        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "remaining_battery_charge")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        batteryLevel_value = batteryCapacity_value = batteryTemp_value = range_remaining = range_remaining_actual = ""

        # call api reusable module
        response = telemetry_Curr_eventType(self, "1001", systemId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", str(response.status_code))
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response to JSON
        response_body = response.json()

        # Validate api response body
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            if dataList_len >= 1:
                for i in range(dataList_len):
                    if response_body["responseData"]["dataList"][i]["name"] == "EV_BATTERY_LEVEL":
                        batteryLevel_value = response_body["responseData"]["dataList"][i]["value"]
                    if response_body["responseData"]["dataList"][i]["name"] == "INFO_EV_BATTERY_CAPACITY":
                        batteryCapacity_value = response_body["responseData"]["dataList"][i]["value"]
                    if response_body["responseData"]["dataList"][i]["name"] == "EV_BATTERY_TEMPERATURE":
                        batteryTemp_value = response_body["responseData"]["dataList"][i]["value"]

            print("EV_BATTERY_LEVEL : ", batteryLevel_value)
            print("INFO_EV_BATTERY_CAPACITY : ", batteryCapacity_value)
            print("EV_BATTERY_TEMPERATURE : ", batteryTemp_value)

            range_remaining = (float(batteryLevel_value) / float(batteryCapacity_value)) * 100
            range_remaining = "{:.2f}".format(range_remaining)

        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response = telemetry_Curr_remainingCharge(self, systemId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", str(response.status_code))
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate api response body
        if response_body["responseCode"] == "1200":
            try:
                range_remaining_actual = response_body["responseData"]["dataList"][0]
                # print("The Remaining Battery Charge (in percentage) stored in Cloud DB : ", range_remaining_actual)
            except:
                print("dataList is empty in api response")
                range_remaining_actual = ""

        print(
            "The Remaining Battery Charge (in percentage) calculated based on telemetry stub values[ REMAINING BATTERY CHARGE = (EV_BATTERY_LEVEL/INFO_EV_BATTERY_CAPACITY)*100 ] : ",
            range_remaining)
        print("The Remaining Battery Charge (in percentage) stored in Cloud DB : ", range_remaining_actual)

        if float(range_remaining) == float(range_remaining_actual):
            testResult(self, "passed",
                       "Battery remaining charge (in percentage) should be calculated using battery level and battery capacity running on device(temeletry stub values)",
                       "Battery remaining charge (in percentage) is calculated using battery level and battery capacity running on device(temeletry stub values). pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Battery remaining charge (in percentage) should be calculated using battery level and battery capacity running on device(temeletry stub values)",
                       "Battery remaining charge (in percentage) is not correct w.r. t battery level and battery capacity running on device(temeletry stub values). pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test8_chargingNotification_charge_port_Connected(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_connected")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_attribute, b2c_ev_charge_port_connected_attribute)

        if b2c_ev_charge_port_open_attribute in str(ls[0]):
            print(
                f"ev_charge_port_connected attribute is printed in device log : ' {b2c_ev_charge_port_connected_attribute} ' ")
            testResult(self, "passed", "ev_charge_port_connected attribute should be present in log",
                       "ev_charge_port_connected attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_connected attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_connected attribute should be present in log ",
                       "ev_charge_port_connected attribute is not present in log or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        charging_ON = b2c_ev_charge_port_connected_attribute + b2c_ev_charge_port_connected_state_ON
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_state_ON, charging_ON)

        if charging_ON in str(ls[0]):
            print(f"EV Charge Port Connected state is printed in device log : ' {charging_ON} ' ")
            testResult(self, "passed", "EV Charge Port Connected state should be published to cloud ",
                       "EV Charge Port Connected state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV Charge Port Connected state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "EV Charge Port Connected state should be published to cloud ",
                       "EV Charge Port Connected state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ev_charge_port_connected_event_type, systemId,
                                                  "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_connected_state_ON)
        print("EV Charge Port Connected State value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_ev_charge_port_open_state_ON) or int(value1) == int(b2c_ev_charge_port_open_state_ON):
            testResult(self, "passed",
                       "EV Charge Port should be in connected/ON state ie EV_CHARGE_PORT_CONNECTED state should be set to 1 at both Device & Cloud",
                       "EV Charge Port is in connected/ON state ie EV_CHARGE_PORT_CONNECTED state is set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port should be in connected/ON state ie EV_CHARGE_PORT_CONNECTED state should be set to 1 at both Device & Cloud",
                       "EV Charge Port is not in connected/ON state ie EV_CHARGE_PORT_CONNECTED state is not set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test9_chargingNotification_inst_charge_rate(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_connected_and_isCharging")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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
        ls = verify_message_in_log(self, b2c_inst_charge_rate_attribute, b2c_inst_charge_rate_attribute)

        if b2c_inst_charge_rate_attribute in str(ls[0]):
            print(f"inst_charge_rate attribute is printed in device log : ' {b2c_inst_charge_rate_attribute} ' ")
            testResult(self, "passed", "inst_charge_rate attribute should be present in log",
                       "inst_charge_rate attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "inst_charge_rate attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "inst_charge_rate attribute should be present in log ",
                       "inst_charge_rate attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        charging_value = b2c_inst_charge_rate_attribute + b2c_inst_charge_rate_value
        ls = verify_message_in_log(self, b2c_inst_charge_rate_attribute, charging_value)

        if charging_value in str(ls[0]):
            print(f"EV BATTERY INSTANTANEOUS CHARGE RATE value should be printed in device log : ' {charging_value} ' ")
            testResult(self, "passed", "EV BATTERY INSTANTANEOUS CHARGE_RATE value should be published to cloud ",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV BATTERY INSTANTANEOUS CHARGE RATE value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "EV BATTERY INSTANTANEOUS CHARGE_RATE value should be published to cloud ",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_inst_charge_rate_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV BATTERY INSTANTANEOUS CHARGE_RATE value configured in the telemetry stub : ",
              b2c_inst_charge_rate_value)
        print("EV BATTERY INSTANTANEOUS CHARGE_RATE value stored in Cloud : ", value, value1)

        if int(value) == int(b2c_inst_charge_rate_value) or int(value1) == int(b2c_inst_charge_rate_value):
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test10_chargingNotification_no_inst_charge_rate(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_connected_and_notCharging")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

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
        ls = verify_message_in_log(self, b2c_inst_charge_rate_attribute, b2c_inst_charge_rate_attribute)

        if b2c_inst_charge_rate_attribute in str(ls[0]):
            print(f"inst_charge_rate attribute is printed in device log : ' {b2c_inst_charge_rate_attribute} ' ")
            testResult(self, "passed", "inst_charge_rate attribute should be present in log",
                       "inst_charge_rate attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "inst_charge_rate attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "inst_charge_rate attribute should be present in log ",
                       "inst_charge_rate attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        charging_value = b2c_inst_charge_rate_attribute + b2c_no_inst_charge_rate_value
        ls = verify_message_in_log(self, b2c_inst_charge_rate_attribute, charging_value)

        if charging_value in str(ls[0]):
            print(f"EV BATTERY INSTANTANEOUS CHARGE RATE value should be printed in device log : ' {charging_value} ' ")
            testResult(self, "passed", "EV BATTERY INSTANTANEOUS CHARGE_RATE value should be published to cloud ",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV BATTERY INSTANTANEOUS CHARGE RATE value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "EV BATTERY INSTANTANEOUS CHARGE_RATE value should be published to cloud ",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusabel module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_inst_charge_rate_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV BATTERY INSTANTANEOUS CHARGE_RATE value configured in the stub : ",
              b2c_no_inst_charge_rate_value)
        print("EV BATTERY INSTANTANEOUS CHARGE_RATE value stored in Cloud : ", value, value1)

        if int(value) == int(b2c_no_inst_charge_rate_value) or int(value1) == int(b2c_no_inst_charge_rate_value):
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test11_chargingNotification_charge_port_open(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_open")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify charging messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_ev_charge_port_open_attribute, b2c_ev_charge_port_open_attribute)

        if b2c_ev_charge_port_open_attribute in str(ls[0]):
            print(
                f"ev_charge_port_open attribute is printed in device log : ' {b2c_ev_charge_port_open_attribute} ' ")
            testResult(self, "passed", "ev_charge_port_open attribute should be present in log",
                       "ev_charge_port_open attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_open attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_open attribute should be present in log ",
                       "ev_charge_port_open attribute is not present in log or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        charging_ON = b2c_ev_charge_port_open_attribute + b2c_ev_charge_port_open_state_ON
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_state_ON, charging_ON)

        if charging_ON in str(ls[0]):
            print(f"EV Charge Port Open state is printed in device log : ' {charging_ON} ' ")
            testResult(self, "passed", "ev_charge_port_open state should be published to cloud ",
                       "ev_charge_port_open state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_open state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_open state should be published to cloud ",
                       "ev_charge_port_opend state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        value = value1 = ""

        # call api reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ev_charge_port_open_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value1 = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV Charge Port Open configured in the stub : ", b2c_ev_charge_port_connected_state_ON)
        print("EV Charge Port Open State value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_ev_charge_port_open_state_ON) or int(value1) == int(b2c_ev_charge_port_open_state_ON):
            testResult(self, "passed",
                       "EV Charge Port Open should be turned ON ie EV_CHARGE_PORT_OPEN state should be set to 1 at both Device & Cloud",
                       "EV Charge Port is  turned ON ie EV_CHARGE_PORT_OPEN state is set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port Open should be  turned ON ie EV_CHARGE_PORT_OPEN state should be set to 1 at both Device & Cloud",
                       "EV Charge Port Open is not turned ON ie EV_CHARGE_PORT_OPEN state is not set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test12_chargingNotification_charge_port_disconnected(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_disconnected")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify charging messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_attribute, b2c_ev_charge_port_connected_attribute)

        if b2c_ev_charge_port_open_attribute in str(ls[0]):
            print(
                f"ev_charge_port_connected attribute is printed in device log : ' {b2c_ev_charge_port_connected_attribute} ' ")
            testResult(self, "passed", "ev_charge_port_connected attribute should be present in log",
                       "ev_charge_port_connected attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_connected attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_connected attribute should be present in log ",
                       "ev_charge_port_connected attribute is not present in log or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        charging_OFF = b2c_ev_charge_port_connected_attribute + b2c_ev_charge_port_connected_state_OFF
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_state_ON, charging_OFF)

        if charging_OFF in str(ls[0]):
            print(f"EV Charge Port Connected state is printed in device log : ' {charging_OFF} ' ")
            testResult(self, "passed", "EV Charge Port Connected state should be published to cloud ",
                       "EV Charge Port Connected state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV Charge Port Connected state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "EV Charge Port Connected state should be published to cloud ",
                       "EV Charge Port Connected state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ev_charge_port_connected_event_type, systemId,
                                                  "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_connected_state_OFF)
        print("EV Charge Port Connected State value stored in Cloud DB : ", value)

        if int(value) == int(b2c_ev_charge_port_open_state_OFF) or int(value1) == int(
                b2c_ev_charge_port_open_state_OFF):
            testResult(self, "passed",
                       "EV Charge Port should be in dicconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state is set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port should be in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is not in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state is not set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-sidestand functionality.
    def test13_telemetry_sideStand_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_sideStand_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - sidestand

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, b2c_telemetry_sidestand_attribute)

        if b2c_telemetry_sidestand_attribute in str(ls[0]):
            print(f"Side stand attribute name printed in device log : ' {b2c_telemetry_sidestand_attribute} ' ")
            testResult(self, "passed", "Side stand attribute should be present in telemetry data",
                       "Side stand attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Side stand attribute should be present in telemetry data ",
                       "Side stand attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_sidestand = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_sidestand)

        if tele_sidestand in str(ls[0]):
            print(f"Side stand value printed in device log : ' {tele_sidestand} ' ")
            testResult(self, "passed", "Side stand value should be published to cloud ",
                       "Side stand value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Side stand value should be published to cloud ",
                       "Side stand value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Side stand value configured in the telemetry stub : ", tele_sidestand)
            print("Side stand value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_sidestand_state_OFF):
            testResult(self, "passed",
                       "Side stand value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Side stand value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Side stand value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Side stand value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-sidestand functionality.
    def test14_telemetry_sideStand_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_sideStand_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - sidestand

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, b2c_telemetry_sidestand_attribute)

        if b2c_telemetry_sidestand_attribute in str(ls[0]):
            print(f"Side stand attribute name printed in device log : ' {b2c_telemetry_sidestand_attribute} ' ")
            testResult(self, "passed", "Side stand attribute should be present in telemetry data",
                       "Side stand attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Side stand attribute should be present in telemetry data ",
                       "Side stand attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_sidestand = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_sidestand)

        if tele_sidestand in str(ls[0]):
            print(f"Side stand value printed in device log : ' {tele_sidestand} ' ")
            testResult(self, "passed", "Side stand value should be published to cloud ",
                       "Side stand value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Side stand value should be published to cloud ",
                       "Side stand value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Side stand value configured in the telemetry stub : ", tele_sidestand)
            print("Side stand value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_sidestand_state_ON):
            testResult(self, "passed",
                       "Side stand value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Side stand value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Side stand value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Side stand value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-headlight functionality.
    def test15_telemetry_headlight_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_headlight_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_headlight_attribute, b2c_telemetry_headlight_attribute)

        if b2c_telemetry_headlight_attribute in str(ls[0]):
            print(f"Headlight attribute name printed in device log : ' {b2c_telemetry_headlight_attribute} ' ")
            testResult(self, "passed", "Headlight attribute should be present in telemetry data",
                       "Headlight attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Headlight attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Headlight attribute should be present in telemetry data ",
                       "Headlight attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_headlight = b2c_telemetry_headlight_attribute + b2c_telemetry_headlight_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_headlight)

        if tele_headlight in str(ls[0]):
            print(f"Headlight value printed in device log : ' {tele_headlight} ' ")
            testResult(self, "passed", "Headlight value should be published to cloud ",
                       "Headlight value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Headlight value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Headlight value should be published to cloud ",
                       "Headlight value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_headlight:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_headlight_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_headlight:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Headlight value configured in the telemetry stub : ", tele_headlight)
        print("Headlight value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_headlight_state_OFF):
            testResult(self, "passed",
                       "Headlight value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Headlight value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Headlight value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Headlight value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-headlight functionality.
    def test16_telemetry_headlight_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_headlight_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_headlight_attribute, b2c_telemetry_headlight_attribute)

        if b2c_telemetry_headlight_attribute in str(ls[0]):
            print(f"Headlight attribute name printed in device log : ' {b2c_telemetry_headlight_attribute} ' ")
            testResult(self, "passed", "Headlight attribute should be present in telemetry data",
                       "Headlight attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Headlight attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Headlight attribute should be present in telemetry data ",
                       "Headlight attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_headlight = b2c_telemetry_headlight_attribute + b2c_telemetry_headlight_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_headlight)

        if tele_headlight in str(ls[0]):
            print(f"Headlight value printed in device log : ' {tele_headlight} ' ")
            testResult(self, "passed", "Headlight value should be published to cloud ",
                       "Headlight value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Headlight value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Headlight value should be published to cloud ",
                       "Headlight value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_headlight:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Headlight value configured in the telemetry stub : ", tele_headlight)
            print("Headlight value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_headlight_state_ON):
            testResult(self, "passed",
                       "Headlight value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Headlight value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Headlight value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Headlight value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-SOS functionality.
    def test17_telemetry_SOS_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_SOS_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_attribute)

        if b2c_telemetry_SOS_attribute in str(ls[0]):
            print(f"Headlight attribute name printed in device log : ' {b2c_telemetry_SOS_attribute} ' ")
            testResult(self, "passed", "SOS attribute should be present in telemetry data",
                       "SOS attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS attribute should be present in telemetry data ",
                       "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_SOS = b2c_telemetry_SOS_attribute + b2c_telemetry_SOS_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_SOS)

        if tele_SOS in str(ls[0]):
            print(f"SOS value printed in device log : ' {tele_SOS} ' ")
            testResult(self, "passed", "SOS value should be published to cloud ",
                       "SOS value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS value should be published to cloud ",
                       "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_SOS:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Headlight value configured in the telemetry stub : ", tele_SOS)
            print("Headlight value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_SOS_state_OFF):
            testResult(self, "passed",
                       "SOS value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "SOS value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "SOS value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "SOS value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-SOS functionality.
    def test18_telemetry_SOS_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_SOS_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_attribute)

        if b2c_telemetry_SOS_attribute in str(ls[0]):
            print(f"Headlight attribute name printed in device log : ' {b2c_telemetry_SOS_attribute} ' ")
            testResult(self, "passed", "SOS attribute should be present in telemetry data",
                       "SOS attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS attribute should be present in telemetry data ",
                       "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_SOS = b2c_telemetry_SOS_attribute + b2c_telemetry_SOS_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_SOS)

        if tele_SOS in str(ls[0]):
            print(f"SOS value printed in device log : ' {tele_SOS} ' ")
            testResult(self, "passed", "SOS value should be published to cloud ",
                       "SOS value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS value should be published to cloud ",
                       "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_SOS:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Headlight value configured in the telemetry stub : ", tele_SOS)
            print("Headlight value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_SOS_state_ON):
            testResult(self, "passed",
                       "SOS value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "SOS value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "SOS value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "SOS value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-SOS functionality.
    def test19_telemetry_tire_pressure_left_front(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_front_tire_pressure")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_front_tire_pressure_attribute,
                                   b2c_telemetry_front_tire_pressure_attribute)

        if b2c_telemetry_battery_temp_attribute in str(ls[0]):
            print(
                f"Front Tire Pressure attribute name printed in device log : ' {b2c_telemetry_front_tire_pressure_attribute} ' ")
            testResult(self, "passed", "Front Tire Pressure attribute should be present in telemetry data",
                       "Front Tire Pressure attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Front Tire Pressure attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Front Tire Pressure attribute should be present in telemetry data ",
                       "Front Tire Pressure attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify tire pressure value in the device logs
        tele_temp = b2c_telemetry_front_tire_pressure_attribute + b2c_telemetry_front_tire_pressure_value
        ls = verify_message_in_log(self, b2c_telemetry_front_tire_pressure_attribute, tele_temp)

        if tele_temp in str(ls[0]):
            print(f"Front Tire Pressure value printed in device log : ' {tele_temp} ' ")
            testResult(self, "passed", "Front Tire pressure value should be published to cloud ",
                       "Front Tire Pressure value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Front Tire Pressure value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Front Tire Pressure value should be published to cloud ",
                       "Front Tire Pressure value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify tire pressure value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusable modules
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_tire_pressure:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")

        # call api reusable modules with event type
        response_body1 = telemetry_Curr_eventType(self, telemetry_tire_pressure_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_tire_pressure:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")

        print("Front Tire Pressure value configured in the telemetry stub : ",
              b2c_telemetry_front_tire_pressure_value)
        print("Front Tire Pressure value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_front_tire_pressure_value) or int(value1) == int(
                b2c_telemetry_front_tire_pressure_value):
            testResult(self, "passed",
                       "Front Tire Pressure value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Front Tire Pressure value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Front Tire Pressure value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Front Tire Pressure value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-SOS functionality.
    def test20_telemetry_tire_pressure_left_rear(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_rear_tire_pressure")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_rear_tire_pressure_attribute,
                                   b2c_telemetry_rear_tire_pressure_attribute)

        if b2c_telemetry_battery_temp_attribute in str(ls[0]):
            print(
                f"Front Tire Pressure attribute name printed in device log : ' {b2c_telemetry_rear_tire_pressure_attribute} ' ")
            testResult(self, "passed", "Rear Tire Pressure attribute should be present in telemetry data",
                       "Rear Tire Pressure attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Rear Tire Pressure attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Rear Tire Pressure attribute should be present in telemetry data ",
                       "Rear Tire Pressure attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify tire pressure value in the device logs
        tele_temp = b2c_telemetry_rear_tire_pressure_attribute + b2c_telemetry_rear_tire_pressure_value
        ls = verify_message_in_log(self, b2c_telemetry_rear_tire_pressure_attribute, tele_temp)

        if tele_temp in str(ls[0]):
            print(f"Rear Tire Pressure value printed in device log : ' {tele_temp} ' ")
            testResult(self, "passed", "Rear Tire pressure value should be published to cloud ",
                       "Rear Tire Pressure value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Rear Tire Pressure value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Rear Tire Pressure value should be published to cloud ",
                       "Rear Tire Pressure value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify tire pressure value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_tire_pressure:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module with event type
        response_body1 = telemetry_Curr_eventType(self, telemetry_tire_pressure_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_tire_pressure:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Rear Tire Pressure value configured in the telemetry stub : ",
              b2c_telemetry_rear_tire_pressure_value)
        print("Rear Tire Pressure value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_rear_tire_pressure_value) or int(value1) == int(
                b2c_telemetry_rear_tire_pressure_value):
            testResult(self, "passed",
                       "Rear Tire Pressure value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Rear Tire Pressure value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Rear Tire Pressure value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Rear Tire Pressure value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-taillight functionality.
    def test21_telemetry_taillight_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_taillight_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_taillight_attribute, b2c_telemetry_taillight_attribute)

        if b2c_telemetry_taillight_attribute in str(ls[0]):
            print(f"Tail light attribute name printed in device log : ' {b2c_telemetry_taillight_attribute} ' ")
            testResult(self, "passed", "Tail light attribute should be present in telemetry data",
                       "Tail light attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Tail light attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Tail light attribute should be present in telemetry data ",
                       "Tail light attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_taillight = b2c_telemetry_taillight_attribute + b2c_telemetry_taillight_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_taillight_attribute, tele_taillight)

        if tele_taillight in str(ls[0]):
            print(f"Tail light value printed in device log : ' {tele_taillight} ' ")
            testResult(self, "passed", "Tail light value should be published to cloud ",
                       "Tail light value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Tail light value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Tail light value should be published to cloud ",
                       "Tail light value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_taillight:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_taillight_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_taillight:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Tail light value configured in the telemetry stub : ", tele_taillight)
        print("Tail light value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_taillight_state_OFF):
            testResult(self, "passed",
                       "Tail light value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Tail light value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Tail light value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Tail light value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-taillight functionality.
    def test22_telemetry_taillight_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_taillight_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_taillight_attribute, b2c_telemetry_taillight_attribute)

        if b2c_telemetry_taillight_attribute in str(ls[0]):
            print(f"Tail light attribute name printed in device log : ' {b2c_telemetry_taillight_attribute} ' ")
            testResult(self, "passed", "Tail light attribute should be present in telemetry data",
                       "Tail light attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Tail light attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Tail light attribute should be present in telemetry data ",
                       "Tail light attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_taillight = b2c_telemetry_taillight_attribute + b2c_telemetry_taillight_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_taillight_attribute, tele_taillight)

        if tele_taillight in str(ls[0]):
            print(f"Tail light value printed in device log : ' {tele_taillight} ' ")
            testResult(self, "passed", "Tail light value should be published to cloud ",
                       "Tail light value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Tail light value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Tail light value should be published to cloud ",
                       "Tail light value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_taillight:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_taillight_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_taillight:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Tail light value configured in the telemetry stub : ", tele_taillight)
        print("Tail light value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_taillight_state_ON):
            testResult(self, "passed",
                       "Tail light value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Tail light value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Tail light value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Tail light value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test23_telemetry_gear_position_2_reverse(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_gear_position_2")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, b2c_telemetry_gear_position_attribute)

        if b2c_telemetry_gear_position_attribute in str(ls[0]):
            print(f"Gear position attribute name printed in device log : ' {b2c_telemetry_gear_position_attribute} ' ")
            testResult(self, "passed", "Gear position attribute should be present in telemetry data",
                       "Gear position light attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position attribute should be present in telemetry data ",
                       "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_gear_position = b2c_telemetry_gear_position_attribute + b2c_telemetry_gear_position_state_2
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, tele_gear_position)

        if tele_gear_position in str(ls[0]):
            print(f"Gear position value printed in device log : ' {tele_gear_position} ' ")
            testResult(self, "passed", "Gear position value should be published to cloud ",
                       "Gear position value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position value should be published to cloud ",
                       "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_gear_position_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Gear position value configured in the telemetry stub : ", tele_gear_position)
        print("Gear position value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_gear_position_state_2):
            testResult(self, "passed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test24_telemetry_gear_position_4_park(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_gear_position_4")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, b2c_telemetry_gear_position_attribute)

        if b2c_telemetry_gear_position_attribute in str(ls[0]):
            print(f"Gear position attribute name printed in device log : ' {b2c_telemetry_gear_position_attribute} ' ")
            testResult(self, "passed", "Gear position attribute should be present in telemetry data",
                       "Gear position light attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position attribute should be present in telemetry data ",
                       "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_gear_position = b2c_telemetry_gear_position_attribute + b2c_telemetry_gear_position_state_4
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, tele_gear_position)

        if tele_gear_position in str(ls[0]):
            print(f"Gear position value printed in device log : ' {tele_gear_position} ' ")
            testResult(self, "passed", "Gear position value should be published to cloud ",
                       "Gear position value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position value should be published to cloud ",
                       "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_gear_position_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Gear position value configured in the telemetry stub : ", tele_gear_position)
        print("Gear position value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_gear_position_state_4):
            testResult(self, "passed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test25_telemetry_gear_position_8_drive(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_gear_position_8")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, b2c_telemetry_gear_position_attribute)

        if b2c_telemetry_gear_position_attribute in str(ls[0]):
            print(f"Gear position attribute name printed in device log : ' {b2c_telemetry_gear_position_attribute} ' ")
            testResult(self, "passed", "Gear position attribute should be present in telemetry data",
                       "Gear position light attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position attribute should be present in telemetry data ",
                       "Gear position attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_gear_position = b2c_telemetry_gear_position_attribute + b2c_telemetry_gear_position_state_8
        ls = verify_message_in_log(self, b2c_telemetry_gear_position_attribute, tele_gear_position)

        if tele_gear_position in str(ls[0]):
            print(f"Gear position value printed in device log : ' {tele_gear_position} ' ")
            testResult(self, "passed", "Gear position value should be published to cloud ",
                       "Gear position value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Gear position value should be published to cloud ",
                       "Gear position value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_gear_position_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_gear_position:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Gear position value configured in the telemetry stub : ", tele_gear_position)
        print("Gear position value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_gear_position_state_8):
            testResult(self, "passed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Gear position value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Gear position value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test26_telemetry_high_beam_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_high_beam_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_high_beam_attribute, b2c_telemetry_high_beam_attribute)

        if b2c_telemetry_high_beam_attribute in str(ls[0]):
            print(f"High-beam state attribute name printed in device log : ' {b2c_telemetry_high_beam_attribute} ' ")
            testResult(self, "passed", "High-beam state attribute should be present in telemetry data",
                       "High-beam state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "High-beam state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "High-beam state attribute should be present in telemetry data ",
                       "High-beam stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_high_beam = b2c_telemetry_high_beam_attribute + b2c_telemetry_high_beam_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_high_beam_attribute, tele_high_beam)

        if tele_high_beam in str(ls[0]):
            print(f"High-beam state printed in device log : ' {tele_high_beam} ' ")
            testResult(self, "passed", "High-beam state should be published to cloud ",
                       "High-beam state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "High-beam state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "High-beam state should be published to cloud ",
                       "High-beam state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_high_beam:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_high_beam_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_high_beam:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("High beam value configured in the telemetry stub : ", tele_high_beam)
        print("High beam value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_high_beam_state_ON):
            testResult(self, "passed",
                       "High-beam state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "High-beam state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "High-beam state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "High-beam state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test27_telemetry_high_beam_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_high_beam_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_high_beam_attribute, b2c_telemetry_high_beam_attribute)

        if b2c_telemetry_high_beam_attribute in str(ls[0]):
            print(f"High-beam state attribute name printed in device log : ' {b2c_telemetry_high_beam_attribute} ' ")
            testResult(self, "passed", "High-beam state attribute should be present in telemetry data",
                       "High-beam state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "High-beam state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "High-beam state attribute should be present in telemetry data ",
                       "High-beam stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_high_beam = b2c_telemetry_high_beam_attribute + b2c_telemetry_high_beam_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_high_beam_attribute, tele_high_beam)

        if tele_high_beam in str(ls[0]):
            print(f"High-beam state printed in device log : ' {tele_high_beam} ' ")
            testResult(self, "passed", "High-beam state should be published to cloud ",
                       "High-beam state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "High-beam state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "High-beam state should be published to cloud ",
                       "High-beam state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_high_beam:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_high_beam_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_high_beam:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("High beam value configured in the telemetry stub : ", tele_high_beam)
        print("High beam value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_high_beam_state_OFF):
            testResult(self, "passed",
                       "High-beam state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "High-beam state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "High-beam state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "High-beam state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test28_telemetry_hazard_light_ON(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_hazard_light_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_hazard_light_attribute, b2c_telemetry_hazard_light_attribute)

        if b2c_telemetry_hazard_light_attribute in str(ls[0]):
            print(
                f"Hazard_light state attribute name printed in device log : ' {b2c_telemetry_hazard_light_attribute} ' ")
            testResult(self, "passed", "Hazard_light state attribute should be present in telemetry data",
                       "Hazard_light state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Hazard_light state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Hazard_light state attribute should be present in telemetry data ",
                       "Hazard_light stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_hazard_light = b2c_telemetry_hazard_light_attribute + b2c_telemetry_hazard_light_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_hazard_light_attribute, tele_hazard_light)

        if tele_hazard_light in str(ls[0]):
            print(f"Hazard_light state printed in device log : ' {tele_hazard_light} ' ")
            testResult(self, "passed", "Hazard_light state should be published to cloud ",
                       "Hazard_light state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Hazard_light state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Hazard_light state should be published to cloud ",
                       "Hazard_light state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_hazard_light:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_hazard_light_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_hazard_light:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Hazard_light value configured in the telemetry stub : ", tele_hazard_light)
        print("Hazard_light value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_hazard_light_state_ON) or int(value1) == int(
                b2c_telemetry_hazard_light_state_ON):
            testResult(self, "passed",
                       "Hazard_light state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Hazard_light state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Hazard_light state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Hazard_light state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test29_telemetry_hazard_light_OFF(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_hazard_light_OFF")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_hazard_light_attribute, b2c_telemetry_hazard_light_attribute)

        if b2c_telemetry_hazard_light_attribute in str(ls[0]):
            print(
                f"Hazard_light state attribute name printed in device log : ' {b2c_telemetry_hazard_light_attribute} ' ")
            testResult(self, "passed", "Hazard_light state attribute should be present in telemetry data",
                       "Hazard_light state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Hazard_light state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Hazard_light state attribute should be present in telemetry data ",
                       "Hazard_light stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_hazard_light = b2c_telemetry_hazard_light_attribute + b2c_telemetry_hazard_light_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_hazard_light_attribute, tele_hazard_light)

        if tele_hazard_light in str(ls[0]):
            print(f"Hazard_light state printed in device log : ' {tele_hazard_light} ' ")
            testResult(self, "passed", "Hazard_light state should be published to cloud ",
                       "Hazard_light state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Hazard_light state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Hazard_light state should be published to cloud ",
                       "Hazard_light state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_hazard_light:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_hazard_light_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_hazard_light:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Hazard_light value configured in the telemetry stub : ", tele_hazard_light)
        print("Hazard_light value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_hazard_light_state_OFF):
            testResult(self, "passed",
                       "Hazard_light state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Hazard_light state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Hazard_light state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Hazard_light state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test30_chargingNotification_charge_port_close(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "chargingNotification_can_charge_port_close")
        time.sleep(15)

        print("Charging Notification can/stub run process is completed, verify logs for notification details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify charging messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_ev_charge_port_open_attribute, b2c_ev_charge_port_open_attribute)

        if b2c_ev_charge_port_open_attribute in str(ls[0]):
            print(
                f"ev_charge_port_open attribute is printed in device log : ' {b2c_ev_charge_port_open_attribute} ' ")
            testResult(self, "passed", "ev_charge_port_open attribute should be present in log",
                       "ev_charge_port_open attribute is present/printed in log")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_open attribute is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_open attribute should be present in log ",
                       "ev_charge_port_open attribute is not present in log or device logs are not updated. pls refer device logs in detail or logs has beeen rotated")

        # verify odo meter value in the device logs
        port_Open_OFF = b2c_ev_charge_port_open_attribute + b2c_ev_charge_port_open_state_OFF
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_state_OFF, port_Open_OFF)

        if port_Open_OFF in str(ls[0]):
            print(f"EV Charge Port Open state is printed in device log : ' {port_Open_OFF} ' ")
            testResult(self, "passed", "ev_charge_port_open state should be published to cloud ",
                       "ev_charge_port_open state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "ev_charge_port_open state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "ev_charge_port_open state should be published to cloud ",
                       "ev_charge_port_opend state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call api reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call api reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ev_charge_port_open_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value1 = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("EV Charge Port Open configured in the stub : ", b2c_ev_charge_port_connected_state_OFF)
        print("EV Charge Port Open State value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_ev_charge_port_open_state_OFF) or int(value1) == int(
                b2c_ev_charge_port_open_state_OFF):
            testResult(self, "passed",
                       "EV Charge Port Open should be turned OFF ie EV_CHARGE_PORT_OPEN state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is  turned OFF ie EV_CHARGE_PORT_OPEN state is set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port Open should be  turned OFF ie EV_CHARGE_PORT_OPEN state should be set to 0 at both Device & Cloud",
                       "EV Charge Port Open is not turned OFF ie EV_CHARGE_PORT_OPEN state is not set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test31_telemetry_ride_mode_normal(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_ride_mode_normal")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, b2c_telemetry_ride_mode_attribute)

        if b2c_telemetry_ride_mode_attribute in str(ls[0]):
            print(f"Ride_mode state attribute name printed in device log : ' {b2c_telemetry_ride_mode_attribute} ' ")
            testResult(self, "passed", "Ride_mode state attribute should be present in telemetry data",
                       "Ride_mode state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_modestate attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state attribute should be present in telemetry data ",
                       "Ride_mode stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_ride_mode = b2c_telemetry_ride_mode_attribute + b2c_telemetry_ride_mode_state_0
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, tele_ride_mode)

        if tele_ride_mode in str(ls[0]):
            print(f"Ride_mode state printed in device log : ' {tele_ride_mode} ' ")
            testResult(self, "passed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ride_mode_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Ride_mode value configured in the telemetry stub : ", tele_ride_mode)
        print("Ride_mode value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_ride_mode_state_0) or int(value1) == int(b2c_telemetry_ride_mode_state_0):
            testResult(self, "passed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test32_telemetry_ride_mode_economy(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_ride_mode_economy")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, b2c_telemetry_ride_mode_attribute)

        if b2c_telemetry_ride_mode_attribute in str(ls[0]):
            print(f"Ride_mode state attribute name printed in device log : ' {b2c_telemetry_ride_mode_attribute} ' ")
            testResult(self, "passed", "Ride_mode state attribute should be present in telemetry data",
                       "Ride_mode state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_modestate attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state attribute should be present in telemetry data ",
                       "Ride_mode stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_ride_mode = b2c_telemetry_ride_mode_attribute + b2c_telemetry_ride_mode_state_1
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, tele_ride_mode)

        if tele_ride_mode in str(ls[0]):
            print(f"Ride_mode state printed in device log : ' {tele_ride_mode} ' ")
            testResult(self, "passed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ride_mode_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Ride_mode value configured in the telemetry stub : ", tele_ride_mode)
        print("Ride_mode value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_ride_mode_state_1) or int(value1) == int(b2c_telemetry_ride_mode_state_1):
            testResult(self, "passed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test33_telemetry_ride_mode_vendorSpecific(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_ride_mode_vendorSpecific")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, b2c_telemetry_ride_mode_attribute)

        if b2c_telemetry_ride_mode_attribute in str(ls[0]):
            print(f"Ride_mode state attribute name printed in device log : ' {b2c_telemetry_ride_mode_attribute} ' ")
            testResult(self, "passed", "Ride_mode state attribute should be present in telemetry data",
                       "Ride_mode state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_modestate attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state attribute should be present in telemetry data ",
                       "Ride_mode stateattribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_ride_mode = b2c_telemetry_ride_mode_attribute + b2c_telemetry_ride_mode_state_2
        ls = verify_message_in_log(self, b2c_telemetry_ride_mode_attribute, tele_ride_mode)

        if tele_ride_mode in str(ls[0]):
            print(f"Ride_mode state printed in device log : ' {tele_ride_mode} ' ")
            testResult(self, "passed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Ride_mode state should be published to cloud ",
                       "Ride_mode state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_ride_mode_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_ride_mode:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Ride_mode value configured in the telemetry stub : ", tele_ride_mode)
        print("Ride_mode value stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_ride_mode_state_2) or int(value1) == int(b2c_telemetry_ride_mode_state_2):
            testResult(self, "passed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Ride_mode state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Ride_mode state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test34_telemetry_mobilize(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_mobilize")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute,
                                   b2c_telemetry_immobilize_state_attribute)

        if b2c_telemetry_immobilize_state_attribute in str(ls[0]):
            print(
                f"Immobilize state attribute name printed in device log : ' {b2c_telemetry_immobilize_state_attribute} ' ")
            testResult(self, "passed", "Immobilize state attribute should be present in telemetry data",
                       "Immobilize state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Immobilize_state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Immobilize_state attribute should be present in telemetry data ",
                       "Immobilize_state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_immobilize_state = b2c_telemetry_immobilize_state_attribute + b2c_telemetry_immobilize_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute, tele_immobilize_state)

        if tele_immobilize_state in str(ls[0]):
            print(f"Immobilize_state printed in device log : ' {tele_immobilize_state} ' ")
            testResult(self, "passed", "Immobilize_state should be published to cloud ",
                       "Immobilize_state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Immobilize_state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Immobilize_state should be published to cloud ",
                       "Immobilize_state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_immobilize_state:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_immobilize_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_immobilize_state:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Immobilize_state configured in the telemetry stub : ", tele_immobilize_state)
        print("Immobilize_state stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_immobilize_state_ON) or int(value1) == int(
                b2c_telemetry_immobilize_state_ON):
            testResult(self, "passed",
                       "Immobilize_state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Immobilize_state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Immobilize_state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Immobilize_state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test35_telemetry_immobilize(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_immobilize")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute,
                                   b2c_telemetry_immobilize_state_attribute)

        if b2c_telemetry_immobilize_state_attribute in str(ls[0]):
            print(
                f"Immobilize state attribute name printed in device log : ' {b2c_telemetry_immobilize_state_attribute} ' ")
            testResult(self, "passed", "Immobilize state attribute should be present in telemetry data",
                       "Immobilize state attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Immobilize_state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Immobilize_state attribute should be present in telemetry data ",
                       "Immobilize_state attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_immobilize_state = b2c_telemetry_immobilize_state_attribute + b2c_telemetry_immobilize_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute, tele_immobilize_state)

        if tele_immobilize_state in str(ls[0]):
            print(f"Immobilize_state printed in device log : ' {tele_immobilize_state} ' ")
            testResult(self, "passed", "Immobilize_state should be published to cloud ",
                       "Immobilize_state is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Immobilize_state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Immobilize_state should be published to cloud ",
                       "Immobilize_state is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_immobilize_state:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_immobilize_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == b2c_telemetry_immobilize_state:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("Immobilize_state configured in the telemetry stub : ", tele_immobilize_state)
        print("Mobilize_state stored in Cloud DB : ", value, value1)

        if int(value) == int(b2c_telemetry_immobilize_state_OFF) or int(value1) == int(
                b2c_telemetry_immobilize_state_OFF):
            testResult(self, "passed",
                       "Immobilize_state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Immobilize_state is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "Immobilize_state should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Immobilize_state is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test36_telemetry_rpm(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_rpm")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, telemetry_rpm_attribute,
                                   telemetry_rpm_attribute)

        if telemetry_rpm_attribute in str(ls[0]):
            print(
                f"RPM value attribute name printed in device log : ' {telemetry_rpm_attribute} ' ")
            testResult(self, "passed", "RPM value attribute should be present in telemetry data",
                       "RPM value attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "RPM value attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "RPM value attribute should be present in telemetry data ",
                       "RPM value attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_rpm = telemetry_rpm_attribute + telemetry_rpm_value
        ls = verify_message_in_log(self, telemetry_rpm_attribute, tele_rpm)

        if tele_rpm in str(ls[0]):
            print(f"RPM value printed in device log : ' {tele_rpm} ' ")
            testResult(self, "passed", "RPM value should be published to cloud ",
                       "RPM value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "RPM value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "RPM value should be published to cloud ",
                       "RPM value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_rpm:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value = ""

        # call reusable module
        response_body1 = telemetry_Curr_eventType(self, telemetry_rpm_event_type, systemId, "valid")

        try:
            dataList_len1 = len(response_body1["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len1):
                if response_body1["responseData"]["dataList"][i]["name"] == telemetry_curr_rpm:
                    value1 = response_body1["responseData"]["dataList"][i]["value"]
                    break
        except:
            print("dataList is empty in api response")
            value1 = ""

        print("RPM value configured in the telemetry stub : ", tele_rpm)
        print("RPM value stored in Cloud DB : ", value, value1)

        if int(value) == int(telemetry_rpm_value) or int(value1) == int(
                telemetry_rpm_value):
            testResult(self, "passed",
                       "RPM value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "RPM value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "RPM value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "RPM value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate telemetry-indicator functionality.
    def test37_telemetry_for_elite(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_elite_set1")
        time.sleep(15)

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify gear_position value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)
        value = value1 = ""

        # call reusable module
        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        response_body = response_body.json()

        try:
            list1 = ["Odo Meter", "Speed", "EV Battery Level", "EV battery Temperature", "Side Stand - ON",
                     "Head light - ON", "SOS - ON", "Fuel Level", "RPM", "Range Remaining","Mobilize", "High Beam - ON"
                     , "Tail Light - ON", "Hazard Light - ON", "Ride Mode - Vendor Specific" " Gear Position -2 ",
                     "Front Tire Pressure"]
            list2 = [telemetry_curr_Odo, telemetry_curr_Speed, telemetry_curr_ev_battery_level,
                     b2c_telemetry_current_battery_temp, b2c_telemetry_sidestand, b2c_telemetry_headlight,
                     b2c_telemetry_SOS, telemetry_curr_Fuel, telemetry_curr_rpm, b2c_telemetry_range_remaining,
                     b2c_telemetry_immobilize_state, b2c_telemetry_high_beam, b2c_telemetry_taillight,
                     b2c_telemetry_hazard_light, b2c_telemetry_ride_mode, b2c_telemetry_gear_position,
                     b2c_telemetry_tire_pressure]
            list3 = [b2c_telemetry_odo_value, b2c_telemetry_speed_value, b2c_telemetry_ev_battery_level_value,
                     b2c_telemetry_normal_battery_temp_value, b2c_telemetry_sidestand_state_ON,
                     b2c_telemetry_headlight_state_ON, b2c_telemetry_SOS_state_ON, b2c_telemetry_fuel_level_value,
                     telemetry_rpm_value, b2c_telemetry_range_remaining_value, b2c_telemetry_immobilize_state_ON,
                     b2c_telemetry_high_beam_state_ON, b2c_telemetry_taillight_state_ON,
                     b2c_telemetry_hazard_light_state_ON, b2c_telemetry_ride_mode_state_2,
                     b2c_telemetry_gear_position_state_2 ,b2c_telemetry_front_tire_pressure_value ]

            # Using zip() to iterate over multiple lists simultaneously
            for i1, i2, i3 in zip(list1, list2, list3):
                print(f'{i1} -> {i2} -> {i3}')
                dataList_len1 = len(response_body["responseData"]["dataList"])
                for i in range(dataList_len1):
                    if response_body["responseData"]["dataList"][i]["name"] == i2:
                        value = response_body["responseData"]["dataList"][i]["value"]
                        break
                print(f'{i1} value configured in the telemetry stub : ', i3)
                print("RPM value stored in Cloud DB : ", value)
                if int(value) == int(i3):
                    testResult(self, "passed",
                               f'{i1}' + " value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                               f'{i1}'" value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                               "cloud logs for detailed info")
                else:
                    testResult(self, "failed",
                               f'{i1}' " value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                               f'{i1}' " value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                               "cloud logs for detailed info")
        except:
            print("dataList is empty or telemetry attribute is missing or mentioned incorrect in api response")
            testResult(self, "failed",
                       "Telemetry attribute value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Something went wrong or Telemetry attribute value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    def test_telemetry_api(self):
        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

    def test_try(self):
        batteryLevel_value = batteryCapacity_value = batteryTemp_value = range_remaining = range_remaining_actual = ""
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        response = telemetry_Curr_eventType(self, "1001", systemId, "valid")

        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            if dataList_len >= 1:
                for i in range(dataList_len):
                    if response_body["responseData"]["dataList"][i]["name"] == "EV_BATTERY_LEVEL":
                        batteryLevel_value = response_body["responseData"]["dataList"][i]["value"]
                    if response_body["responseData"]["dataList"][i]["name"] == "INFO_EV_BATTERY_CAPACITY":
                        batteryCapacity_value = response_body["responseData"]["dataList"][i]["value"]
                    if response_body["responseData"]["dataList"][i]["name"] == "EV_BATTERY_TEMPERATURE":
                        batteryTemp_value = response_body["responseData"]["dataList"][i]["value"]

            print("EV_BATTERY_LEVEL : ", batteryLevel_value)
            print("INFO_EV_BATTERY_CAPACITY : ", batteryCapacity_value)
            print("EV_BATTERY_TEMPERATURE : ", batteryTemp_value)

            range_remaining = (float(batteryLevel_value) / float(batteryCapacity_value)) * 100
            range_remaining = "{:.2f}".format(range_remaining)
            print("The Remaining Battery Charge (in percentage) calculated based on telemetry stub : ", range_remaining)
        except:
            print("dataList is empty in api response")
            value = ""

        response = telemetry_Curr_remainingCharge(self, systemId, "valid")

        response_body = response.json()

        if response_body["responseCode"] == "1200":
            try:
                range_remaining_actual = response_body["responseData"]["dataList"][0]
                print("The Remaining Battery Charge (in percentage) stored in Cloud DB : ", range_remaining_actual)
            except:
                print("dataList is empty in api response")
                range_remaining_actual = ""

        if range_remaining == range_remaining_actual:
            print("PASS")
