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

class Test_CreateFactoryConf_API:

    def test_positive_factory_conf_save_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be saved successfully for the given model.",
                           "Factory Conf - Vehicle configuration is saved successfully for this model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0]["message"] == "Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be saved successfully for this model.",
                           "Factory Conf - Vehicle configuration already exists for this model.")
                assert True

        else:
            print("Error: Unable to save vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_factory_conf_save_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "telemetry_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be saved successfully for the given model.",
                           "Factory Conf - Telemetry configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0]["message"] == "Mode Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be saved successfully for the given model.",
                           "Factory Conf - Telemetry configuration already exists for the given model.")
                assert True
        else:
            print(
                "Error: Unable to save factory telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_save_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "command_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be saved successfully for the given model.",
                           "Factory Conf - Command configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0]["message"] == "Mode Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be saved successfully for the given model.",
                           "Factory Conf - Command configuration already exists for the given model.")
                assert True
        else:
            print(
                "Error: Unable to save factory command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_save_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, model, version, "alert_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be saved successfully for the given model.",
                           "Factory Conf - Alert configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0]["message"] == "Mode Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be saved successfully for the given model.",
                           "Factory Conf - Alert configuration already exists for the given model.")
                assert True

        else:
            print("Error: Unable to save factory alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_CreateFactoryConf_API_Negative:

    @pytest.mark.Smoke
    def test1a_negative_vehicleConfigurations_createFactoryConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")


        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for invalid apikey.",
                   "Create Factory Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1b_negative_vehicleConfigurations_createFactoryConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")


        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for empty apikey.",
                   "Create Factory Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1c_negative_vehicleConfigurations_createFactoryConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for no apikey.",
                   "Create Factory Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1d_negative_vehicleConfigurations_createFactoryConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for empty x-requestor.",
                   "Create Factory Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1e_negative_vehicleConfigurations_createFactoryConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for no x-requestor.",
                   "Create Factory Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1f_negative_vehicleConfigurations_createFactoryConfiguration_invalid_version(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "xyz"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        if response_body["errors"][0]["errorCode"] == "16038" and response_body["errors"][0]["message"] == "Invalid version":
            testResult(self, "passed",
                   "Create Factory Configuration API should throw appropriate error message for invalid version",
                   "Create Factory Configuration API showing/throwing appropriate error message for invalid version")
        else:
            testResult(self, "failed",
                       "Create Factory Configuration API should throw appropriate error message for invalid version",
                       "Create Factory Configuration API is not showing/throwing appropriate error message for invalid version")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1g_negative_vehicleConfigurations_createFactoryConfiguration_empty_version(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = ""
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 404:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1h_negative_vehicleConfigurations_createFactoryConfiguration_invalid_content_type(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "invalid_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1i_negative_vehicleConfigurations_createFactoryConfiguration_empty_content_type(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "abc"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "empty_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1j_negative_vehicleConfigurations_createFactoryConfiguration_empty_conf(self):
        print("----------------------------------------------------------")

        model = "model" + ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
        version = "3.0"
        RegionalAPNEndpoints = "xyz"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
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

    @pytest.mark.Smoke
    def test1k_negative_vehicleConfigurations_createFactoryConfiguration_invalid_model(self):
        print("----------------------------------------------------------")

        model = "@@@"
        version = "3.0"
        RegionalAPNEndpoints = "xyz"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into json
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16037" and response_body["errors"][0][
            "message"] == "Invalid model":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1l_negative_vehicleConfigurations_createFactoryConfiguration_empty_model(self):
        print("----------------------------------------------------------")

        model = ""
        version = "3.0"
        RegionalAPNEndpoints = "xyz"

        print("model: ", model)
        print("version: ", version)
        print("RegionalAPNEndpoints: ", RegionalAPNEndpoints)

        # Verify command & control response
        response = vehicleConfigurations_createFactoryConfigurationForModel(self, model, version, RegionalAPNEndpoints,
                                                                            "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")