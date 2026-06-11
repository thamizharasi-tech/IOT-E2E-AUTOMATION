import os, sys, datetime, time, subprocess, inspect, logging

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
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.notifications import notification_verify_alert_details_v2

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_VehConf_AddRemove:

    def test_add_feature(self):

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
        elif cloudEnv in ["GCP-QA3", "RE-DEV", "GCP-QA4"]:
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
                #self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger ADD FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "ADD"
        if cloudEnv not in r8_patch2_envs:
            path = "vehicle_settings.vehicle_features"
        else:
            path = "vehicle_settings.vehicle_function"
        attribute = "tyre_pressure"
        value = "1"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Attribute :", attribute)
        print("Value :", value)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, updateScope, modelCode, country,
                                                                    "ADD")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False
            #self.result.set_result(TestResults.failed)

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "ADD Feature - Configuration update should be triggered successfully",
                           "ADD Feature - Configuration update is triggered successfully")
                assert True
                #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "ADD Feature - Configuration update should be triggered successfully",
                       "ADD Feature - Configuration update is not triggered successfully")
            #self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation - Configuration status by trackingId: ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Add Tyre Pressure - Configuration update should  be 'PROGRESSING'",
                           "Add Tyre Pressure - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Add Tyre Pressure- Configuration update should success/completed",
                       "Add Tyre Pressure - Configuration update is success/completed")
            assert True
            #self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Add Tyre Pressure - Configuration update should success/completed",
                       "Add Tyre Pressure - Configuration update is not success/completed")
            #self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

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

        print("----------------------------------------------------------")

    def test_edit_feature(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger EDIT FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in r8_patch2_envs:
            path = "vehicle_settings.vehicle_features.tyre_pressure"
        else:
            path = "vehicle_settings.vehicle_function.tyre_pressure"
        attribute = "tyre_pressure"
        value = "0"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Value :", value)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, updateScope, modelCode, country,
                                                                    "EDIT")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
            #self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False
            #self.result.set_result(TestResults.failed)

        # Validate response body
        trackingId = ""
        if response_body["status"] == "Progressing":
            if response_body["trackingId"]:
                print("----------------------------------------------------------")
                trackingId = response_body["trackingId"]
                print("trackingId: ", response_body["trackingId"])
                print("----------------------------------------------------------")
                testResult(self, "verificationPassed",
                           "EDIT Feature - Configuration update should be triggered successfully",
                           "EDIT Feature - Configuration update is triggered successfully")
                assert True
                #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is not triggered successfully")
            #self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation - Configuration status by trackingId: ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed", "EDIT Feature - Configuration update should  be 'PROGRESSING'",
                           "EDIT Feature - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "EDIT Feature- Configuration update should success/completed",
                       "EDIT Feature - Configuration update is success/completed")
            assert True
            #self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "EDIT Feature - Configuration update should success/completed",
                       "EDIT Feature - Configuration update is not success/completed")
            #self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

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

    def test_delete_feature(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger DELETE FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "DELETE"
        if cloudEnv not in r8_patch2_envs:
            path = "vehicle_settings.vehicle_features.tyre_pressure"
        else:
            path = "vehicle_settings.vehicle_function.tyre_pressure"
        attribute = "tyre_pressure"
        value = "0"
        updateScope = modelCode = country = ""

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, updateScope, modelCode, country,
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
                testResult(self, "verificationPassed",
                           "DELETE Feature - Configuration update should be triggered successfully",
                           "DELETE Feature - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "DELETE Feature - Configuration update should be triggered successfully",
                       "DELETE Feature - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("DEVICE SIDE VALIDATION AFTER TRIGGERING UPDATE REQUEST FROM CLOUD")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationPassed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to validate the checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validation - Configuration status by trackingId: ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        for i in range(5):
            # Verify command & control response
            response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

            # Validate response status code
            if response.status_code == 200 or response.status_code == 207:
                assert True
                #self.result.set_result(TestResults.passed)
            else:
                print("Response status is not as expected OR something went wrong, please check API response")
                #self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["results"][0]["status"] == "PROGRESSING":
                testResult(self, "verificationPassed",
                           "Delete Tyre Pressure - Configuration update should  be 'PROGRESSING'",
                           "Delete Tyre Pressure - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Delete Tyre Pressure- Configuration update should success/completed",
                       "Delete Tyre Pressure - Configuration update is success/completed")
            assert True
            #self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Delete Tyre Pressure - Configuration update should success/completed",
                       "Delete Tyre Pressure - Configuration update is not success/completed")
            #self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            #self.result.set_result(TestResults.failed)
            assert False

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




