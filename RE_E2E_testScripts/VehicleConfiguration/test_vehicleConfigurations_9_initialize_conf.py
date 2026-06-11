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

class Test_vehConf_initializeConfig_API:

    def test_positive_initialize_config(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        initializeConfiguration(self, systemId, model)

class Test_CreateInitialConfig_Negative:

    @pytest.mark.Smoke
    def test9a_negative_VehicleConfiguration_createInitialConfig_invali_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Create Initial Configuration API should throw appropriate error message for invalid apikey.",
                   "Create Initial Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9b_negative_VehicleConfiguration_createInitialConfig_empty_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Create Initial Configuration API should throw appropriate error message for empty apikey.",
                   "Create Initial Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9c_negative_VehicleConfiguration_createInitialConfig_no_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Create Initial Configuration API should throw appropriate error message for no apikey.",
                   "Create Initial Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9d_negative_VehicleConfiguration_createInitialConfig_empty_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Create Initial Configuration API should throw appropriate error message for empty x-requestor.",
                   "Create Initial Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9e_negative_VehicleConfiguration_createInitialConfig_no_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Create Initial Configuration API should throw appropriate error message for no x-requestor.",
                   "Create Initial Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9f_negative_VehicleConfiguration_createInitialConfig_invalid_action(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "invalid_action")

        if response.status_code == 400:
            assert True
        else:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16006" and response_body["errors"][0]["message"] == "Invalid action":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9g_negative_VehicleConfiguration_createInitialConfig_invalid_systemId(self):
        print("----------------------------------------------------------")

        systemId = "xyz1"

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9h_negative_VehicleConfiguration_createInitialConfig_empty_systemId(self):
        print("----------------------------------------------------------")

        systemId = ""

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9i_negative_VehicleConfiguration_createInitialConfig_invalid_model(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "xyz"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16003" and response_body["errors"][0][
            "message"] == "Factory Config does not exist for this model":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9j_negative_VehicleConfiguration_createInitialConfig_empty_model(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = ""

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16010" and response_body["errors"][0][
            "message"] == "Unable to retrieve model for the system id {}. Please enter a valid system id":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9k_negative_VehicleConfiguration_createInitialConfig_empty_action(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = "Cruiser"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_createInitialConfig_new(self, systemId, model, "empty_action")

        if response.status_code == 400:
            assert True
        else:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16006" and response_body["errors"][0][
            "message"] == "Invalid action":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

