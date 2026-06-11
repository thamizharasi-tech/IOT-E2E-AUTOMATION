import pytest

from C2CModules.primary_IVI_device_modules import getVIN
from C2CModules.sota_api_modules import SOTA_getScriptModel, SOTA_VehicleOnboard
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # SOTA-GetScriptModel
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_sota_getScriptModel(self):

        model = "adp"
        name = "IVI"
        partNo = "test"
        sn = "Hii"
        vin = "VINQCOMIVI0006663"

        # call api reusable module
        response = SOTA_VehicleOnboard(self, model, name, partNo, sn, vin, "valid")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getScriptModel_invalid_apikey(self):
        # call api reusable module
        response = SOTA_getScriptModel(self, "invalid_apiKey")

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
    def test2_negative_sota_getScriptModel_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = SOTA_getScriptModel(self, "empty_apiKey")

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
    def test3_negative_sota_getScriptModel_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = SOTA_getScriptModel(self, "no_apiKey")

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
    def test4_negative_sota_getScriptModel_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # # pageNo = str(dict1["pageNo"])
            # # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # # pageNo = "1"
            # # pageSize = "10"

        # call api reusable module
        response = SOTA_getScriptModel(self, "empty_x-requestor")

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
    def test5_negative_sota_getScriptModel_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-GetScriptModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            # pageNo = str(dict1["pageNo"])
            # pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # pageNo = "1"
            # pageSize = "10"

        # call api reusable module
        response = SOTA_getScriptModel(self, "no_x-requestor")

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

