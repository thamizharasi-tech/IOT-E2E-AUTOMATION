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

#class Test_VehicleConfigurations:

class Test_vehConf_update_factoryConf_API:

    def test_positive_factory_conf_update_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_factory_conf_update_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be updated successfully for the given model.",
                           "Factory Conf - Telemetry configuration is updated successfully for the given model.")
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

    def test_positive_factory_conf_update_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be updated successfully for the given model.",
                           "Factory Conf - Command configuration is updated successfully for the given model.")
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

    def test_positive_factory_conf_update_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be updated successfully for the given model.",
                           "Factory Conf - Alert configuration is updated successfully for the given model.")
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

class Test_UpdateFactoryConfig_Negative:

    @pytest.mark.Smoke
    def test2a_negative_vehicleConfigurations_updateFactoryConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for invalid apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2b_negative_vehicleConfigurations_updateFactoryConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for empty apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2c_negative_vehicleConfigurations_updateFactoryConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for no apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2d_negative_vehicleConfigurations_updateFactoryConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for empty x-requestor.",
                   "Update Factory Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2e_negative_vehicleConfigurations_updateFactoryConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for no x-requestor.",
                   "Update Factory Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2f_negative_vehicleConfigurations_updateFactoryConfiguration_non_existing_model(self):
        print("----------------------------------------------------------")

        model = "mo123del"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        if response_body["errors"][0]["errorCode"] == "16003" and response_body["errors"][0]["message"] == "Factory Config does not exist for this model":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2g_negative_vehicleConfigurations_updateFactoryConfiguration_invalid_model(self):
        print("----------------------------------------------------------")

        model = "@@"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        if response_body["errors"][0]["errorCode"] == "16037" and response_body["errors"][0][
            "message"] == "Invalid model":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2g_negative_vehicleConfigurations_updateFactoryConfiguration_empty_model(self):
        print("----------------------------------------------------------")

        model = ""
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 404:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2h_negative_vehicleConfigurations_updateFactoryConfiguration_invalid_content_type(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "invalid_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2i_negative_vehicleConfigurations_updateFactoryConfiguration_empty_content_type(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "empty_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2j_negative_vehicleConfigurations_updateFactoryConfiguration_empty_configuration(self):
        print("----------------------------------------------------------")

        model = "Adp"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_updateFactoryConfigurationForModel(self, model, RegionalAPNEndpoints,
                                                                            "empty_configuration")

        if response.status_code == 400:
            assert True
        else:
            assert False

        #Parse API response into json
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16035" and response_body["errors"][0]["message"] == "Configuration field is empty":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

