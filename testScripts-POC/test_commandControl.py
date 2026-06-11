import time

import pytest

from C2CModules.commandControl_modules import commandControl_Request, commandControl_Tracking, \
    get_commandCtrl_trackingId, commandControl_Request_header_validation, commandControl_Tracking_header_validation
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_CommandControl:

    # CommandControl Request & Tracking
    @pytest.mark.Smoke
    def test1_positive_CommandControl_Request_Tracking(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("App Id :", appid)
            print("Name :", name)
            print("Area :", area)
            print("Value :", value)
            print("VIN :", vin)

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            #time.sleep(180)

            response = response.json()

            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

            print("App Id :", appid)
            print("Name :", name)
            print("Area :", area)
            print("Value :", value)
            print("VIN :", vin)

            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(180)

            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Tracking(self, trackingId)

        print("----------------------------------------------------------")

    # CommandControl Request
    @pytest.mark.Smoke
    def test2_positive_CommandControl_Request(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request(self, appid, name, area, value, vin)
        time.sleep(30)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["status"] == 1
        print("Tracking Id :", response_body["responseData"]["trackingId"])

        print("----------------------------------------------------------")

        # valid_trackingID

    # CommandControl Tracking
    @pytest.mark.Smoke
    def test3_positive_CommandControl_Tracking_valid_trackingID(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")

        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
            response = commandControl_Tracking_header_validation(self, trackingId, "valid")
        if dict1['Flag'] == "Yes" or dict1['Flag'] == "No":
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            # Read api test data resp from excel sheet
            dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(30)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            response_body = response.json()

            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response_body)

        response = commandControl_Tracking_header_validation(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        assert response_body["responseCode"] == "1200" or response_body["responseCode"] == 1200
        trackingId_actual = response_body["responseData"]["trackingId"]
        if trackingId == trackingId_actual:
            print("Tracking Status : ", response_body["responseData"]["trackingStatus"])
            print("VIN : ", response_body["responseData"]["data"][0]["vin"])
            print("SystemId : ", response_body["responseData"]["data"][0]["systemId"])
            print("Status : ", response_body["responseData"]["data"][0]["status"])
        else:
            print("Tracking id mismatch")
            assert False

        print("----------------------------------------------------------")

    # CommandControl Tracking -
    @pytest.mark.Smoke
    def test4_positive_CommandControl_Tracking_valid_trackingID_FAILED_status(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking_FAILED_status")

        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
            response = commandControl_Tracking_header_validation(self, trackingId, "valid")
        if dict1['Flag'] == "Yes" or dict1['Flag'] == "No":
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            # Read api test data resp from excel sheet
            dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(30)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            response_body = response.json()

            # read tracking id
            trackingId = get_commandCtrl_trackingId(self, response_body)

        response = commandControl_Tracking_header_validation(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        assert response_body["responseCode"] == "1200" or response_body["responseCode"] == 1200
        trackingId_actual = response_body["responseData"]["trackingId"]
        if trackingId == trackingId_actual:
            print("Tracking Status : ", response_body["responseData"]["trackingStatus"])
            print("VIN : ", response_body["responseData"]["data"][0]["vin"])
            print("SystemId : ", response_body["responseData"]["data"][0]["systemId"])
            print("Status : ", response_body["responseData"]["data"][0]["status"])
            assert response_body["responseData"]["data"][0]["status"] == 105
        else:
            print("Tracking id mismatch")
            assert False

        print("----------------------------------------------------------")



    # invalid_apikey
    def test1_negative_CommandControl_Request_Tracking_invalid_apikey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request_header_validation(self, appid, name, area, value, vin,
                                                            "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # empty_apikey
    def test2_negative_CommandControl_Request_Tracking_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request_header_validation(self, appid, name, area, value, vin,
                                                            "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # no_apiKey
    def test3_negative_CommandControl_Request_Tracking_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request_header_validation(self, appid, name, area, value, vin,
                                                            "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        if response_body["message"] == "Required authentication headers are missing":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # empty_x-requestor
    def test4_negative_CommandControl_Request_Tracking_empty_x_requestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request_header_validation(self, appid, name, area, value, vin,
                                                            "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "x-requestor header cannot be blank":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # no_x-requestor
    def test5_negative_CommandControl_Request_Tracking_no_x_requestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request")
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request_header_validation(self, appid, name, area, value, vin,
                                                            "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid vin
    def test6_negative_CommandControl_Request_Tracking_invalid_vin(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_invalid_vin")
        print("dict1 : ", dict1)
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VIN123"

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request(self, appid, name, area, value, vin)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response body
        assert response_body["responseCode"] == str(14511)
        assert response_body["message"] == "VIN length should be 17"
        print("----------------------------------------------------------")

    # empty app_id

    def test7_negative_CommandControl_Request_Tracking_empty_app_id(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_empty_app_id")

        print("dict1 : ", dict1)
        appid = str(dict1["appid"])

        if appid == "None":
            appid = ''

        name = str(dict1["name"])
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request(self, appid, name, area, value, vin)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response body
        assert response_body["responseCode"] == str(14519)
        assert response_body["message"] == "AppId cannot be null or empty"

        print("----------------------------------------------------------")

        # empty name

    def test8_negative_CommandControl_Request_Tracking_empty_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_empty_name")

        print("dict1 : ", dict1)
        appid = str(dict1["appid"])
        name = str(dict1["name"])
        if name == "None":
            name = ''
        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request(self, appid, name, area, value, vin)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response body
        assert response_body["responseCode"] == str(14501)
        assert response_body["message"] == "commandName can not be empty"
        print("----------------------------------------------------------")

    def test9_negative_CommandControl_Request_Tracking_empty_vin(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Request_empty_vin")

        print("dict1 : ", dict1)
        appid = str(dict1["appid"])
        name = str(dict1["name"])

        area = int(dict1["area"])
        value = int(dict1["value"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            vin = str(dict1["vin"])
            if vin == "None":
                vin = ''

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        print("App Id :", appid)
        print("Name :", name)
        print("Area :", area)
        print("Value :", value)
        print("VIN :", vin)

        response = commandControl_Request(self, appid, name, area, value, vin)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response body
        assert response_body["responseCode"] == str(14511)
        assert response_body["message"] == "VIN length should be 17"

        print("----------------------------------------------------------")

    # invalid_apikey
    def test10_negative_CommandControl_Tracking_invalid_apikey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")
        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(60)

            # read trac/king id
            trackingId = get_commandCtrl_trackingId(self, response)

        response = commandControl_Tracking_header_validation(self, trackingId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # empty_apiKey
    def test11_negative_CommandControl_Tracking_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")
        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(60)

            # read trac/king id
            trackingId = get_commandCtrl_trackingId(self, response)

        response = commandControl_Tracking_header_validation(self, trackingId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        if response_body["message"] == "api keys are not matching. Please provide valid key":
            assert True
        elif "api keys are not matching" in response_body["message"]:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # no_apiKey
    def test12_negative_CommandControl_Tracking_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")
        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(60)

            # read trac/king id
            trackingId = get_commandCtrl_trackingId(self, response)

        response = commandControl_Tracking_header_validation(self, trackingId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # empty_x-requestor
    def test13_negative_CommandControl_Tracking_invalid_empty_x_requestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")
        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(60)

            # read trac/king id
            trackingId = get_commandCtrl_trackingId(self, response)

        response = commandControl_Tracking_header_validation(self, trackingId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # verify api response
        if response_body["message"] == "x-requestor header cannot be blank":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # no_x-requestor
    def test14_negative_CommandControl_Tracking_no_x_requestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking")
        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            appid = str(dict1["appid"])
            name = str(dict1["name"])
            area = int(dict1["area"])
            value = int(dict1["value"])

            # Call command & control reusable module
            response = commandControl_Request(self, appid, name, area, value, vin)
            time.sleep(60)

            # read trac/king id
            trackingId = get_commandCtrl_trackingId(self, response)

        response = commandControl_Tracking_header_validation(self, trackingId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # verify api response
        if response_body["message"] == "Required authentication headers are missing":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid_trackingID
    def test15_negative_CommandControl_Tracking_invalid_trackingID(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "CommandControl", "CommandControl_Tracking_invalid_trackingID")

        trackingId = str(dict1["trackingId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            trackingId = str(dict1["trackingId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            trackingId = "12345"

        response = commandControl_Tracking_header_validation(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Verify api response
        assert response_body["responseCode"] == "14520"
        assert response_body["message"] == "No data found for the request Id"

        print("----------------------------------------------------------")
