import time

import pytest

from C2CModules.APIM_ReusableModules import commandControl_Request_APIIM_horn, commandControl_Request_APIIM_headlight, \
    commandControl_Request_APIIM_hazardlight, commandControl_Request_APIIM_flashlight, \
    commandControl_Request_APIIM_emergencylight, commandControl_Request_APIIM_ambientlight, \
    commandControl_Request_APIIM_taillight, commandControl_Request_APIIM_readinglight, \
    commandControl_Request_APIIM_Buzzbike, commandControl_Request_APIIM_ignition, \
    commandControl_Request_APIIM_immobilize
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset





class Test_CommandControl:

    # APIIM CommandControl Request Horn-ON
    @pytest.mark.Smoke
    def test1_positive_APIIM_CommandControl_Request_HornON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "horn-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_horn")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                #vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"



            # Call command & control reusable module
            response = commandControl_Request_APIIM_horn(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                    testResult(self,"passed","Command should be send successfully","Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                    testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                    print("something went wrong")



            print("----------------------------------------------------------")

    # APIIM CommandControl Request Horn-OFF
    @pytest.mark.Smoke
    def test2_positive_APIIM_CommandControl_Request_HornOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "horn-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_horn")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_horn(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Headlight-ON
    @pytest.mark.Smoke
    def test3_positive_APIIM_CommandControl_Request_HeadlightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "headlight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_headlight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_headlight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Headlight-OFF
    @pytest.mark.Smoke
    def test4_positive_APIIM_CommandControl_Request_HeadlightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "headlight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_headlight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_headlight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Hazardlight-ON
    @pytest.mark.Smoke
    def test5_positive_APIIM_CommandControl_Request_HazardlightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "hazardlight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_hazardlight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_hazardlight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Hazardlight-OFF
    @pytest.mark.Smoke
    def test6_positive_APIIM_CommandControl_Request_HazardlightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "hazardlight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_hazardlight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_hazardlight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Flashlight-ON
    @pytest.mark.Smoke
    def test7_positive_APIIM_CommandControl_Request_FlashlightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "flashlight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_flashlight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_flashlight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Flashlight-OFF
    @pytest.mark.Smoke
    def test8_positive_APIIM_CommandControl_Request_FlashlightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "flashlight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_flashlight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_flashlight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Emergencylight-ON
    @pytest.mark.Smoke
    def test9_positive_APIIM_CommandControl_Request_EmergencylightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "emergencylight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_emergencylight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_emergencylight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Emergencylight-OFF
    @pytest.mark.Smoke
    def test10_positive_APIIM_CommandControl_Request_EmergencylightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "emergencylight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_emergencylight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_emergencylight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Ambientlight-ON
    @pytest.mark.Smoke
    def test11_positive_APIIM_CommandControl_Request_AmbientlightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "ambientlight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ambientlight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_ambientlight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Ambientlight-OFF
    @pytest.mark.Smoke
    def test12_positive_APIIM_CommandControl_Request_AmbientlightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "ambientlight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ambientlight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_ambientlight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Taillight-ON
    @pytest.mark.Smoke
    def test13_positive_APIIM_CommandControl_Request_TaillightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "taillight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_taillight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_taillight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Taillight-OFF
    @pytest.mark.Smoke
    def test14_positive_APIIM_CommandControl_Request_TaillightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "taillight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_taillight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_taillight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Readinglight-ON
    @pytest.mark.Smoke
    def test15_positive_APIIM_CommandControl_Request_ReadinglightON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "readinglight-on"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_readinglight")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_readinglight(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Readinglight-OFF
    @pytest.mark.Smoke
    def test16_positive_APIIM_CommandControl_Request_ReadinglightOFF(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "readinglight-off"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_readinglight")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_readinglight(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request BuzzBike-ON
    @pytest.mark.Smoke
    def test17_positive_APIIM_CommandControl_Request_BuzzBilke_ON(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "BUZZ-BIKE-ON"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_buzzbike")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_Buzzbike(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")



    # APIIM CommandControl Request BuzzBike-OFF
    @pytest.mark.Smoke
    def test18_positive_APIIM_CommandControl_Request_BuzzBilke_OFF(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "BUZZ-BIKE-OFF"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_buzzbike")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_Buzzbike(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Handle-lock
    @pytest.mark.Smoke
    def test19_positive_APIIM_CommandControl_Request_Handle_lock(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "HANDLE-LOCK"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ignition")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_ignition(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Handle-unlock
    @pytest.mark.Smoke
    def test20_positive_APIIM_CommandControl_Request_Handle_unlock(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "HANDLE-UNLOCK"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ignition")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_ignition(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Ignition-ON
    @pytest.mark.Smoke
    def test21_positive_APIIM_CommandControl_Request_Ignition_ON(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "IGNITION-ON"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ignition")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_ignition(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Ignition-OFF
    @pytest.mark.Smoke
    def test22_positive_APIIM_CommandControl_Request_Ignition_OFF(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "IGNITION-OFF"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_ignition")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_ignition(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")

    # APIIM CommandControl Request Immobilize
    @pytest.mark.Smoke
    def test23_positive_APIIM_CommandControl_Request_Immobilize(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        testCaseName = "IMMOBILIZE"
        dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_immobilize")
        appid = str(dict1["appid"])
        systemId = str(dict1["systemId"])

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # vin = str(dict1["vin"])
            appid = str(dict1["appid"])
            print("App Id :", appid)
        else:
            appid = "demo_2022_app2"
            systemId = "sys65234240668f11eeabae"

        # Call command & control reusable module
        response = commandControl_Request_APIIM_immobilize(self, appid, systemId, testCaseName)

        response_body = response.json()
        if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed", "Command should be send successfully", "Command send successfully")
        elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
            testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # APIIM CommandControl Request Immobilize
    @pytest.mark.Smoke
    def test24_positive_APIIM_CommandControl_Request_Mobilize(self):
            print("----------------------------------------------------------")
            # Read api test data resp from excel sheet
            testCaseName = "MOBILIZE"
            dict1 = read_api_data_from_excel(self, "CommandControl", "APIIM_CommandControl_Request_immobilize")
            appid = str(dict1["appid"])
            systemId = str(dict1["systemId"])

            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                # vin = str(dict1["vin"])
                appid = str(dict1["appid"])
                print("App Id :", appid)
            else:
                appid = "demo_2022_app2"
                systemId = "sys65234240668f11eeabae"

            # Call command & control reusable module
            response = commandControl_Request_APIIM_immobilize(self, appid, systemId, testCaseName)

            response_body = response.json()
            if response_body["responseData"]["status"] == 1 and response_body["message"] == "Data Saved Successfully":
                testResult(self, "passed", "Command should be send successfully", "Command send successfully")
            elif response_body["responseData"]["status"] != 1 and response_body["message"] != "Data Saved Successfully":
                testResult(self, "failed", "Command should not be send successfully", "Command send successfully")
            else:
                print("something went wrong")

            print("----------------------------------------------------------")