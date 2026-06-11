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
from datetime import datetime, timedelta
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.notifications import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_Service_Remainder_Alert_R8S3:

    def test_service_remainder_alert_r8s3(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
            modelCode = str(dict1["modelCode"])
            country = str(dict1["country"])
            model = modelCode + "-" + country
        #elif cloudEnv in ["RE-DEV"]:
         #   modelCode = str(dict1["modelCode"])
          #  country = str(dict1["country"])
           # model = modelCode + country
        else:
            model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("TRIGGER EDIT FEATURE REQUEST Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_service.service_reminder"
        attribute = ""
        odometer_reading = 5000
        # service_date = "2025-02-21"
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
        response = vehicleConfigurations_updateVehicleConfiguration(self, action, path, attribute, value, systemId,
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

            print(response.status_code)

            print("----------------------------------------------------------")

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
        print("DEVICE SIDE VALIDATIONS IN MASTER_CONF.JSON FOR ODO AND SERVICE DATE : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        odo_device = read_masterConfJsonFile_v2(self, "odometer_value", "service_remainder")

        service_date_device = read_masterConfJsonFile_v2(self, "service_date", "service_remainder")

        print("Odometer value :", odo_device)
        print("Service Date: ", service_date_device)

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
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("GET UPDATED CONFIGURATION ON THE CLOUD Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                odo_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                    "odometer_reading"]
                service_date_cloud = \
                response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                    "service_date"]
                if odo_cloud == odometer_reading and service_date_cloud == service_date:
                    testResult(self, "passed",
                               "Odometer updated value should be present in the vehicle configuration",
                               "Odometer updated value is present in the vehicle configuration.")
                    assert True
                    #self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

            # Restart rule engine service
            restart_rule_engine_service(self, onboardingType, chipsetType, "path2")
            time.sleep(20)

            # ================================TELEMETRY ODO====================================
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
            ls = verify_message_in_log(self, telemetry_odo_attribute1, telemetry_odo_attribute1)

            if telemetry_odo_attribute1 in str(ls[0]):
                print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute1} ' ")
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

            response = telemetry_Curr_eventType(self, telemetry_odo_event_type1, systemId, "valid")

            # Parse API response into JSON
            response_body = response.json()

            try:
                dataList_len = len(response_body["responseData"]["signals"])
                for j in range(dataList_len):
                    if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo or \
                            response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo1:
                        value = response_body["responseData"]["signals"][j]["value"]
                        reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                        break
            except:
                value = response_body["responseData"]["signals"][0]["value"]
                print("dataList is empty in api response")

            print("Odometer value configured in the stub : ", telemetry_odometer_value)
            print("Odometer value stored in Cloud DB : ", value)

            if float(value) == float(telemetry_odometer_value):
                testResult(self, "passed",
                           "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                           "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                           "cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                           "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                           "cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOff_simulation")
        #time.sleep(5)

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOn_simulation")
        time.sleep(5)

        print("Telemetry-Ignition On stub run process is completed, verify logs for telemetry details : ")
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

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.failed)

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
        # print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # print("Logs are fetched from device to host machine @ desired location ")
        # print("----------------------------------------------------------")

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
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
            verify_notification_details_v2(self, systemId, service_remainder_categoryName, service_remainder_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, service_remainder_categoryName,
                                                 service_remainder_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test_service_remainder_alert_r8_patch2(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        #dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        #if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
         #   modelCode = str(dict1["modelCode"])
          #  country = str(dict1["country"])
           # model = modelCode + "-" + country
        #elif cloudEnv in ["RE-DEV"]:
         #   modelCode = str(dict1["modelCode"])
          #  country = str(dict1["country"])
           # model = modelCode + country
        #else:
            #model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("TRIGGER EDIT FEATURE REQUEST Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.vehicle_service.service_reminder"
            odometer_reading = 5000
            # service_date = "2025-02-21"
            # Get the current date
            current_date = datetime.now()

            # Calculate the date 1 day from the current date
            future_date = current_date + timedelta(days=1)

            # Convert the future date to string in the same format
            service_date = future_date.strftime("%Y-%m-%d")

            value = {"odometer_reading": odometer_reading, "service_date": service_date}
        else:
            path = "vehicle_settings.vehicle_function.service_due"
            odometer_reading = 5000
            # service_date = "2025-02-21"

            # get tomorrow's date in epoch milli seconds
            service_date = int((datetime.now(timezone.utc) + timedelta(days=1)).timestamp() * 1000)

            value = {"distance": odometer_reading, "time": service_date}
        attribute = updateScope = modelCode = country= ""

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

            print(response.status_code)

            print("----------------------------------------------------------")

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
        print("DEVICE SIDE VALIDATIONS IN MASTER_CONF.JSON FOR ODO AND SERVICE DATE : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        odo_device = read_masterConfJsonFile_v2(self,cloudEnv, "odometer_value", "service_remainder")

        service_date_device = read_masterConfJsonFile_v2(self, cloudEnv, "service_date", "service_remainder")

        print("Odometer value :", odo_device)
        print("Service Date: ", service_date_device)

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
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("GET UPDATED CONFIGURATION ON THE CLOUD Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv not in r8_patch2_envs:
                    odo_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                        "odometer_reading"]
                    service_date_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                        "service_date"]
                else:
                    odo_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["service_due"][
                        "distance"]
                    service_date_cloud = \
                        response_body["configurations"]["vehicle_settings"]["vehicle_function"]["service_due"][
                            "time"]
                if odo_cloud == odometer_reading and service_date_cloud == service_date:
                    testResult(self, "passed",
                               "Odometer updated value should be present in the vehicle configuration",
                               "Odometer updated value is present in the vehicle configuration.")
                    assert True
                    #self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

        # Restart rule engine service
        restart_rule_engine_service(self, onboardingType, chipsetType, "path2")
        time.sleep(20)

        # ================================TELEMETRY ODO====================================
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
        ls = verify_message_in_log(self, telemetry_odo_attribute1, telemetry_odo_attribute1)

        if telemetry_odo_attribute1 in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute1} ' ")
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

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value):
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOff_simulation")
        #time.sleep(5)

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOn_simulation")
        time.sleep(5)

        print("Telemetry-Ignition On stub run process is completed, verify logs for telemetry details : ")
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

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            telemetry_ignition_value = "1"
        else:
            telemetry_ignition_value = "4"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value

        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_Curr_ignition_state or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_ignition_ev2:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.failed)

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
        # print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # print("Logs are fetched from device to host machine @ desired location ")
        # print("----------------------------------------------------------")

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
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, service_remainder_categoryName, service_remainder_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, service_remainder_categoryName,
                                                 service_remainder_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test_service_remainder_alert_r8_patch4s14(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        systemId = read_vehicleJsonFile(self, "system_id")

        cloudEnv = read_cloud_env(self)

        #dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)

        #if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
         #   modelCode = str(dict1["modelCode"])
          #  country = str(dict1["country"])
           # model = modelCode + "-" + country
        #elif cloudEnv in ["RE-DEV"]:
         #   modelCode = str(dict1["modelCode"])
          #  country = str(dict1["country"])
           # model = modelCode + country
        #else:
            #model = fetch_vehicle_model_by_systemId(self, systemId)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("TRIGGER EDIT FEATURE REQUEST Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        if cloudEnv not in ["GCP-QA2","GCP-QA8"]:
            path = "vehicle_settings.vehicle_service.service_reminder"
            odometer_reading = 5000
            # service_date = "2025-02-21"
            # Get the current date
            current_date = datetime.now()

            # Calculate the date 1 day from the current date
            future_date = current_date + timedelta(days=1)

            # Convert the future date to string in the same format
            service_date = future_date.strftime("%Y-%m-%d")

            value = {"odometer_reading": odometer_reading, "service_date": service_date}
        else:
            path = "vehicle_settings.vehicle_function.service_due"
            odometer_reading = 5000
            # service_date = "2025-02-21"

            # get tomorrow's date in epoch milli seconds
            service_date = int((datetime.now(timezone.utc) + timedelta(days=1)).timestamp() * 1000)

            value = {"distance": odometer_reading, "time": service_date}
        attribute = updateScope = modelCode = country= ""

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
        if response_body["status"] == "Progressing" or response_body["status"] == "PROGRESSING":
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

            print(response.status_code)

            print("----------------------------------------------------------")

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
        print("DEVICE SIDE VALIDATIONS IN MASTER_CONF.JSON FOR ODO AND SERVICE DATE : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        odo_device = read_masterConfJsonFile_v2(self,cloudEnv, "odometer_value", "service_remainder")

        service_date_device = read_masterConfJsonFile_v2(self, cloudEnv, "service_date", "service_remainder")

        print("Odometer value :", odo_device)
        print("Service Date: ", service_date_device)

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
            #self.result.set_result(TestResults.passed)
            assert True
        else:
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("GET UPDATED CONFIGURATION ON THE CLOUD Via VEHICLE CONFIGURATION API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body["message"] == "Success":
                if cloudEnv not in ["GCP-QA2","GCP-QA8"]:
                    odo_cloud = response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                        "odometer_reading"]
                    service_date_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_service"]["service_reminder"][
                        "service_date"]
                else:
                    odo_cloud = \
                    response_body["configurations"]["vehicle_settings"]["vehicle_function"]["service_due"][
                        "distance"]
                    service_date_cloud = \
                        response_body["configurations"]["vehicle_settings"]["vehicle_function"]["service_due"][
                            "time"]
                if odo_cloud == odometer_reading and service_date_cloud == service_date:
                    testResult(self, "passed",
                               "Odometer updated value should be present in the vehicle configuration",
                               "Odometer updated value is present in the vehicle configuration.")
                    assert True
                    #self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message:", response_body["message"])
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to fetch vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            #self.result.set_result(TestResults.failed)

        # Restart rule engine service
        restart_rule_engine_service(self, onboardingType, chipsetType, "path2")
        time.sleep(20)

        # ================================TELEMETRY ODO====================================
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
        ls = verify_message_in_log(self, telemetry_odo_attribute1, telemetry_odo_attribute1)

        if telemetry_odo_attribute1 in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute1} ' ")
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

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo or \
                        response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo1:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value):
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")
        print("Run Telemetry-Ignition Off stub on device : ")

        #run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOff_simulation")
        #time.sleep(5)

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "device_authentication_flag")
        time.sleep(5)

        print("Telemetry-Ignition On stub run process is completed, verify logs for telemetry details : ")
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

        # verify Device Authentication flag attribute in the device

        tele_device_authentication_flag_on = telemetry_attribute_device_authentication_flag + telemetry_attribute_device_authentication_flag_value_1

        ls = verify_message_in_log(self, telemetry_attribute_device_authentication_flag_value_1, tele_device_authentication_flag_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_attribute_device_authentication_flag} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify Ignition Off value @ cloud
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_event_type_6500, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_device_authentication_flag:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_attribute_device_authentication_flag_value_1)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_attribute_device_authentication_flag_value_1):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.passed)
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
            # self.result.set_result(TestResults.failed)

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
        # print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # print("Logs are fetched from device to host machine @ desired location ")
        # print("----------------------------------------------------------")

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
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4","GCP-QA2","GCP-QA8"]:
            verify_notification_details_v2(self, systemId, service_remainder_categoryName, service_remainder_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, service_remainder_categoryName,
                                                 service_remainder_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")