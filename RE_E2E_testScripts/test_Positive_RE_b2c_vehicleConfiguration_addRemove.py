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


class Test_Veh_conf_setup:

    def test_positive_vehicle_conf_prerequisite(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        print("===========================================")
        print("SET CONFIGURATION ON THE CLOUD SIDE")
        print("===========================================")
        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        #version = ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".0"

        version = "3.0"

        #step 1:
        factoryConfiguration(self, model, version)

        #step 2:
        masterConfiguration(self, model, version)

        #step 3:
        initializeConfiguration(self, systemId, model)

        # step 4:
        getConfiguration(self, systemId)

    def test_onboard_sevice(self):
        # step 3: fresh onboarding to take effect of new configuration - Ignore if configuration doesn't exist for the onboarded vehicle else need one fresh onboarding
        # step 4:
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, TC)
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType)

    def test_rehome(self):

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)
        action = "rehome"

        # Call api reusable module
        response = deviceRehoming(self, systemId, action, "valid")

    def test_setGet_config(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        initializeConfiguration(self, systemId, model)

        #step 5:
        getConfiguration(self, systemId)

    def test_push_conf(self):

        print("===========================================")
        print("SET CONFIGURATION ON THE DEVICE SIDE")
        print("===========================================")
        systemId = read_vehicleJsonFile(self, "system_id")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")
        response_body = response.json()
        cloud_conf = response_body["configurations"]
        print("Updating latest conf....")
        save_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\vehicleConfiguration\master_conf.json"

        # Save the updated configuration to the desired folder
        with open(save_path, "w") as f:
            json.dump(cloud_conf, f)

        print(f"Configuration updated successfully and saved to {save_path}.")


        #step 6:
        push_vehicleConf_files_on_primary_IVI_devive(self, onboardingType, chipsetType, "master_conf")

        print("Vehicle Conf Files are pushed on the device")

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        cloud_checksum = generate_cloud_checksum(self, "master_conf")
        device_checksum = generate_device_checksum(self, "master_conf")

        if cloud_checksum == device_checksum:
            print("Checksum is matching")
        else:
            print("Checksum is mismatch")

    def test_rule_engine(self):
        restart_rule_engine_service(self, onboardingType, chipsetType)


class Test_VehConf_AddRemove:

    def test_add_feature(self):

        update_master_conf(self, "insert_tyrePressure")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        response = vehicleConfigurations_updateMasterConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Vehicle configuration should update successfully for the given model.",
                           "The vehicle configuration has been successfully updated for the specified model.")
                assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger ADD FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "ADD"
        path = "vehicle_settings.vehicle_features"
        attribute = "tyre_pressure"
        value = "1"

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Attribute :", attribute)
        print("Value :", value)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, "ADD")

        print("----------------------------------------------------------")

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
                           "ADD Feature - Configuration update should be triggered successfully",
                           "ADD Feature - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "ADD Feature - Configuration update should be triggered successfully",
                       "ADD Feature - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(30)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

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

        # Read master_conf.json file
        tyrePressure_value = read_masterConfJsonFile_v2(self, "add_tyre_pressure", "Add_Remove")

        print("Tyre Pressure :", tyrePressure_value)

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
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
                testResult(self, "verificationPassed", "Add Tyre Pressure - Configuration update should  be 'PROGRESSING'",
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
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Add Tyre Pressure - Configuration update should success/completed",
                       "Add Tyre Pressure - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        status = ""

        if tyrePressure_value == value:
            testResult(self, "passed", "Tyre pressure feature and value should be added in master_conf.json file on device",
                       "Tyre pressure feature and value is added in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Tyre pressure feature and value should be added in master_conf.json file on device",
                       "Tyre pressure feature and value is not added in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
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
                vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                if "tyre_pressure" in vehicle_features:
                    if vehicle_features["tyre_pressure"] == value:
                        testResult(self, "passed",
                                   "Tyre Pressure Feature and value should be present in the vehicle configuration",
                                   "Tyre Pressure Feature and value is present in the vehicle configuration.")
                        assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_edit_feature(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger EDIT FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_features.tyre_pressure"
        attribute = "tyre_pressure"
        value = "0"

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Value :", value)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, "EDIT")

        print("----------------------------------------------------------")

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
                           "EDIT Feature - Configuration update should be triggered successfully",
                           "EDIT Feature - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(30)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

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

        # Read master_conf.json file
        tyrePressure_value = read_masterConfJsonFile_v2(self, "add_tyre_pressure", "Add_Remove")

        print("Tyre Pressure :", tyrePressure_value)

        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
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
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "EDIT Feature - Configuration update should success/completed",
                       "EDIT Feature - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
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
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
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
                vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                if "tyre_pressure" in vehicle_features:
                    if vehicle_features["tyre_pressure"] == value:
                        testResult(self, "passed",
                                   "Tyre Pressure Feature updated value should be present in the vehicle configuration",
                                   "Tyre Pressure Feature updated value is present in the vehicle configuration.")
                        assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

    def test_delete_feature(self):

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger DELETE FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "DELETE"
        path = "vehicle_settings.vehicle_features.tyre_pressure"
        attribute = "tyre_pressure"
        value = "0"

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, "DELETE")

        print("----------------------------------------------------------")

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

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(30)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

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
        print("Cloud Side Validations : ")
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
                testResult(self, "verificationPassed", "Delete Tyre Pressure - Configuration update should  be 'PROGRESSING'",
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
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Delete Tyre Pressure - Configuration update should success/completed",
                       "Delete Tyre Pressure - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        status = ""

        # Read master_conf.json file
        vehicle_features = read_masterConfJsonFile_v2(self, "add_tyre_pressure", "Add_Remove")

        print("vehicle_features :", vehicle_features)

        print("----------------------------------------------------------")

        if "tyre_pressure" not in vehicle_features:
            testResult(self, "passed", "Tyre pressure feature and value should be deleted in master_conf.json file on device",
                       "Tyre pressure feature and value is deleted in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Tyre pressure feature and value should be deleted in master_conf.json file on device",
                       "Tyre pressure feature and value is not deleted in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
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
                vehicle_features = response_body["configurations"]["vehicle_settings"]["vehicle_features"]
                if "tyre_pressure" not in vehicle_features:
                        testResult(self, "passed",
                                   "Tyre Pressure Feature and value should be deleted in the vehicle configuration",
                                   "Tyre Pressure Feature and value is deleted in the vehicle configuration.")
                        assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

class Test_Service_Remainder_Alert:

    def test_service_remainder_alert(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")

        model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger EDIT FEATURE REQUEST Via Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_service.service_reminder"
        attribute = ""
        odometer_reading = 5900
        #service_date = "2025-02-21"
        # Get the current date
        current_date = datetime.now()

        # Calculate the date 1 day from the current date
        future_date = current_date + timedelta(days=1)

        # Convert the future date to string in the same format
        service_date = future_date.strftime("%Y-%m-%d")

        value = {"odometer_reading": odometer_reading, "service_date": service_date}

        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Value :", value)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId, "EDIT")

        print("----------------------------------------------------------")

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
                           "EDIT Feature - Configuration update should be triggered successfully",
                           "EDIT Feature - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "EDIT Feature - Configuration update should be triggered successfully",
                       "EDIT Feature - Configuration update is not triggered successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "DeviceOnboarding")
        #time.sleep(30)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

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

        # Read master_conf.json file
        odo_device = read_masterConfJsonFile_v2(self, "odometer_value", "service_remainder")

        service_date_device = read_masterConfJsonFile_v2(self, "service_date", "service_remainder")

        print("Odometer value :", odo_device)
        print("Service Date: ", service_date_device)

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        status = ""

        if odo_device == odometer_reading:
            testResult(self, "passed", "Odo meter value should be updated in master_conf.json file on device",
                       "Odo meter value is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Odo meter value should be updated in master_conf.json file on device",
                       "Odo meter value is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        if service_date_device == service_date:
            testResult(self, "passed", "Service date should be updated in master_conf.json file on device",
                       "Service date is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Service date should be updated in master_conf.json file on device",
                       "Service date is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)

        print("----------------------------------------------------------")

        if status != "FAIL":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Cloud Side Validations : ")
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
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "EDIT Feature - Configuration update should success/completed",
                       "EDIT Feature - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert False
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
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
                odo_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"]["odometer_reading"]
                service_date_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"]["service_date"]
                if odo_cloud == odometer_reading and service_date_cloud == service_date:
                    testResult(self, "passed",
                                   "Odometer updated value should be present in the vehicle configuration",
                                       "Odometer updated value is present in the vehicle configuration.")
                    assert True
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False

        #================================TELEMETRY ODO====================================
        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Odometer stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_odo")
        time.sleep(5)

        print("Telemetry-Odometer stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # Telemetry-Odometer

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
            testResult(self, "passed",
                           "Device logs should contain the logs for odometer",
                           "Device logs contains the logs for odometer, pls refer device logs for "
                           "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                    "Odometer logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                           "Device logs should contain the logs for Odometer",
                           "Device logs doesnot contain the logs for Odometer or failed to read the device log, pls refer device logs for "
                           "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odometer value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_odometer_value):
            testResult(self, "passed",
                           "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                           "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                           "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                           "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                           "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                           "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignition_on")
        time.sleep(5)

        print("Telemetry-Ignition Off stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # Telemetry-Ignition Off

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off attribute in the device
        ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Lock_ignition_attribute)

        if Command_Lock_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {Command_Lock_ignition_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs contains the logs for Ignition Off, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Ignition Off",
                       "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_on_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_on_value):
            testResult(self, "passed",
                       "Ignition Statevalue should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * *")
        print("=======Service Remainder Alert=======")
        print("* * * * * * * * * * * * * * * * * * *")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the alert is sent from device to cloud when tampering event occurs
        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, service_remainder_alert_notification_deviceLog_string,
                                   service_remainder_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        print("----------------------------------------------------------")

        # Call verification module to validate alert details
        notification_verify_alert_details_v2(self, systemId, service_remainder_categoryName, service_remainder_notification_name,
                                             notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")



