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
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId
from C2CModules.deviceRegistration_modules import *
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


# Vehicle Conf API Test script

# class Test:

class Test_vehConf_save_factoryConf_API:

    def test_positive_factory_conf_save_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8","GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        #else:
         #   model = fetch_vehicle_model_by_systemId(self, systemId)
        # version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "vehicle_conf")

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
            if response_body["errors"][0]["errorCode"] == "16002" and response_body["errors"][0][
                "message"] == "Factory Config version already exist for this model":
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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8","GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        #else:
          #  model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "telemetry_conf")

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
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
                "message"] == "Mode Factory Config version already exist for this model":
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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country,  version, "command_conf")

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
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
                "message"] == "Mode Factory Config version already exist for this model":
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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "alert_conf")

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
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
                "message"] == "Mode Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be saved successfully for the given model.",
                           "Factory Conf - Alert configuration already exists for the given model.")
                assert True

        else:
            print("Error: Unable to save factory alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_save_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "dtc_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - DTC configuration should be saved successfully for the given model.",
                           "Factory Conf - DTC configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16049" and response_body["errors"][0][
                "message"] == "Mode Factory Config version already exist for this model":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be saved successfully for the given model.",
                           "Factory Conf - Alert configuration already exists for the given model.")
                assert True

        else:
            print("Error: Unable to save factory alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_update_factoryConf_API:

    def test_positive_factory_conf_update_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5","GCP-QA2"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_factory_conf_update_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA2","GCP-QA8"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be updated successfully for the given model.",
                           "Factory Conf - Telemetry configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_update_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA2"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be updated successfully for the given model.",
                           "Factory Conf - Command configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_update_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA2"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be updated successfully for the given model.",
                           "Factory Conf - Alert configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_update_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA2"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, cloudEnv, model, country, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - DTC configuration should be updated successfully for the given model.",
                           "Factory Conf - DTC configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_get_factoryConf_API:

    def test_positive_factory_conf_get_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be fetched successfully for this model.",
                           "Factory Conf - Vehicle configuration is fetched successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_factory_conf_get_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be fetched successfully for the given model.",
                           "Factory Conf - Telemetry configuration is fetched successfully for the given model.")
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

    def test_positive_factory_conf_get_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be fetched successfully for the given model.",
                           "Factory Conf - Command configuration is fetched successfully for the given model.")
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

    def test_positive_factory_conf_get_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be fetched successfully for the given model.",
                           "Factory Conf - Alert configuration is fetched successfully for the given model.")
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

    def test_positive_factory_conf_get_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchFactoryConfigurationForModel_new(self, cloudEnv, model, country, version, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - DTC configuration should be fetched successfully for the given model.",
                           "Factory Conf - DTC configuration is fetched successfully for the given model.")
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


class Test_vehConf_delete_factoryConf_API:

    def test_positive_factory_conf_delete_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be deleted successfully for this model.",
                           "Factory Conf - Vehicle configuration is deleted successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to delete vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_factory_conf_delete_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Telemetry configuration should be deleted successfully for the given model.",
                           "Factory Conf - Telemetry configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_delete_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Command configuration should be deleted successfully for the given model.",
                           "Factory Conf - Command configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_delete_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Alert configuration should be deleted successfully for the given model.",
                           "Factory Conf - Alert configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_factory_conf_delete_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteFactoryConfigurationForModel_new(self, cloudEnv, model, country, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - DTC configuration should be deleted successfully for the given model.",
                           "Factory Conf - DTC configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_save_masterConf_API:

    def test_positive_master_conf_save_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4","GCP-QA2","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be saved successfully for the given model.",
                           "Master Conf - Vehicle configuration is saved successfully for this model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16000" and response_body["errors"][0][
                "message"] == "Master Config version already exist for this model":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be saved successfully for the given model.",
                           "Master Conf - Vehicle configuration already exists for the given model.")
                assert True

        else:
            print("Error: Unable to save vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_save_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4","GCP-QA2","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "telemetry_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be saved successfully for the given model.",
                           "Master Conf - Telemetry configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to save master telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_save_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4","GCP-QA2","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "command_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be saved successfully for the given model.",
                           "Master Conf - Command configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to save master command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_save_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4","GCP-QA2","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "alert_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be saved successfully for the given model.",
                           "Master Conf - Alert configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to save master alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_save_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4","GCP-QA2","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        # version = "4.1"
        version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "dtc_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - DTC configuration should be saved successfully for the given model.",
                           "Master Conf - DTC configuration is saved successfully for the given model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to save master alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_update_masterConf_API:

    def test_positive_master_conf_update_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = "4.1"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be updated successfully for this model.",
                           "Master Conf - Vehicle configuration is updated successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_update_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be updated successfully for the given model.",
                           "Master Conf - Telemetry configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_update_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be updated successfully for the given model.",
                           "Master Conf - Command configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_update_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be updated successfully for the given model.",
                           "Master Conf - Alert configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_update_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - DTC configuration should be updated successfully for the given model.",
                           "Master Conf - DTC configuration is updated successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_get_MasterConf_API:

    def test_positive_master_conf_get_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "vehicle_conf")

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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "telemetry_conf")

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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "command_conf")

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

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "alert_conf")

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

    def test_positive_master_conf_get_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_fetchMasterConfigurationForModel_new(self, cloudEnv, model, country, version, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - DTC configuration should be fetched successfully for the given model.",
                           "Master Conf - DTC configuration is fetched successfully for the given model.")
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


class Test_vehConf_delete_masterConf_API:

    def test_positive_master_conf_delete_vehicle_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Vehicle configuration should be deleted successfully for this model.",
                           "Master Conf - Vehicle configuration is deleted successfully for this model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print("Error: Unable to delete vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_positive_master_conf_delete_telemetry_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "3.0"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, "telemetry_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Telemetry configuration should be deleted successfully for the given model.",
                           "Master Conf - Telemetry configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete telemetry configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_delete_command_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, "command_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Command configuration should be deleted successfully for the given model.",
                           "Master Conf - Command configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete command configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_delete_alert_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, "alert_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - Alert configuration should be deleted successfully for the given model.",
                           "Master Conf - Alert configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

    def test_positive_master_conf_delete_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3","GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        version = "4.1"

        response = vehicleConfigurations_deleteMasterConfigurationForModel_new(self, cloudEnv, model, country, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Master Conf - DTC configuration should be deleted successfully for the given model.",
                           "Master Conf - DTC configuration is deleted successfully for the given model.")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete alert configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")


class Test_vehConf_initializeConfig_API:

    def test_positive_initialize_config(self):
        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        initializeConfiguration(self, systemId, model)


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

    def test_positive_get_config_dtc_conf(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "dtc_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "DTC configuration fetched successfully for the given vehicle.",
                           "The DTC configuration has been successfully retrieved for the specified vehicle.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch alert configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_factoryReset:

    def test_vehicle_conf_factory_reset(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        #systemId = "7238"

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

class Test_vehConf_globalConf_API:

    def test_positive_create_global_vehicle_configuration(self):

        version = ''.join([str(random.randint(1, 99)).zfill(1) for _ in range(1)]) + "." + ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        #version = "4.1"

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

        #version = "4.1"

        version = ''.join([str(random.randint(1, 99)).zfill(1) for _ in range(1)]) + "." + ''.join(
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

        #version = "4.1"
        version = ''.join([str(random.randint(1, 99)).zfill(1) for _ in range(1)]) + "." + ''.join(
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

        #version = "4.1"
        version = ''.join([str(random.randint(1, 99)).zfill(1) for _ in range(1)]) + "." + ''.join(
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

    def test_positive_create_global_dtc_configuration(self):

        #version = "4.1"
        version = ''.join([str(random.randint(1, 99)).zfill(1) for _ in range(1)]) + "." + ''.join(
            [str(random.randint(1, 9)).zfill(1) for _ in range(1)])

        response = vehicleConfigurations_createGlobalConfiguration(self, version, "dtc_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global DTC configuration should be saved successfully",
                           "Global DTC configuration is saved successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        elif response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == "16062" and response_body["errors"][0][
                "message"] == "Global master config version already exists":
                testResult(self, "passed",
                           "Global DTC configuration should be saved successfully",
                           "Global DTC configuration already exists")
                assert True

        else:
            print("Error: Unable to save global dtc configuration. Please check the API response for more details.",
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

    def test_positive_update_global_dtc_conf(self):

        response = vehicleConfigurations_updateGlobalConfiguration(self, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global DTC configuration should be updated successfully",
                           "Global DTC configuration is updated successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to update global dtc configuration. Please check the API response for more details.",
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

    def test_positive_get_global_dtc_conf(self):

        response = vehicleConfigurations_getGlobalConfiguration(self, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global DTC configuration should be fetched successfully",
                           "Global DTC configuration is fetched successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to fetch global dtc configuration. Please check the API response for more details.",
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

    def test_positive_delete_global_dtc_conf(self):

        response = vehicleConfigurations_deleteGlobalConfiguration(self, "dtc_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Global DTC configuration should be deleted successfully",
                           "Global DTC configuration is deleted successfully")
                assert True
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
        else:
            print(
                "Error: Unable to delete global dtc configuration. Please check the API response for more details.",
                "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("----------------------------------------------------------")

class Test_vehConf_create_bundle_API:

    def test_positive_vehicle_configuration_create_bundle(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "GCP-QA4", "GCP-QA5", "GCP-QA8", "GCP-QA2","GCP-PERF2","GCP-QA2-EU"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        response = vehicleConfigurations_create_bundle(self, cloudEnv, model, country, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Create Bundle API should be triggered successfully",
                           "Create Bundle API is triggered successfully")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False

        else:
            print("Unable to create bundle of vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

class Test_vehicleMode_precondition:

    def test_pos_save_vacation_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_update_vacation_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE", "PRIVACY_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_privacy_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2,
                                 "save_precondition")

    def test_pos_update_privacy_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE", "VACATION_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_incognito_mode_precondition_enable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2,
                                 "save_precondition")

    def test_pos_update_incognito_mode_precondition_enable(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "enable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "vehicleMode", "operator": "in", "value": ["NORMAL_MODE"], "isActive": True}

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2,
                                 "update_precondition")

    def test_pos_save_vacation_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_save_privacy_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")

    def test_pos_save_incognito_mode_precondition_disable(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DEV", "RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        subAction = "disable"
        statePreconditions1 = {"attribute": "connectionState", "operator": "eq", "value": ["CONNECTED"], "isActive": True}
        statePreconditions2 = {"attribute": "ota", "operator": "in", "value": [ "SCHEDULED", "SUCCESS", "FAILURE" ], "isActive": True }

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Sub Action :", subAction)
        print("Precondition-1 :", statePreconditions1)
        print("Precondition-2 :", statePreconditions2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, cloudEnv, model, country, action, subAction, statePreconditions1, statePreconditions2, "save_precondition")











