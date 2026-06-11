import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random
import re

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
from C2CModules.commandControl_modules import commandControl_Service_Request, \
    read_commandCtrl_trackingId, \
    commandControl_Service_Tracking, verify_commandCtrl_status
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.ddl import *
from C2CModules.notifications import notification_verify_alert_details_v2

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_Telemetryconf:

    def test_telemetry_conf_normal(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "normal_mode")

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 15000
        time.sleep(60)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_telemetry_conf_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Privacy_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "privacy_mode")
        time.sleep(120)

        telemetry_msgs = ["constr_and_send_proto_msg success for 1001"]
        event_id = 1001
        push_freq = 25000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_telemetry_conf_privacy(self):

        #validate_device_telemetry_message(self, onboardingType, telemetry_msgs, event_id, push_freq)

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Privacy_without_startEndTime")



        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "privacy_mode")
        time.sleep(120)

        telemetry_msgs = ["constr_and_send_proto_msg success for 1001"]
        event_id = 1001
        push_freq = 25000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_dis_mode(self):
        # Test Data*
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "Privacy_without_startEndTime")

    def test_telemetry_in_log(self):

        print("*" * 50)
        print("Validation on device side after configured the push frequency:")
        print("*" * 50)

        telemetry_msgs = []
        tc = "normal_mode"
        push_freq = 15000

        print("*" * 50)
        print("Validation on device side after configured the push frequency:")
        print("*" * 50)

        telemetry_msgs = []

        # Determine telemetry message and event ID based on test case
        if tc == "normal_mode" or tc == "vacation_mode":
            telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
            event_id = 3101
        elif tc == "privacy_mode":
            telemetry_msgs = ["constr_and_send_proto_msg success for 1001"]
            event_id = 1001

        timestamps = []

        # Extract timestamps for all matching log entries
        for telemetry_msg in telemetry_msgs:
            try:
                with open(C2CtestReport_c2cLogsPath + 'c2clogs.txt', 'r') as logfile:
                    log_entries = []
                    for line in logfile:
                        if telemetry_msg in line:
                            log_entries.append(line)  # Collect all matching lines

                    if not log_entries:
                        print(f"No matching log entries found for '{telemetry_msg}'.")
                        continue

                    print(f"Found {len(log_entries)} occurrences of '{telemetry_msg}'.")

                    # Process each log entry
                    for log_entry in log_entries:
                        try:
                            # Extract and parse the timestamp
                            timestamp_str = log_entry.split()[0] + " " + log_entry.split()[
                                1]  # Example: "03-28 05:58:30.827"
                            timestamp = datetime.strptime(timestamp_str, "%m-%d %H:%M:%S.%f")
                            timestamps.append(timestamp)
                            print(f"Extracted Timestamp: {timestamp}")
                        except ValueError as e:
                            print(f"Timestamp Parsing Failed for '{log_entry}': {str(e)}")

            except Exception as e:
                print(f"Exception while processing telemetry message '{telemetry_msg}': {str(e)}")

        # Validate timestamps
        if len(timestamps) < 2:
            print("Not enough timestamps were extracted. Validation failed.")
            return

        time_differences = []
        timestamps.sort()  # Ensure timestamps are sorted before calculating differences

        for i in range(1, len(timestamps)):
            time_diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
            time_differences.append(time_diff)
            print(f"Time Difference Between Event {i} and Event {i + 1}: {time_diff} seconds")

            # Validate against the expected frequency of 15 seconds
            if abs(time_diff - (push_freq/1000)) <= 0.01:  # Allow tolerance of ±0.01 seconds
                testResult(self, "passed",
                           f"Validate telemetry message frequency for event '{event_id}'",
                           f"Telemetry message frequency is valid: {time_diff} seconds.")
            else:
                testResult(self, "failed",
                           f"Validate telemetry message frequency for event '{event_id}'",
                           f"Telemetry message frequency mismatch: Expected 15 seconds, Found {time_diff} seconds.")
                assert False, f"Telemetry message frequency mismatch: Expected 15 seconds, Found {time_diff}."

        # Summary Output
        print("\n[SUMMARY OF TIME DIFFERENCES]")
        if time_differences:
            for i, diff in enumerate(time_differences, start=1):
                print(f"Event {i} to Event {i + 1}: {diff} seconds.")
        else:
            print("No time differences were calculated. Ensure multiple log entries exist.")

class Test_modes_future_date:

    def test_updated_vacation_mode_future_date(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        # Get the current start time in milliseconds
        current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        start_time = current_time + 60000 #1 min

        # Calculate end time for 5 minutes later
        end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                                   end_time, "valid")

        time.sleep(120)
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validation when the device is in incognito mode: ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        telemetry_msgs = [
            "constr_and_send_proto_msg success for 3101",
            "constr_and_send_proto_msg success for 6510",
            "constr_and_send_proto_msg success for 6517",
            "constr_and_send_proto_msg success for 1001",
            "constr_and_send_proto_msg success for 2001"
        ]

        # Initialize result aggregation for a summary at the end
        results = []

        # Verify each message using verify_message_in_log
        for msg in telemetry_msgs:
            # Call the verify_message_in_log function to check if the message exists in the log
            result, frequency = verify_message_in_log(self, msg,
                                                      msg)  # Pass message1 and message2 (or the same message)

            # Handle the results
            if result != "Error":
                print(f" => Found telemetry message '{msg}' in logs.")
                print(f"Matching log line for '{msg}': {result.strip()}")
                testResult(self, "failed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Failed", "details": result.strip(), "frequency": frequency})
            else:
                print(f" => Not found telemetry message '{msg}' in logs.\n")
                testResult(self, "passed",
                           f"Validate that telemetry navigation for '{msg}' is stopped for the configured frequency",
                           f"Telemetry message '{msg}' is not publishing to the cloud. Please refer to device logs for detailed info.")
                results.append({"message": msg, "status": "Passed", "details": None, "frequency": frequency})

        # Summary Output
        print("\n[SUMMARY]")
        for result in results:
            print(f"Message: {result['message']} - Status: {result['status']}")
            if result['details']:
                print(f"  Matching Line: {result['details']}")
                print(f"  Frequency: {result['frequency']}")

        print("----------------------------------------------------------")

        # Wait until the end_time
        while current_time < end_time:
            remaining_time = (end_time - current_time) / 1000  # Convert remaining time to seconds
            print(f"Waiting until end_time... Remaining time: {remaining_time:.2f} seconds")
            time.sleep(10)  # Check every 10 seconds
            current_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # After end_time is reached
        print("end_time reached. Proceeding with the operation...")
        time.sleep(10)

        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(30)
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Validate vacation mode is disabled in master_conf.json : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        # Read master_conf.json file
        vacationMode_Disabled = read_masterConfJsonFile_v2(self, "VacationMode_Enabled", "incognitoMode")

        print(" Vacation Mode - Enabled :", vacationMode_Disabled)

        print("----------------------------------------------------------")
        status = ""

        if vacationMode_Disabled == "false" or vacationMode_Disabled == False:
            testResult(self, "passed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is set to False in master_conf.json file on device")
        else:
            testResult(self, "verificationFailed",
                       "Vacation Mode Flag should be set to False in master_conf.json file on device",
                       "Vacation Mode Flag is not set to False in master_conf.json file on device")
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

        # Fetch configuration from the vehicle configuration API
        response = vehicleConfigurations_getConfig_new(self, systemId, "vehicle_conf")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            if response_body.get("message") == "Success":
                # Extract vehicle mode configuration
                vehicle_mode = response_body["configurations"]["vehicle_settings"].get("vehicle_mode")

                # Handle each mode
                if "vacation_mode" in vehicle_mode:
                    mode_config = vehicle_mode["vacation_mode"]
                    if mode_config["enabled"] == "false" or mode_config["enabled"] == False:
                        testResult(self, "passed",
                                   "Vacation Mode Flag should be set to True in master_conf.json file on cloud",
                                   "Vacation Mode Flag is set to True in master_conf.json file on cloud")
                        assert True
                else:
                    print("Invalid or unsupported vehicle mode.")

class Test_command_precondition:

    def test_cmd_precondition_normal(self):

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run cstub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("CSTUB - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_cmd_precondition_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Vacation_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "vacation_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_cmd_precondition_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Privacy_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_cmd_precondition_incognito(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.incognito_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Incognito_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

class Test_Alert:

    def test_over_speed_alert_normal(self):

        #systemId = read_vehicleJsonFile(self, "system_id")
        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_alert_over_speed_vacation(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        #getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Vacation_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "vacation_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_alert_over_speed_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Privacy_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_alert_over_speed_incognito(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.incognito_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "Incognito_without_startEndTime")

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

class Test_vehicle_modes:

    def test_vacation_mode_enable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        #time.sleep(20)

        print("----------------------------------------------------------")
        print("Run Vehicle Mode A2A Test on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_test")

        print("Vehicle Mode A2A Test run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "vacationMode_without_startEndTime")

    def test_vacation_mode_disable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        #time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        disabled = False
        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "vacationMode_without_startEndTime")

    def test_privacy_mode_enable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "privacyMode_without_startEndTime")

    def test_privacy_mode_disable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.privacy_mode"
        enabled = True
        disabled = False
        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "privacyMode_without_startEndTime")

    def test_incognito_mode_enable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.incognito_mode"
        enabled = True
        disabled = False
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

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, enabled, start_time,
                       end_time, "incognitoMode_without_startEndTime")

    def test_incognito_mode_disable(self):

        getset_config_v2(self, onboardingType, chipsetType, "master_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.incognito_mode"
        enabled = True
        disabled = False
        # Get the current start time in milliseconds
        start_time = end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        # Calculate end time for 5 minutes later
        #end_time = start_time + 300000  # 5 minutes in milliseconds

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # set vacation mode
        vehicle_mode_set_via_cloud_v2(self, onboardingType, chipsetType, systemId, action, path, disabled, start_time,
                       end_time, "incognitoMode_without_startEndTime")

class Test_vehConf_normalMode:

    def test_telemetry_conf_normal(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "normal_mode")

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 15000
        time.sleep(60)

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_normal(self):

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run cstub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("CSTUB - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================



        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_cmd_precondition_normal_new(self):

        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run cstub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("CSTUB - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================



        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_over_speed_alert_normal(self):

        #systemId = read_vehicleJsonFile(self, "system_id")
        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "normal_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "normal_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_vacationMode:

    def test_telemetry_conf_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "vacation_mode")
        time.sleep(120)

        telemetry_msgs = ["constr_and_send_proto_msg success for 3101"]
        event_id = 3101
        push_freq = 20000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_vacation(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "vacation_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_alert_over_speed_vacation(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "vacation_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "vacation_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_vacation_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "vacation_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_privacyMode:

    def test_telemetry_conf_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_push_frequency_update(self, onboardingType, chipsetType, "privacy_mode")
        time.sleep(120)

        telemetry_msgs = ["constr_and_send_proto_msg success for 1001"]
        event_id = 1001
        push_freq = 11000

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        validate_device_telemetry_message(self, telemetry_msgs, event_id, push_freq)

    def test_cmd_precondition_privacy(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_alert_over_speed_privacy(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "privacy_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "privacy_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_privacy_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "privacy_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_vehConf_incognitoMode:

    def test_cmd_precondition_incognito(self):

        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "dtc")
        time.sleep(5)

        print("cstub - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        getset_config_v2(self, onboardingType, chipsetType, "command_conf", "path2")
        time.sleep(20)

        vehicle_conf_command_precondition_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run stub on device for speed
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for Speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_speed")
        time.sleep(5)

        print("TELEMETRY SPEED - stub run process is completed, verify logs for alert details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        b2c_telemetry_speed_value = "10"
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value

        ls = verify_message_in_log(self, b2c_telemetry_speed_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is set to {b2c_telemetry_speed_value}, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                f"Speed value is not set to {b2c_telemetry_speed_value} or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationPassed", f"Precondition: Speed value should be set to {b2c_telemetry_speed_value} ",
                       f"Speed value is not set to {b2c_telemetry_speed_value}, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "SPEED":
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if float(value) == float(b2c_telemetry_speed_value):
            testResult(self, "verificationPassed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("------------------------------------------")
        print("Initiate Command - VEHICLE LOCK via API : ")
        print("------------------------------------------")

        # Read api configuration/common data
        try:
            dict = read_api_data_from_excel(self, "API_Common_Data", "app_id")
            appId = str(dict["Value"])
        except:
            appId = command_appId

        name = command_vehicleLock
        appId = command_appId
        time_value = command_time
        area = command_area
        value = command_value_1
        timeout = command_timeout

        print("Name : ", name)
        print("System Id : ", systemId)
        print("APP Id : ", appId)
        print("Time : ", time_value)
        print("Area : ", area)
        print("Value : ", value)
        print("Timeout : ", timeout)

        # Initiate command request
        response = commandControl_Service_Request(self, name, systemId, appId, time_value, area, value, timeout)

        # ===========================================================================================
        # Device side validations : Fetch logs & verify command & control msg
        # ===========================================================================================

        print("------------------------------------------")
        print("Device Validations for initiated command : ")
        print("------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Verify command control msgs & type code in fetched device logs
        # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
        # ls = verify_message_in_log(self, Command_Lock_ignition_attribute, Command_Acc_ignition_value)
        # print(ls)

        # ===========================================================================================
        # Cloud side validations for preconditions
        # ===========================================================================================

        print("------------------------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("------------------------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(10)
        actual_status = ""
        expected_status = expected_success_status

        try:

            # Parse API response in JSON
            response = response.json()

            # read tracking id
            trackingId = read_commandCtrl_trackingId(self, response)

            # Verify command & control resp
            response = commandControl_Service_Tracking(self, trackingId)

            # Parse API response in JSON
            response = response.json()

            # Verify command & control status
            actual_status = verify_commandCtrl_status(self, response)

            if actual_status == expected_status:
                testResult(self, "passed",
                           "The Command status should be " + expected_status,
                           "The Command status is " + actual_status)
            else:
                testResult(self, "failed",
                           "The Command status should be " + expected_status,
                           "The Command status is not " + expected_status + " rather it is '" + actual_status + "' or something went wrong. Refer api response")
        except:
            testResult(self, "failed",
                       "The Command status should be " + expected_status,
                       "The Command status is not " + expected_status + " or something went wrong. Refer api response")

        print("----------------------------------------------------------")

    def test_alert_over_speed_incognito(self):

        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "incognito_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_speed:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Over Speed value configured in the stub : ", telemetry_over_speed_value)
        print("Over Speed value stored in Cloud DB : ", value)

        if int(value) == int(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def test_telemetry_conf_add_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "incognito_mode", "ADD_NEW_TELEMETRY_BLOCK")

    def test_telemetry_conf_remove_new_block_normal_mode(self):

        getset_config_v2(self, onboardingType, chipsetType, "telemetry_conf", "path2")
        time.sleep(20)

        vehicle_conf_telemtry_addRemove_new_block(self, onboardingType, chipsetType, "incognito_mode", "REMOVE_TELEMETRY_BLOCK")

class Test_periodic_syncup:

    def test_vacation_mode_enable_periodic_syncup(self):

        # 1.Insert tyre pressure in master conf file in local folder
        print("==> 1.Adding tyre pressure in local folder")
        systemId = read_vehicleJsonFile(self, "system_id")

        update_master_conf(self, "insert_tyrePressure")

        # --------------------------------
        # update factory conf
        # --------------------------------

        model = fetch_vehicle_model_by_systemId(self, systemId)
        # model = "Cruiser"

        # 2.update factory conf on the cloud
        print("==> 2. Updating Factory Conf")
        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            # self.result.set_result(TestResults.failed)

        # 3. Do the factory reset to reflect updated factory conf on the cloud
        print("==> 3. Factory Reset")
        vehicle_conf_factory_reset(self, systemId)

        # trigger vacation mode
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("==> 4. Trigger Vacation Mode vai Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 180000  # 1 min

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

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
                           "Vacation Mode - Configuration update should be triggered successfully",
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
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationFailed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationPassed",
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
            if response.status_code == 400:
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
            elif response_body["results"][0]["status"] == "FAILED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert False
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("==>5. Validating file upload during periodic syncUp")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2clogs\c2clogs.txt"  # Update with actual path

        pattern = r'CM_FU:recieved file name :(\S+\.json)'  # Regex pattern to capture filename

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_data = file.read()

        match = re.search(pattern, log_data)
        if match:
            filename = match.group(1)
            print(f"Extracted filename: {filename}")
        else:
            print("No matching filename found.")

        print("==>6. Get Presigned Url")
        response = ddl_get_presigned_url(self, systemId, filename, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            download_link = response_body["fileMetadata"]["downloadLink"]
            fileName = response_body["fileMetadata"]["fileName"]
            expirationDate = response_body["fileMetadata"]["expirationDate"]

            print(" Download link: ", download_link)
            print("File Name: ", fileName)
            print("Expiration Date: ", expirationDate)

            testResult(self, "verificationPassed", "File should Uploaded successfully on the cloud",
                       "File successfully uploaded on the cloud")
        else:
            testResult(self, "verificationFailed", "File should Uploaded successfully on the cloud",
                       "File not uploaded on the cloud or filename not found in the device log")

        print("==> Trigger vacation Mode request after periodic syncup")

        # set vacation mode
        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

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
                           "Vacation Mode - Configuration update should be triggered successfully",
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
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

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

    def test_vacation_mode_enable_periodic_syncup_v2(self):

        # 1.Insert tyre pressure in master conf file in local folder
        print("==> 1.Adding tyre pressure in local folder")
        systemId = read_vehicleJsonFile(self, "system_id")

        update_master_conf(self, "insert_tyrePressure")

        # --------------------------------
        # update factory conf
        # --------------------------------

        model = fetch_vehicle_model_by_systemId(self, systemId)
        # model = "Cruiser"

        # 2.update factory conf on the cloud
        print("==> 2. Updating Factory Conf")
        response = vehicleConfigurations_updateFactoryConfigurationForModel_new(self, model, "vehicle_conf")

        # Parse the API response into JSON format
        response_body = response.json()

        # Validate the response status code and message
        if response.status_code == 200:
            if response_body["message"] == "Success":
                testResult(self, "passed",
                           "Factory Conf - Vehicle configuration should be updated successfully for this model.",
                           "Factory Conf - Vehicle configuration is updated successfully for this model.")
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("Unexpected response message during update:", response_body["message"])
                assert False
                # self.result.set_result(TestResults.failed)
        else:
            print("Error: Unable to update vehicle configuration. Please check the API response for more details.",
                  "Status Code:", response.status_code, "Response Body:", response_body)
            assert False
            # self.result.set_result(TestResults.failed)

        # 3. Do the factory reset to reflect updated factory conf on the cloud
        print("==> 3. Factory Reset")
        vehicle_conf_factory_reset(self, systemId)

        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")
        # trigger vacation mode
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("==> 4. Trigger Vacation Mode vai Vehicle configuration API : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        # Test Data*

        action = "EDIT"
        path = "vehicle_settings.vehicle_mode.vacation_mode"
        enabled = True
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        end_time = start_time + 180000  # 1 min

        print("----------------------------------------------------------")
        print("System Id :", systemId)
        print("Action :", action)
        print("Path :", path)
        print("Start Time :", start_time)
        print("End Time :", end_time)
        print("----------------------------------------------------------")

        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

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
                           "Vacation Mode - Configuration update should be triggered successfully",
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
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        device_checksum = "successfully got checksum of the file"
        cloud_checksum = "successfully got cloud checksum"
        checksum_validation_status = "checksum validation"

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, device_checksum,
                                   device_checksum)

        if device_checksum in str(ls[0]):
            print(f" => Device got the checksum of the file successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       " Device got the checksum of the file successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the checksum of the file.")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the checksum of the file successfully",
                       "Failed to get the checksum of the file. or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, cloud_checksum,
                                   cloud_checksum)
        if cloud_checksum in str(ls[0]):
            print(f" => Device got the cloud checksum successfully")
            testResult(self, "verificationFailed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Device got the cloud checksum successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to get the cloud checksum")
            testResult(self, "verificationPassed",
                       "Validate that device should receive/get the cloud checksum successfully",
                       "Failed to get the cloud checksum or log file is not updated with required details , pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        ls = verify_message_in_log(self, checksum_validation_status,
                                   checksum_validation_status)
        if checksum_validation_status in str(ls[0]):
            print(f" => Checksum should be validated successfully")
            testResult(self, "verificationFailed",
                       "Validate the device & cloud checksum successfully",
                       "Checksum is validated successfully, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(f" => Failed to validate the checksum")
            testResult(self, "verificationPassed",
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
            if response.status_code == 400:
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
            elif response_body["results"][0]["status"] == "FAILED":
                break

            time.sleep(10)

        # Validate response body
        if response_body["results"][0]["status"] == "COMPLETED":
            testResult(self, "failed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is success/completed")
            assert False
            # self.result.set_result(TestResults.passed)
        elif response_body["results"][0]["status"] == "FAILED":
            testResult(self, "passed", "Vacation Mode - Configuration update should success/completed",
                       "Vacation Mode - Configuration update is not success/completed")
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Something went wrong, Please check API Response for more details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("==>5. Validating file upload during periodic syncUp")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        # Extract filename from logs
        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2clogs\c2clogs.txt"
        pattern = r'CM_FU:recieved file name :(\S+\.json)'

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            log_data = file.read()

        match = re.search(pattern, log_data)
        if match:
            filename = match.group(1).strip().lower()
            print(f"[DEBUG] Extracted filename from logs: '{filename}'")
        else:
            print("No matching filename found in logs.")
            assert False

        print("==>6. Get file metadata")

        offset = 1
        limit = 100
        match_found = False

        while True:
            response = ddl_get_file_metadata(self, str(offset), str(limit), systemId, "systemId")

            if response.status_code == 200:
                response_body = response.json()

                if response_body["message"] == "Data Fetched Successfully":
                    pageNo = response_body["pageNo"]
                    pageSize = response_body["pageSize"]
                    totalPages = response_body["totalPages"]
                    totalRecords = response_body["totalRecords"]

                    print("Page No: ", pageNo)
                    print("Page Size: ", pageSize)
                    print("Total Pages: ", totalPages)
                    print("Total Records: ", totalRecords)

                    data_len = len(response_body["metaData"])
                    print("[DEBUG] Available filenames in metadata:")
                    for i in range(data_len):
                        file_name = response_body["metaData"][i]["file-name"].strip().lower()
                        print(f"  - {file_name}")

                    if data_len >= 1:
                        for i in range(data_len):
                            uploadId = response_body["metaData"][i]["uploadId"]
                            system_id = response_body["metaData"][i]["system_id"]
                            file_upload_time = response_body["metaData"][i]["file-upload-time"]
                            file_name = response_body["metaData"][i]["file-name"].strip().lower()

                            print(
                                f"[DEBUG] Comparing metadata filename: '{file_name}' with extracted filename: '{filename}'")

                            if file_name == filename:
                                print("Upload Id: ", uploadId)
                                print("System Id: ", system_id)
                                print("file_upload_time: ", file_upload_time)
                                print("file_name: ", file_name)
                                testResult(self, "passed",
                                           "File metadata details should be fetched successfully for the respective vehicle",
                                           "File metadata details are fetched successfully for the vehicle")
                                match_found = True
                                break

                    if match_found or offset >= response_body["totalPages"]:
                        break

                    offset += 1

                else:
                    print("Response message is not expected. Rather than found: ", response_body["message"])
                    assert False

            elif response.status_code == 204:
                print("No data available")
                assert False
            else:
                print("Response status code is not expected. Rather than found: ", response.status_code)
                assert False

        if not match_found:
            print(f"[ERROR] Matching filename '{filename}' not found in metadata records")
            assert False

        print("==> Trigger vacation Mode request after periodic syncup")

        # set vacation mode
        print("Set vehicle mode precondition on device for speed and lvl2 property")
        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_mode_precondition")
        # call update vehicle configuration api module
        response = vehicleConfigurations_updateVehicleConfiguration_vacation_mode_new(self, action, path, enabled,
                                                                                      start_time, end_time, systemId,
                                                                                      "valid")

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
                           "Vacation Mode - Configuration update should be triggered successfully",
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
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

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

class Test_vehicleMode_precondition:

    def test_save_vacation_mode_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE"]
        isActive_2 = True

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        response = vehicleConfigurations_save_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2, operator_2, value_2, isActive_2, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            if response_body["status"] == "COMPLETED":

                testResult(self, "passed", "Vehicle mode precondition should be saved successfully","Vehicle mode precondition is saved successfully")

                assert True
            else:
                testResult(self, "failed", "Vehicle mode precondition should be saved successfully",
                           "Vehicle mode precondition is not saved successfully")
                assert False

        else:
            print("Response status code is not as expected OR something went wrong, please check API response", response.status_code)
            assert False

        #Fetch the precondition

        response = vehicleConfigurations_get_precondition(self, model, action, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            status = response_body["status"]
            model = response_body["model"]
            action = response_body["action"]
            result = response_body["result"]

            if status == "COMPLETED":
                print("Status: ", status)
                print("Model: ", model)
                print("Action: ", action)
                print("Result: ", result)

                testResult(self, "passed", "Vehicle mode precondition should be fetched successfully",
                           "Vehicle mode precondition is fetched successfully")

                assert True
            else:
                testResult(self, "failed", "Vehicle mode precondition should be fetched successfully",
                           "Vehicle mode precondition is not fetched successfully")
                assert False

        else:
            print("Response status code is not as expected OR something went wrong, please check API response",
                  response.status_code)
            assert False

    def test_update_vacation_mode_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE","PRIVACY_MODE"]
        isActive_2 = True

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        response = vehicleConfigurations_update_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2, operator_2, value_2, isActive_2, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            if response_body["status"] == "COMPLETED":

                testResult(self, "passed", "Vehicle mode precondition should be updated successfully","Vehicle mode precondition is updated successfully")

                assert True
            else:
                testResult(self, "failed", "Vehicle mode precondition should be updated successfully",
                           "Vehicle mode precondition is not updated successfully")
                assert False

        else:
            print("Response status code is not as expected OR something went wrong, please check API response", response.status_code)
            assert False

        #Fetch the precondition

        response = vehicleConfigurations_get_precondition(self, model, action, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            status = response_body["status"]
            model = response_body["model"]
            action = response_body["action"]
            result = response_body["result"]

            if status == "COMPLETED":
                print("Status: ", status)
                print("Model: ", model)
                print("Action: ", action)
                print("Result: ", result)

                testResult(self, "passed", "Vehicle mode precondition should be fetched successfully",
                           "Vehicle mode precondition is fetched successfully")

                assert True
            else:
                testResult(self, "failed", "Vehicle mode precondition should be fetched successfully",
                           "Vehicle mode precondition is not fetched successfully")
                assert False

        else:
            print("Response status code is not as expected OR something went wrong, please check API response",
                  response.status_code)
            assert False

class Test_vehicleMode_precondition1:

    def test_pos_save_vacation_mode_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE"]
        isActive_2 = True
        subAction = ""

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2, operator_2, value_2, isActive_2,subAction, "save_precondition")

    def test_pos_update_vacation_mode_precondition(self):

        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "vacation_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE","PRIVACY_MODE"]
        isActive_2 = True
        subAction = "enable"

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2, operator_2, value_2, isActive_2, subAction, "update_precondition")

    def test_pos_save_privacy_mode_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE"]
        isActive_2 = True

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2,
                                 operator_2, value_2, isActive_2, "save_precondition")

    def test_pos_update_privacy_mode_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "privacy_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE", "PRIVACY_MODE"]
        isActive_2 = True
        subAction = "enable"

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2,
                                 operator_2, value_2, isActive_2, "update_precondition")

    def test_pos_save_incognito_mode_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE"]
        isActive_2 = True

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2,
                                 operator_2, value_2, isActive_2, "save_precondition")

    def test_pos_update_incognito_mode_precondition(self):
        systemId = read_vehicleJsonFile(self, "system_id")
        model = fetch_vehicle_model_by_systemId(self, systemId)
        action = "incognito_mode"
        attribute_1 = "currentState"
        operator_1 = "eq"
        value_1 = ["ACTIVE"]
        isActive_1 = True
        attribute_2 = "vehicleMode"
        operator_2 = "in"
        value_2 = ["NORMAL_MODE", "PRIVACY_MODE"]
        isActive_2 = True

        print("----------------------------------------------------------")
        print("Model:", model)
        print("Action :", action)
        print("Attribute-1 :", attribute_1)
        print("Operator-1 :", operator_1)
        print("Value-1 :", value_1)
        print("isActive-1 :", isActive_1)
        print("Attribute-2 :", attribute_2)
        print("Operator-2 :", operator_2)
        print("Value-2 :", value_2)
        print("isActive-2 :", isActive_2)
        print("----------------------------------------------------------")

        vehicleMode_precondition(self, model, action, attribute_1, operator_1, value_1, isActive_1, attribute_2,
                                 operator_2, value_2, isActive_2, "update_precondition")
