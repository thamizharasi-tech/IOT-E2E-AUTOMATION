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



class Test_Restore:

    def test_vehicle_conf_factory_restore(self):

        systemId = "7bGAkRf49Ysgwa9BwLSsg"#read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

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
                           "Vehicle Conf Restore - Configuration reset should be triggered successfully",
                           "Vehicle Conf Restore - Configuration reset is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vehicle Conf Restore - Configuration reset should be triggered successfully",
                       "Vehicle Conf Restore - Configuration reset is not triggered successfully")
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

class Test_restore_configuration_Negative:

    @pytest.mark.Smoke
    def test1a_negative_vehicleConfigurations_restore_configuration_invalid_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "restore Configuration API should throw appropriate error message for invalid apikey.",
                   "restore Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1b_negative_vehicleConfigurations_update_restore_configuration_empty_apikey(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId,
                                                                           "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "restore Master Configuration API should throw appropriate error message for empty apikey.",
                   "restore Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1c_negative_vehicleConfigurations_update_restore_configuration_no_apikey(self):
        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId,
                                                                           "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "restore Master Configuration API should throw appropriate error message for no apikey.",
                   "restore Master Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1d_negative_vehicleConfigurations_update_restore_configuration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId,
                                                                           "empty_x-requestor")
        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "restore Master Configuration API should throw appropriate error message for empty x-requestor.",
                   "restore Master Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1e_negative_vehicleConfigurations_update_restore_configuration_no_xrequestor(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId,
                                                                           "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "restore Master Configuration API should throw appropriate error message for no x-requestor.",
                   "restore Master Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1f_negative_vehicleConfigurations_update_restore_configuration_invalid_content_type(self):

        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "invalid_content_type")

        # Validate api status & response
        if response.status_code == 415:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1g_negative_vehicleConfigurations_update_restore_configuration_empty_content_type(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId,  "empty_content_type")

        if response.status_code == 415:
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1h_negative_vehicleConfigurations_update_restore_configuration_invalid_systemId(self):

        print("----------------------------------------------------------")
        systemId = "xyz"
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16020" and response_body["errors"][0]["errors"][0]["message"] == "Vehicle Config does not exist for this system id":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1i_negative_vehicleConfigurations_update_restore_configuration_empty_systemId(self):

        print("----------------------------------------------------------")
        systemId = ""
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16090" and response_body["errors"][0][
            "message"] == "System ID must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1j_negative_vehicleConfigurations_update_restore_configuration_without_systemId(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "without_systemId")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16090" and response_body["errors"][0][
            "message"] == "System ID must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1k_negative_vehicleConfigurations_update_restore_configuration_empty_version(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = ""

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16092" and response_body["errors"][0][
            "message"] == "Version must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1l_negative_vehicleConfigurations_update_restore_configuration_without_version(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "without_version")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16092" and response_body["errors"][0][
            "message"] == "Version must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1m_negative_vehicleConfigurations_update_restore_configuration_invalid_version(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 0.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16020" and response_body["errors"][0]["errors"][0][
            "message"] == "Vehicle Config does not exist for this system id":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1n_negative_vehicleConfigurations_update_restore_configuration_invalid_configType(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "xyz"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16051" and response_body["errors"][0]["errors"][0][
            "message"] == "Invalid value for the configType.":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1o_negative_vehicleConfigurations_update_restore_configuration_empty_configType(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = ""
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16091" and response_body["errors"][0][
            "message"] == "Configuration type must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1p_negative_vehicleConfigurations_update_restore_configuration_without_configType(self):

        print("----------------------------------------------------------")
        systemId = read_vehicleJsonFile(self, "system_id")
        configurationType = "alert_configurations"
        version = 3.0

        response = vehicleConfigurations_restore(self, configurationType, version, systemId, "without_configurationType")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["code"] == "16091" and response_body["errors"][0][
            "message"] == "Configuration type must not be empty":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")


