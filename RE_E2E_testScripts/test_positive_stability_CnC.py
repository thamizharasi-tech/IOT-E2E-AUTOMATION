import json
import time
import pytest
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from C2CModules.commandControl_modules import commandControl_wrapper, get_commandCtrl_trackingId, \
    commandControl_Tracking, verify_commandCtrl_apiResp_status
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, getVIN, \
    get_SystemId
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
sched = BlockingScheduler()
self = ''


@pytest.mark.positive
def testmy_interval_job():
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

    if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]):
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


sched.add_job(testmy_interval_job, 'interval', seconds=1800)
sched.start()
