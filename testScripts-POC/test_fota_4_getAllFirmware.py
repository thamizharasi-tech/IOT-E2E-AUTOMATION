import pytest

from C2CModules.fota_api_modules import FOTA_GetAllFirmware
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # Fota-Get all Firmware
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_fota_getallfirmware(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, temp)

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["data"]) >= 1:
                print("Id : ", response_body["responseData"]["data"][0]["id"])
                print("Created Date : ", response_body["responseData"]["data"][0]["createdDate"])
                print("Model : ", response_body["responseData"]["data"][0]["model"])
                print("Status : ", response_body["responseData"]["data"][0]["status"])
                print("Description : ", response_body["responseData"]["data"][0]["description"])

                print("System : ", response_body["responseData"]["data"][0]["system"])
                print("Firmware Version : ", response_body["responseData"]["data"][0]["firmwareVersion"])
                print("File Name : ", response_body["responseData"]["data"][0]["fileName"])

                print("IsDiffImage : ", response_body["responseData"]["data"][0]["isDiffImage"])
                print("IsBase : ", response_body["responseData"]["data"][0]["isBase"])
                print("IsFullImage : ", response_body["responseData"]["data"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["data"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["data"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["data"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the firmware details successfully",
                           "Successfully fetched the values/data for firmware ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the firmware details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the firmware details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_invalidapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
                "message"] == "api keys are not matching. Please provide valid key":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching..please provide valid key"

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
                "message"] == "Required authentication headers are missing..!!!!":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False

        print("----------------------------------------------------------")

    # pageNo less than 0
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_pageno_lessthanzero(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware_pageNo_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(14088) or response_body["responseData"]["message"] == "Page number must not be less than one":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid pageNo like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_invalidpageno(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["Response Code"] == str(14122) or response_body["Response Message"] == "Input parameter is invalid":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # pageSize lessthan zero
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_pagesize_lessthanzero(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware_pageSize_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, temp)
        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14088) or response_body["responseData"]["message"] == "Page number must not be less than one":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid pageSize like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_fota_getallfirmware_invalidpageno(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, temp)
        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14088) or response_body["Response Message"] == "Page number must not be less than one":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # without queryparams
    @pytest.mark.Smoke
    def test1_Positive_fota_getallfirmware_without_queryparams(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllFirmware(self, pageNo, pageSize, "removeQueryParams_from_url")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["data"]) >= 1:
                print("Id : ", response_body["responseData"]["data"][0]["id"])
                print("Created Date : ", response_body["responseData"]["data"][0]["createdDate"])
                print("Model : ", response_body["responseData"]["data"][0]["model"])
                print("Status : ", response_body["responseData"]["data"][0]["status"])
                print("Description : ", response_body["responseData"]["data"][0]["description"])

                print("System : ", response_body["responseData"]["data"][0]["system"])
                print("Firmware Version : ", response_body["responseData"]["data"][0]["firmwareVersion"])
                print("File Name : ", response_body["responseData"]["data"][0]["fileName"])

                print("IsDiffImage : ", response_body["responseData"]["data"][0]["isDiffImage"])
                print("IsBase : ", response_body["responseData"]["data"][0]["isBase"])
                print("IsFullImage : ", response_body["responseData"]["data"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["data"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["data"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["data"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the firmware details successfully",
                           "Successfully fetched the values/data for firmware ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the firmware details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the firmware details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")
