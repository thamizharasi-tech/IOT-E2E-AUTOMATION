import pytest

from C2CModules.sota_api_modules import SOTA_GetPreconditions
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # Sota-getPrecondition
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_positive_sota_getPrecondition(self):
        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("Id : ", response_body["responseData"]["dataList"][0]["id"])
                print("Precondition : ", response_body["responseData"]["dataList"][0]["precondition"])
                print("Description : ", response_body["responseData"]["dataList"][0]["description"])

                testResult(self, "passed", "Should fetch all the SOTA package preconditions successfully",
                           "Successfully fetched the preconditions for SOTA package ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the SOTA package preconditions successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the SOTA package preconditions successfully ",
                       "Failed to fetch preconditions list " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")


class Test_negative:

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getListOfModels_invalid_apikey(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "invalid_apiKey")

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
    def test2_negative_sota_getListOfModels_empty_apikey(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "empty_apiKey")

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

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_sota_getListOfModels_no_apikey(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "no_apiKey")

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

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_sota_getListOfModels_empty_xrequestor(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "x-requestor header cannot be blank" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_sota_getListOfModels_no_xrequestor(self):

        print("----------------------------------------------------------")

        # call api reusable module
        response = SOTA_GetPreconditions(self, "no_x-requestor")

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
