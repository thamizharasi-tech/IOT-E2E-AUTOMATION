import os,sys,datetime,time,subprocess,inspect,logging

import json
import time
from datetime import timezone

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.fms_modules import get_tridId_from_log, read_tripId_from_Trip_waypoints, latest_trip_meta, \
    latest_trip_details, calculate_trip_distance, calculate_trip_duration, \
    calculate_average_speed, calculate_battery_consumed, calculate_trip_battery_efficiency, \
    read_latest_trip_details_attribute_value
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, pull_files_from_primary_IVI, read_masterConfJsonFile_v2, read_vehicleModeJsonFile
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.vehicle_configurations import vehicleConfigurations_updateVehicleConfiguration, \
    vehicleConfigurations_configurationUpdateTracking, vehicleConfigurations_getConfig, vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_Vacation_Mode:

    def test_postive_vacation_mode_v2(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Trigger Vacation Mode
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Trigger Vacation Mode vai Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 300000

        value= {
            "enabled": enabled,
            "start_time": start_time,
            "end_time": end_time
        }

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled, start_time, end_time, systemId, "valid")

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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should be triggered successfully",
                           "Vacation Mode - Configuration update is triggered successfully")
                assert True
                # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Vacation Mode - Configuration update should be triggered successfully",
                       "Vacation Mode - Configuration update is not triggered successfully")
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
        vacationMode_Enabled = read_masterConfJsonFile_v2(self, "VacationMode_Enabled","vacationMode")
        vacationMode_StartTime = read_masterConfJsonFile_v2(self, "VacationMode_StartTime","vacationMode")
        vacationMode_EndTime = read_masterConfJsonFile_v2(self, "VacationMode_EndTime","vacationMode")

        print(" Vacation Mode - Enabled :", vacationMode_Enabled)
        print(" Vacation Mode - Start Time :", vacationMode_StartTime)
        print(" Vacation Mode - End Time :", vacationMode_EndTime)

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
                testResult(self, "verificationPassed", "Vacation Mode - Configuration update should  be 'PROGRESSING'",
                           "Vacation Mode - Configuration update is PROGRESSING")
            # Validate response body
            elif response_body["results"][0]["status"] == "COMPLETED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert True
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
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

        if vacationMode_Enabled == enabled:
            testResult(self, "passed", "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is set to True in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to True in master_conf.json file on device",
                       "Vacation Mode Flag is not set to True in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if vacationMode_StartTime == start_time:
            testResult(self, "passed", "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Start time should be updated in master_conf.json file on device",
                       "Vacation Mode Start time is not updated in master_conf.json file on device")
            status = "FAIL"
            print("Status", status)
        print("----------------------------------------------------------")

        if vacationMode_EndTime == end_time:
            testResult(self, "passed", "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is updated in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode End time should be updated in master_conf.json file on device",
                       "Vacation Mode End time is not updated in master_conf.json file on device")
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


