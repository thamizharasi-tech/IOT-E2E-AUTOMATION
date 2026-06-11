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

class Test_vehConf_delete_masterConf_API:

    def test_positive_master_conf_delete_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be deleted successfully for this model.",
                           "Master Conf - Vehicle configuration is deleted successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to delete vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_delete_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, model, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be deleted successfully for the given model.",
                           "Master Conf - Telemetry configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_delete_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, model, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be deleted successfully for the given model.",
                           "Master Conf - Command configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_delete_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, model, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be deleted successfully for the given model.",
                           "Master Conf - Alert configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_DeleteMasterConfig_Negative:

    @pytest.mark.Smoke
    def test8a_negative_vehicleConfigurations_deleteMasterConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                       "Delete Master Configuration API should throw appropriate error message for invalid apikey.",
                       "Delete Master Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8b_negative_vehicleConfigurations_deleteMasterConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                       "Delete Master Configuration API should throw appropriate error message for empty apikey.",
                       "Delete Master Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8c_negative_vehicleConfigurations_deleteMasterConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                       "Delete Master Configuration API should throw appropriate error message for no apikey.",
                       "Delete Master Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8d_negative_vehicleConfigurations_deleteMasterConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                       "Delete Master Configuration API should throw appropriate error message for empty xrequestor.",
                       "Delete Master Configuration API showing/throwing appropriate error message for empty xrequestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8e_negative_vehicleConfigurations_deleteMasterConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                       "Delete Master Configuration API should throw appropriate error message for no xrequestor.",
                       "Delete Master Configuration API showing/throwing appropriate error message for no xrequestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8f_negative_vehicleConfigurations_deleteMasterConfiguration_invalid_model(self):
        print("----------------------------------------------------------")

        model = "Mo123del"

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16001" and response_body["errors"][0]["message"] == "Master Config does not exist for this model":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8g_negative_vehicleConfigurations_deleteMasterConfiguration_empty_model(self):
        print("----------------------------------------------------------")

        model = ""

        print("model: ", model)

        # Verify command & control response
        response = vehicleConfigurations_deleteMasterConfigurationForModel(self, model, "valid")

        if response.status_code == 404:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")
