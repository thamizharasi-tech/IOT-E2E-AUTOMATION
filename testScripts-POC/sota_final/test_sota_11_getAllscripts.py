import pytest

from C2CModules.sota_api_modules import SOTA_ListScripts
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # Fota-Get all scripts
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_sota_getallscripts(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Script Id : ", response_body["responseData"]["dataList"][0]["scriptId"])
                print("Script Name : ", response_body["responseData"]["dataList"][0]["scriptName"])
                print("Command : ", response_body["responseData"]["dataList"][0]["command"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Preconditions : ", response_body["responseData"]["dataList"][0]["preconditions"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Application Name : ", response_body["responseData"]["dataList"][0]["applicationName"])
                print("Target Version : ", response_body["responseData"]["dataList"][0]["targetVersion"])
                print("Notes : ", response_body["responseData"]["dataList"][0]["notes"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])

                testResult(self, "passed", "Should fetch all the script details successfully",
                           "Successfully fetched the values/data for scripts ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the script details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the script details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_invalidapikey(self):

        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching..please provide valid key"

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_emptyapikey(self):

        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "empty_apiKey")
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
    def test1_negative_sota_getallscripts_noapikey(self):

        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize,"no_apiKey")
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
    def test1_negative_sota_getallscripts_emptyxrequestor(self):

        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_noxrequestor(self):

        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # pageNo less than 0
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_pageno_lessthanzero(self):
        temp = "invalid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts_pageNo_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15047):
            assert response_body["responseData"]["message"] == "Page number must not be less than one"
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid pageNo like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_invalid_pageNo(self):
        temp = "invalid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "xy"
            pageSize = "10"
        print(pageNo, pageSize)
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["error"] == str(15084):
            assert response_body["message"] == "Unable to find mandatory input parameter"
        else:
            assert False

        print("----------------------------------------------------------")

    # pageSize lessthan zero
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_pageSize12_lessthanzero(self):
        temp = "invalid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts_pageSize_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "-1"

        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, temp)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15048):
            assert response_body["responseData"]["message"] == "Page size must not be less than one"
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid pageSize like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getallscripts_invalid_pageSize(self):
        temp = "invalid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "xy"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["error"] == str(15084):
            assert response_body["message"] == "Unable to find mandatory input parameter"
        else:
            assert False

        print("----------------------------------------------------------")

    # without queryparams(pageNo,pageSize)
    @pytest.mark.Smoke
    def test1_Positive_sota_getallscripts_without_queryparams(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScripts")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListScripts(self, pageNo, pageSize, "removeQueryParams_from_url")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Script Id : ", response_body["responseData"]["dataList"][0]["scriptId"])
                print("Script Name : ", response_body["responseData"]["dataList"][0]["scriptName"])
                print("Command : ", response_body["responseData"]["dataList"][0]["command"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Preconditions : ", response_body["responseData"]["dataList"][0]["preconditions"])
                print("Created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Application Name : ", response_body["responseData"]["dataList"][0]["applicationName"])
                print("Target Version : ", response_body["responseData"]["dataList"][0]["targetVersion"])
                print("Notes : ", response_body["responseData"]["dataList"][0]["notes"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])

                testResult(self, "passed", "Should fetch all the script details successfully",
                           "Successfully fetched the values/data for scripts ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the script details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the script details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")
