import pytest
import random
from C2CModules.fota_api_modules import FOTA_createScript, get_preCondition_from_preconditionDetails_api, \
    get_verisons_from_versionDetails_api, get_model_by_getListOfModelsCount_api
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


# ---------------------------------------------------------
# FOTA-create script negative testscripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_create_script(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)
        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(14000):
            if response_body["responseData"]['message'] == "Success":
                scriptId = response_body["responseData"]['scriptId']
                testResult(self, "passed", "Script should be created ",
                           "Script is created successfully")

        elif response_body["responseCode"] != str(14000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Script should be created",
                       "Script is not created successfully   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------------------
    # FOTA-create script API : Negative Testcases
    # ---------------------------------------------------------------------------------------


class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalidapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "invalid_apiKey")

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
    def test2_negative_fota_create_script_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "empty_apiKey")

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
    def test3_negative_fota_create_script_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_apiKey")

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
    def test4_negative_fota_create_script_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "empty_x-requestor")

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
    def test5_negative_fota_create_script_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_x-requestor")

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
    def test1_negative_fota_create_script_invalid_model(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"
            model = "mod123%^"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14049)
        assert response_body["responseData"]["message"] == "Model contains specials characters"
        print("----------------------------------------------------------")

    # invalid model
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_model(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"
            model = "mod123"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14024)
        assert response_body["responseData"]["message"] == "No firmware package available"
        print("----------------------------------------------------------")

    # invalid name-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_name(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = str(dict1["Script name"])

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA#$%_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14059)
        assert response_body["responseData"]["message"] == "Name contains special character"
        print("----------------------------------------------------------")

    # invalid precondition
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_precondition(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_precondition")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = "engine1#$"
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14091)
        assert response_body["responseData"]["message"] == "Invalid preconditions present in the request"
        print("----------------------------------------------------------")

    # invalid releasenotes-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_releasenotes(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_releasenotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api %&%"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14060)
        assert response_body["responseData"]["message"] == "release-note contains special character"
        print("----------------------------------------------------------")

    # invalid ecu-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_ecu(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_ecu")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI@"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

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
    def test1_negative_fota_create_script_invalid_ecu(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_ecu")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI1"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14024)
        assert response_body["responseData"]["message"] == "No firmware package available"
        print("----------------------------------------------------------")

    # invalid sourceVersion-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_sourceVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_sourceVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            sourceVersion = "11$"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14063)
        assert response_body["responseData"]["message"] == "source-version contains special characters"
        print("----------------------------------------------------------")

    # invalid sourceVersion-without special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_sourceVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_sourceVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            sourceVersion = "11ad"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14024)
        assert response_body["responseData"]["message"] == "No firmware package available"
        print("----------------------------------------------------------")

    # invalid targetVersion-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_targetVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_targetVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "11$"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14064)
        assert response_body["responseData"]["message"] == "target-version contains special characters"
        print("----------------------------------------------------------")

    # invalid targetVersion- without special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_invalid_targetVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_invalid_targetVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "11sd"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14024)
        assert response_body["responseData"]["message"] == "No firmware package available"
        print("----------------------------------------------------------")

    # empty model
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_model(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = str(dict1["ecuType"])
            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"
            model = ""

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14001)
        assert response_body["responseData"]["message"] == "model is not allowed to be empty"
        print("----------------------------------------------------------")

    # empty name
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_name(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = str(dict1["Script name"])
            if scriptName == "None":
                scriptName = ""
            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = ""
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14058)
        assert response_body["responseData"]["message"] == "Name cannot be empty"
        print("----------------------------------------------------------")

    # empty precondition
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_precondition(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_precondition")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            if precondition == "None":
                precondition = ""
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = ""
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14091)
        assert response_body["responseData"]["message"] == "Invalid preconditions present in the request"
        print("----------------------------------------------------------")

    # empty releasenotes
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_releasenotes(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_releasenotes")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = str(dict1["ecuType"])
            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = ""
            targetVersion = "111"
        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14013)
        assert response_body["responseData"]["message"] == "release-note is not allowed to be empty"
        print("----------------------------------------------------------")

    # empty ecu
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_ecu(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_ecu")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = ""
            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = ""
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14003)
        assert response_body["responseData"]["message"] == "ecu is not allowed to be empty"
        print("----------------------------------------------------------")

    # empty sourceVersion
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_sourceVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_sourceVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = ""
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            sourceVersion = ""

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14015)
        assert response_body["responseData"]["message"] == "source-version is not allowed to be empty"
        print("----------------------------------------------------------")

    # empty targetVersion
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_empty_targetVersion(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript_empty_targetVersion")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = ""
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = ""

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, temp)

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14016)
        assert response_body["responseData"]["message"] == "target-version is not allowed to be empty"
        print("----------------------------------------------------------")

    # without model
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_model(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_model")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14001)
        assert response_body["responseData"]["message"] == "model is not allowed to be empty"
        print("----------------------------------------------------------")

    # without name
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_name(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = str(dict1["Script name"])
            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_name")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14058)
        assert response_body["responseData"]["message"] == "Name cannot be empty"
        print("----------------------------------------------------------")

    # without precondition
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_precondition(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])

            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_precondition")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14062)
        assert response_body["responseData"]["message"] == "Precondition cannot be null"
        print("----------------------------------------------------------")

    # without releasenotes
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_releasenotes(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_releaseNote")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14013)
        assert response_body["responseData"]["message"] == "release-note is not allowed to be empty"
        print("----------------------------------------------------------")

    # without ecu
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_ecu(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])
            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_ecu")


        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14003)
        assert response_body["responseData"]["message"] == "ecu is not allowed to be empty"
        print("----------------------------------------------------------")

    # no sourceVersion
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_no_sourceVersion(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            if sourceVersion == "None":
                sourceVersion = ""
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])
            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_sourceVersion")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14015)
        assert response_body["responseData"]["message"] == "source-version is not allowed to be empty"
        print("----------------------------------------------------------")

    # without targetVersion
    @pytest.mark.Smoke
    def test1_negative_fota_create_script_without_targetVersion(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createScript")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = str(dict1["command"])
            scriptName = "FOTA_" + command + "_" + random_id

            ecu_type = str(dict1["ecuType"])

            sourceVersion = str(dict1["sourceVersion"])
            precondition = str(dict1["preconditions-1"])
            targetVersion = str(dict1["packageVersion"])

            releaseNote = str(dict1["releaseNote"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual data :")
            model = get_model_by_getListOfModelsCount_api(self)
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(4) for _ in range(1)])
            command = "INSTALL"
            scriptName = "FOTA_" + command + "_" + random_id
            ecu_type = "IVI"
            precondition = get_preCondition_from_preconditionDetails_api(self)
            sourceVersion, targetVersion = get_verisons_from_versionDetails_api(self, model)
            releaseNote = "create Script via api"
            targetVersion = "111"

        # Call api reusable model
        response = FOTA_createScript(self, model, scriptName, precondition, ecu_type, sourceVersion, targetVersion,
                                     releaseNote, "no_targetVersion")

        # Validate response status code
        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == str(14016)
        assert response_body["responseData"]["message"] == "target-version is not allowed to be empty"
        print("----------------------------------------------------------")
