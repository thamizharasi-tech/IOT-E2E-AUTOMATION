import pytest

from C2CModules.fota_api_modules import FOTA_getScriptModel
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # FOTA-GetScriptModel
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_fota_getScriptModel(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "valid")

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
                if len(response_body["responseData"]["data"][0]["scripts"]) >= 1:
                    print("RefId :", response_body["responseData"]["data"][0]["scripts"][0]["refId"])
                    print("Name :", response_body["responseData"]["data"][0]["scripts"][0]["name"])
                    print("Status :", response_body["responseData"]["data"][0]["scripts"][0]["status"])

                testResult(self, "passed", "Should fetch all the scripts of firmware modules successfully",
                           "Successfully fetched scripts of the modules for firmware ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the scripts of firmware modules successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the scripts of firmware modules successfully ",
                       "Failed to fetch module script list " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getScriptModel_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "invalid_apiKey")

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
    def test2_negative_fota_getScriptModel_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "empty_apiKey")

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
    def test3_negative_fota_getScriptModel_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "no_apiKey")

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
    def test4_negative_fota_getScriptModel_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "empty_x-requestor")

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
    def test5_negative_fota_getScriptModel_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # pageNo = str(dict1["pageNo"])
            # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # pageNo = "1"
            # pageSize = "10"

        # call api reusable module
        response = FOTA_getScriptModel(self, "no_x-requestor")

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

