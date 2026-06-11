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
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test1_chargeNotification:

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test1_chargingNotification_charge_port_Connected(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for charging notification
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run charging notification stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run ev charging stub on device : ")

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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify ev_charge_port_connected attribute in the device logs
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

        # verify ev_charge_port_connected state/value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_connected_state_ON)
            print("EV Charge Port Connected State value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_ev_charge_port_open_state_ON):
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
    def test2_chargingNotification_inst_charge_rate(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for ev charging
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run ev charging stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run ev charging stub on device : ")

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
        # Device side validations : verify messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify inst_charge_rate attribute in the device logs
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

        # verify inst_charge_rate value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV BATTERY INSTANTANEOUS CHARGE_RATE value configured in the ev charging stub : ",
                  b2c_inst_charge_rate_value)
            print("EV BATTERY INSTANTANEOUS CHARGE_RATE value stored in Cloud : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_inst_charge_rate_value):
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port connected functionality.
    def test3_chargingNotification_no_inst_charge_rate(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for ev charging
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run ev charging stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run ev charging stub on device : ")

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

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify inst_charge_rate attribute in the device logs
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

        # verify inst_charge_rate value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_inst_charge_rate:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV BATTERY INSTANTANEOUS CHARGE_RATE value configured in the stub : ",
                  b2c_no_inst_charge_rate_value)
            print("EV BATTERY INSTANTANEOUS CHARGE_RATE value stored in Cloud : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_no_inst_charge_rate_value):
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "passed",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "EV BATTERY INSTANTANEOUS CHARGE RATE value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port disconnected functionality.
    def test4_chargingNotification_charge_port_disconnected(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for charging notification
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run charging notification stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run ev charging stub on device : ")

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
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify ev_charge_port_connected attribute in the device logs
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

        # verify ev_charge_port_connected state/value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_connected:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_connected_state_OFF)
            print("EV Charge Port Connected State value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_ev_charge_port_open_state_OFF):
            testResult(self, "passed",
                       "EV Charge Port should be in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state is set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port should be in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is not in disconnected/OFF state ie EV_CHARGE_PORT_CONNECTED state is not set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port open functionality.
    def test5_chargingNotification_charge_port_open(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for ev charging
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run ev charging stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub on device : ")

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

        # verify attribute in the device logs
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
            testResult(self, "passed", "EV Charge Port Open state should be published to cloud ",
                       "EV Charge Port Open state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV Charge Port Open state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "EV Charge Port Open state should be published to cloud ",
                       "EV Charge Port Open state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify ev_charge_port_connected state/value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_open_state_ON)
            print("EV Charge Port Open state/value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_ev_charge_port_open_state_ON):
            testResult(self, "passed",
                       "EV Charge Port should be in open/ON state ie EV_CHARGE_PORT_OPEN state should be set to 1 at both Device & Cloud",
                       "EV Charge Port is in open/ON state ie EV_CHARGE_PORT_OPEN state is set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port should be in open/ON state ie EV_CHARGE_PORT_OPEN state should be set to 1 at both Device & Cloud",
                       "EV Charge Port is not in open/ON state ie EV_CHARGE_PORT_OPEN state is not set to 1 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)

    @pytest.mark.regression
    # Validate charge port open functionality.
    def test6_chargingNotification_charge_port_closed(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for ev charging
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Push updated conf files for charging notification test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for charging notification test ")

        # ===========================================================================================
        # Run ev charging stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub on device : ")

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

        # verify attribute in the device logs
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
        charging_OFF = b2c_ev_charge_port_open_attribute + b2c_ev_charge_port_open_state_OFF
        ls = verify_message_in_log(self, b2c_ev_charge_port_connected_state_OFF, charging_OFF)

        if charging_OFF in str(ls[0]):
            print(f"EV Charge Port Open state is printed in device log : ' {charging_OFF} ' ")
            testResult(self, "passed", "EV Charge Port Open state should be published to cloud ",
                       "EV Charge Port Open state is published to cloud and device logs are updated with charging details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "EV Charge Port Open state is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "EV Charge Port Open state should be published to cloud ",
                       "EV Charge Port Open state is not published to cloud or device logs are not updated. pls refer device logs in detail or logs has been rotated")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify ev_charge_port_connected state/value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_ev_charge_port_open:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("EV Charge Port configured in the stub : ", b2c_ev_charge_port_open_state_OFF)
            print("EV Charge Port Open state/value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_ev_charge_port_open_state_OFF):
            testResult(self, "passed",
                       "EV Charge Port should be in closed/OFF state ie EV_CHARGE_PORT_OPEN state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is in closed/OFF state ie EV_CHARGE_PORT_OPEN state is set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "EV Charge Port should be in closed/OFF state ie EV_CHARGE_PORT_OPEN state should be set to 0 at both Device & Cloud",
                       "EV Charge Port is not in closed/OFF state ie EV_CHARGE_PORT_OPEN state is not set to 0 at both Device & Cloud . pls refer "
                       "device & cloud logs for detailed info")

        time.sleep(10)
