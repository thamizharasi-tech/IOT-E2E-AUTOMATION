import pytest

from C2CModules.fota_api_modules import FOTA_scriptReleaseNoteUpdate, FOTA_GetAllScriptDetails
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # FOTA_PATCH: scriptReleaseNoteUpdate
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_fota_scriptReleaseNoteUpdate(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize ="10"

            # call api reusable module
            response = FOTA_GetAllScriptDetails(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
                message = response_body["responseData"]["message"]
                print('Message : ', message)
                if len(response_body["responseData"]["data"]) >= 1:
                    scriptId = response_body["responseData"]["data"][0]["refId"]
                    print("Script Id : ", scriptId)

            releaseNote = "test123"

        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            testResult(self, "passed", "Should update script releaseNote successfully",
                       "Successfully updated script releaseNote")
        elif response_body["responseCode"] != 14000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should update script releaseNote successfully",
                       "Failed to update script releaseNote" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_scriptReleaseNoteUpdate_invalidapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "invalid_apiKey")
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
    def test1_negative_fota_scriptReleaseNoteUpdate_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "empty_apiKey")
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
    def test1_negative_fota_scriptReleaseNoteUpdate_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "no_apiKey")
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
    def test1_negative_fota_scriptReleaseNoteUpdate_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_scriptReleaseNoteUpdate_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # invalid scriptId
    @pytest.mark.Smoke
    def test1_negative_fota_scriptReleaseNoteUpdate_invalid_scriptId(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate_invalid_scriptId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "xyz"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14046):
            assert response_body["responseData"]["message"] == "No records found"

        print("----------------------------------------------------------")

    # invalid releaseNote-contain special char

    @pytest.mark.Smoke
    def test1_negative_fota_scriptReleaseNoteUpdate_invalid_releaseNote(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate_invalid_releaseNote")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = FOTA_GetAllScriptDetails(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
                message = response_body["responseData"]["message"]
                print('Message : ', message)
                if len(response_body["responseData"]["data"]) >= 1:
                    scriptId = response_body["responseData"]["data"][0]["refId"]
                    print("Script Id : ", scriptId)

            releaseNote = "aaaa@"

        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14060):
            assert response_body["responseData"]["message"] == "release-note contains special character"

        print("----------------------------------------------------------")

    # empty release-note
    @pytest.mark.Smoke
    def test1_negative_fota_scriptReleaseNoteUpdate_empty_releaseNote(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate_empty_releaseNote")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
            if releaseNote == "None":
                releaseNote = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = ""
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, temp)
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
    def test1_negative_fota_scriptReleaseNoteUpdate_without_releaseNote(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-PATCH-scriptReleaseNoteUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            releaseNote = "test123"
        # call api reusable module
        response = FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, "no_releaseNote")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(14013):
            assert response_body["responseData"]["message"] == "release-note is not allowed to be empty"
