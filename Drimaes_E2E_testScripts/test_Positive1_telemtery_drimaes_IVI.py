import time
import pytest

from C2CModules.c2c_modules import testResult
from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, \
    run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, get_SystemId
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi


class Test1_telemetry:

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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_telemetry_stubtel")
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
        tele_odo = telemetry_odo_attribute + telemetry_odo_value
        ls = verify_message_in_log(self, telemetry_odo_value, tele_odo)

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

        # verify odo meter value in the telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code_tel)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code_tel in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code_tel} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            #print("c2c logs line data : => ", ls[0])

            # try:
            #     msg_body_data = decode_msg_body(str(ls[0]))
            #
            #     if telemetry_odo_value in msg_body_data:
            #         testResult(self, "passed",
            #                    "Odo meter value should be present in the telemetry message published to the cloud",
            #                    "Odo meter value is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
            #                    "device logs for detailed info")
            #     else:
            #         print("\n")
            #         testResult(self, "verificationFailed",
            #                    "Odo meter value should be present in the telemetry message published to the cloud",
            #                    "Odo meter value is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
            #                    "device logs for detailed info")
            # except:
            #     print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print(
                "Telemetry message is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
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

        response_body = telemetry_Curr(self, telemetry_odo_event_type, systemId)
        # print(response_body)
        try:
            #id = response_body["responseData"]["dataList"][0]["id"]
            #name = response_body["responseData"]["dataList"][0]["name"]
            #value = response_body["responseData"]["dataList"][0]["value"]
            dataList_len = len(response_body["responseData"]["dataList"])
            #print(dataList_len)
            i=0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Odo meter value configured in the telemetry stub : ", telemetry_odo_value)
            print("Odo meter value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(telemetry_odo_value):
            testResult(self, "passed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "passed",
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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_telemetry_stubtel")
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
        telemetry_fuel_level_value1 = telemetry_fuel_level_attribute + telemetry_fuel_level_value
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

        # verify fuel level value in the telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code_tel)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code_tel in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code_tel} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            #print("c2c logs line data : => ", ls[0])

            # try:
            #     msg_body_data = decode_msg_body(str(ls[0]))
            #
            #     if telemetry_odo_value in msg_body_data:
            #         testResult(self, "passed",
            #                    "Fuel level value should be present in the telemetry message published to the cloud",
            #                    "Fuel level value is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
            #                    "device logs for detailed info")
            #     if trip_start_event_type_code not in msg_body_data:
            #         testResult(self, "verificationFailed",
            #                    "Fuel level value should be present in the telemetry message published to the cloud",
            #                    "Fuel level value is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
            #                    "device logs for detailed info")
            # except:
            #     print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print(
                "Telemetry message is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
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

        response_body = telemetry_Curr(self, telemetry_fuel_level_event_type, systemId)

        try:
            id = response_body["responseData"]["dataList"][0]["id"]
            name = response_body["responseData"]["dataList"][0]["name"]
            value = response_body["responseData"]["dataList"][0]["value"]
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

        if value == telemetry_fuel_level_value:
            print("Fuel level value configured in the telemetry stub : ", telemetry_fuel_level_value)
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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_telemetry_stubtel")
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
        ls = verify_message_in_log(self, telemetry_ev_battery_level_attribute, telemetry_ev_battery_level_attribute)

        if telemetry_fuel_level_attribute in str(ls[0]):
            print(f"Telemetry_ev_battery_level attribute name printed in device log : ' {telemetry_ev_battery_level_attribute} ' ")
            testResult(self, "passed", "Telemetry_ev_battery_level attribute should be present in telemetry data",
                       "Telemetry_ev_battery_level attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Telemetry_ev_battery_level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry_ev_battery_level attribute should be present in telemetry data ",
                       "Telemetry_ev_battery_level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        telemetry_ev_battery_level_value1 = telemetry_ev_battery_level_attribute + telemetry_ev_battery_level_value
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

        # verify fuel level value in the telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code_tel)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code_tel in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code_tel} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

        if str(ls[0]) == "Error":
            print(
                "Telemetry message is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
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

        response_body = telemetry_Curr(self, telemetry_ev_battery_level_event_type, systemId)

        try:
            id = response_body["responseData"]["dataList"][0]["id"]
            name = response_body["responseData"]["dataList"][0]["name"]
            value = response_body["responseData"]["dataList"][0]["value"]
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

        if value == telemetry_ev_battery_level_value:
            print("telemetry_ev_battery_level value configured in the telemetry stub : ", telemetry_ev_battery_level_value)
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
    # Validate telemetry-speed functionality.
    def test1_telemetry_speed(self):
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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_telemetry_stubtel")
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
            print(f"speed attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
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
        tele_odo = telemetry_odo_attribute + telemetry_odo_value
        ls = verify_message_in_log(self, telemetry_odo_value, tele_odo)

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

        # verify odo meter value in the telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code_tel)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code_tel in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code_tel} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

            # print("c2c logs line data : => ", ls[0])

            # try:
            #     msg_body_data = decode_msg_body(str(ls[0]))
            #
            #     if telemetry_odo_value in msg_body_data:
            #         testResult(self, "passed",
            #                    "Odo meter value should be present in the telemetry message published to the cloud",
            #                    "Odo meter value is present in the telemetry message published to the cloud and device logs are updated accordingly, pls refer "
            #                    "device logs for detailed info")
            #     else:
            #         print("\n")
            #         testResult(self, "verificationFailed",
            #                    "Odo meter value should be present in the telemetry message published to the cloud",
            #                    "Odo meter value is not present in the telemetry message published to the cloud or device logs are not updated accordingly, pls refer "
            #                    "device logs for detailed info")
            # except:
            #     print("Unable to decode message body data due to truncated logs")

        if str(ls[0]) == "Error":
            print(
                "Telemetry message is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
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

        response_body = telemetry_Curr(self, telemetry_odo_event_type, systemId)
        # print(response_body)
        try:
            # id = response_body["responseData"]["dataList"][0]["id"]
            # name = response_body["responseData"]["dataList"][0]["name"]
            # value = response_body["responseData"]["dataList"][0]["value"]
            dataList_len = len(response_body["responseData"]["dataList"])
            # print(dataList_len)
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Odo meter value configured in the telemetry stub : ", telemetry_odo_value)
            print("Odo meter value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(telemetry_odo_value):
            testResult(self, "passed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "passed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

























    @pytest.mark.regression
    # Validate telemetry-HVAC_TEMPERATURE_CURRENT functionality.
    def test2_telemetry_hvac_temp_current(self):
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

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "paho_telemetry_stubtel")
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
            print(f"HVAC_TEMPERATURE_CURRENT attribute name printed in device log : ' {telemetry_fuel_level_attribute} ' ")
            testResult(self, "passed", "HVAC_TEMPERATURE_CURRENT attribute should be present in telemetry data",
                       "Fuel level attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Fuel level attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Fuel level attribute should be present in telemetry data ",
                       "Fuel levl attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        telemetry_fuel_level_value1 = telemetry_fuel_level_attribute + telemetry_fuel_level_value
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
            testResult(self, "verificationFailed", "Odo-meter value should be published to cloud ",
                       "Fuel levl value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # verify fuel level value in the telemetry message published to cloud
        ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, telemetry_msg_type_code_tel)

        if telemetry_msg_id_published2Cloud in str(ls[0]) and telemetry_msg_type_code_tel in str(ls[0]):
            print(
                f"Telemetry message published to cloud' {telemetry_msg_id_published2Cloud} with {telemetry_msg_type_code_tel} '")
            testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is published to cloud and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")

        if str(ls[0]) == "Error":
            print(
                "Telemetry message is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Telemetry message should be published to cloud via Hub ",
                       "Telemetry message is not published to cloud or device logs are not updated. pls refer device "
                       "logs in detail ")
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

        response_body = telemetry_Curr(self, telemetry_HVAC_temp_current_event_type, systemId)

        # id = response_body["responseData"]["dataList"][0]["id"]
        # name = response_body["responseData"]["dataList"][0]["name"]
        # value = response_body["responseData"]["dataList"][0]["value"]
        #
        # if value == telemetry_fuel_level_value:
        #     print("Fuel level value configured in the telemetry stub : ", telemetry_fuel_level_value)
        #     print("Fuel level value stored in Cloud DB : ", value)
        #     testResult(self, "passed",
        #                "Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
        #                "Fuel level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
        #                "cloud logs for detailed info")
        # else:
        #     testResult(self, "failed",
        #                "Fuel level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
        #                "Fuel level value is not stored in the Cloud DB  or not same as that of configured in the telemetry stub running on device . pls refer "
        #                "device logs for detailed info")
        # time.sleep(10)