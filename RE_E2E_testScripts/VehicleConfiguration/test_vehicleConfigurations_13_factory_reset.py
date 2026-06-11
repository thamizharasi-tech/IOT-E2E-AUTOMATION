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

class Test_factoryReset:

    def test_vehicle_conf_factory_reset(self):

        #systemId = read_vehicleJsonFile(self, "system_id")
        systemId = "7238"

        response = vehicleConfigurations_factoryReset(self, systemId, "valid")

        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False
            # self.result.set_result(TestResults.failed)

        # Validate response body
        trackingId = ""
        if response_body["status"] == "PROGRESSING":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "Factory Reset - Configuration reset should be triggered successfully",
                           "Factory Reset - Configuration reset is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Factory Reset - Configuration reset should be triggered successfully",
                       "Factory Reset - Configuration reset is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Tracking API : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            print(response.status_code)

            print("----------------------------------------------------------")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed", "Factory Reset - Configuration reset should  be 'PROGRESSING'",
                           "Factory Reset - Configuration reset is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Factory Reset - Configuration reset should success/completed",
                       "Factory Reset - Configuration reset is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Factory Reset - Configuration reset should success/completed",
                       "Factory Reset - Configuration reset is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

class Test_FactoryReset_Negative:

    @pytest.mark.Smoke
    def test2a_negative_vehicleConfigurations_factoryReset_invalid_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api stauts & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for invalid apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2b_negative_vehicleConfigurations_factoryReset_empty_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for empty apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2c_negative_vehicleConfigurations_factoryReset_no_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for no apikey.",
                   "Update Factory Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2d_negative_vehicleConfigurations_factoryReset_empty_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for empty x-requestor.",
                   "Update Factory Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2e_negative_vehicleConfigurations_factoryReset_no_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Update Factory Configuration API should throw appropriate error message for no x-requestor.",
                   "Update Factory Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2f_negative_vehicleConfigurations_factoryReset_invalid_action(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "invalid_action")

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
    def test2g_negative_vehicleConfigurations_factoryReset_empty_action(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "empty_action")

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

    @pytest.mark.Smoke
    def test2h_negative_vehicleConfigurations_factoryReset_invalid_systemId(self):
        print("----------------------------------------------------------")

        systemId = "xyz"

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16005" and response_body["errors"][0]["errors"][0][
            "message"] == "Vehicle config does not exist for this system id":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2i_negative_vehicleConfigurations_factoryReset_empty_systemId(self):
        print("----------------------------------------------------------")

        systemId = ""

        # Verify command & control response
        response = vehicleConfigurations_factoryReset(self, systemId, "valid")

        if response.status_code == 404:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

