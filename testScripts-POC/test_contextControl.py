import pytest

from C2CModules.e2e_testData import telemetry_odo_event_type
from C2CModules.contextControl_modules import context_Control
from C2CModules.primary_IVI_device_modules import get_SystemId
from utils.XLUtils import read_api_data_from_excel
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset

class Test_Telemetry:

    # ContextControl
    @pytest.mark.Smoke
    def test1_positive_ContextControl(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "ContextControl", "ContextControl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            enable = str(dict1["enable"])
            frequency = str(dict1["frequency"])
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, deviceType_IVI, drimaes_ivi_chipset)
            block_id = telemetry_odo_event_type
            reason_code = 0
            enable = 'true'
            frequency = 1

        # Call telemetry reusable module
        response_body = context_Control(self, block_id, reason_code, enable, frequency, systemId)

        assert (response_body["responseCode"] == "1200")
        try:
            print(response_body["message"])
        except:
            print('message is not displayed')

        print("----------------------------------------------------------")

