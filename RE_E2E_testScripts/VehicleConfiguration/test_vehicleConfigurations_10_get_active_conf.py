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

class Test_vehConf_getConfig_API:

    def test_positive_get_config_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Vehicle configuration fetched successfully for the given vehicle.",
                           "The vehicle configuration has been successfully retrieved for the specified vehicle.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_get_config_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "telemetry_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Telemetry configuration fetched successfully for the given vehicle.",
                           "The telemetry configuration has been successfully retrieved for the specified vehicle.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch telemetry configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_get_config_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "command_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Command configuration fetched successfully for the given vehicle.",
                           "The command configuration has been successfully retrieved for the specified vehicle.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch command configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_get_config_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "alert_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Alert configuration fetched successfully for the given vehicle.",
                           "The alert configuration has been successfully retrieved for the specified vehicle.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_GetActiveConfig_Negative:


    @pytest.mark.Smoke
    def test10a_negative_VehicleConfiguration_getConfig_invalid_apikey(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Get Configuration API should throw appropriate error message for invalid apiKey.",
                   "Get Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10b_negative_VehicleConfiguration_getConfig_empty_apikey(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Get Configuration API should throw appropriate error message for empty apiKey.",
                   "Get Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10c_negative_VehicleConfiguration_getConfig_no_apikey(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Get Configuration API should throw appropriate error message for no apiKey.",
                   "Get Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10d_negative_VehicleConfiguration_getConfig_empty_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Get Configuration API should throw appropriate error message for empty x-requestor.",
                   "Get Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10e_negative_VehicleConfiguration_getConfig_no_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Get Configuration API should throw appropriate error message for no x-requestor.",
                   "Get Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10f_negative_VehicleConfiguration_getConfig_invalid_systemId(self):
        print("----------------------------------------------------------")

        systemId = "@@@@"

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16020" and response_body["errors"][0]["message"] == "Vehicle Config does not exist for this system id":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10g_negative_VehicleConfiguration_getConfig_empty_systemId(self):
        print("----------------------------------------------------------")

        systemId = ""

        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_getConfig(self, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")
