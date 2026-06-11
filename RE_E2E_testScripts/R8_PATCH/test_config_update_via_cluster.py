import json
import time
from datetime import timezone
import random

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.vehicle_state import *
from C2CModules.telemetry_modules import *
from C2CModules.commandControl_modules import *
from C2CModules.ddl import *


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_Vehicle_Modes_from_cluster:

    def test_positive_vacation_mode_enable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Enable vacation mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vacation_mode_enable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 1
        else:
            enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Vacation")

        print("----------------------------------------------------------")

    def test_positive_vacation_mode_disable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Disable vacation mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vacation_mode_disable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 0
        else:
            enabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Vacation")

        print("----------------------------------------------------------")

    def test_positive_privacy_mode_enable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Enable Privacy mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "privacy_mode_enable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 1
        else:
            enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Privacy")

        print("----------------------------------------------------------")

    def test_positive_privacy_mode_disable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Disable vacation mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "privacy_mode_disable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 0
        else:
            enabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Privacy")

        print("----------------------------------------------------------")

    def test_positive_incognito_mode_enable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Enable Incognito mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "incognito_mode_enable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 1
        else:
            enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Incognito")

        print("----------------------------------------------------------")

    def test_positive_incognito_mode_disable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Disable Incognito mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "incognito_mode_disable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 0
        else:
            enabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Incognito")

        print("----------------------------------------------------------")

    def test_positive_remote_diagnostic_mode_enable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Enable remote diagnostic mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_enable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 1
        else:
            enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "RemoteDiagnostic")

        print("----------------------------------------------------------")

    def test_positive_remote_diagnostic_mode_disable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Disable remote diagnostic mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_disable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 0
        else:
            enabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "RemoteDiagnostic")

        print("----------------------------------------------------------")

    def test_positive_service_mode_enable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Enable service mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_enable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 1
        else:
            enabled = True

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Service")

        print("----------------------------------------------------------")

    def test_positive_service_mode_disable(self):

        print("--------------------------------------------------------------------------------------")

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remote_diagnostic_mode_precondition")

        print("--------------------------------------------------------------------------------------")

        print("--------------------------------------------------------------------------------------")

        print("Disable service mode from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "service_mode_disable")

        print("--------------------------------------------------------------------------------------")

        # Test Data*

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        if cloudEnv in ["GCP-QA5"]:
            enabled = 0
        else:
            enabled = False

        vehicle_mode_set_from_cluster(self, cloudEnv, onboardingType, chipsetType, systemId, enabled,
                                      "Service")

        print("----------------------------------------------------------")

    def test_positive_add_feature(self):

        print("= = = = = = = = = = = = = = = = = = ")
        print("Update new feature in master configuration before initiating the request on the device")
        print("= = = = = = = = = = = = = = = = = = ")

        cloudEnv = read_cloud_env(self)

        update_master_conf(self, cloudEnv, "insert_tyrePressure")

        systemId = read_vehicleJsonFile(self, "system_id")

        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["RE-DM1"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        elif cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4", "GCP-QA5"]:
            model = str(dict1["modelCode"])
            country = str(dict1["country"])
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, cloudEnv, model, country,
                                                                               "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Vehicle configuration should update successfully for the given model.",
                           "The vehicle configuration has been successfully updated for the specified model.")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            # self.result.set_result(TestResults.failed)

        print("Add new feature from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "add_new_feature_from_cluster")

        print("--------------------------------------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        systemId = read_vehicleJsonFile(self, "system_id")
        attribute = "tyre_pressure"
        value = "1"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Attribute :", attribute)
        print("Value :", value)
        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("VALIDATE UPDATED CONFIGURATION IN MASTER_CONF.JSON")

        # Read master_conf.json file
        tyrePressure_value = read_masterConfJsonFile_v2(self, cloudEnv, "add_tyre_pressure", "Add_Remove")

        status = ""

        if tyrePressure_value == value:
            testResult(self, "passed",
                       "Tyre pressure feature and value should be added in master_conf.json file on device",
                       "Tyre pressure feature and value is added in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Tyre pressure feature and value should be added in master_conf.json file on device",
                       "Tyre pressure feature and value is not added in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv not in ["GCP-QA4", "GCP-QA5"]:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                else:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_function"]

                # Check for 'tyre_pressure' feature
                if "tyre_pressure" in vehicle_features:
                    if vehicle_features["tyre_pressure"] == value:
                        testResult(self, "passed",
                                   "Tyre Pressure Feature and value should be present in the vehicle configuration",
                                   "Tyre Pressure Feature and value is present in the vehicle configuration.")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        print("Tyre pressure value does not match the expected value.")
                        assert False
                        #self.result.set_result(TestResults.failed)
                else:
                    # Log an error if 'tyre_pressure' feature is missing
                    print("Tyre Pressure feature is not found in vehicle features.")
                    testResult(self, "failed",
                               "Tyre Pressure Feature should be present in the vehicle configuration",
                               "'Tyre Pressure' feature is missing in the vehicle configuration.")
                    assert False
                    #self.result.set_result(TestResults.failed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

    def test_positive_edit_feature(self):

        print("Edit feature from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "edit_feature_from_cluster")

        print("--------------------------------------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        systemId = read_vehicleJsonFile(self, "system_id")
        attribute = "tyre_pressure"
        value = "0"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Attribute :", attribute)
        print("Value :", value)
        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("VALIDATE UPDATED CONFIGURATION IN MASTER_CONF.JSON")

        # Read master_conf.json file
        tyrePressure_value = read_masterConfJsonFile_v2(self, cloudEnv, "add_tyre_pressure", "Add_Remove")

        status = ""

        if tyrePressure_value == value:
            testResult(self, "passed", "Tyre pressure value should be updated in master_conf.json file on device",
                       "Tyre pressure feature value is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Tyre pressure feature value should be updated in master_conf.json file on device",
                       "Tyre pressure feature value is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv not in r8_patch2_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                else:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_function"]

                # Check for 'tyre_pressure' feature
                if "tyre_pressure" in vehicle_features:
                    if vehicle_features["tyre_pressure"] == value:
                        testResult(self, "passed",
                                   "Tyre Pressure Feature and value should be present in the vehicle configuration",
                                   "Tyre Pressure Feature and value is present in the vehicle configuration.")
                        assert True
                        #self.result.set_result(TestResults.passed)
                    else:
                        print("Tyre pressure value does not match the expected value.")
                        assert False
                        #self.result.set_result(TestResults.failed)
                else:
                    # Log an error if 'tyre_pressure' feature is missing
                    print("Tyre Pressure feature is not found in vehicle features.")
                    testResult(self, "failed",
                               "Tyre Pressure Feature should be present in the vehicle configuration",
                               "'Tyre Pressure' feature is missing in the vehicle configuration.")
                    assert False
                    #self.result.set_result(TestResults.failed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

    def test_positive_delete_feature(self):

        print("Delete feature from cluster")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "delete_feature_from_cluster")

        print("--------------------------------------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        systemId = read_vehicleJsonFile(self, "system_id")
        attribute = "tyre_pressure"
        value = "1"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Attribute :", attribute)
        print("Value :", value)
        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Get Configuration On the cloud via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv not in r8_patch2_envs:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                else:
                    vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_function"]

                # Check for 'tyre_pressure' feature
                if "tyre_pressure" in vehicle_features:
                    if vehicle_features["tyre_pressure"] == value:
                        testResult(self, "failed",
                                   "Tyre Pressure Feature and value should not be present in the vehicle configuration",
                                   "Tyre Pressure Feature and value is present in the vehicle configuration.")
                        assert False
                        #self.result.set_result(TestResults.failed)
                    else:
                        print("Tyre pressure value does not match the expected value.")
                        assert False
                        #self.result.set_result(TestResults.failed)
                else:
                    # Log an error if 'tyre_pressure' feature is missing
                    print("Tyre Pressure feature is not found in vehicle features.")
                    testResult(self, "passed",
                               "Tyre Pressure Feature should not be present in the vehicle configuration",
                               "'Tyre Pressure' feature is missing in the vehicle configuration.")
                    assert True
                    #self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)