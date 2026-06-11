import ast
import json
import os.path
import time
import requests
import re
import zstandard as zstd

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.primary_IVI_device_modules import *
from C2CModules.e2e_testData import *
from C2CModules.testResults import testResult

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
deviceSerialNo = b2c_ivi_adbSerialNo


# ------------------------------------------
# DDL Reusable Modules
# ------------------------------------------

# API operation to fetch vehicle group details with pagination
def ddl_download_file(self, systemId, fileName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_download_file")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{fileName}', fileName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    if "ROLE_MASKED" in tc:
        header_x['user-role'] = "ROLE_MASKED"
    elif "ROLE_UNMASKED" in tc:
        header_x['user-role'] = "ROLE_UNMASKED"
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload), stream=True)

    return response


def ddl_get_presigned_url(self, systemId, fileName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_get_presigned_url")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{fileName}', fileName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('DDL_get_presigned_url', response.text)
    save_api_resp_in_excel(self, "API_Data", "DDL_get_presigned_url", response.text)

    return response


def get_and_download_ddl_file(self, systemId, tc):
    """
    Extract filenames from log file, validate via API, and download valid files.
    """

    pattern = r'\bDDL_TELE_15\w+\.data\b'  # Regex pattern to match filenames
    log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2clogs\c2clogs.txt"
    download_folder = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File"

    # Ensure directories exist
    os.makedirs(download_folder, exist_ok=True)

    # Clear the download folder
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    successful_filenames = []

    try:
        # Step 1: Extract filenames from the log file
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as logfile:
            filenames = set(re.findall(pattern, logfile.read()))  # Find unique filenames
        print(f"Extracted {len(filenames)} filenames from log file.")

        for filename in filenames:
            print(f"Validating filename: {filename}")
            try:
                response = ddl_download_file(self, systemId, filename, tc)

                if response and response.status_code == 200:
                    # Save the file locally
                    download_path = os.path.join(download_folder, filename)
                    try:
                        print(f"Saving file to: {download_path}")
                        with open(download_path, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=8192):
                                if chunk:  # Only write non-empty chunks
                                    file.write(chunk)
                        print(f"File downloaded successfully: {download_path}")
                        successful_filenames.append(filename)
                        testResult(self, "passed", "DDL file download should complete successfully",
                                   "DDL file was downloaded and stored correctly.")
                    except PermissionError as e:
                        print(f"Permission denied: {e}")
                        testResult(self, "failed", "DDL file download should complete successfully",
                                   f"Permission denied while saving the file: {e}")
                    except Exception as e:
                        print(f"An unexpected error occurred while saving the file: {e}")
                        testResult(self, "failed", "DDL file download should complete successfully",
                                   f"Unexpected error while saving the file: {e}")
            except requests.exceptions.RequestException as e:
                print(f"Error during file download: {e}")
            except Exception as e:
                print(f"An unexpected error occurred during validation: {e}")

        # Fail the test if no successful filenames were found
        # if not successful_filenames:
        #   testResult(self, "failed", "DDL file download should complete successfully",
        #             "No valid DDL files were downloaded.")
        # return []

        return successful_filenames



    except FileNotFoundError as e:
        print(f"Log file not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []


def decompress_downloaded_files_from_folder(self, tc, successful_filenames):
    """
    Decompress any one .data file from the list of successful filenames and store it in a different folder.
    """

    folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File"
    target_folder = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File\DDL_Decompressed_Files"

    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    if not successful_filenames:
        print(f"No successful filenames provided.")
        assert False
        return

    print(f"Found {len(successful_filenames)} successful filenames.")

    # Select any one file from the list (e.g., the first file)
    filename = successful_filenames[0]
    file_path = os.path.join(folder_path, filename)
    extracted_file_path = os.path.join(target_folder, "extracted_" + filename)

    # Ensure the file exists before opening
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'rb') as compressed:
                dctx = zstd.ZstdDecompressor()
                with open(extracted_file_path, 'wb') as destination:
                    dctx.copy_stream(compressed, destination)
            print(f"Decompression completed for: {filename}")
            testResult(self, "passed", "File decompression should complete successfully",
                       f"File {filename} was decompressed and saved.")
        except Exception as e:
            print(f"An error occurred while decompressing {filename}: {e}")
            testResult(self, "failed", "File decompression should complete successfully",
                       f"Error while decompressing {filename}: {e}")
    else:
        print(f"File not found: {file_path}")
        testResult(self, "failed", "File decompression should complete successfully",
                   f"File {filename} not found in source folder.")


def validate_telemetry_data_from_decompressed_file(self, tc):
    # Folder path
    folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File\DDL_Decompressed_Files"

    # Get list of files in the folder
    files = os.listdir(folder_path)

    # Process each file
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()

                # Extract first occurrence of "body" using regex
                match = re.search(r'"body":"({.*?})"', content)  # Locate JSON inside "body"
                if match:
                    body_content = match.group(1).replace('\\"', '"')  # Fix escaped quotes

                    try:
                        body_data = json.loads(body_content)  # Convert to valid JSON
                    except json.JSONDecodeError:
                        print(f"Skipping `{file_name}` due to malformed stringified JSON in `body`.")
                        continue

                    # Extract and validate latitude & longitude values for both roles
                    validation_passed = True

                    if "telemetry" in body_data:
                        for item in body_data["telemetry"][0]["data"]:
                            if item["id"] in [559940097, 559940098]:  # Latitude or Longitude
                                value = item["value"]

                                # Validate for both masked & unmasked user roles
                                if tc == "ROLE_MASKED":
                                    status = "MASKED" if not value.replace(".", "").isdigit() else "NOT MASKED"
                                elif tc == "ROLE_UNMASKED":  # Unmasked role
                                    status = "UNMASKED" if value.replace(".", "").isdigit() else "MASKED"

                                print(
                                    f"File: {file_name} | ID: {item['id']} | Role: {tc} | Status: {status} | Value: {value}")
                                if tc == "ROLE_MASKED" and status != "MASKED":
                                    validation_passed = False
                                elif tc == "ROLE_UNMASKED" and status != "UNMASKED":
                                    validation_passed = False

                        # **Pass or fail validation based on role**
                        if validation_passed:
                            testResult(self, "passed", "Telemetry validation should complete successfully",
                                       f"Telemetry data in {file_name} matches expected masking behavior.")
                        else:
                            testResult(self, "failed", "Telemetry validation should complete successfully",
                                       f"Telemetry data in {file_name} does NOT match expected masking behavior.")

                else:
                    print(f"No valid JSON found in `body` for {file_name}, skipping...")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")


# read data from multiple json
def validate_telemetry_data_from_decompressed_file_v2(self, tc):
    # Folder path
    folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File\DDL_Decompressed_Files"

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


# ---------------------------------------------------------------
# DDL New Reusable modules
# --------------------------------------------------------------
def ddl_get_file_metadata(self, offset, limit, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_file_meta")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace('{limit}', limit)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    if tc == "systemId":
        json_object["systemIds"][0] = systemId
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DDL_file_meta', response.text)
    save_api_resp_in_excel(self, "API_Data", "DDL_file_meta", response.text)

    return response


def ddl_download_file_by_uploadId(self, uploadId, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_download_file_upload_id")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{uploadId}', uploadId).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    if "ROLE_MASKED" in tc:
        header_x['user-role'] = "ROLE_MASKED"
    elif "ROLE_UNMASKED" in tc:
        header_x['user-role'] = "ROLE_UNMASKED"
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload), stream=True)

    return response


def get_file_metadata(self, offset, limit, systemId, tc):
    uploadId = file_name = None

    # reusable function to get the file metadata
    response = ddl_get_file_metadata(self, offset, limit, systemId, "systemId")

    if response.status_code == 200:

        response_body = response.json()

        if response_body["message"] == "Data Fetched Successfully":
            pageNo = response_body["pageNo"]
            pageSize = response_body["pageSize"]
            totalRecords = response_body["totalRecords"]

            print("Page No: ", pageNo)
            print("Page Size: ", pageSize)
            print("Total Records: ", totalRecords)

            data_len = len(response_body["metaData"])
            if data_len >= 1:
                found_match = False

                for i in range(data_len):
                    file_name = response_body["metaData"][i]["file-name"]
                    uploadId = response_body["metaData"][i]["uploadId"]

                    #
                    tc_upper = tc.strip().upper()
                    fname = file_name.upper()

                    if (tc_upper == "DDL_FILE" and fname.startswith("RFF_15")) or (
                            tc_upper == "DDL_FILE" and fname.startswith("RFF_ 15")):
                        found_match = True
                    elif (tc_upper == "REMOTE_DIAGNOSTIC_FILE" and fname.startswith("RFF_1002")) or (
                            tc_upper == "REMOTE_DIAGNOSTIC_FILE" and fname.startswith("RFF_ 1002")):
                        found_match = True
                    elif (tc_upper == "TELEMETRY_FILE" and fname.startswith("RFF_5001")) or (
                            tc_upper == "TELEMETRY_FILE" and fname.startswith("RFF_ 5001")):
                        found_match = True
                    elif tc_upper in fname:
                        found_match = True

                    if not found_match:
                        continue

                    # Print all details (your original logic)
                    print("Content Length: ", response_body["metaData"][i]["content-length"])
                    print("File Type: ", response_body["metaData"][i]["file-type"])
                    print("File Created Time: ", response_body["metaData"][i]["file-created-time"])
                    print("Upload Id: ", uploadId)
                    print("System Id: ", response_body["metaData"][i]["system_id"])
                    print("vin: ", response_body["metaData"][i]["vin"])
                    print("file_upload_time: ", response_body["metaData"][i]["file-upload-time"])
                    print("file_name: ", file_name)

                    testResult(self, "passed",
                               "File metadata details should be fetched successfully for the respective vehicle",
                               "File metadata details are fetched successfully for the vehicle")
                    break

                if not found_match:
                    print(f"No file matched tc='{tc}'.")
                    assert False

            else:
                print("No metadata records were processed. Data is empty")
                assert False
        else:
            print("Response message is not expected. Rather than found: ", response_body["message"])
            assert False
    elif response.status_code == 204:
        print("No data available")
        assert False
    else:
        print("Response status code is not expected. Rather than found: ", response.status_code)

    return uploadId, file_name


def get_and_download_ddl_file_v2(self, systemId, file, tc):
    if "DDL_FILE" in file:
        download_folder = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File"
    elif "REMOTE_DIAGNOSTIC_FILE" in file:
        download_folder = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Remote_Diagnostic_File"
    elif "TELEMETRY_FILE" in file:
        download_folder = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Telemetry_File"
    offset = "1"
    limit = "500"
    action = "DOWNLOAD"

    # Ensure directories exist
    os.makedirs(download_folder, exist_ok=True)

    # Clear the download folder
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"[ERROR] Failed to delete {file_path}. Reason: {e}")

    successful_filenames = []

    if "DDL_FILE" in file:
        uploadId, file_name = get_file_metadata(self, offset, limit, systemId, "DDL_FILE")
    elif "REMOTE_DIAGNOSTIC_FILE" in file:
        uploadId, file_name = get_file_metadata(self, offset, limit, systemId, "REMOTE_DIAGNOSTIC_FILE")
    elif "TELEMETRY_FILE" in file:
        uploadId, file_name = get_file_metadata(self, offset, limit, systemId, "TELEMETRY_FILE")
    uploadId = str(uploadId)
    filename = file_name

    response = ddl_download_file_by_uploadId(self, uploadId, action, tc)

    if response and response.status_code == 200:
        download_path = os.path.join(download_folder, filename)
        try:
            print(f"[INFO] Saving file to: {download_path}")
            with open(download_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"[INFO] File downloaded successfully: {download_path}")
            successful_filenames.append(filename)
            testResult(self, "passed", "DDL file download should complete successfully",
                       "DDL file was downloaded and stored correctly.")
        except PermissionError as e:
            print(f"[ERROR] Permission denied: {e}")
            testResult(self, "failed", "DDL file download should complete successfully",
                       f"Permission denied while saving the file: {e}")
        except Exception as e:
            print(f"[ERROR] Unexpected error while saving the file: {e}")
            testResult(self, "failed", "DDL file download should complete successfully",
                       f"Unexpected error while saving the file: {e}")

    return successful_filenames


def decompress_downloaded_files_from_folder_v2(self, tc, successful_filenames, onboarding_Type, chipset_type):
    """
    Push a .data file to IVI device, run conversion stub to generate JSON, and pull the JSON back to local.
    """

    if "DDL_FILE" in tc:
        folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File"
        target_folder = os.path.join(folder_path, "DDL_Decompressed_Files")
        converted_file_folder = os.path.join(folder_path, "DDL_Converted_JSON_File")
    elif "REMOTE_DIAGNOSTIC_FILE" in tc:
        folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Remote_Diagnostic_File"
        target_folder = os.path.join(folder_path, "Remote_Diagnostic_Decompressed_Files")
        converted_file_folder = os.path.join(folder_path, "Remote_Diagnostic_Converted_JSON_File")
    else:
        print("[ERROR] Unknown test case type in 'tc'.")
        testResult(self, "failed", "File conversion should complete successfully",
                   "Unsupported test case type for decompression.")
        return

    # Ensure target folders exist
    os.makedirs(target_folder, exist_ok=True)
    os.makedirs(converted_file_folder, exist_ok=True)

    if not successful_filenames:
        print("[ERROR] No successful filenames provided.")
        return

    print(f"[INFO] Found {len(successful_filenames)} successful filenames.")

    # Select the first file
    filename = successful_filenames[0]
    file_path = os.path.join(folder_path, filename)

    if not os.path.isfile(file_path):
        print(f"[ERROR] File not found: {file_path}")
        testResult(self, "failed", "File decompression should complete successfully",
                   f"File {filename} not found in source folder.")
        return

    try:
        extracted_file_path = os.path.join(target_folder, filename)

        # Detect file type
        with open(file_path, 'rb') as _f:
            magic = _f.read(1)  # Read first byte

        if magic == b'{':
            # File is already JSON
            print(f"[INFO] File {filename} appears to be JSON already. Skipping decompression.")
            extracted_file_path = file_path  # Use original file as-is
        else:
            # Validate Zstd magic number
            with open(file_path, 'rb') as _f:
                magic4 = _f.read(4)
            if magic4 != b'\x28\xb5\x2f\xfd':  # Zstandard magic number
                raise ValueError(
                    f"Invalid compression format for {filename}. "
                    f"Expected Zstd (magic 28 B5 2F FD), got {magic4.hex(' ').upper()}."
                )

            # Proceed with decompression
            print(f"[INFO] Decompressing {filename} locally...")
            with open(file_path, 'rb') as compressed:
                dctx = zstd.ZstdDecompressor()
                with open(extracted_file_path, 'wb') as destination:
                    dctx.copy_stream(compressed, destination)
            print(f"[INFO] Decompression completed: {extracted_file_path}")

        # Push file (decompressed or original) to IVI device
        push_cmd = f"push {extracted_file_path} /data"
        print(f"[INFO] Pushing file with command: {push_cmd}")
        push_result = run_command_on_primary_IVI_device(self, deviceSerialNo, push_cmd)
        print(f"[INFO] File push result: {push_result}")
        time.sleep(3)

        # Run conversion stub
        print("[INFO] Preparing to run conversion stub...")
        stub_result = run_paho_command_on_primary_IVI(self, onboarding_Type, chipset_type, 'ddl_file_conversion_stub')

        run_script_cmd = f"shell sh /data/ddl_file_conversion_stub.sh {filename}"
        print(f"[INFO] Executing stub with command: {run_script_cmd}")
        script_output = run_command_on_primary_IVI_device(self, deviceSerialNo, run_script_cmd)
        print(f"[INFO] Stub execution result: {script_output}")
        time.sleep(3)

        # Pull converted JSON file back to local
        converted_filename = filename.replace(".data", ".json")
        pull_command = f"pull /data/{converted_filename} {converted_file_folder}"
        print(f"[INFO] Pulling converted JSON file with command: {pull_command}")
        pull_result = run_command_on_primary_IVI_device(self, deviceSerialNo, pull_command)
        print(f"[INFO] Pull result: {pull_result}")

        # Validate pull success
        if "No such file" in pull_result or not os.path.isfile(os.path.join(converted_file_folder, converted_filename)):
            print("[ERROR] Converted JSON file not found on device or not pulled locally.")
            testResult(self, "failed", "File conversion should complete successfully",
                       f"Converted JSON file missing for {filename}.")
        else:
            testResult(self, "passed", "File conversion should complete successfully",
                       f"File {filename} processed and JSON pulled successfully.")

    except Exception as e:
        hint = ""
        if isinstance(e, ValueError) and "Invalid compression format" in str(e):
            hint = (" Hint: If you're checking file type on Windows, the 'file' command won't work. "
                    "Use PowerShell 'Format-Hex <file>' to inspect the magic bytes; Zstd should Use PowerShell 'Format-Hex <file>' to inspect the magic bytes; Zstd should start with 28 B5 2F FD.")
        print(f"[ERROR] An error occurred while processing {filename}: {e}.{hint}")
        testResult(self, "failed", "File conversion should complete successfully",
                   "File conversion is not complete successfully")


def validate_telemetry_data_from_decompressed_file_v3(self, cloudEnv, file, tc):
    # Determine folder path (avoid overwriting by using elif)
    if cloudEnv in ["GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8", "GCP-QA2", "GCP-PERF2"]:
        if "DDL_FILE" in file:
            folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File"
        elif "REMOTE_DIAGNOSTIC_FILE" in file:
            folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Remote_Diagnostic_File"
        else:
            print("[ERROR] Unknown file type.")
            return
    else:
        if "DDL_FILE" in file:
            folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\DDL_File\DDL_Converted_JSON_File"
        elif "REMOTE_DIAGNOSTIC_FILE" in file:
            folder_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\Remote_Diagnostic_File\Remote_Diagnostic_Converted_JSON_File"
        else:
            print("[ERROR] Unknown file type.")
            return

    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        try:
            # Avoid shadowing the 'file' parameter
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            # Try to extract JSON from "body" field if present
            match = re.search(r'"body":"({.*?})"', content, re.DOTALL)
            if match:
                body_content = match.group(1).replace('\\"', '"')
                try:
                    body_data = json.loads(body_content)
                except json.JSONDecodeError:
                    print(f"Skipping `{file_name}` due to malformed JSON in `body`.")
                    continue
            else:
                # Try loading full content as JSON directly
                try:
                    body_data = json.loads(content)
                except json.JSONDecodeError:
                    print(f"Skipping `{file_name}` due to malformed full JSON.")
                    continue

            # Determine which key holds telemetry data
            telemetry_key = "telemetry" if "telemetry" in body_data else "data" if "data" in body_data else None
            if not telemetry_key:
                print(f"No telemetry data found in `{file_name}`, skipping...")
                print(f"Top-level keys in `{file_name}`: {list(body_data.keys())}")
                continue

            telemetry_entries = body_data[telemetry_key]
            if isinstance(telemetry_entries, list) and telemetry_entries:
                telemetry_data = telemetry_entries[0].get("data",
                                                          telemetry_entries if telemetry_key == "data" else [])
            else:
                telemetry_data = []

            validation_passed = True

            # Helper: robust numeric detection
            def _is_numeric(val):
                if isinstance(val, (int, float)):
                    return True
                if isinstance(val, str):
                    try:
                        float(val)  # handles negatives and scientific notation
                        return True
                    except ValueError:
                        return False
                return False

            for item in telemetry_data:
                if item.get("id") in [559940097, 559940098]:  # Latitude or Longitude
                    # Collect values from both "value" and "dc"
                    values = []

                    # Direct value
                    if "value" in item:
                        v = item["value"]
                        if isinstance(v, list):
                            values.extend(v)
                        else:
                            values.append(v)

                    # Values under "dc" with multiple possible keys (snakeCase/camelCase)
                    elif "dc" in item:
                        for dc_entry in item.get("dc", []):
                            # Prefer numeric arrays; masked data tends to be string arrays/base64
                            for key in ("floatArrayValue", "doubleArrayValue", "float_array_value", "stringArrayValue",
                                        "string_array_value"):
                                arr = dc_entry.get(key, [])
                                if isinstance(arr, list):
                                    values.extend(arr)
                                elif arr is not None:
                                    # In case a single value is present
                                    values.append(arr)

                    # If no values found, log and continue
                    if not values:
                        print(f"[INFO] No values found for ID {item.get('id')} in {file_name}")
                        continue

                    for value in values:
                        is_numeric = _is_numeric(value)

                        if tc == "ROLE_MASKED":
                            status = "MASKED" if not is_numeric else "NOT MASKED"
                            if status != "MASKED":
                                validation_passed = False
                        elif tc == "ROLE_UNMASKED":
                            status = "UNMASKED" if is_numeric else "MASKED"
                            if status != "UNMASKED":
                                validation_passed = False
                        else:
                            # Unknown role
                            status = "UNKNOWN_ROLE"
                            print(f"[WARN] Unknown role `{tc}`. Expected ROLE_MASKED or ROLE_UNMASKED.")
                            validation_passed = False

                        # Highlight masked/unmasked explicitly
                        if status == "MASKED":
                            print(f"[MASKED DATA] File: {file_name} | ID: {item['id']} | Value: {value}")
                        else:
                            print(
                                f"File: {file_name} | ID: {item['id']} | Role: {tc} | Status: {status} | Value: {value}")

            if validation_passed:
                testResult(self, "passed", "Telemetry validation should complete successfully",
                           f"Telemetry data in {file_name} matches expected masking behavior for role `{tc}`.")
            else:
                testResult(self, "failed", "Telemetry validation should complete successfully",
                           f"Telemetry data in {file_name} does NOT match expected masking behavior for role `{tc}`.")
                return  # Stop further execution if validation fails

        except Exception as e:
            print(f"[ERROR] Error processing {file_name}: {e}")
            testResult(self, "failed", "Telemetry validation should complete successfully",
                       "Telemetry validation is not complete successfully")


def ddl_token_file_upload(self, fileName, fileSize, hashAlgorithm, hash, fileType, action, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_token_file_upload")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["files"][0]["fileName"] = fileName
    json_object["files"][0]["fileSize"] = fileSize
    json_object["files"][0]["hashAlgorithm"] = hashAlgorithm
    json_object["files"][0]["hash"] = hash
    json_object["files"][0]["fileType"] = fileType
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload), stream=True)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DDL_token_file_upload', response.text)
    save_api_resp_in_excel(self, "API_Data", "DDL_token_file_upload", response.text)

    return response


def ddl_delete_file(self, uploadId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DDL_delete_API")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{uploadId}', uploadId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload), stream=True)

    return response


