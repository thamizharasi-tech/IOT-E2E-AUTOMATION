import ast
import json
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# COTA - telemetry-cota-controller

def COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code, enable, frequency,
                           data_items, filter_plugins, msg_type, buffer1, count1, timeout1, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_telemetry_request")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["buffer"] = buffer
    json_object["count"] = count
    json_object["timeout"] = timeout
    json_object["config"][0]["operation"] = operation
    json_object["config"][0]["block_id"] = block_id
    json_object["config"][0]["reason_code"] = reason_code
    json_object["config"][0]["enable"] = enable
    json_object["config"][0]["frequency"] = frequency
    json_object["config"][0]["data_items"][0] = data_items
    json_object["config"][0]["filter_plugins"][0] = filter_plugins
    json_object["config"][0]["msg_type"] = msg_type
    json_object["config"][0]["buffer"] = buffer1
    json_object["config"][0]["count"] = count1
    json_object["config"][0]["timeout"] = timeout1

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_telemetry_request', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_telemetry_request", response.text)

    return response


def COTA_telemetry_getCotaDetails_by_requestId(self, requestId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_telemetry_getCotaDetails_by_requestId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{requestId}', requestId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_telemetry_getCotaDetails_by_requestId', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_telemetry_getCotaDetails_by_requestId", response.text)

    return response


def COTA_telemetry_getCurrentState(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_telemetry_getCurrentState")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_telemetry_getCurrentState', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_telemetry_getCurrentState", response.text)

    return response


def COTA_liveCommandTracking_getCurrentFrequency(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_liveCommandTracking_getCurrentFrequency")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_liveCommandTracking_getCurrentFrequency', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_liveCommandTracking_getCurrentFrequency", response.text)

    return response


# COTA - command-cota-controller

def COTA_command_request(self, systemId, enable, operation, ccid, name, precondition, postcondition, condition_handler,
                          command_handler, timeout, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_command_request")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["config"][0]["enable"] = enable
    json_object["config"][0]["operation"] = operation
    if tc == "no_ccid":
        del json_object["config"][0]["ccid"]
    else:
        json_object["config"][0]["ccid"] = ccid
    if tc == "no_name":
        del json_object["config"][0]["name"]
    else:
        json_object["config"][0]["name"] = name
    json_object["config"][0]["precondition"][0] = precondition
    json_object["config"][0]["postcondition"][0] = postcondition
    json_object["config"][0]["condition_handler"] = condition_handler
    json_object["config"][0]["command_handler"] = command_handler
    json_object["config"][0]["timeout"] = timeout

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_command_request', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_command_request", response.text)

    return response


def COTA_command_getCotaDetails_by_requestId(self, requestId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_command_getCotaDetails_by_requestId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{requestId}', requestId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_command_getCotaDetails_by_requestId', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_command_getCotaDetails_by_requestId", response.text)

    return response


def COTA_command_getCurrentState(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "COTA_command_getCurrentState")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('COTA_command_getCurrentState', response.text)
    save_api_resp_in_excel(self, "API_Data", "COTA_command_getCurrentState", response.text)

    return response
