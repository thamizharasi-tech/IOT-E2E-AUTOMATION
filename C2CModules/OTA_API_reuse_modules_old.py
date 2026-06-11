import ast
import json
import time

import requests

from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel


# ---------------------------------
# API Modules
# ---------------------------------

# FOTA API Reusable modules :


# FOTA-firmwareUpload

def FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase, isFull, downloadConsent, installConsent,
                        rebootConsent, filename, firmwareVer):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-firmwareUpload")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["system"] = system
    json_object["description"] = description
    json_object["isDiffImage"] = isDiffImage
    json_object["isBase"] = isBase
    json_object["isFull"] = isFull
    json_object["downloadConsent"] = downloadConsent
    json_object["installConsent"] = installConsent
    json_object["rebootConsent"] = rebootConsent
    # json_object["firmwareVersion"] = firmwareVer
    json_object["filename"] = filename
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-firmwareUpload",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-firmwareUpload', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-firmwareUpload", response.text)

    # Validate response status code
    assert (
                response.status_code == 200 or response.status_code == 400), "Status code is not 200. Rather found : " + str(
        response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-createScript

def FOTA_createScript(self, model, ScriptName, precondition, ecu_type, sourceVersion, targetVersion, releaseNote):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-createScript")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :

    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["name"] = ScriptName
    json_object["precondition"][0] = precondition
    json_object["steps"][0]["ecu"] = ecu_type
    json_object["steps"][0]["sourceVersion"] = sourceVersion
    json_object["steps"][0]["targetVersion"] = targetVersion
    json_object["releaseNote"] = releaseNote
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createScript",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-createScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-createScript", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-GetAllFirmware

def FOTA_GetAllFirmware(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllFirmware")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllFirmware",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetAllFirmware', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetAllFirmware", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-Get-Firmware-models

def FOTA_Get_Firmware_models(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-Get-Firmware-models")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-Get-Firmware-models",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-Get-Firmware-models', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-Get-Firmware-models", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-getVersionDetails

def FOTA_getVersionDetails(self, modelName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-getVersionDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{modelName}', modelName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-getVersionDetails",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-getVersionDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-getVersionDetails", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-Get-Scriptmodel

def FOTA_Get_Scriptmodel(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-Get-Scriptmodel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-Get-Scriptmodel",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-Get-Scriptmodel', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-Get-Scriptmodel", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-GetAllScriptDetails

def FOTA_GetAllScriptDetails(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllScriptDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllScriptDetails",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetAllScriptDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetAllScriptDetails", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-createPresigneUrl

def FOTA_createPresigneUrl(self, filename, system, model_name):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-createPresigneUrl")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filename"] = filename
    json_object["system"] = system
    json_object["model-name"] = model_name
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createPresigneUrl",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-createPresigneUrl', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-createPresigneUrl", response.text)

    # Validate response status code
    if response.status_code == 200 or response.status_code == 400:
        assert True
    else:
        print(response)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-uploadFile

def FOTA_uploadFile(self, upload_url, filepath):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-uploadFile")
    # base_url = str(dict["Base Url"])
    # endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    # payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(upload_url, headers=header_x, data=open(filepath, 'rb').read())

    print("API response : ", response)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-uploadFile",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.put(upload_url, headers=headers, data=open(filepath, 'rb').read())
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    # save_api_resp_into_file('FOTA-uploadFile', response.text)
    # save_api_resp_in_excel(self, "API_Data", "FOTA-uploadFile", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = ''

    return response_body


# FOTA-createSchedule

def FOTA_createSchedule(self, vin, scriptId, startDate, endDate):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-createSchedule")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vins"][0] = vin
    json_object["scriptid"] = scriptId
    json_object["period"]["startDate"] = startDate
    json_object["period"]["endDate"] = endDate
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createSchedule",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-createSchedule', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-createSchedule", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-GetAllScheduleDetails

def FOTA_GetAllScheduleDetails(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllScheduleDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllScheduleDetails",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetAllScheduleDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetAllScheduleDetails", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-GetScheduleStatus

def FOTA_GetScheduleStatus(self, scheduleId, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetScheduleStatus")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', scheduleId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vins"] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    pload = json.dumps(payload)
    print("------------------", pload)
    response = requests.post(complete_url, headers=header_x, data=pload)
    print("API response : ", response.text)
    print(response)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetScheduleStatus",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetScheduleStatus', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetScheduleStatus", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# FOTA-GetPreconditions
def FOTA_GetPreconditions(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-Get-Precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-Get-Precondition",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-Get-Precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-Get-Precondition", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA API reusable modules :

# SOTA-CreatePresignUrl

def SOTA_CreatePresignUrl(self, filename, system, model_name):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreatePresignUrl")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filename"] = filename
    json_object["system"] = system
    json_object["model-name"] = model_name
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreatePresignUrl",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreatePresignUrl', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreatePresignUrl", response.text)

    # Validate response status code
    if response.status_code == 200 or response.status_code == 400:
        assert True
    else:
        print(response)
        assert False

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-uploadPackage

def SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase, isFull, downloadConsent, installConsent,
                       rebootConsent, packageName, packageVersion):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-uploadPackage")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    # print(payload)
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["system"] = system
    json_object["description"] = description
    json_object["isDiffImage"] = isDiffImage
    # json_object["isBase"] = isBase
    # json_object["isFull"] = isFull
    json_object["downloadConsent"] = downloadConsent
    json_object["installConsent"] = installConsent
    json_object["rebootConsent"] = rebootConsent
    json_object["packageVersion"] = packageVersion
    json_object["packageName"] = packageName
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadPackage",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-uploadPackage', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-uploadPackage", response.text)

    # Validate response status code
    assert (
                response.status_code == 200 or response.status_code == 400), "Status code is not 200. Rather found : " + str(
        response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-CreateScript

def SOTA_CreateScript(self, model, system, scriptName, command, appName, targetVersion, notes):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreateScript")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["system"] = system
    json_object["scriptName"] = scriptName
    json_object["command"] = command
    json_object["appName"] = appName
    json_object["targetVersion"] = targetVersion
    json_object["notes"] = notes
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateScript",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreateScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreateScript", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-uploadFile

def SOTA_uploadFile(self, upload_url, filepath):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-uploadFile")
    # base_url = str(dict["Base Url"])
    # endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    # payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Header :
    header_x = ast.literal_eval(headers)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    print(upload_url)
    # payload = {'file': filepath}
    # print(filepath)
    response = requests.put(upload_url, data=filepath, headers=header_x)
    print("API response : ", response.text)

    # try:
    #     # Parse API response into JSON
    #     response_body = response.json()
    #
    #     if response_body["Message"] == "User is not authorized to access this resource":
    #         print("\n")
    #         # Generate token
    #         token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
    #         update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadFile",
    #                                             "SOTA-GetToken")
    #         time.sleep(60)
    #         response = requests.put(upload_url, data=filepath, headers=headers)
    #         print("API response : ", response.text)
    # except:
    #     print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    # save_api_resp_into_file('SOTA-uploadFile', response.text)
    # save_api_resp_in_excel(self, "API_Data", "SOTA-uploadFile", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    # response_body = response.json()
    response_body = ''

    return response_body


# SOTA-ListPackages

def SOTA_ListPackages(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListPackages")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListPackages",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListPackages', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListPackages", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-ListScripts

def SOTA_ListScripts(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListScripts")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScripts",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListScripts', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListScripts", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-CreateSchedule

def SOTA_CreateSchedule(self, vin, scriptId, startDate, endDate):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreateSchedule")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    # print(payload)
    json_object = json.loads(payload)
    json_object["vins"][0] = vin
    json_object["scriptId"] = scriptId
    json_object["period"]["startDate"] = startDate
    json_object["period"]["endDate"] = endDate
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateSchedule",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreateSchedule', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreateSchedule", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-ListSchedules

def SOTA_ListSchedules(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListSchedules")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListSchedules",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListSchedules', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListSchedules", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-List ScheduleVin

def SOTA_ListScheduleVin(self, scheduleId, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListScheduleVin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', scheduleId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vins"][0] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScheduleVin",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListScheduleVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListScheduleVin", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-GetPreconditions

def SOTA_GetPreconditions(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-GetPreconditions")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-GetPreconditions",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-GetPreconditions', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-GetPreconditions", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-ListApps

def SOTA_ListApps(self, model):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListApps")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{modelName}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListApps",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListApps', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListApps", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-ListModels1

def SOTA_ListModels1(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListModels1")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels1",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListModels1', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListModels1", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-ListModels

def SOTA_ListModels(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListModels")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListModels', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListModels", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-UpdatePackageDescription

def SOTA_UpdatePackageDescription(self, packageId, desc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-UpdatePackageDescription")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{PackageId}', packageId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object['description'] = desc
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-UpdatePackageDescription",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-UpdatePackageDescription', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-UpdatePackageDescription", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-EditScriptNotes

def SOTA_EditScriptNotes(self, reqId, desc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-EditScriptNotes")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{reqId}', reqId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object['description'] = desc
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-EditScriptNotes",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-EditScriptNotes', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-EditScriptNotes", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-DeletePackage

def SOTA_DeletePackage(self, packageId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeletePackage")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{PackageId}', packageId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeletePackage",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeletePackage', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeletePackage", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-DeleteScript

def SOTA_DeleteScript(self, scriptId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeleteScript")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{reqId}', scriptId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteScript",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeleteScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeleteScript", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SOTA-DeleteScript_scheduleId

def SOTA_DeleteScript_scheduleId(self, scheduleId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeleteScript_scheduleId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', scheduleId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteScript_scheduleId",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeleteScript_scheduleId', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeleteScript_scheduleId", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


def mahindra_create_incident(self, system_id):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Mahindra_CreateIncident")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', system_id)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Success":
            print("\n")

        else:
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Mahindra_getToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Mahindra_CreateIncident",
                                                "Mahindra-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('mahindra-create-incident', response.text)
    save_api_resp_in_excel(self, "API_Data", "mahindra-create-incident", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


