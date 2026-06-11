import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.APIM_ReusableModules import getTelemetryCurrValue
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_smoke:

    # get telemetry curr value
    @pytest.mark.Smoke
    def test1_positive_get_telemetry_curr_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_system_CurrValue")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryCurrValues")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry handles value
    @pytest.mark.Smoke
    def test2_positive_get_telemetry_handles_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_handles_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForHandles")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry tail-light value
    @pytest.mark.Smoke
    def test3_positive_get_telemetry_tail_light_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_tail-light_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForTailLight")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                           "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                           "Failed to fetch telemetry data" + " Reason for failure is : " +
                           response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry head-light value
    @pytest.mark.Smoke
    def test4_positive_get_telemetry_head_light_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_head-light_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForHeadLight")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry horn value
    @pytest.mark.Smoke
    def test5_positive_get_telemetry_horn_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_horn_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForHorn")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry hazard-light value
    @pytest.mark.Smoke
    def test6_positive_get_telemetry_hazardlight_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_hazard-light_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForHazardLight")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry high-beam-light-state value
    @pytest.mark.Smoke
    def test7_positive_get_telemetry_highBeamlightState_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_highBeamLightState_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForHighBeamLightState")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry indicator value
    @pytest.mark.Smoke
    def test8_positive_get_telemetry_indicator_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_indicator_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForIndicator")
        #validate response code
        #assert(response.status_code == 200), "status code is not 200.Rather than found: "+str(response.status_code)
        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry side-stand value
    @pytest.mark.Smoke
    def test9_positive_get_telemetry_sideStand_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_side-stand_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForSideStand")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

    # get telemetry battery-readings value
    @pytest.mark.Smoke
    def test10_positive_get_telemetry_batteryReadings_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_batteryReadings_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForBatteryReadings")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

   # get telemetry battery level value
    @pytest.mark.Smoke
    def test11_positive_get_telemetry_batteryLevel_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_batteryLevel_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForBatteryLevel")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

   # get telemetry battery temperature value
    @pytest.mark.Smoke
    def test12_positive_get_telemetry_batteryTemperature_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_batteryTemperature_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForBatteryTemperature")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

  # get telemetry battery bms temperature value
    @pytest.mark.Smoke
    def test13_positive_get_telemetry_batteryBMSTemperature_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_batteryBMSTemperature_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForBatteryBMSTemperature")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

 # get telemetry location value
    @pytest.mark.Smoke
    def test14_positive_get_telemetry_location_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_location_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForLocation")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

 # get telemetry ignition value
    @pytest.mark.Smoke
    def test15_positive_get_telemetry_ignitionStatus_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_ignitionStatus_Value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForIgnitionStatus")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

 # get telemetry engine mobilize value
    @pytest.mark.Smoke
    def test16_positive_get_telemetry_engineMobilize_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_engine_mobilize_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForEngineMobilize")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

 # get telemetry tyre pressure value
    @pytest.mark.Smoke
    def test17_positive_get_telemetry_tyre_pressure_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_tyre_pressure_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForTyrePressure")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry front right tyre pressure value
    @pytest.mark.Smoke
    def test18_positive_get_telemetry_front_right_tyre_pressure_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_front_right_tyre_pressure_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForFrontRightTyrePressure")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry front left tyre pressure value
    @pytest.mark.Smoke
    def test19_positive_get_telemetry_front_left_tyre_pressure_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_front_left_tyre_pressure_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForFrontLeftTyrePressure")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry rear right tyre pressure value
    @pytest.mark.Smoke
    def test20_positive_get_telemetry_rear_right_tyre_pressure_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_rear_right_tyre_pressure_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForRearRightTyrePressure")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry rear left tyre pressure value
    @pytest.mark.Smoke
    def test21_positive_get_telemetry_rear_left_tyre_pressure_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_rear_left_tyre_pressure_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForRearLeftTyrePressure")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry rear critical threshold value
    @pytest.mark.Smoke
    def test22_positive_get_telemetry_rear_critical_threshold_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_rear_critical_threshold_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForRearCriticalPressureThreshold")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry front critical threshold value
    @pytest.mark.Smoke
    def test23_positive_get_telemetry_rear_critical_threshold_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_front_critical_threshold_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForFrontCriticalPressureThreshold")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry engine odometer value
    @pytest.mark.Smoke
    def test24_positive_get_telemetry_engine_odometer_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_engine_Odometer_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForEngineOdometer")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")

# get telemetry range remaining value
    @pytest.mark.Smoke
    def test25_positive_get_telemetry_range_remaining_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "get_telemetry_range_remaining_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("SystemId: ",systemId)

        # Call api reusable module
        response = getTelemetryCurrValue(self,systemId,"telemetryValuesForRangeRemaining")

        # Parse API response into JSON
        response_body=response.json()
        #validate response
        if response.status_code == 200:
            if response_body["message"] == "Data Fetched Successfully":
                message = response_body["message"]
                print('Message : ', message)
                print("Id: ",response_body["responseData"]["signals"][0]["id"])
                print("Name: ", response_body["responseData"]["signals"][0]["name"])
                print("Unit: ", response_body["responseData"]["signals"][0]["unit"])
                print("Value: ", response_body["responseData"]["signals"][0]["value"])
                print("Updated Time: ", response_body["responseData"]["signals"][0]["updatedTime"])
                print("Reason Code: ", response_body["responseData"]["signals"][0]["reasonCode"])
                print("Area: ", response_body["responseData"]["signals"][0]["area"])
                print("Area Name: ", response_body["responseData"]["signals"][0]["areaName"])
                testResult(self, "passed", "Telemetry values/datas should fetch successfully",
                       "Telemetry values/datas fetched successfully")
            elif response_body["message"] != "Data Fetched Successfully":
                testResult(self, "failed", "Telemetry values/datas should fetch successfully",
                       "Failed to fetch telemetry data" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Response code is not 200.Rather found: "+str(response.status_code))

        print("----------------------------------------------------------")