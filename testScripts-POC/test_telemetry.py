import pytest

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset, telemetry_odo_event_type
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.telemetry_modules import telemetry_Curr
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_Telemetry:

    # Telemetry_curr
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Curr(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            event_type = str(dict1["eventType"])
            systemId = str(dict1["SystemId"])

            # Call telemetry reusable module
            response_body = telemetry_Curr(self, event_type, systemId)
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            event_type = telemetry_odo_event_type
            response_body = telemetry_Curr(self, event_type, systemId)

        assert (response_body["responseCode"] == "1200")
        assert (response_body["responseData"]["message"] == "Successfully fetched the current values")
        tel_len = len(response_body["responseData"]["dataList"])
        for i in range(tel_len):
            name = response_body["responseData"]["dataList"][i]["name"]
            if name == "FUEL_LEVEL":
                id = response_body["responseData"]["dataList"][i]["id"]
                value = response_body["responseData"]["dataList"][i]["value"]
                break
            else:
                value = None

        print("----------------------------------------------------------")

