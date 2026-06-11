import pytest

from C2CModules.fota_api_modules import FOTA_getVersionDetails, FOTA_GetListOfModelsCount, \
    get_model_by_getListOfModelsCount_api
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # FOTA-getVersionDetails
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_fota_getVersionDetails(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api(self)

        # call api reusable module
        response = FOTA_getVersionDetails(self, model,"valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["data"]) >= 1:
                print("ECU : ", response_body["responseData"]["data"]["ecus"][0]["ecu"])
                print("Source Versions : ", response_body["responseData"]["data"]["ecus"][0]["srcVersions"][0])
                print("target Versions : ", response_body["responseData"]["data"]["ecus"][0]["targetVersions"][0])

                testResult(self, "passed", "Should fetch all the model source & target versions successfully",
                           "Successfully fetched the source & target versions for desired model ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch all the model source & target versions successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as pass")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch all the model source & target versions successfully",
                       "Failed to fetch source & target version list " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_getListOfModels_invalid_apikey(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api

        # call api reusable module
        response = FOTA_getVersionDetails(self, model, "invalid_apiKey")

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
    def test2_negative_fota_getListOfModels_empty_apikey(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api

        # call api reusable module
        response = FOTA_getVersionDetails(self, model, "empty_apiKey")

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
    def test3_negative_fota_getListOfModels_no_apikey(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api

        # call api reusable module
        response = FOTA_getVersionDetails(self, model, "no_apiKey")

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
    def test4_negative_fota_getListOfModels_empty_xrequestor(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api

        # call api reusable module
        response = FOTA_getVersionDetails(self, model, "empty_x-requestor")

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
    def test5_negative_fota_getListOfModels_no_xrequestor(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = get_model_by_getListOfModelsCount_api

        # call api reusable module
        response = FOTA_getVersionDetails(self, model,  "no_x-requestor")

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

    @pytest.mark.Smoke
    def test6_Positive_fota_getVersionDetails_invalid_model(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "adp$%$"

        # call api reusable module
        response = FOTA_getVersionDetails(self, model,"invalid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(14047) or response_body["responseCode"] == 14047 or response_body["responseData"]["message"] =="No firmware found for given model":

                testResult(self, "passed", "Should throw proper error message for invalid model name",
                           "Showing proper error message for invalid model name")

        elif response_body["responseCode"] != 14047:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should throw proper error message for invalid model name",
                       "Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7_Positive_fota_getVersionDetails_empty_model(self):

        # read api data from excel sheet
        global model
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-getVersionDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = ""

        # call api reusable module
        response = FOTA_getVersionDetails(self, model,"invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(14001) or response_body["responseCode"] == 14001 or response_body["responseData"]["message"] =="model is not allowed to be empty":

                testResult(self, "passed", "Should throw proper error message for empty model name",
                           "Showing proper error message for empty model name")

        elif response_body["responseCode"] != 14001:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should throw proper error message for empty model name",
                       "Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")
