import pytest
import random
import json
import time

from C2CModules.app_data_usage import App_data_usage_getAppUsageDetails
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

class Test_App_data_usage_getAppUsageDetails:

    @pytest.mark.Smoke
    def test_positive_app_data_usage_getAppDataUsage_allParametersDetails(self):
        print("----------------------------------------------------------")

        systemid = "ClNEfcVXFUxoxgBSQmjyV"
        offset = "0"
        limit = "10"

        print("systemid: ", systemid)
        print("offset",offset)
        print("limit",limit)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemid, offset,limit, "valid")

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
    def test_negative_app_data_usage_getAppDataUsage_invalid_systemID(self):
        print("----------------------------------------------------------")
        systemid = "ClNEfcVXFUxoxg12345"
        offset = "0"
        limit = "10"

        print("systemid: ", systemid)
        print("offset", offset)
        print("limit", limit)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemid, offset,limit, "invalid")

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
    def test_positive_app_data_usage_getAppDataUsage_offsetLessThan0(self):
        print("----------------------------------------------------------")

        systemid = "ClNEfcVXFUxoxgBSQmjyV"
        offset = "-1"
        limit = "10"

        print("systemid: ", systemid)
        print("offset", offset)
        print("limit", limit)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemid, offset,limit, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Offset value cannot be less than 0" and \
                response_body["errors"][0]["errorCode"] == "17028":
            testResult(self, "passed",
                       "Offset value cannot be less than 0",
                       "Offset value cannot be less than 0")
            assert True
        else:
            testResult(self, "failed",
                       "Offset value cannot be less than 0",
                       "Offset value cannot be less than 0")
            assert False

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test_positive_app_data_usage_getAppDataUsage_offsetnull(self):
        print("----------------------------------------------------------")

        systemid = "ClNEfcVXFUxoxgBSQmjyV"
        offset = ""
        limit = "10"

        print("systemid: ", systemid)
        print("offset", offset)
        print("limit", limit)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemid, offset,limit, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Offset cannot be empty or null" and \
                response_body["errors"][0]["errorCode"] == "17026":
            testResult(self, "passed",
                       "Offset cannot be empty or null",
                       "Offset cannot be empty or null")
            assert True
        else:
            testResult(self, "failed",
                       "Offset cannot be empty or null",
                       "Offset cannot be empty or null")
            assert False

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test_positive_app_data_usage_getAppDataUsage_withoutlimit(self):
        print("----------------------------------------------------------")

        systemid = "ClNEfcVXFUxoxgBSQmjyV"
        offset = "0"
        limit = ""

        print("systemid: ", systemid)
        print("offset", offset)
        print("limit",limit)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemid, offset, limit,  "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 400:
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["message"] == "Limit cannot be empty or null" and \
                response_body["errors"][0]["errorCode"] == "17027":
            testResult(self, "passed",
                       "Limit cannot be empty or null",
                       "Limit cannot be empty or null")
            assert True
        else:
            testResult(self, "failed",
                       "Offset cannot be empty or null",
                       "Offset cannot be empty or null")
            assert False

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1a_negative_app_data_usage_getAppUsageDetails_invalid_apikey(self):
        print("----------------------------------------------------------")

        systemId = "IpU0NxD8jeI8XjU4NOOgQ"

        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
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
    def test1b_negative_app_data_usage_getAppUsageDetails_empty_apikey(self):
        print("----------------------------------------------------------")

        systemId = "IpU0NxD8jeI8XjU4NOOgQ"

        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
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
    def test1c_negative_app_data_usage_getAppUsageDetails_no_apikey(self):
        print("----------------------------------------------------------")

        systemId = "IpU0NxD8jeI8XjU4NOOgQ"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
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
    def test1d_negative_app_data_usage_getAppUsageDetails_empty_xrequestor(self):
        print("----------------------------------------------------------")
        systemId = "IpU0NxD8jeI8XjU4NOOgQ"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
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
    def test1e_negative_app_data_usage_getAppUsageDetails_no_xrequestor(self):
        print("---------------------------------------------------------------")
        systemId = "IpU0NxD8jeI8XjU4NOOgQ"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
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
    def test1e_negative_app_data_usage_getAppUsageDetails_invalid_content_type(self):
        print("----------------------------------------------------------")
        systemId = "IpU0NxD8jeI8XjU4NOOgQ"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
                                                     "invalid_apiKey")
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_content_type")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for invalid_content_type.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for invalid_content_type.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1f_negative_app_data_usage_getAppUsageDetails_empty_content_type(self):
        print("----------------------------------------------------------")
        systemId = "IpU0NxD8jeI8XjU4NOOgQ"
        print("systemId: ", systemId)

        # Verify command & control response
        response = App_data_usage_getAppUsageDetails(self, systemId,
                                                     "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_content_type")

        testResult(self, "passed",
                   "update_restore Master Configuration API should throw appropriate error message for empty_content_type.",
                   "update_restore Master Configuration API showing/throwing appropriate error message for empty_content_type.")

        print("----------------------------------------------------------")

