import pytest

from C2CModules.fota_api_modules import FOTA_firmwareDescriptionUpdate, get_firmId_from_firmwareDetails_api
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # FOTA_PATCH: firmware desc update
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_FOTA_firmwareDescriptionUpdate(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            testResult(self, "passed", "Should update firmware description successfully",
                       "Successfully updated firmware description")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should update firmware description successfully",
                       "Failed to update firmware description" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_firmwareDescriptionUpdate_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_fota_firmwareDescriptionUpdate_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_fota_firmwareDescriptionUpdate_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_fota_firmwareDescriptionUpdate_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_fota_firmwareDescriptionUpdate_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # invalid firmId
    @pytest.mark.Smoke
    def test6_negative_fota_firmwareDescriptionUpdate_invalid_firmId(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription_invalid_firmId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = "xyz"
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["Response Code"] == str(14122):
            assert response_body["Response Message"] == "Input parameter is invalid"

        print("----------------------------------------------------------")

    # invalid description-contain special char

    @pytest.mark.Smoke
    def test7_negative_fota_firmwareDescriptionUpdate_invalid_description(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription_invalid_description")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api ^%&&**"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(14060) or response_body["responseData"]["message"] == "description contains special character":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # empty release-note
    @pytest.mark.Smoke
    def test8_negative_fota_firmwareDescriptionUpdate_empty_description(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = ""
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14013):
            assert response_body["responseData"]["message"] == "release-note is not allowed to be empty"

        print("----------------------------------------------------------")

    # without release-note
    @pytest.mark.Smoke
    def test9_negative_fota_firmwareDescriptionUpdate_without_description(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-firmwareDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            firmId = get_firmId_from_firmwareDetails_api(self)
            description = "firmware description update through patch api"
        # call api reusable module
        response = FOTA_firmwareDescriptionUpdate(self, firmId, description, "no_description")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14013):
            assert response_body["responseData"]["message"] == "release-note is not allowed to be empty"
