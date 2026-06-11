import pytest

from C2CModules.sota_api_modules import SOTA_EditScriptNotes, SOTA_ListScripts
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

from C2CModules.testResults import testResult


class Test_smoke:

    # -----------------------------------------------------------------
    # SOTA_PATCH: scriptReleaseNoteUpdate
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_SOTA_EditScriptNotes(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize ="10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, temp)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            testResult(self, "passed", "Should update script release note successfully",
                       "Successfully updated script release note")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should update script release note successfully",
                       "Failed to update script release note" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_invalid_apikey(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "invalid_apiKey")
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
    def test1_negative_SOTA_EditScriptNotes_empty_apikey(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "empty_apiKey")
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
    def test1_negative_SOTA_EditScriptNotes_no_apikey(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "no_apiKey")
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
    def test1_negative_SOTA_EditScriptNotes_empty_xrequestor(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_no_xrequestor(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "no_x-requestor")
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
    def test1_negative_SOTA_EditScriptNotes_invalid_scriptId(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = "3a4832a9$%c0a9c0"
            releaseNote = "release notes updated"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, temp)

        # Validate response status code

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15035):
            assert response_body["responseData"]["message"] == "Script not found"
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid releaseNote-contain special char

    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_invalid_releaseNote(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = "@$#$@$@"
        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15000):
            assert response_body["responseData"]["message"] == "Success"
        else:
            assert False

        print("----------------------------------------------------------")

    # empty release-note
    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_empty_releaseNote(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = ""

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, temp)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15030):
            assert response_body["responseData"]["message"] == "notes cannot be empty"
        else:
            assert False

        print("----------------------------------------------------------")

    # without release-note
    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_without_releaseNote(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNo = "1"
            pageSize = "10"

            # call api reusable module
            response = SOTA_ListScripts(self, pageNo, pageSize, temp)

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response
            scriptId = "3a4832a9-59d4-40a9-8832-a959d4c0a9c0"
            if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
                # message = response_body["responseData"]["message"]
                # print('Message : ', message)
                if len(response_body["responseData"]["dataList"]) >= 1:
                    scriptId = response_body["responseData"]["dataList"][0]["scriptId"]
                    print("Script Id : ", scriptId)

            releaseNote = ""

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote,"no_releaseNote")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15030):
            assert response_body["responseData"]["message"] == "notes cannot be empty"
        else:
            assert False

    # without release-note
    @pytest.mark.Smoke
    def test1_negative_SOTA_EditScriptNotes_empty_scriptId(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-EditScriptNotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scriptId = ""
            releaseNote = "script update"

        # call api reusable module
        response = SOTA_EditScriptNotes(self, scriptId, releaseNote, "invalid")
        # Validate response status code
        assert (response.status_code == 405), "Status code is not 405. Rather found : " + str(
            response.status_code)

