import pytest
import random
import json
import time

from C2CModules.app_data_usage import App_data_usage_getAppDataUsage
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.vehicle_configurations import vehicleConfigurations_createMasterConfigurationForModel, \
    vehicleConfigurations_updateMasterConfigurationForModel, vehicleConfigurations_fetchMasterConfigurationForModel, \
    vehicleConfigurations_deleteMasterConfigurationForModel, vehicleConfigurations_createFactoryConfigurationForModel, \
    vehicleConfigurations_updateVehicleConfiguration, vehicleConfigurations_updateFactoryConfigurationForModel, \
    vehicleConfigurations_deleteFactoryConfigurationForModel, vehicleConfigurations_fetchFactoryConfigurationForModel, \
    vehicleConfigurations_configurationUpdateTracking, vehicleConfigurations_getConfig, \
    vehicleConfigurations_createInitialConfig, vehicleConfigurations_updateVehicleConfiguration_vacation_mode, \
    vehicleConfigurations_update_restore_configuration
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult
from C2CModules.api_modules import verify_api_response_for_invalid_header


OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
global model, version, RegionalAPNEndpoints

class Test_App_data_usage_getAppDataUsage:

    @pytest.mark.Smoke
    def test_positive_app_data_usage_getAppDataUsage_allParameters(self):
        print("----------------------------------------------------------")

        systemid = "ClNEfcVXFUxoxgBSQmjyV"
        appID = "com.google.music"

        print("systemid: ", systemid)
        print("appID:", appID)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemid, appID,"valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Data Fetched Successfully",
                       "Data Fetched Successfully")
            assert True
        else:
            testResult(self, "failed", "Data not Fetched Successfully",
                       "Data not Fetched Successfully")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1a_negative_app_data_usage_getAppDataUsage_invalid_apikey(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                     "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "update_restore Configuration API should throw appropriate error message for invalid apikey.",
                   "update_restore Configuration API showing/throwing appropriate error message for empty apikey.")
    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test_negative_app_data_usage_getAppDataUsage_invalid_systemID(self):
        print("----------------------------------------------------------")
        systemid = "ClNEfcVXFUxoxgBS12345"
        appID = "com.google.music"

        print("systemid: ", systemid)
        print("appID:", appID)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemid, appID,"invalid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 204:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "no content":
            testResult(self, "passed", "no content",
                       "no content")
            assert True
        else:
            testResult(self, "failed", "Data not Fetched Successfully",
                       "Data not Fetched Successfully")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test_negative_app_data_usage_getAppDataUsage_invalid_parameters(self):
        print("----------------------------------------------------------")
        systemid = "ClNEfcVXFUxoxgBS1234"
        appID = "com.google.music"

        print("systemid: ", systemid)
        print("appID:", appID)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemid, appID, "invalid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code is 403 Forbidden
        if response.status_code == 403:
            # Validate the response message
            assert response_body.get("message") == "Required authentication headers are missing"
            print("Required authentication headers are missing")
        else:
            print("Test failed: Expected 403 Forbidden")
            assert False

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1a_negative_app_data_usage_getAppDataUsage_invalid_apikey(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "update_restore Configuration API should throw appropriate error message for invalid apikey.",
                   "update_restore Configuration API showing/throwing appropriate error message for empty apikey.")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1b_negative_app_data_usage_getAppDataUsage_empty_apikey(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for empty apikey.",
                   "update_restore Configuration API showing/throwing appropriate error message for empty apikey.")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1c_negative_app_data_usage_getAppDataUsage_no_apikey(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for no apikey.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1d_negative_app_data_usage_getAppDataUsage_empty_xrequestor(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")
        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for empty x-requestor.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1e_negative_app_data_usage_getAppDataUsage_no_xrequestor(self):
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for no x-requestor.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for no x-requestor.")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1e_negative_app_data_usage_getAppDataUsage_invalid_content_type(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")
        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_content_type")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for invalid_content_type.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for invalid_content_type.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1f_negative_app_data_usage_getAppDataUsage_empty_content_type(self):
        print("----------------------------------------------------------")
        systemId = "ClNEfcVXFUxoxgBSQmjyV"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppDataUsage(self, systemId,
                                                  "invalid_apiKey")
        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_content_type")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for empty_content_type.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for empty_content_type.")

        print("----------------------------------------------------------")


