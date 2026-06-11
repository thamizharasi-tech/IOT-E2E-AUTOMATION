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

class Test_vehConf_get_MasterConf_API:

    def test_positive_master_conf_get_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, model, version, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be fetched successfully for this model.",
                           "Master Conf - Vehicle configuration is fetched successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_get_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, model, version, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be fetched successfully for the given model.",
                           "Master Conf - Telemetry configuration is fetched successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_get_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, model, version, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be fetched successfully for the given model.",
                           "Master Conf - Command configuration is fetched successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_get_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, model, version, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be fetched successfully for the given model.",
                           "Master Conf - Alert configuration is fetched successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_GetMasterConfig_Negative:

    @pytest.mark.Smoke
    def test7a_negative_vehicleConfigurations_getMasterConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Get Master Configuration API should throw appropriate error message for invalid apikey.",
                   "Get Master Configuration API showing/throwing appropriate error message for invalid apikey.")


        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7b_negative_vehicleConfigurations_getMasterConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "Vehicle_Configuration", "VehicleConfiguration_getMasterConfig")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            version = str(dict1["version"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Adp"
            version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Get Master Configuration API should throw appropriate error message for empty apikey.",
                   "Get Master Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7c_negative_vehicleConfigurations_getMasterConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        model = "Adp"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Get Master Configuration API should throw appropriate error message for no apikey.",
                   "Get Master Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7d_negative_vehicleConfigurations_getMasterConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Get Master Configuration API should throw appropriate error message for empty x-requestor.",
                   "Get Master Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7e_negative_vehicleConfigurations_getMasterConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        model = "Adp"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Get Master Configuration API should throw appropriate error message for no x-requestor.",
                   "Get Master Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7f_negative_vehicleConfigurations_getMasterConfiguration_non_exist_model(self):
        print("----------------------------------------------------------")

        model = "Mo123del"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "valid")


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
    def test7g_negative_vehicleConfigurations_getMasterConfiguration_invalid_model(self):
        print("----------------------------------------------------------")

        model = "@@"
        version = "3.0"

        print("model: ", model)
        print("version: ", version)

        # Verify command & control response
        response = vehicleConfigurations_fetchMasterConfigurationForModel(self, model, version, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16001" and response_body["errors"][0][
            "message"] == "Master Config does not exist for this model":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")
