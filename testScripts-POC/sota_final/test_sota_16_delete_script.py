import pytest

from C2CModules.sota_api_modules import get_ScriptId_from_ScriptDetails_api, \
    SOTA_DeleteScript
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


# ---------------------------------------------------------
# SOTA-delete script negative test scripts
# ---------------------------------------------------------


class Test_positive:

    @pytest.mark.Smoke
    def test1_positive_sota_delete_script(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id. : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15000):
            if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                "message"] == "Success":
                assert True
                testResult(self, "passed", "Script should be deleted/removed successfully",
                           "Script is deleted/removed successfully")

        elif response_body["responseCode"] != str(15000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Script should be deleted/removed successfully",
                       "Script is not deleted/removed successfully" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
        print("----------------------------------------------------------")


class Test_negative:
    # ---------------------------------------------------------------------------------------
    # SOTA-script delete API : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_delete_script_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "invalid_apiKey")

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
    def test1_negative_sota_delete_script_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "empty_apiKey")

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
    def test1_negative_sota_delete_script_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "no_apiKey")

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
    def test1_negative_sota_delete_script_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_delete_script_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid scriptId
    @pytest.mark.Smoke
    def test1_negative_sota_deletescript_invalid_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript_invalid_scriptId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = "scriptId$#123"

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(15035) or response_body["responseData"]["message"] == (
                "Script not found"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # scriptId doesnot exists
    @pytest.mark.Smoke
    def test1_negative_sota_deletescript_incorrect_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript_invalid_scriptId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = "876982734"
        else:
            scriptId = "0976123"

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(15035) or response_body["responseData"]["message"] == (
                "Script not found"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty scriptId
    @pytest.mark.Smoke
    def test1_negative_deletescript_empty_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = ""
        else:
            scriptId = ""

        print("Script Id : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "invalid")

        # Validate response status code
        if response.status_code == 405:
            assert True
        else:
            print("Status code is not 405. Rather found : " + str(response.status_code))
            assert False
        print("----------------------------------------------------------")
    # scriptId doesnot exists
    @pytest.mark.Smoke
    def test1_negative_sota_deletescript_alreadyDeletedScriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scriptId = str(dict1["scriptId"])
        else:
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("Script Id. : => ", scriptId)

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "valid")

        # Validate response status code
        if response.status_code == 200:
            # print("API response status code is :", str(response.status_code))
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            #self.result.set_result(TestResults.failed)
            assert False

        # Call api reusable model
        response = SOTA_DeleteScript(self, scriptId, "valid")

        # Validate response status code
        if response.status_code == 400:
            # print("API response status code is :", str(response.status_code))
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(15035) or response_body["responseData"]["message"] == (
                "Script not found"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")
