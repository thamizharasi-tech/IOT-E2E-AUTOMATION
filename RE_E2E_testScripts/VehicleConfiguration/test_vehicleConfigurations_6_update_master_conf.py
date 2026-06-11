import pytest
import random
import json
import time

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult
from C2CModules.api_modules import verify_api_response_for_invalid_header


OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
global model, version, RegionalAPNEndpoints

class Test_vehConf_update_masterConf_API:

    def test_positive_master_conf_update_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be updated successfully for this model.",
                           "Master Conf - Vehicle configuration is updated successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_update_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be updated successfully for the given model.",
                           "Master Conf - Telemetry configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_update_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be updated successfully for the given model.",
                           "Master Conf - Command configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_update_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be updated successfully for the given model.",
                           "Master Conf - Alert configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_UpdateMasterConfig_Negative:

    @pytest.mark.Smoke
    def test6a_negative_vehicleConfigurations_updateMasterConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Update Master Configuration API should throw appropriate error message for invalid api-key.",
                   "Update Master Configuration API showing/throwing appropriate error message for invalid api-key.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6b_negative_vehicleConfigurations_updateMasterConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Update Master Configuration API should throw appropriate error message for empty api-key.",
                   "Update Master Configuration API showing/throwing appropriate error message for empty api-key.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6c_negative_vehicleConfigurations_updateMasterConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Update Master Configuration API should throw appropriate error message for no api-key.",
                   "Update Master Configuration API showing/throwing appropriate error message for no api-key.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6d_negative_vehicleConfigurations_updateMasterConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Update Master Configuration API should throw appropriate error message for empty x-requestor.",
                   "Update Master Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6e_negative_vehicleConfigurations_updateMasterConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Update Master Configuration API should throw appropriate error message for no x-requestor.",
                   "Update Master Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6f_negative_vehicleConfigurations_updateMasterConfiguration_invalid_content_type(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                           "invalid_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6g_negative_vehicleConfigurations_updateMasterConfiguration_empty_content_type(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                           "empty_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6h_negative_vehicleConfigurations_updateMasterConfiguration_non_exist_model(self):
        print("----------------------------------------------------------")

        model = "Mo123del"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                           "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16001" and response_body["errors"][0]["message"] == "Master Config does not exist for this model":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6i_negative_vehicleConfigurations_updateMasterConfiguration_invalid_model(self):
        print("----------------------------------------------------------")

        model = "@@"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                           "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16037" and response_body["errors"][0][
            "message"] == "Invalid model":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6j_negative_vehicleConfigurations_updateMasterConfiguration_empty_configuration(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateMasterConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                           "empty_configuration")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16035" and response_body["errors"][0][
            "message"] == "Configuration field is empty":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")
