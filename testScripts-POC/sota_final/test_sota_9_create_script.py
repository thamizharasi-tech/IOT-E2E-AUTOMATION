import time

import pytest
import random
from C2CModules.sota_api_modules import SOTA_CreateScript, get_preCondition_from_preconditionDetails_api, \
    get_verisons_from_versionDetails_api, get_model_by_getListOfModelsCount_api
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


# ---------------------------------------------------------
# SOTA-create script negative test scripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_sota_create_script(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15000):
            if response_body["responseData"]['message'] == "Success":
                scriptId = response_body["responseData"]['scriptId']
                print("Script Id : ", scriptId)
                testResult(self, "passed", "Script should be created successfully ",
                           "Script is created successfully")
                # self.result.set_result(TestResults.passed)
                assert True

        elif response_body["responseCode"] != str(15000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Script should be created successfully",
                       "Script is not created successfully   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------------------
    # sota-create script API : Negative Testcases
    # ---------------------------------------------------------------------------------------


class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "invalid_apiKey")

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
    def test2_negative_sota_create_script_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_sota_create_script_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_sota_create_script_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_sota_create_script_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid model-contain special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            model = "adp%"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15014)
        assert response_body["responseData"]["message"] == "model contains special characters"
        print("----------------------------------------------------------")

    # invalid model
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_incorrect_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            model = "mod123"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15045)
        assert response_body["responseData"]["message"] == "package does not exist"
        print("----------------------------------------------------------")

    # invalid name-contain special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_name(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "@%SOTA_ " + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15068)
        assert response_body["responseData"]["message"] == "Script name contains special characters"
        print("----------------------------------------------------------")

    # invalid precondition
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_precondition(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = "engine#"
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15062)
        assert response_body["responseData"]["message"] == "Invalid preconditions present in the request"
        print("----------------------------------------------------------")

    # invalid releasenotes-contain special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_releaseNotes(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_releasenotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "@@@ create Script via api $$$"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15000)
        assert response_body["responseData"]["message"] == "Success"
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_command(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL#$"
            scriptName = "SOTA_" + "INSTALL" + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "@@@ create Script via api $$$"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15071)
        assert response_body["responseData"]["message"] == "Command contains special character"
        print("----------------------------------------------------------")

    # invalid ecu-contain special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_ecu_splChar(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_ecu")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI@1"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14050)
        assert response_body["responseData"]["message"] == "Ecu contains special characters"
        print("----------------------------------------------------------")

    # invalid ecu-without special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_ecu(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI1"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14024)
        assert response_body["responseData"]["message"] == "No sota package available"
        print("----------------------------------------------------------")

    # invalid appVersion-contain special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_appName(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_appName")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            appName = "$%^&&"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15045)
        assert response_body["responseData"]["message"] == "package does not exist"
        print("----------------------------------------------------------")

    # invalid appVersion-without special char
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_invalid_appVersion(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_appVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            appVersion = "111111"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15045)
        assert response_body["responseData"]["message"] == "package does not exist"
        print("----------------------------------------------------------")

        # invalid appVersion-contain special char
        @pytest.mark.Smoke
        def test1_negative_sota_create_script_invalid_appName(self):
            # read api data from excel sheet
            dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript_invalid_appName")
            if dict1['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                model = str(dict1["model"])
                random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
                command = str(dict1["command"])
                scriptName = "SOTA_" + command + "_" + random_id
                system = str(dict["ecuType"])
                appName = str(dict1["packageName"])
                precondition = str(dict1["preconditions-1"])
                appVersion = str(dict1["packageVersion"])
                releaseNote = str(dict1["releaseNote"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual data :")
                model = get_model_by_getListOfModelsCount_api(self)
                random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
                command = "INSTALL"
                scriptName = "SOTA_" + command + "_" + random_id
                system = "IVI"
                precondition = get_preCondition_from_preconditionDetails_api(self)
                appName, appVersion = get_verisons_from_versionDetails_api(self, model)
                releaseNote = "create Script via api"
                appName = "$%^&&"

            # Call api reusable model
            response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]),
                                         releaseNote,
                                         precondition, "invalid")

            # Validate response status code
            if response.status_code == 400:
                assert True
            else:
                print("Status code is not 400. Rather found : " + str(response.status_code))
                assert False
            # Parse API response into JSON
            response_body = response.json()
            assert response_body["responseCode"] == str(15045)
            assert response_body["responseData"]["message"] == "package does not exist"
            print("----------------------------------------------------------")

    # empty model
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            model = ""

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15009)
        assert response_body["responseData"]["message"] == "model cannot be null or empty"
        print("----------------------------------------------------------")


    # empty model
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_command(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = ""
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = ""
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"


        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15070)
        assert response_body["responseData"]["message"] == "Command cannot be empty"
        print("----------------------------------------------------------")


    # empty name
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_name(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = ""
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = ""
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15067)
        assert response_body["responseData"]["message"] == "Script name cannot be empty"
        print("----------------------------------------------------------")

    # empty precondition
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_precondition(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = ""
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = ""
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15062)
        assert response_body["responseData"]["message"] == "Invalid preconditions present in the request"
        print("----------------------------------------------------------")

    # empty releasenotes
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_releaseNotes(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = ""

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15030)
        assert response_body["responseData"]["message"] == "notes cannot be empty"
        print("----------------------------------------------------------")

    # empty ecu
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_ecu(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = ""
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = ""
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15029)
        assert response_body["responseData"]["message"] == "system cannot be empty"
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_appName(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = ""
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            appName = ""

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15072)
        assert response_body["responseData"]["message"] == "app_name cannot be empty"
        print("----------------------------------------------------------")

    # empty sourceVersion
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_empty_appVersion(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = ""
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            appVersion = ""

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion), releaseNote,
                                     precondition, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15073)
        assert response_body["responseData"]["message"] == "target version cannot be empty"
        print("----------------------------------------------------------")

    # without model
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_without_model(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_model")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15009)
        assert response_body["responseData"]["message"] == "model cannot be null or empty"
        print("----------------------------------------------------------")

    # without name
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_without_name(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "no_scriptName")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15067)
        assert response_body["responseData"]["message"] == "Script name cannot be empty"
        print("----------------------------------------------------------")

    # without precondition
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_without_precondition(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_preconditions")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15069)
        assert response_body["responseData"]["message"] == "Precondition cannot be empty"
        print("----------------------------------------------------------")

    # without releasenotes
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_without_releaseNotes(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_notes")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15030)
        assert response_body["responseData"]["message"] == "notes cannot be empty"
        print("----------------------------------------------------------")

    # without ecu
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_without_ecu(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_system")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15029)
        assert response_body["responseData"]["message"] == "system cannot be empty"
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test1_negative_sota_create_script_no_appName(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition, "no_appName")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15072)
        assert response_body["responseData"]["message"] == "app_name cannot be empty"
        print("----------------------------------------------------------")

    # no sourceVersion
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_no_appVersion(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_targetVersion")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15073)
        assert response_body["responseData"]["message"] == "target version cannot be empty"
        print("----------------------------------------------------------")

    # no sourceVersion
    @pytest.mark.Smoke
    def test1_negative_sota_create_script_no_command(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,"no_command")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(15070)
        assert response_body["responseData"]["message"] == "Command cannot be empty"
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_negative_sota_create_script_duplicate(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-CreateScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "SOTA_" + command + "_" + random_id
            system = str(dict1["ecuType"])
            appName = str(dict1["packageName"])
            precondition = str(dict1["preconditions-1"])
            appVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "SOTA_" + command + "_" + random_id
            system = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            appName, appVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"

        # Call api reusable model
        response1 = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "valid")

        print("response1 : ", response1.text)
        time.sleep(5)
        response = SOTA_CreateScript(self, model, system, scriptName, command, appName, str(appVersion[0]), releaseNote,
                                     precondition,
                                     "valid")
        print("response2 : ", response.text)

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body1 = response1.json()
        response_body = response.json()

        if response_body["responseCode"] == str(15000):
            if response_body["responseData"]['message'] == "Success":
                scriptId1 = response_body1["responseData"]['scriptId']
                scriptId = response_body["responseData"]['scriptId']
                print("Script Id : ", scriptId)
                if scriptId1 == scriptId:
                    testResult(self, "passed", "Only one script Id should be generated/created, for same script name for same model",
                               "Only one script Id is created, for same script name for same model")
                    # self.result.set_result(TestResults.passed)
                    assert True
                else:
                    testResult(self, "passed", "Only one script Id should be generated/created, for same script name for same model",
                               "Script is not created or created more than once")
                    # self.result.set_result(TestResults.failed)
                    assert False

        elif response_body["responseCode"] != str(15000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Script should be created successfully",
                       "Script is not created successfully   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")