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

class Test_UpdateVehicleConfiguration_Negative:

    def test11a_negative_vehicleConfigurations_updateVehicleConfiguration_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled, start_time, end_time, systemId, "invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Update Configuration API should throw appropriate error message for invalid apikey.",
                   "Update Configuration API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11b_negative_vehicleConfigurations_updateVehicleConfiguration_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId, "empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Update Configuration API should throw appropriate error message for empty apikey.",
                   "Update Configuration API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11c_negative_vehicleConfigurations_updateVehicleConfiguration_no_apikey(self):
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId, "no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Update Configuration API should throw appropriate error message for no apikey.",
                   "Update Configuration API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11d_negative_vehicleConfigurations_updateVehicleConfiguration_empty_xrequestor(self):
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId, "empty_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Update Configuration API should throw appropriate error message for empty x-requestor.",
                   "Update Configuration API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11e_negative_vehicleConfigurations_updateVehicleConfiguration_no_xrequestor(self):
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        start_time = current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Update Configuration API should throw appropriate error message for no x-requestor.",
                   "Update Configuration API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11f_negative_vehicleConfigurations_updateVehicleConfiguration_invalid_action(self):
        print("----------------------------------------------------------")

        action = "xyz"
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "ADD")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16034" and response_body["errors"][0]["message"] == "Invalid RequestBody":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11g_negative_vehicleConfigurations_updateVehicleConfiguration_empty_action(self):
        print("----------------------------------------------------------")

        action = ""
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "ADD")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16034" and response_body["errors"][0][
            "message"] == "Invalid RequestBody":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11h_negative_vehicleConfigurations_updateVehicleConfiguration_without_action(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "without_action")

        if response.status_code == 400:
            assert True
        else:
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16034" and response_body["errors"][0]["message"] == "Invalid RequestBody":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11i_negative_vehicleConfigurations_updateVehicleConfiguration_invalid_path(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "xyz"
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "ADD")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16048" and response_body["errors"][0]["errors"][0][
            "message"] == "Add Operation failed as attributes Haptic1 is not present in the model in path xyz":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11j_negative_vehicleConfigurations_updateVehicleConfiguration_empty_path(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = ""
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "ADD")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11k_negative_vehicleConfigurations_updateVehicleConfiguration_without_path(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "without_path")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11l_negative_vehicleConfigurations_updateVehicleConfiguration_empty_attribute(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = ""
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11m_negative_vehicleConfigurations_updateVehicleConfiguration_without_attribute(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = ""
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "without_attribute")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11n_negative_vehicleConfigurations_updateVehicleConfiguration_empty_value(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "haptic1"
        value = ""
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11o_negative_vehicleConfigurations_updateVehicleConfiguration_without_value(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "haptic1"
        value = "1"
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "without_value")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16042" and response_body["errors"][0][
            "message"] == "Add Operation failed due required parameter is missing":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11p_negative_vehicleConfigurations_updateVehicleConfiguration_empty_systemId(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic"
        value = "1"
        systemId = ""

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16028" and response_body["errors"][0]["errors"][0][
            "message"] == "This system does not currently have a vehicle configuration(s) assigned.":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11q_negative_vehicleConfigurations_updateVehicleConfiguration_without_systemId(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "Haptic"
        value = "1"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "without_systemId")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16083" and response_body["errors"][0][
            "message"] == "System IDs must be provided when update scope is not specified":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11q_negative_vehicleConfigurations_updateVehicleConfiguration_edit_non_exist_feature(self):
        print("----------------------------------------------------------")

        action = "EDIT"
        path = "vehicle_settings.vehicle_features.Hello"
        attribute = "Haptic"
        value = "1"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "EDIT")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16044" and response_body["errors"][0]["errors"][0][
            "message"] == "Edit Operation failed due to non existent path vehicle_settings.vehicle_features.Hello":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11r_negative_vehicleConfigurations_updateVehicleConfiguration_edit_exist_feature_with_the_value_not_defined_in_rule(self):
        print("----------------------------------------------------------")

        action = "EDIT"
        path = "vehicle_settings.vehicle_features.haptic"
        attribute = "Haptic"
        value = "xyz"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "EDIT")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16046" and response_body["errors"][0]["errors"][0][
            "message"] == "Rule Validation failed with reason haptic should be a boolean..":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11s_negative_vehicleConfigurations_updateVehicleConfiguration_delete_non_exist_feature(self):
        print("----------------------------------------------------------")

        action = "DELETE"
        path = "vehicle_settings.vehicle_features.haptic111"
        attribute = "Haptic"
        value = "xyz"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "DELETE")

        # Parse API response into JSON
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
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        # Validate response status code
        if response.status_code ==400:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["results"][0]["status"] == "FAILED":
            if response_body["results"][0]["results"][0]["errorCode"] == "16043" and response_body["results"][0]["results"][0]["errorMessage"] == "Delete Operation failed due to non existent path":
                # self.result.set_result(TestResults.passed)
                assert True
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11t_negative_vehicleConfigurations_updateVehicleConfiguration_add_exist_feature(self):
        print("----------------------------------------------------------")

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "haptic"
        value = "1"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "ADD")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16045" and response_body["errors"][0]["errors"][0][
            "message"] == "Add Operation failed as attribute haptic already exists at path: vehicle_settings.vehicle_features":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11u_negative_vehicleConfigurations_updateVehicleConfiguration_edit_exist_value(self):
        print("----------------------------------------------------------")

        action = "EDIT"
        path = "vehicle_settings.vehicle_features.haptic"
        attribute = "haptic"
        value = "1"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "EDIT")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test11v_negative_vehicleConfigurations_updateVehicleConfiguration_edit_exist_value(self):
        print("----------------------------------------------------------")

        action = "EDIT"
        path = "vehicle_settings.vehicle_features.haptic"
        attribute = "haptic"
        value = "1"
        systemId = read_vehicleJsonFile(self, "system_id")

        print("action: ", action)
        print("path: ", path)
        print("attribute: ", attribute)
        print("value: ", value)
        print("systemId: ", systemId)

        # Verify command & control response
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
                                                                    "EDIT")

        if response.status_code == 400:
            assert True
        else:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errors"][0]["errorCode"] == "16061" and response_body["errors"][0]["errors"][0][
            "message"] == "The new value for the field is identical to the current value. No changes were made.":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")