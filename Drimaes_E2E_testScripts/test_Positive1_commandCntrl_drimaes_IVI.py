import time

from C2CModules.commandControl_modules import *
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.telemetry_modules import telemetry_Curr

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi

class Test1_commandCntrl:

    def test1_Command_window_position(self):
        # ===========================================================================================
        # Initiate Command vai API
        # ===========================================================================================

        # Get vin from device
        vin = getVIN(self, OnboardingType, chipsetType)

        # Read api configuration/common data
        dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
        appid = str(dict["Value"])
        print("APP Id : ", appid)

        # Initiate command request
        response = commandControl_Request(self, appid, "WINDOW_POSITION", 4096, 0, vin)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("-----------------------------")
        print("Device Validations : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        status = verify_msg_details_pub2Cloud(self, commndctrl_msg_type_code, "")

        print("Status : ", status)

        verify_commandCtrl_msg_in_deviceLogs(self, OnboardingType, chipsetType, commndctrl_msg_type_code, "")

        #verify_commandCtrl_msg_in_deviceLogs(self, OnboardingType, chipsetType, telemetry_msg_id_published2Cloud, commndctrl_msg_resp_type_code)

        # ===========================================================================================
        # Cloud side validations : verify command & control status
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Validations : ")
        print("-----------------------------")
        time.sleep(60)

        # read tracking id
        trackingId = get_commandCtrl_trackingId(self, response)

        # Verify command & control resp
        response = commandControl_Tracking(self, trackingId)

        # Verify command & control status
        verify_commandCtrl_apiResp_status(self, response)

        print("----------------------------------------------------------")

    def test2_Command_havc_seat_temperature(self):
        # ===========================================================================================
        # Initiate Command vai API
        # ===========================================================================================

        # test data
        command = "HVAC_SEAT_TEMPERATURE"
        area = 1
        value = 4

        # Get vin from device
        vin = getVIN(self, OnboardingType, chipsetType)

        # Initiate command request
        response = commandControl_Request(self, appid, command, area, value, vin)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================
        print("-----------------------------")
        print("Device Validations : ")
        print("-----------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        status = verify_msg_details_pub2Cloud(self, commndctrl_msg_type_code, "")

        print("Status : ", status)
        verify_commandCtrl_msg_in_deviceLogs(self, OnboardingType, chipsetType, commndctrl_msg_type_code, "")

        # ===========================================================================================
        # Cloud side validations : verify command & control status
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Validations : ")
        print("-----------------------------")
        time.sleep(60)

        # read tracking id
        trackingId = get_commandCtrl_trackingId(self, response)

        # Verify command & control resp
        response = commandControl_Tracking(self, trackingId)

        # Verify command & control status
        verify_commandCtrl_apiResp_status(self, response)

        # Verify telemetry curr resp

        # Get systemId
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        response_body = telemetry_Curr(self, telemetry_HVAC_seat_temp_event_type, systemId)

        assert(response_body['responseCode'] == str(1200))
        msg = response_body["responseData"]["message"]
        name = response_body["responseData"]["dataList"][0]["name"]
        unit = response_body["responseData"]["dataList"][0]["unit"]
        actual_value = response_body["responseData"]["dataList"][0]["value"]
        reasonCode = response_body["responseData"]["dataList"][0]["reasonCode"]
        actual_area = response_body["responseData"]["dataList"][0]["area"]
        actual_areaName = response_body["responseData"]["dataList"][0]["areaName"]

        assert(name == command)
        assert(actual_value == str(value))
        assert(reasonCode == 37)
        assert(actual_area == str(area))
        assert(actual_areaName == 'ROW_1_LEFT')
        assert(msg == "Successfully fetched the current values")