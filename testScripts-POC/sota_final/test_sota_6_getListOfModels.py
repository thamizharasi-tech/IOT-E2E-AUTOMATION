import pytest

from C2CModules.sota_api_modules import SOTA_ListModels1
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # sota-GetListOfModels&Count
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_sota_getListOfModelsCount(self):
        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_ListModels1(self, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Module : ", response_body["responseData"]["dataList"][0])

                testResult(self, "passed", "Should fetch all the sota-package modules successfully",
                           "Successfully fetched the modules for sota-package ")
                # self.result.set_result(TestResults.passed)
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the sota-package modules successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the sota-package modules successfully ",
                       "Failed to fetch module list " + " Reason for failure is : " +
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
    def test1_negative_sota_getListOfModels_invalid_apikey(self):
        print("----------------------------------------------------------")

        # call api reusable module
        response = response = SOTA_ListModels1(self, "invalid_apiKey")

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
    def test2_negative_sota_getListOfModels_empty_apikey(self):
        print("----------------------------------------------------------")

        # call api reusable module
        response = response = SOTA_ListModels1(self, "empty_apiKey")

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

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getListOfModels_no_apikey(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = response = SOTA_ListModels1(self, "no_apiKey")

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
    def test1_negative_sota_getListOfModels_empty_xrequestor(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = response = SOTA_ListModels1(self, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "x-requestor header cannot be blank" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank":
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

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getListOfModels_no_xrequestor(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = response = SOTA_ListModels1(self, "no_x-requestor")

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