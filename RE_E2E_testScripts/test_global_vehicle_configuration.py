import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random

from C2CModules.e2e_testData import *

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_vehConf_save_globalConf_API:

    def test_positive_create_global_vehicle_configuration(self):

        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        #version = "3.0"

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Vehicle configuration should be saved successfully",
                           "Global Vehicle configuration is saved successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16062" and response_body["errors"][0]["message"] == "Global master config version already exists":
                testResult(self, "passed",
                           "Global Vehicle configuration should be saved successfully",
                           "Global Vehicle configuration already exists")
                assert True

        else:
            print("Error: Unable to save global vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_create_global_telemetry_configuration(self):

        #version = "3.0"

        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "telemetry_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Telemetry configuration should be saved successfully",
                           "Global Telemetry configuration is saved successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16062" and response_body["errors"][0][
                "message"] == "Global master config version already exists":
                testResult(self, "passed",
                           "Global Command configuration should be saved successfully",
                           "Global Command configuration already exists")
                assert True
        else:
            print(
                "Error: Unable to save global telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_create_global_command_configuration(self):

        #version = "3.0"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "command_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Command configuration should be saved successfully",
                           "Global Command configuration is saved successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16062" and response_body["errors"][0][
                "message"] == "Global master config version already exists":
                testResult(self, "passed",
                           "Global Command configuration should be saved successfully",
                           "Global Command configuration already exists")
                assert True
        else:
            print(
                "Error: Unable to save global command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_create_global_alert_configuration(self):

        #version = "3.0"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "alert_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Alert configuration should be saved successfully",
                           "Global Alert configuration is saved successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16062" and response_body["errors"][0][
                "message"] == "Global master config version already exists":
                testResult(self, "passed",
                           "Global alert configuration should be saved successfully",
                           "Global alert configuration already exists")
                assert True

        else:
            print("Error: Unable to save global alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_create_global_alert_configuration_empty_version(self):

        version = ""

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "alert_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 404:
                assert True

        else:
            print("Error: Unable to save global alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_update_global_vehicle_conf(self):

        response = vehicleConfigurations_updateGlobalConfiguration(self, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Vehicle configuration should be updated successfully",
                           "Global Vehicle configuration is updated successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update global vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_update_global_telemetry_conf(self):

        response = vehicleConfigurations_updateGlobalConfiguration(self, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Telemetry configuration should be updated successfully",
                           "Global Telemetry configuration is updated successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update global telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_update_global_command_conf(self):

        response = vehicleConfigurations_updateGlobalConfiguration(self, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Command configuration should be updated successfully for the given model.",
                           "Global Command configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update global command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_update_global_alert_conf(self):

        response = vehicleConfigurations_updateGlobalConfiguration(self, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Alert configuration should be updated successfully",
                           "Global Alert configuration is updated successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update global alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_get_global_vehicle_conf(self):

        response = vehicleConfigurations_getGlobalConfiguration(self, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Vehicle configuration should be fetched successfully",
                           "Global Vehicle configuration is fetched successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch global vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_get_global_telemetry_conf(self):

        response = vehicleConfigurations_getGlobalConfiguration(self, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Telemetry configuration should be fetched successfully",
                           "Global Telemetry configuration is fetched successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch global telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_get_global_command_conf(self):

        response = vehicleConfigurations_getGlobalConfiguration(self, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Command configuration should be fetched successfully",
                           "Global Command configuration is fetched successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch global command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_get_global_alert_conf(self):

        response = vehicleConfigurations_getGlobalConfiguration(self, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Alert configuration should be fetched successfully",
                           "Global Alert configuration is fetched successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch global alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_delete_global_vehicle_conf(self):

        response = vehicleConfigurations_deleteGlobalConfiguration(self, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Vehicle configuration should be deleted successfully",
                           "Global Vehicle configuration is deleted successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to delete global vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_delete_global_telemetry_conf(self):

        response = vehicleConfigurations_deleteGlobalConfiguration(self, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Telemetry configuration should be deleted successfully",
                           "Global Telemetry configuration is deleted successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete global telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_delete_global_command_conf(self):

        response = vehicleConfigurations_deleteGlobalConfiguration(self, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Command configuration should be deleted successfully",
                           "Global Command configuration is deleted successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete global command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_delete_global_alert_conf(self):

        response = vehicleConfigurations_deleteGlobalConfiguration(self, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global Alert configuration should be deleted successfully",
                           "Global Alert configuration is deleted successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete global alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")
