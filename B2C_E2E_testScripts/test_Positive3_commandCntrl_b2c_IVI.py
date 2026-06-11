import time

from C2CModules.commandControl_modules import *
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.telemetry_modules import telemetry_Curr

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test1_commandCntrl:

    def test1_CommandControl_Ignition_Lock(self):
        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition3")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_ON, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 1 ",
                       "Side stand state is set to 1, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 1 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 1, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value_0):
            testResult(self, "verificationPassed",
                       "Speed should be set to 0 on cloud",
                       "Speed should set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed should be set to 0 on cloud",
                       "Speed is not set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        # verify side stand value @ cloud
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_OFF)
            print("side stand state stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value_0):
            testResult(self, "verificationPassed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is not set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Ignition ON via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_HandleLock', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Lock_ignition_value)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

    def test2_CommandControl_handle_unlock(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition2")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]) :
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_OFF, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 0, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value_0):
            testResult(self, "verificationPassed",
                       "Speed should be set to 0 on cloud",
                       "Speed should set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed should be set to 0 on cloud",
                       "Speed is not set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        # verify side stand value @ cloud
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_OFF)
            print("side stand state stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_sidestand_state_OFF):
            testResult(self, "verificationPassed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is not set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Ignition Unlock via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_HandleUnlock', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Unlock_ignition_value)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")
        print("----------------------------------------------------------")

    def test3_CommandControl_Ignition_Off(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition1")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value_0):
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
        print("-----------------------------")
        print("Initiate Command - Ignition OFF via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_IgnitionOFF', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

        print("----------------------------------------------------------")

    def test4_CommandControl_Ignition_On(self):
        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition2")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_OFF, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 0, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_OFF)
            print("side stand state stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value_0):
            testResult(self, "verificationPassed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Side stand state should be set to 0 on cloud",
                       "Side stand state is not set to 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Ignition ON via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_IgnitionON', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_On_ignition_value)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

    def test5_CommandControl_Immobilize(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition1")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]) :
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_speed_value_0) or int(value) == 0:
                testResult(self, "verificationPassed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Immobilize via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_Immobilize', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute, b2c_telemetry_immobilize_state_attribute + b2c_telemetry_immobilize_state_ON)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

        print("----------------------------------------------------------")

    def test6_CommandControl_mobilize(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition3")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_ON, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 1 ",
                       "Side stand state is set to 1, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 1 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 1, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_ON)
            print("side stand state stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_sidestand_state_ON):
                testResult(self, "verificationPassed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is not set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Mobilize via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_wrapper(self, systemId, 'CommandControl_Mobilize', appid)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, b2c_telemetry_immobilize_state_attribute, b2c_telemetry_immobilize_state_attribute + b2c_telemetry_immobilize_state_OFF)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

    def test7_CommandControl_whizBike_playsound(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition3")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_ON, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 1 ",
                       "Side stand state is set to 1, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 1 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 1, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_ON)
            print("side stand state stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_sidestand_state_ON):
                testResult(self, "verificationPassed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is not set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Whiz Bike - Play sound via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        #response = commandControl_wrapper(self, systemId, 'CommandControl_BuzzBike', appid)
        response = commandControl_Request(self, appid, 'WHIZZ_BIKE', '0', '2', vin)

        # parse api response into json
        response = response.json()

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, 'command execution success',
                                   'command execution success')
        print(ls)

        ls = verify_message_in_log(self, 'resp sent successfully',
                                   'resp sent successfully')

        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

    def test8_CommandControl_whizBike_blinkIndicators(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition3")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_ON, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 1 ",
                       "Side stand state is set to 1, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 1 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 1, pls refer device & cloud logs for detailed info")

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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_ON)
            print("side stand state stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_sidestand_state_ON):
                testResult(self, "verificationPassed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Side stand state should be set to 1 on cloud",
                           "Side stand state is not set to 1 on cloud . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Whiz Bike -  Blink Indicators via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        # response = commandControl_wrapper(self, systemId, 'CommandControl_BuzzBike', appid)
        response = commandControl_Request(self, appid, 'WHIZZ_BIKE', '0', '1', vin)

        # parse api response into json
        response = response.json()

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, 'command execution success',
                                   'command execution success')
        print(ls)

        ls = verify_message_in_log(self, 'resp sent successfully',
                                   'resp sent successfully')

        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

    def test9_CommandControl_SoS_ACTIVATE(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition1")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]) :
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_speed_value_0) or int(value) == 0:
                testResult(self, "verificationPassed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - SOS Reset (Value 1) via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        # response = commandControl_remoteOperation(self, "CommandControl_SOS", systemId, "ACTIVATE", appid)
        response = commandControl_Request(self, appid, "SOS", "0", "1", vin)

        # parse api response into json
        response = response.json()

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_attribute + b2c_telemetry_SOS_state_ON)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

        print("----------------------------------------------------------")

    def test10_CommandControl_SoS_DEACTIVATE(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition1")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]) :
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
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
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("Speed value stored in Cloud DB : ", value)
            if int(value) == int(b2c_telemetry_speed_value_0) or int(value) == 0:
                testResult(self, "verificationPassed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                           "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                           "cloud logs for detailed info")
        except:
            print("dataList is empty in api response")
            value = ""

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - SOS Reset (Value 0) via API : ")
        print("-----------------------------")

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        # response = commandControl_remoteOperation(self, "CommandControl_SOS", systemId, "DEACTIVATE", appid)
        response = commandControl_Request(self, appid, "SOS", "0", "0", vin)

        # parse api response into json
        response = response.json()

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations for initiated command : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        ls = verify_message_in_log(self, b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_attribute + b2c_telemetry_SOS_state_OFF)
        print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(60)

        try:
            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

            # Verify command & control status
            verify_commandCtrl_apiResp_status(self, response)
            testResult(self, "passed",
                       "Command execution should be completed and status (103) should be updated on cloud",
                       "Command execution is completed successfully and status (103) is updated on cloud")
        except:
            testResult(self, "failed",
                       "Command execution should be completed successfully and status (103) should be updated on cloud",
                       "Command execution is not completed successfully")

        print("----------------------------------------------------------")
