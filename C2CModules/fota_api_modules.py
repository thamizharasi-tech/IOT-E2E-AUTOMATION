import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel, XlsxReader, save_data_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# FOTA API Reusable modules :


# FOTA-firmwareUpload

def FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase, isFull, downloadConsent, installConsent,
                        rebootConsent, filename, firmwareVer, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if temp == "no_model":
        del json_object["model"]
    else:
        json_object["model"] = model
    if temp == "no_system":
        del json_object["system"]
    else:
        json_object["system"] = system
    if temp == "no_description":
        del json_object["description"]
    else:
        json_object["description"] = description
    if temp == "no_isDiffImage":
        del json_object["isDiffImage"]
    else:
        json_object["isDiffImage"] = isDiffImage
    if temp == "no_isBase":
        del json_object["isBase"]
    else:
        json_object["isBase"] = isBase
    if temp == "no_isFull":
        del json_object["isFull"]
    else:
        json_object["isFull"] = isFull
    if temp == "no_downloadConsent":
        del json_object["downloadConsent"]
    else:
        json_object["downloadConsent"] = downloadConsent
    if temp == "no_installConsent":
        del json_object["installConsent"]
    else:
        json_object["installConsent"] = installConsent

    if temp == "no_rebootConsent":
        del json_object["rebootConsent"]
    else:
        json_object["rebootConsent"] = rebootConsent

    if temp == "no_filename":
        del json_object["filename"]
    else:
        json_object["filename"] = filename

    # json_object["firmwareVersion"] = firmwareVer
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

    return response


# FOTA-createScript

def FOTA_createScript(self, model, ScriptName, precondition, ecu_type, sourceVersion, targetVersion, releaseNote, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :

    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["name"] = ScriptName
    json_object["precondition"][0] = precondition
    json_object["steps"][0]["ecu"] = ecu_type
    json_object["steps"][0]["sourceVersion"] = sourceVersion
    json_object["steps"][0]["targetVersion"] = targetVersion
    json_object["releaseNote"] = releaseNote
    if "no_model" in temp:
        del json_object["model"]
    elif "no_name" in temp:
        del json_object["name"]
    elif "no_precondition" in temp:
        del json_object["precondition"]
    elif "no_ecu" in temp:
        del json_object["steps"][0]["ecu"]
    elif "no_sourceVersion" in temp:
        del json_object["steps"][0]["sourceVersion"]
    elif "no_targetVersion" in temp:
        del json_object["steps"][0]["targetVersion"]
    elif "no_releaseNote" in temp:
        del json_object["releaseNote"]

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

    return response


# FOTA-edit script
def FOTA_scriptReleaseNoteUpdate(self, scriptId, releaseNote, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-PATCH-scriptReleaseNoteUpdate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scriptId}', scriptId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :

    json_object = json.loads(payload)
    json_object["release-note"] = releaseNote
    if "no_releaseNote" in temp:
        del json_object["release-note"]

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
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-PATCH-scriptReleaseNoteUpdate",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-PATCH-scriptReleaseNoteUpdate', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-PATCH-scriptReleaseNoteUpdate", response.text)

    return response


# FOTA-edit firmware
def FOTA_firmwareDescriptionUpdate(self, firmId, description, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-PATCH-firmwareDescription")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{firmId}', str(firmId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :

    json_object = json.loads(payload)
    json_object["description"] = description
    if "no_description" in temp:
        del json_object["description"]

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
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-PATCH-firmwareDescription",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-PATCH-firmwareDescription', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-PATCH-firmwareDescription", response.text)

    return response




# FOTA-GetAllFirmware

def FOTA_GetAllFirmware(self, pageNo, pageSize, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllFirmware")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if "{pageNo}" in endpoint or "{pageSize}" in endpoint:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)
    elif "pageNumber" in endpoint or "pageSize" in endpoint:
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=" + str(pageNo)).replace(
            'pageSize=', "pageSize=" + pageSize)
    else:
        complete_url = str(base_url + endpoint)

    if "removeQueryParams_from_url" in temp:
        # Remove query params from the url
        complete_url = complete_url.split('?')[0]
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    return response


# FOTA-Get-Firmware-models

def FOTA_GetFirmwareModels(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetFirmwareModels")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

def FOTA_getVersionDetails(self, modelName, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    return response


# FOTA-Get-Scriptmodel

def FOTA_getScriptModel(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetScriptModel")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetScriptModel",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetScriptModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetScriptModel", response.text)


    return response


# FOTA-GetAllScriptDetails

def FOTA_GetAllScriptDetails(self, pageNo, pageSize, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllScriptDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if "{pageNo}" in endpoint or "{pageSize}" in endpoint:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)
    elif "pageNumber" in endpoint or "pageSize" in endpoint:
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=" + str(pageNo)).replace(
            'pageSize=', "pageSize=" + pageSize)
    else:
        complete_url = str(base_url + endpoint)
    if "removeQueryParams_from_url" in temp:
        # Remove query params from the url
        complete_url = complete_url.split('?')[0]
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    print("API response status code is :", str(response.status_code))

    return response


# FOTA-createPresigneUrl

def FOTA_createPresigneUrl(self, filename, system, model_name, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if temp == "no_filename":
        del json_object["filename"]
    else:
        json_object["filename"] = filename
    if temp == "no_system":
        del json_object["system"]
    else:
        json_object["system"] = system
    if temp == "no_model":
        del json_object["model-name"]
    else:
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

    return response


# FOTA-uploadFile

def FOTA_uploadFile(self, upload_url, filepath, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-uploadFile")
    # base_url = str(dict["Base Url"])
    # endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    # payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    return response


# FOTA-createSchedule

def FOTA_createSchedule(self, vin, scriptId, startDate, endDate, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if temp == "no_vin":
        del json_object["vins"]
    else:
        json_object["vins"][0] = vin
    if temp == "no_scriptId":
        del json_object["scriptid"]
    else:
        json_object["scriptid"] = scriptId
    if temp == "no_startDate":
        del json_object["period"]["startDate"]
    else:
        json_object["period"]["startDate"] = startDate
    if temp == "no_endDate":
        del json_object["period"]["endDate"]
    else:
        json_object["period"]["endDate"] = endDate
    if temp == "no_period":
        del json_object["period"]
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

    return response


# FOTA-GetAllScheduleDetails

def FOTA_GetAllScheduleDetails(self, pageNo, pageSize, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetAllScheduleDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if "{pageNo}" in endpoint or "{pageSize}" in endpoint:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)
    elif "pageNumber" in endpoint or "pageSize" in endpoint:
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=" + str(pageNo)).replace(
            'pageSize=', "pageSize=" + pageSize)
    else:
        complete_url = str(base_url + endpoint)

    if "removeQueryParams_from_url" in temp:
        # Remove query params from the url
        complete_url = complete_url.split('?')[0]

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    return response


# FOTA-GetScheduleStatus

def FOTA_GetScheduleStatus(self, scheduleId, vin, temp):
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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

    return response


# FOTA-GetPreconditions
def FOTA_GetPreconditions(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetPrecondition")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetPrecondition",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetPrecondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetPrecondition", response.text)
    return response


# FOTA-FOTA-GetListOfModels&Count

def FOTA_GetListOfModelsCount(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetListOfModels&Count")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetListOfModels&Count",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetListOfModels&Count', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetListOfModels&Count", response.text)

    return response


def FOTA_GetListOfModelsCount(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-GetListOfModels&Count")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetListOfModels&Count",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-GetListOfModels&Count', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-GetListOfModels&Count", response.text)

    return response



def FOTA_deleteFirmware(self, firmId, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-DeleteFirmware")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{firmId}', str(firmId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteFirmware",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-DeleteFirmware', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-DeleteFirmware", response.text)

    return response


def FOTA_deleteScript(self, scriptId, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-DeleteScript")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scriptId}', str(scriptId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteScript",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-DeleteScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-DeleteScript", response.text)

    return response


def FOTA_deleteSchedule(self, scheduleId, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "FOTA-DeleteSchedule")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', str(scheduleId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "FOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteSchedule",
                                                "FOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('FOTA-DeleteSchedule', response.text)
    save_api_resp_in_excel(self, "API_Data", "FOTA-DeleteSchedule", response.text)

    return response



# Reusable modules
def get_model_by_getListOfModelsCount_api(self):
    # get model
    response = FOTA_GetListOfModelsCount(self, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        data_len = len(response_body["responseData"]["data"])
        if data_len>= 1:
            for i in range(data_len):
                model = response_body["responseData"]["data"][i]
                if model == "adp":
                    model = "adp"
                    break
                else:
                    model = response_body["responseData"]["data"][0]
            print("Module : ", model)

        else:
            print(" => module datalist is empty")
            model = ""
            assert False
    return model

def get_firmId_from_firmwareDetails_api(self):
    # call api reusable module
    global firmId
    response = FOTA_GetAllFirmware(self, str(1), str(10), "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        if len(response_body["responseData"]["data"]) >= 1:
            firmId = response_body["responseData"]["data"][0]["id"]
        else:
            print("datalist is empty")
            firmId = ""
    return firmId

def get_ScriptId_from_ScriptDetails_api(self):
    # call api reusable module
    response = FOTA_GetAllScriptDetails(self, str(1), str(10), "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        if len(response_body["responseData"]["data"]) >= 1:
            refId = response_body["responseData"]["data"][0]["refId"]
            print("Ref Id : ", response_body["responseData"]["data"][0]["refId"])
        else:
            print("datalist is empty")
            refId = ""
    return refId

def get_ScheduledId_from_ScheduleDetails_api(self):
    # call api reusable module
    response = FOTA_GetAllScheduleDetails(self, str(1), str(10), "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        if len(response_body["responseData"]["data"]) >= 1:
            refId = response_body["responseData"]["data"][0]["refId"]
            print("Ref Id : ", response_body["responseData"]["data"][0]["refId"])
        else:
            print("datalist is empty")
            refId = ""
    return refId

def get_preCondition_from_preconditionDetails_api(self):
    # call api reusable module
    global precondition
    response = FOTA_GetPreconditions(self, "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        if len(response_body["responseData"]["data"]) >= 1:
            precondition = response_body["responseData"]["data"][0]["precondition"]
            print("precondition : ", precondition)
        else:
            print("datalist is empty")
            precondition = ""
    return precondition

def get_verisons_from_versionDetails_api(self, model):
    # call api reusable module
    global sourceVersion, targetVersion
    response = FOTA_getVersionDetails(self, model,"valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(14000) or response_body["responseCode"] == 14000:
        message = response_body["responseData"]["message"]
        print('Message : ', message)
        data_len = len(response_body["responseData"]["data"])
        if data_len >= 1:
            print("ECU : ", response_body["responseData"]["data"]["ecus"][0]["ecu"])
            sourceVersion = response_body["responseData"]["data"]["ecus"][0]["srcVersions"][0]
            targetVersion = response_body["responseData"]["data"]["ecus"][0]["targetVersions"][1]
            if sourceVersion == targetVersion:
                sourceVersion = response_body["responseData"]["data"]["ecus"][0]["srcVersions"][0]
                targetVersion = response_body["responseData"]["data"]["ecus"][0]["targetVersions"][2]
            print("Source Versions : ", sourceVersion)
            print("target Versions : ", targetVersion)
        else:
            print("datalist is empty")
            sourceVersion = targetVersion = ""
    return sourceVersion, targetVersion



def save_firmwareId_in_excel(self, firmwareId):
    save_data_in_excel(self, "FOTA", 'FOTA-GetAllFirmware', 16, firmwareId)
    save_data_in_excel(self, "FOTA", 'FOTA-PATCH-firmwareDescription', 16, firmwareId)
    save_data_in_excel(self, "FOTA", 'FOTA-DeleteFirmware', 16, firmwareId)
    save_data_in_excel(self, "FOTA", 'FOTA-GetAllFirmware_pageNo_lessthanZero', 16, firmwareId)
    save_data_in_excel(self, "FOTA", 'FOTA-DeleteFirmware', 16, firmwareId)
    save_data_in_excel(self, "FOTA", 'FOTA-DeleteFirmware', 16, firmwareId)
