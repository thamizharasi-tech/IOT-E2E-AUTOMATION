import json
import time
from datetime import timezone, datetime
import random
import re
import requests
import zstandard as zstd
import os
import hashlib


from C2CModules.e2e_testData import *

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId
from C2CModules.notifications import notification_verify_alert_details_v2
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta
from C2CModules.ddl import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test_ddl:

    def test1_positive_bikeSecuritySafety_deep_logging(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        time.sleep(60)

        # read the logs
        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\c2clogs.txt"  # Replace with the actual path

        pattern = r'\bDDL_TELE_15\w+\.data\b'
        filenames = set()
        file_status_codes = {}

        try:
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as logfile:
                for line in logfile:
                    matches = re.findall(pattern, line)
                    filenames.update(matches)

            if filenames:
                print(f"Found {len(filenames)} unique filenames:")
                for filename in filenames:
                    print(f"Validating filename: {filename}")
                    response = ddl_download_file(self, systemId, filename, "ROLE_UNMASKED")
                    file_status_codes[filename] = response.status_code
                    if response.status_code == 200:
                        testResult(self, "passed", "DDL File should be stored on the cloud",
                                   "DDL file stored on the cloud")
                    else:
                        print(f"Failed for filename: {filename} with status code: {response.status_code}")

                print("Filenames and their status codes:")
                for filename, status_code in file_status_codes.items():
                    if status_code == 200:
                        print(f"{filename}: {status_code} - Uploaded successfully on the cloud")
                    elif status_code == 204:
                        print(f"{filename}: {status_code} - Failed to upload on the cloud")
                    else:
                        print(f"{filename}: {status_code}")

                if any(status_code == 200 for status_code in file_status_codes.values()):
                    print("Test case passed: At least one API call was successful.")
                else:
                    print("Test case failed: No successful API call for any filename.")
                    assert False, "No successful API call for any filename."
            else:
                print("No matching filenames found.")
                assert False, "No matching filenames found."

        except PermissionError as e:
            print(f"Permission denied: {str(e)}")
            assert False, f"Permission denied: {str(e)}"
        except Exception as e:
            print(f"Exception while processing the log file: {str(e)}")
            assert False, f"Exception while processing the log file: {str(e)}"

    def test1_positive_deep_logging_download_file_user_role_masked(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        time.sleep(60)

        successful_filenames = get_and_download_ddl_file(self, systemId, "ROLE_MASKED")
        decompress_downloaded_files_from_folder(self, "ROLE_MASKED", successful_filenames)
        validate_telemetry_data_from_decompressed_file(self, "ROLE_MASKED")

    def test1_positive_deep_logging_download_file_user_role_unmasked(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        time.sleep(60)

        successful_filenames = get_and_download_ddl_file(self, systemId, "ROLE_UNMASKED")
        decompress_downloaded_files_from_folder(self, "ROLE_UNMASKED", successful_filenames)
        validate_telemetry_data_from_decompressed_file(self, "ROLE_UNMASKED")

class Test_ddl_v2:

    def test1_positive_deep_logging_download_file_user_role_masked_v2(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        #time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        #time.sleep(60)

        successful_filenames = get_and_download_ddl_file_v2(self, systemId, "ROLE_MASKED")
        decompress_downloaded_files_from_folder(self, "ROLE_MASKED", successful_filenames)
        validate_telemetry_data_from_decompressed_file(self, "ROLE_MASKED")

    def test1_positive_deep_logging_download_file_user_role_unmasked_v2(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        time.sleep(60)

        successful_filenames = get_and_download_ddl_file_v2(self, systemId, "ROLE_UNMASKED")
        decompress_downloaded_files_from_folder(self, "ROLE_UNMASKED", successful_filenames)
        validate_telemetry_data_from_decompressed_file(self, "ROLE_UNMASKED")


class Test_try_logic:

    def test_test(self):

        # Folder path
        folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File\DDL_Decompressed_Files"

        file_name = "extracted_DDL_TELE_15_1746410171986.data"

        tc = "ROLE_MASKED"

        # Get list of files in the folder
        files = os.listdir(folder_path)

        # Process each file
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                    # Step 1: Handle multiple JSON objects in the file
                    json_blocks = content.split("\n")  # Assuming each JSON object is on a new line
                    for json_str in json_blocks:
                        try:
                            outer_json = json.loads(json_str)  # Load individual JSON structure
                        except json.JSONDecodeError as e:
                            print(f"Skipping one JSON block in `{file_name}` due to invalid format. Error: {e}")
                            continue

                        # Step 2: Ensure `body` is parsed separately if present
                        if "body" in outer_json:
                            try:
                                body_json = json.loads(outer_json["body"])  # Convert stringified JSON to dictionary
                            except json.JSONDecodeError as e:
                                print(f"Skipping `{file_name}` due to malformed JSON in `body`. Error: {e}")
                                continue

                            # Step 3: Extract telemetry data for validation
                            telemetry_data = body_json.get("telemetry", [])
                            validation_passed = True

                            if telemetry_data:
                                for item in telemetry_data[0]["data"]:
                                    if item["id"] in [559940097, 559940098]:  # Latitude or Longitude
                                        value = item["value"]

                                        # Validation for masked & unmasked roles
                                        try:
                                            float_value = float(value)  # Ensure it's a valid float
                                            is_numeric = True
                                        except ValueError:
                                            is_numeric = False

                                        if tc == "ROLE_MASKED":
                                            status = "MASKED" if not is_numeric else "NOT MASKED"
                                        elif tc == "ROLE_UNMASKED":
                                            status = "UNMASKED" if is_numeric else "MASKED"

                                        print(
                                            f"File: {file_name} | ID: {item['id']} | Role: {tc} | Status: {status} | Value: {value}")

                                        if (tc == "ROLE_MASKED" and status != "MASKED") or (
                                                tc == "ROLE_UNMASKED" and status != "UNMASKED"):
                                            validation_passed = False

                                # **Pass or fail validation based on role**
                                if validation_passed:
                                    testResult(self, "passed",
                                               f"Telemetry validation for `{file_name}` completed successfully.",
                                               f"Telemetry data matches expected masking behavior. Role: {tc}")
                                else:
                                    testResult(self, "failed", f"Telemetry validation for `{file_name}` failed.",
                                               f"Telemetry data does NOT match expected masking behavior. Role: {tc}")

                        else:
                            print(f"No valid `body` field found in `{file_name}`, skipping...")

            except Exception as e:
                print(f"Error processing `{file_name}`: {e}")

    def test_test1(self):

        # Folder path
        offset = "1"
        limit = "10"
        systemId = read_vehicleJsonFile(self, "system_id")
        uploadId = get_file_metadata(self, offset, limit, systemId, "valid")