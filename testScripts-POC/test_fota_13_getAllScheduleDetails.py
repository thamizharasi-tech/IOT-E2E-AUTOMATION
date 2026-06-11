import pytest

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.fota_api_modules import FOTA_GetAllScheduleDetails
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_smoke:

    # -----------------------------------------------------------------
    # Fota-Get all schedule
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_fota_getallSchedules(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["data"]) >= 1:
                print("Model : ", response_body["responseData"]["data"][0]["model"])
                print("Status : ", response_body["responseData"]["data"][0]["status"])
                print("Offered : ", response_body["responseData"]["data"][0]["offered"])
                print("Accepted : ", response_body["responseData"]["data"][0]["accepted"])
                print("Completed : ", response_body["responseData"]["data"][0]["complete"])

                print("Created Date : ", response_body["responseData"]["data"][0]["createdDate"])
                print("Updated By : ", response_body["responseData"]["data"][0]["updatedBy"])
                print("Start Date : ", response_body["responseData"]["data"][0]["startDate"])
                print("End Date : ", response_body["responseData"]["data"][0]["endDate"])
                print("Script Id : ", response_body["responseData"]["data"][0]["script"]["id"])
                print("Script Name : ", response_body["responseData"]["data"][0]["script"]["name"])
                print("PreConditions : ", response_body["responseData"]["data"][0]["script"]["preConditions"])
                print("Notes : ", response_body["responseData"]["data"][0]["script"]["notes"])
                print("System Name : ", response_body["responseData"]["data"][0]["script"]["systems"][0]["name"])
                print("Source Version : ",
                      response_body["responseData"]["data"][0]["script"]["systems"][0]["sourceVersion"])
                print("Target Version : ",
                      response_body["responseData"]["data"][0]["script"]["systems"][0]["targetVersion"])
                print("Ref Id : ", response_body["responseData"]["data"][0]["refId"])

                testResult(self, "passed", "Should fetch all the FOTA schedule details successfully",
                           "Successfully fetched the values/data for fota schedule ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the FOTA schedule details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the FOTA schedule details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getallSchedules_invalidapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "invalid_apiKey")
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
    def test1_negative_fota_getallSchedules_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "empty_apiKey")
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
    def test1_negative_fota_getallSchedules_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "no_apiKey")
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
    def test1_negative_fota_getallschedules_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_getallschedules_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # invalid pageNo
    @pytest.mark.Smoke
    def test1_negative_fota_getallSchedules_invalid_pageno(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["Response Code"] == str(14122) or response_body[
            "Response Message"] == "Input parameter is invalid":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid pageSize
    @pytest.mark.Smoke
    def test1_negative_fota_getallSchedules_invalid_pagesize(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "-1"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14089) and response_body["responseData"][
            "message"] == "Page size must not be less than one":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # without queryparams(pageNo,pageSize)
    @pytest.mark.Smoke
    def test1_Positive_fota_getallSchedules_without_queryparams(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetAllScheduleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = FOTA_GetAllScheduleDetails(self, pageNo, pageSize, "removeQueryParams_from_url")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["data"]) >= 1:
                print("Model : ", response_body["responseData"]["data"][0]["model"])
                print("Status : ", response_body["responseData"]["data"][0]["status"])
                print("Offered : ", response_body["responseData"]["data"][0]["offered"])
                print("Accepted : ", response_body["responseData"]["data"][0]["accepted"])
                print("Completed : ", response_body["responseData"]["data"][0]["complete"])

                print("Created Date : ", response_body["responseData"]["data"][0]["createdDate"])
                print("Updated By : ", response_body["responseData"]["data"][0]["updatedBy"])
                print("Start Date : ", response_body["responseData"]["data"][0]["startDate"])
                print("End Date : ", response_body["responseData"]["data"][0]["endDate"])
                print("Script Id : ", response_body["responseData"]["data"][0]["script"]["id"])
                print("Script Name : ", response_body["responseData"]["data"][0]["script"]["name"])
                print("PreConditions : ", response_body["responseData"]["data"][0]["script"]["preConditions"])
                print("Notes : ", response_body["responseData"]["data"][0]["script"]["notes"])
                print("System Name : ", response_body["responseData"]["data"][0]["script"]["systems"][0]["name"])
                print("Source Version : ",
                      response_body["responseData"]["data"][0]["script"]["systems"][0]["sourceVersion"])
                print("Target Version : ",
                      response_body["responseData"]["data"][0]["script"]["systems"][0]["targetVersion"])
                print("Ref Id : ", response_body["responseData"]["data"][0]["refId"])

                testResult(self, "passed", "Should fetch all the FOTA schedule details successfully",
                           "Successfully fetched the values/data for fota schedule ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the FOTA schedule details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the FOTA schedule details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")
