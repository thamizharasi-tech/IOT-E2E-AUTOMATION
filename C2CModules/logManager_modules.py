import ast
import json
import time
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import logManager_token_generation, logManager_update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel


# ---------------------------
# Incident-controller APIs
# ---------------------------
def logManager_createIncident(self, systemId, notes, userName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_CreateIncident")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object[0]["notes"] = notes
    json_object[0]["userName"] = userName
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:

        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_CreateIncident",
                                                           "LogManager_getToken")

            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_CreateIncident', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_CreateIncident", response.text)

    return response


def logManager_updateIncident(self, systemId, incidentId, notes, userName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_UpdateIncident")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{incidentId}', str(incidentId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object[0]["notes"] = notes
    json_object[0]["userName"] = userName
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateIncident",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_UpdateIncident', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_UpdateIncident", response.text)

    return response


def logManager_fetchIncidentDetails(self, systemId, offset, limit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchIncidentDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{offset}', offset).replace(
        '{limit}', limit)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchIncidentDetails",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchIncidentDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchIncidentDetails", response.text)

    return response


# ---------------------------
# Log Config APIs
# ---------------------------

def logManager_fetchLogConfig(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchLogConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchLogConfig",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchLogConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchLogConfig", response.text)

    return response


def logManager_updateLogConfig(self, systemId, uploadInterval, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_UpdateLogConfig")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["uploadInterval"] = uploadInterval
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateLogConfig",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_UpdateLogConfig', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_UpdateLogConfig", response.text)

    return response


def logManager_updateLogConfig_status(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_UpdateLogConfig_status")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateLogConfig_status",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_UpdateLogConfig_status', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_UpdateLogConfig_status", response.text)

    return response


# ---------------------------
# User Vehicle APIs
# ---------------------------


def logManager_fetchAllUserDetails_onTheBasisOfVehicleId(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                           "LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId", response.text)

    return response


def logManager_saveAllUser_registeredWithVehicleId(self, systemId, text, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_SaveAllUser_RegisteredWithVehicleId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object[0] = text
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                           "LogManager_SaveAllUser_RegisteredWithVehicleId",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_SaveAllUser_RegisteredWithVehicleId', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_SaveAllUser_RegisteredWithVehicleId", response.text)

    return response


def logManager_fetchAllVehiclesDetails_onTheBasisOfUsername(self, userName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', userName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                           "LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername", response.text)

    return response


def logManager_saveVehicleDetailsToUser(self, userName, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', userName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object[0] = systemId

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_SaveVehicleDetailsToUser', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser", response.text)

    return response


def logManager_fetchAllUserDetails(self, offset, limit, sortDirection, sortBy, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchAllUserDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace(
        '{limit}', limit).replace('{sortDirection}', sortDirection).replace('{sortBy}', sortBy)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            # Generate token
            print("Generate token : ")
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchAllUserDetails",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchAllUserDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchAllUserDetails", response.text)

    return response


def logManager_saveVehicleDetailsToUser1(self, userName, systemId, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', userName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vehiclesAssigned"][0]["systemId"] = systemId
    json_object["vehiclesAssigned"][0]["vin"] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_SaveVehicleDetailsToUser', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser", response.text)

    return response


# ---------------------------
# Log Management APIs
# ---------------------------

def logManager_fetchVehicleDetails(self, offset, limit, sortDirection, sortBy, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchVehicleDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace(
        '{limit}', limit).replace('{sortDirection}', sortDirection).replace('{sortBy}', sortBy)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchVehicleDetails",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchVehicleDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchVehicleDetails", response.text)

    return response


def logManager_fetchLogFiles_basedOnLogSearchCriteria(self, systemId, offset, limit, sortDirection, sortBy, logName,
                                                      logType, logUploadType, incidentId,
                                                      notes, fromDate, toDate, fileCreatedTime, incidentIdReport, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchLogFiles_basedOnLogSearchCriteria")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{offset}', offset).replace(
        '{limit}', limit).replace('{sortDirection}', sortDirection).replace('{sortBy}', sortBy)

    if logName == "NA":
        complete_url = complete_url.replace('&logName={logName}', '')
    else:
        complete_url = complete_url.replace('{logName}', logName)
    if logType == "NA":
        complete_url = complete_url.replace('&logType={logType}', '')
    else:
        complete_url = complete_url.replace('{logType}', logType)
    if logUploadType == "NA":
        complete_url = complete_url.replace('&logUploadType={logUploadType}', '')
    else:
        complete_url = complete_url.replace('{logUploadType}', logUploadType)
    if incidentId == "NA":
        complete_url = complete_url.replace('&incidentId={incidentId}', '')
    else:
        complete_url = complete_url.replace('{incidentId}', str(incidentId))
    if notes == "NA":
        complete_url = complete_url.replace('&notes={notes}', '')
    else:
        complete_url = complete_url.replace('{notes}', notes)
    if fromDate == "NA":
        complete_url = complete_url.replace('&fromDate={fromDate}', '')
    else:
        complete_url = complete_url.replace('{fromDate}', str(fromDate))
    if toDate == "NA":
        complete_url = complete_url.replace('&toDate={toDate}', '')
    else:
        complete_url = complete_url.replace('{toDate}', str(toDate))
    if fileCreatedTime == "NA":
        complete_url = complete_url.replace('&fileCreatedTime={fileCreatedTime}', '')
    else:
        complete_url = complete_url.replace('{fileCreatedTime}', str(fileCreatedTime))
    if incidentIdReport == "NA":
        complete_url = complete_url.replace('&incidentIdReport={incidentIdReport}', '')
    else:
        complete_url = complete_url.replace('{incidentIdReport}', str(incidentIdReport))

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchLogFiles",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchLogFiles', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchLogFiles", response.text)

    return response


def logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_FetchLogFiles")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{offset}', offset).replace(
        '{limit}', limit).replace('{sortDirection}', sortDirection).replace('{sortBy}', sortBy)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchLogFiles",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_FetchLogFiles', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_FetchLogFiles", response.text)

    return response


def logManager_downloadAndViewLogFileContent(self, systemId, logId, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_DownloadAndViewLogFileContent")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace(
        '{LogId}', str(logId)).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_DownloadAndViewLogFileContent",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_DownloadAndViewLogFileContent', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_DownloadAndViewLogFileContent", response.text)

    return response


def logManager_addDescriptionToLogFile(self, systemId, logId, description, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_AddDescriptionToLogFile")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{LogId}', str(logId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["description"] = description
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_AddDescriptionToLogFile",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_AddDescriptionToLogFile', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_AddDescriptionToLogFile", response.text)

    return response


def logManager_deleteLogFile(self, systemId, logId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_DeleteLogFile")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{LogId}', str(logId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        if response.status_code == 401:
            print("Generate token : ")
            # Generate token
            logManager_token_generation(self)
            logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_DeleteLogFile",
                                                           "LogManager_getToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)

    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_DeleteLogFile', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_DeleteLogFile", response.text)

    return response
