import pytest

from C2CModules.sota_api_modules import SOTA_ListPackages
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_smoke:

    # -----------------------------------------------------------------
    # Sota-Get all packages
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_positive_sota_getAllPackages(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Id : ", response_body["responseData"]["dataList"][0]["packageId"])
                print("created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Description : ", response_body["responseData"]["dataList"][0]["description"])

                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Filename : ", response_body["responseData"]["dataList"][0]["filename"])

                print("IsDiffImage : ", response_body["responseData"]["dataList"][0]["isDiffImage"])
                # print("IsBase : ", response_body["responseData"]["dataList"][0]["isBase"])
                # print("IsFullImage : ", response_body["responseData"]["dataList"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["dataList"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["dataList"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["dataList"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the package details successfully",
                           "Successfully fetched the values/data for package ")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the package details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
                # self.result.set_result(TestResults.failed)
                assert False
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the package details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_invalidapikey(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_emptyapikey(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_noapikey(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_emptyxrequestor(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            #print("API response status code is :", response.status_code)
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_noxrequestor(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # pageNo less than 0
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_pageno_lessthanzero(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages_pageNo_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "-1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15047) and response_body["responseData"][
            "message"] == "Page number must not be less than one":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # invalid pageNo like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_invalid_pageno(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages_invalid_pageNo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "xy"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["error"] == str(15084) and response_body[
            "message"] == "Unable to find mandatory input parameter":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # pageSize lessthan zero
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_pagesize_lessthanzero(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages_pageSize_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "-1"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "valid")
        # Validate response status code
        if response.status_code == 400:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15048) and response_body["responseData"][
            "message"] == "Page size must not be less than one":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # invalid pageSize like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getAllPackages_invalid_pageSize(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages_invalid_pageSize")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "1@"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 400:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["error"] == str(15084) and response_body[
            "message"] == "Unable to find mandatory input parameter":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams
    @pytest.mark.Smoke
    def test1_Positive_sota_getAllPackages_without_queryparams(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"
        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "removeQueryParams_from_url")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Id : ", response_body["responseData"]["dataList"][0]["packageId"])
                print("created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Description : ", response_body["responseData"]["dataList"][0]["description"])

                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Filename : ", response_body["responseData"]["dataList"][0]["filename"])

                print("IsDiffImage : ", response_body["responseData"]["dataList"][0]["isDiffImage"])
                # print("IsBase : ", response_body["responseData"]["dataList"][0]["isBase"])
                # print("IsFullImage : ", response_body["responseData"]["dataList"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["dataList"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["dataList"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["dataList"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the package details successfully",
                           "Successfully fetched the values/data for package ")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the package details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
                # self.result.set_result(TestResults.failed)
                assert False
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the package details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams
    @pytest.mark.Smoke
    def test1_Positive_sota_getAllPackages_with_queryparams_status(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "queryParams_status")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Id : ", response_body["responseData"]["dataList"][0]["packageId"])
                print("created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Description : ", response_body["responseData"]["dataList"][0]["description"])

                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Filename : ", response_body["responseData"]["dataList"][0]["filename"])

                print("IsDiffImage : ", response_body["responseData"]["dataList"][0]["isDiffImage"])
                # print("IsBase : ", response_body["responseData"]["dataList"][0]["isBase"])
                # print("IsFullImage : ", response_body["responseData"]["dataList"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["dataList"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["dataList"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["dataList"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the package details successfully",
                           "Successfully fetched the values/data for package ")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the package details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
                # self.result.set_result(TestResults.failed)
                assert False
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the package details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams
    @pytest.mark.Smoke
    def test1_Positive_sota_getAllPackages_with_queryparams_model(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListPackages")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

        # call api reusable module
        response = SOTA_ListPackages(self, pageNo, pageSize, "queryParams_model")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Id : ", response_body["responseData"]["dataList"][0]["packageId"])
                print("created Time : ", response_body["responseData"]["dataList"][0]["createdTime"])
                print("Model : ", response_body["responseData"]["dataList"][0]["model"])
                print("Status : ", response_body["responseData"]["dataList"][0]["status"])
                print("Description : ", response_body["responseData"]["dataList"][0]["description"])

                print("System : ", response_body["responseData"]["dataList"][0]["system"])
                print("Filename : ", response_body["responseData"]["dataList"][0]["filename"])

                print("IsDiffImage : ", response_body["responseData"]["dataList"][0]["isDiffImage"])
                # print("IsBase : ", response_body["responseData"]["dataList"][0]["isBase"])
                # print("IsFullImage : ", response_body["responseData"]["dataList"][0]["isFullImage"])
                print("DownloadConsent : ", response_body["responseData"]["dataList"][0]["downloadConsent"])
                print("InstallConsent : ", response_body["responseData"]["dataList"][0]["installConsent"])
                print("RebootConsent : ", response_body["responseData"]["dataList"][0]["rebootConsent"])
                testResult(self, "passed", "Should fetch all the package details successfully",
                           "Successfully fetched the values/data for package ")
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the package details successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
                # self.result.set_result(TestResults.failed)
                assert False
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the package details successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

