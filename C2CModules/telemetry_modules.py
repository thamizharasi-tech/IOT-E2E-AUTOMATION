import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *


# Telemetry - Telemetry_Curr
def telemetry_Curr(self, event_type, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId).replace('{eventTypeValue}',
                                                                                 str(event_type))
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body["message"]))
        assert False

    assert (response_body["responseData"]["message"] == "Successfully fetched the current values")

    return response_body


# Telemetry_CurrForEventType
def telemetry_Curr_eventType(self, event_type, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_CurrForEventType")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{eventType}',
                                                                                    str(event_type))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_CurrForEventType",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_CurrForEventType', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_CurrForEventType", response.text)

    return response


# Telemetry_Curr_byVIN
def telemetry_Curr_byVIN(self, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_byVIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{vin}', vin)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_byVIN",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_byVIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_byVIN", response.text)

    return response


# Telemetry_Curr_byVINandEventType
def telemetry_Curr_byVIN_eventType(self, event_type, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_byVINandEventType")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{vin}', vin).replace('{eventType}',
                                                                          str(event_type))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_CurrForEventType",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_byVINandEventType', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_byVINandEventType", response.text)

    return response


# Telemetry_Curr_byVINandEventIds
def telemetry_Curr_byVINandEventIds(self, event_id, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_byVINandEventIds")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{vin}', vin)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object['ids'][0] = event_id
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_byVINandEventIds",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_byVINandEventIds', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_byVINandEventIds", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body["message"]))
        assert False

    assert (response_body["responseData"]["message"] == "Successfully fetched the current values")

    return response_body


# Telemetry_CurrForEventType
def telemetry_Curr_eventType(self, event_type, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_CurrForEventType")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)

    if tc == "no_eventType":
        complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('?eventType={eventType}',
                                                                                    "")
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('{eventType}',
                                                                                             str(event_type))
    complete_url = complete_url.replace(' ', '')

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    #print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_CurrForEventType",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_CurrForEventType', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_CurrForEventType", response.text)

    return response


# Telemetry - Telemetry_Curr_sensorValues
def telemetry_Curr_sensorValues(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_sensorValues")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_sensorValues",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_sensorValues', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_sensorValues", response.text)

    return response


# Telemetry - Telemetry_Curr_sensorValues
def telemetry_Curr_sensorElements(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_sensorElements")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_sensorElements",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_sensorElements', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_sensorElements", response.text)

    return response


# Telemetry - Telemetry_Curr_remaining charge
def telemetry_Curr_remainingCharge(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_remainingCharge")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data",
                                                "Telemetry_Curr_remainingCharge",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_remainingCharge', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_remainingCharge", response.text)

    return response


# Telemetry Metadata details
def telemetry_metadata_details(self, elementId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Metadata_Details")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    if tc == "no_elementId":
        print(endpoint)
        endpoint = endpoint.replace('?elementId={elementId}', '')
        complete_url = str(base_url + endpoint)
    elif tc == "empty_elementId":
        complete_url = str(base_url + endpoint).replace('{elementId}', '')
    else:
        complete_url = str(base_url + endpoint).replace('{elementId}', elementId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_Metadata_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Metadata_Details",
                                                "Telemetry_Metadata_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Metadata_Details', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Metadata_Details", response.text)

    return response


# Telemetry Publisher Config
def telemetry_publisher_config(self, eventType, isActive, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryPublisher")
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
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_eventType":
        del json_object['eventType']
    else:
        json_object['eventType'] = eventType
    if tc == "no_isActive":
        del json_object['isActive']
    else:
        json_object['isActive'] = isActive
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryPublisher")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryPublisher",
                                                "TelemetryPublisher_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryPublisher', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryPublisher", response.text)

    return response


# SOS SERVICE
def Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type, reason_code,
                tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Sos_Service")
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
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_vin":
        del json_object["meta"]['vin']
    else:
        json_object["meta"]['vin'] = vin
    if tc == "no_deviceId":
        del json_object["meta"]['device_id']
    else:
        json_object["meta"]['device_id'] = device_id
    if tc == "no_systemId":
        del json_object["meta"]['system_id']
    else:
        json_object["meta"]['system_id'] = system_id
    if tc == "no_subsystemId":
        del json_object["meta"]['sub_system_id']
    else:
        json_object["meta"]['sub_system_id'] = sub_system_id
    if tc == "no_time":
        del json_object["telemetry"][0]['time']
    else:
        json_object["telemetry"][0]['time'] = time
    if tc == "no_id":
        del json_object["telemetry"][0]["data"][0]['id']
    else:
        json_object["telemetry"][0]["data"][0]['id'] = elementId
    if tc == "no_area":
        del json_object["telemetry"][0]["data"][0]['area']
    else:
        json_object["telemetry"][0]["data"][0]['area'] = area
    if tc == "no_value":
        del json_object["telemetry"][0]["data"][0]['value']
    else:
        json_object["telemetry"][0]["data"][0]['value'] = value
    if tc == "no_eventType":
        del json_object["telemetry"][0]['event_type']
    else:
        json_object["telemetry"][0]['event_type'] = event_type
    if tc == "no_reasoncode":
        del json_object["telemetry"][0]['reason_code']
    else:
        json_object["telemetry"][0]['reason_code'] = reason_code
    if tc == "no_data":
        del json_object["telemetry"][0]["data"]
    if tc == "no_telemetry":
        del json_object["telemetry"]
    if tc == "no_meta":
        del json_object["meta"]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Sos_Service")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Sos_Service",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Sos_Service', response.text)
    save_api_resp_in_excel(self, "API_Data", "Sos_Service", response.text)

    return response


# Telemetry - Telemetry_Curr_sensorValues_withpayload
def telemetry_Curr_sensorValues(self, systemId, eventType, id, name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_sensorValues")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    if tc == "no_SystemId":
        complete_url = str(base_url + endpoint).replace('?systemId={systemId}', '')
    # elif tc == "VIN":
    # complete_url = str(base_url + endpoint)+'&vin={vin}'.replace('{vin}', vin)
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    # complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)

    json_object["names"][0] = name

    json_object["eventTypes"][0] = eventType
    json_object["ids"][0] = id

    if tc == "EventType":

        del json_object["names"]
        del json_object["ids"]

    elif tc == "id15":
        del json_object["names"]
        json_object["ids"] = id

    elif tc == "name15":
        del json_object["ids"]
        json_object["names"] = name

    elif tc == "delid":
        del json_object["ids"]

    elif tc == "valid" or "no_SystemID":
        del json_object["names"]


    else:
        json_object["names"][0] = name

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_sensorValues",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_sensorValues', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_sensorValues", response.text)

    return response


# Telemetry - Telemetry_Curr_sensorValues_withVIN_In_payload
def telemetry_Curr_sensorValues_VIN(self, vin, eventType, id, name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_sensorValues_VIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    if tc == "no_SystemId":
        complete_url = str(base_url + endpoint).replace('?vin={vin}', '')
    else:
        complete_url = str(base_url + endpoint).replace('{vin}', vin)
    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    # complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["names"][0] = name
    json_object["eventTypes"][0] = eventType
    json_object["ids"][0] = id
    if tc == "EventType":
        del json_object["names"]
        del json_object["ids"]
    elif tc == 'IDAndName':
        json_object["names"][0] = name
        json_object["ids"][0] = id
        json_object["eventTypes"][0] = eventType
    elif tc == "delid":
        del json_object["ids"]
    elif tc == "valid" or "no_SystemID":
        del json_object["names"]
    else:
        json_object["names"][0] = name

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_sensorValues_VIN",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_sensorValues', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_sensorValues_VIN", response.text)

    return response


# Telemetry - Telemetry_Curr_sensorValues_withVIN&systemID_In_payload
def telemetry_Curr_sensorValues_systemIDAndVIN(self, systemId, vin, eventType, id, name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Curr_sensorValues_SystemID&VIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    if tc == "no_SystemId":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('?vin={vin}', '')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{vin}', vin)
    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    # complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)

    json_object["names"][0] = name

    json_object["eventTypes"][0] = eventType
    json_object["ids"][0] = id

    if tc == "EventType":

        del json_object["names"]
        del json_object["ids"]

    elif tc == 'IDAndName':
        json_object["names"][0] = name
        json_object["ids"][0] = id
        json_object["eventTypes"][0] = eventType

    elif tc == "delid":
        del json_object["ids"]

    elif tc == "valid" or "no_SystemID":
        del json_object["names"]

    else:
        json_object["names"][0] = name

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr_sensorValues_SystemID&VIN",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Curr_sensorValues', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Curr_sensorValues_SystemID&VIN", response.text)

    return response


# ---------------------------------
# RE API Modules
# ---------------------------------

# => POST API operation to fetch current location details for the List of systems with event type

def vehicle_live_location(self, systemId, eventId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_vehicle_live_location")
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
    headers = header_update(header_x, tc)

    # Payload :
    json_object = json.loads(payload)

    if tc == "vehicleLocation_without_eventId":
        del json_object["criteria"]["eventType"]
    elif tc == "vehicleLocation_without_systemId":
        del json_object["criteria"]["systemId"]
    elif tc == "vehicleLocation_without_criteria":
        del json_object["criteria"]
    elif tc == "vehicleLocation_empty_criteria":
        del json_object["criteria"]["eventType"]
        del json_object["criteria"]["systemId"]
    elif tc == "vehicleLocation_invalid_contentType":
        headers["Content-Type"] = "application/com.c2c.telemetry.dto.v1.v1+json"
    elif tc == "vehicleLocation_empty_contentType":
        headers["Content-Type"] = ""
    elif tc == "vehicleLocation_without_contentType":
        del headers["Content-Type"]
    elif tc == "vehicleLocation_multiple_systemIds":
        json_object["criteria"]["systemId"] = ["134", systemId]
    elif tc == "vehicleLocation_multiple_systemIds_eventIds":
        json_object["criteria"]["systemId"] = ["134", systemId]
        json_object["criteria"]["eventType"] = [eventId, 2003]
    elif tc == "vehicleLocation_single_systemId_multiple_eventIds":
        json_object["criteria"]["systemId"] = [systemId]
        json_object["criteria"]["eventType"] = [eventId, 2003]
    elif tc == "vehicleLocation_valid_and_invalid_systemId":
        json_object["criteria"]["systemId"] = ["134a", systemId]
    elif tc == "vehicleLocation_duplicate_systemIds":
        json_object["criteria"]["systemId"] = [systemId, systemId]
    else:
        json_object["criteria"]["systemId"][0] = systemId
        json_object["criteria"]["eventType"][0] = eventId

    payload = json_object

    print("Headers : ", headers)
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=headers, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_vehicle_live_location",
                                                "Telemetry_AuthToken")
            time.sleep(120)
            response = requests.post(complete_url, headers=headers, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_vehicle_live_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_vehicle_live_location", response.text)

    return response


def last_parked_location(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_last_parked_location")
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
    headers = header_update(header_x, tc)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=headers, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_last_parked_location",
                                                "Telemetry_AuthToken")
            time.sleep(120)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_last_parked_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_last_parked_location", response.text)

    return response

# Telemetry_CurrForEventType
def telemetry_Curr_eventType_global(self, event_type, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_CurrForEventType_global")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)

    if tc == "no_eventType":
        complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('?eventType={eventType}',
                                                                                    "")
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('{eventType}',
                                                                                             str(event_type))
    complete_url = complete_url.replace(' ', '')

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    #print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Telemetry_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_CurrForEventType_global",
                                                "Telemetry_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_CurrForEventType_global', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_CurrForEventType_global", response.text)

    return response

def read_and_verify_telemetry_data(self, expected_json, actual_json, attribute):
    expected_signals = expected_json["responseData"]["signals"][0]
    actual_signals = actual_json["responseData"]["signals"][0]

    expected_names = [sig["name"] for sig in expected_signals]
    actual_names = [sig["name"] for sig in actual_signals]

    print("--------------------------------------------------------------------")
    print("Attribute Name :", attribute)

    stauts = ""

    # Fail if attribute not in expected JSON
    if attribute not in expected_names:
        msg = attribute + " not found in expected JSON"
        testResult(self, "verificationFailed",
                   attribute + " should exist in expected JSON",
                   msg)
        stauts = "fail"

    # Fail if attribute not in actual JSON
    elif attribute not in actual_names:
        msg = attribute + " not found in actual JSON"
        testResult(self, "verificationFailed",
                   attribute + " should exist in actual JSON",
                   msg)
        stauts = "fail"

    else:
        # Attribute exists in both → pass
        testResult(self, "passed",
                   attribute + " should exist in both expected and actual JSON",
                   attribute + " exists in both expected and actual JSON")
        stauts = "pass"

    return stauts

# E2E operation to verify telemetry last parked location
def telemetry_lastParkedLocation(self, cloudEnv, systemId):
    times = 0
    try:

        # Hit last parked location API & validate response
        for i in range(5):
            times += 1
            now = datetime.now()
            current_dateTime = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            print("No of iterations/hits :", times, "  Current DateTime :", current_dateTime)

            # Call reusable old curr module
            response = last_parked_location(self, systemId, "valid")

            # Validate status code
            if response.status_code == 200:
                break
            else:
                time.sleep(30)

        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "RE-UAT", "GCP-QA2"]:
            test_attribute_list = [telemetry_attribute_gps_speed1, telemetry_attribute_gps_status,
                                   telemetry_attribute_gsm_signalStrength,
                                   telemetry_attribute_networkOpName, telemetry_attribute_timestamp,
                                   telemetry_attribute_deltaDistCovered,
                                   telemetry_attribute_pdop, telemetry_attribute_hdop, telemetry_attribute_gps_fix,
                                   telemetry_attribute_latitude_dir, telemetry_attribute_longitude_dir,
                                   telemetry_attribute_latitude, telemetry_attribute_longitude,
                                   telemetry_attribute_altitude,
                                   telemetry_attribute_direction1]
        else:
            test_attribute_list = [telemetry_attribute_gps_speed, telemetry_attribute_gps_status,
                               telemetry_attribute_gsm_signalStrength,
                               telemetry_attribute_networkOpName, telemetry_attribute_timestamp,
                               telemetry_attribute_deltaDistCovered,
                               telemetry_attribute_pdop, telemetry_attribute_hdop, telemetry_attribute_gps_fix,
                               telemetry_attribute_latitude_dir, telemetry_attribute_longitude_dir,
                               telemetry_attribute_latitude, telemetry_attribute_longitude,
                               telemetry_attribute_altitude,
                               telemetry_attribute_direction]

        # Validate last parked location json
        overall_status = []
        failed_attributes = []  # collect failed attributes

        for attribute in test_attribute_list:
            print("--------------------------------------------------------------------")
            print("Attribute Name : ", attribute)
            if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "RE-UAT", "GCP-QA2"]:
                status = read_and_verify_telemetry_data(self, last_parked_expected_output2, response_body, attribute)
            elif cloudEnv in ["GCP-QA", "GCP-DEMO2"]:
                status = read_and_verify_telemetry_data(self, last_parked_expected_output1, response_body, attribute)
            else:
                status = read_and_verify_telemetry_data(self, last_parked_expected_output, response_body, attribute)

            overall_status.append(status)
            if status.startswith("fail"):  # ✅ track which attribute failed
                failed_attributes.append(attribute)

        #Fail the script if ANY telemetry attribute is not matching
        if failed_attributes:
            testResult(self, "failed",
                       "Last Parked Location attribute values should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "The following attributes are missing or not matching: "
                       + ", ".join(failed_attributes)
                       + ". Please refer to device & cloud logs for detailed info")
            assert False
        else:
            testResult(self, "passed",
                       "Last Parked Location attribute values should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "All Last Parked Location attributes are present in the Cloud DB and same as that of configured in the stub running on device. Please refer to device & cloud logs for detailed info")


    except Exception as e:
        print("Something went wrong")
        testResult(self, "failed",
                   "Last Parked Location attribute values should be stored in the Cloud DB and same as that of configured in the stub running on device",
                   "Something went wrong. Last Parked Location attribute values are not stored in the Cloud DB  or not same as that of configured in the stub running on device pls refer "
                   "device & cloud logs for detailed info")
        assert False

# E2E operation to verify telemetry update
def telemetry_liveLocation(self, systemId, eventId, tc):
    try:
        # ===========================================================================================
        # Hit telemetry curr at configured interval
        # ===========================================================================================
        global times, value, msg_no
        gps_speed_values = []
        latitude_values = []
        longitude_values = []
        altitude_values = []
        direction_values = []
        times = 0

        # Hit Telemetry Curr API & validate telemetry attribute value
        for i in range(4):
            times += 1
            now = datetime.now()
            current_dateTime = now.strftime('%Y-%m-%d %H:%M:%S.%f')
            print("No of iterations/hits :", times, "  Current DateTime :", current_dateTime)

            # Call reusable old curr module
            if (tc == "vehicleLocation" or tc == "vehicleLocation_multiple_systemIds"
                    or tc == "vehicleLocation_duplicate_systemIds" or tc ==
                    "vehicleLocation_valid_and_invalid_systemId"):
                response = vehicle_live_location(self, systemId, eventId, tc)
            elif tc == "realTimeTracking":
                response = telemetry_Curr_eventType(self, eventId, systemId, tc)
            elif tc == "realTimeTracking_empty_eventId" or tc == "realTimeTracking_without_eventId":
                response = telemetry_Curr_eventType(self, "", systemId, tc)
            elif tc == "vehicleLocation_without_eventId":
                response = vehicle_live_location(self, systemId, "", tc)

            # Validate status code
            assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            # assert (response_body["responseCode"] == "1200" or response_body["responseCode"] == 1200)
            # assert (response_body["responseData"]["message"] == "Successfully fetched the current values")

            if "vehicleLocation" in tc:
                try:
                    dataList_len = len(response_body["responseData"]["data"][0]["signals"])
                    actual_systemId = response_body["responseData"]["data"][0]["systemId"]

                    if systemId == actual_systemId:
                        print("System Id : ", actual_systemId)

                    # print(dataList_len)
                    for j in range(dataList_len):
                        # print(response_body["responseData"]["dataList"][j]["name"])
                        if response_body["responseData"]["data"][0]["signals"][j][
                            "name"] == telemetry_attribute_gps_speed or \
                                response_body["responseData"]["data"][0]["signals"][j][
                                    "name"] == telemetry_attribute_gps_speed1:
                            gps_speed_value = response_body["responseData"]["data"][0]["signals"][j]["value"]
                        if response_body["responseData"]["data"][0]["signals"][j][
                            "name"] == telemetry_attribute_latitude:
                            latitude_value = response_body["responseData"]["data"][0]["signals"][j]["value"]
                        if response_body["responseData"]["data"][0]["signals"][j][
                            "name"] == telemetry_attribute_longitude:
                            longitude_value = response_body["responseData"]["data"][0]["signals"][j]["value"]
                        if response_body["responseData"]["data"][0]["signals"][j][
                            "name"] == telemetry_attribute_altitude:
                            altitude_value = response_body["responseData"]["data"][0]["signals"][j]["value"]
                        if response_body["responseData"]["data"][0]["signals"][j][
                            "name"] == telemetry_attribute_direction or \
                                response_body["responseData"]["data"][0]["signals"][j][
                                    "name"] == telemetry_attribute_direction1:
                            direction_value = response_body["responseData"]["data"][0]["signals"][j]["value"]
                except:
                    print("dataList is empty in api response")
                    gps_speed_value = latitude_value = longitude_value = altitude_value = direction_value = ""

            if "realTimeTracking" in tc:
                try:
                    dataList_len = len(response_body["responseData"]["signals"])
                    # print(dataList_len)

                    # print(dataList_len)
                    for j in range(dataList_len):
                        # print(response_body["responseData"]["dataList"][j]["name"])
                        if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_gps_speed or \
                                response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_gps_speed1:
                            gps_speed_value = response_body["responseData"]["signals"][j]["value"]
                        if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_latitude:
                            latitude_value = response_body["responseData"]["signals"][j]["value"]
                        if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_longitude:
                            longitude_value = response_body["responseData"]["signals"][j]["value"]
                        if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_altitude:
                            altitude_value = response_body["responseData"]["signals"][j]["value"]
                        if response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_direction or \
                                response_body["responseData"]["signals"][j]["name"] == telemetry_attribute_direction1:
                            direction_value = response_body["responseData"]["signals"][j]["value"]
                except:
                    print("dataList is empty in api response")
                    gps_speed_value = latitude_value = longitude_value = altitude_value = direction_value = ""

            print("------------------------------------------------")
            print("gps_speed_value :", gps_speed_value)
            print("latitude_value :", latitude_value)
            print("longitude_value :", longitude_value)
            print("altitude_value :", altitude_value)
            print("direction_value :", direction_value)
            print("------------------------------------------------")

            gps_speed_values.append(gps_speed_value)
            latitude_values.append(latitude_value)
            longitude_values.append(longitude_value)
            altitude_values.append(altitude_value)
            direction_values.append(direction_value)

            telemetry_gps_speed_array_length = len(gps_speed_values)
            telemetry_latitude_array_length = len(latitude_values)
            # telemetry_longitude_array_length = len(longitude_values)
            # telemetry_altitude_array_length = len(altitude_values)
            # telemetry_direction_array_length = len(direction_values)

            print("Telemetry list length :", telemetry_gps_speed_array_length)

            if telemetry_gps_speed_array_length >= 2 or telemetry_latitude_array_length >= 2:
                print("------------------------------------------------")
                print("GPS Speed Array :", gps_speed_values)
                print("Latitude Array :", latitude_values)
                print("Longitude Array :", longitude_values)
                print("Altitude Array :", altitude_values)
                print("Direction Array :", direction_values)
                print("------------------------------------------------")
                # print("Length :", len(gps_speed_values))
                # print(gps_speed_values[len(gps_speed_values) - 2])
                # print("-------------------------")

                if gps_speed_values[len(gps_speed_values) - 2] == "":
                    gps_speed_values[len(gps_speed_values) - 2] = 0
                if latitude_values[len(latitude_values) - 2] == "":
                    latitude_values[len(latitude_values) - 2] = 0
                if longitude_values[len(longitude_values) - 2] == "":
                    longitude_values[len(longitude_values) - 2] = 0
                if altitude_values[len(altitude_values) - 2] == "":
                    altitude_values[len(altitude_values) - 2] = 0
                if direction_values[len(direction_values) - 2] == "":
                    direction_values[len(direction_values) - 2] = 0

            if len(gps_speed_values) >= 4:
                if gps_speed_values[len(gps_speed_values) - 1] == gps_speed_values[len(gps_speed_values) - 2] == \
                        gps_speed_values[
                            len(gps_speed_values) - 3] == \
                        gps_speed_values[len(gps_speed_values) - 4]:
                    print(" => Telemetry - GPS Speed value is not updated for consecutive four packets")
                    assert False
                else:
                    print(" => Telemetry - GPS Speed value is updated for consecutive four packets")
                    assert True
                print("------------------------------------------------")

            if len(latitude_values) >= 4:
                if latitude_values[len(latitude_values) - 1] == latitude_values[len(latitude_values) - 2] == \
                        latitude_values[
                            len(latitude_values) - 3] == \
                        latitude_values[len(latitude_values) - 4]:
                    print(" => Telemetry - Latitude value is not updated for consecutive four packets")
                    assert False
                else:
                    print(" => Telemetry - Latitude value is updated for consecutive four packets")
                    assert True
                print("------------------------------------------------")

            if len(longitude_values) >= 4:
                if longitude_values[len(longitude_values) - 1] == longitude_values[len(longitude_values) - 2] == \
                        longitude_values[
                            len(longitude_values) - 3] == \
                        gps_speed_values[len(longitude_values) - 4]:
                    print(" => Telemetry - Longitude value is not updated for consecutive four packets")
                    assert False
                else:
                    print(" => Telemetry - Longitude value is updated for consecutive four packets")
                    assert True
                print("------------------------------------------------")

            if len(altitude_values) >= 4:
                if altitude_values[len(altitude_values) - 1] == altitude_values[len(altitude_values) - 2] == \
                        altitude_values[
                            len(altitude_values) - 3] == \
                        altitude_values[len(altitude_values) - 4]:
                    print(" => Telemetry - Altitude value is not updated for consecutive four packets")
                    assert False
                else:
                    print(" => Telemetry - Altitude value is updated for consecutive four packets")
                    assert True
                print("------------------------------------------------")

            if len(direction_values) >= 4:
                if direction_values[len(direction_values) - 1] == direction_values[len(direction_values) - 2] == \
                        direction_values[
                            len(direction_values) - 3] == \
                        direction_values[len(direction_values) - 4]:
                    print(" => Telemetry - Direction value is not updated for consecutive four packets")
                    assert False
                else:
                    print(" => Telemetry - Direction value is updated for consecutive four packets")
                    assert True
                print("------------------------------------------------")

            time.sleep(30)

            # print("---------------------------------------------------------------------")

    except Exception as e:
        print("Something went wrong")
        assert False

# ------------------------------------------
# LastPark Location Reusable Modules
# ------------------------------------------
def lastPark_location_create_elements(self, Parameter1, Parameter2, Parameter3, Parameter4, Parameter5, Parameter6,
                                      Parameter7, Parameter8, Parameter9, Parameter10, Parameter11, Parameter12,
                                      Parameter13, Parameter14, Parameter15, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_save_last_parked_location")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object[0] = Parameter1
    json_object[1] = Parameter2
    json_object[2] = Parameter3
    json_object[3] = Parameter4
    json_object[4] = Parameter5
    json_object[5] = Parameter6
    json_object[6] = Parameter7
    json_object[7] = Parameter8
    json_object[8] = Parameter9
    json_object[9] = Parameter10
    json_object[10] = Parameter11
    json_object[11] = Parameter12
    json_object[12] = Parameter13
    json_object[13] = Parameter14
    json_object[14] = Parameter15
    print("----------------------------------------------------------")
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_save_last_parked_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_save_last_parked_location", response.text)

    return response
def lastPark_location_update_elements(self, attributeName, modelCode, elementId, eventType, values,
                                      idName, unit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_update_last_parked_location")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{attributeName}', attributeName).replace('{modelCode}', modelCode)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["elementId"] = elementId
    json_object["attributeName"] = attributeName
    json_object["modelCode"] = modelCode
    json_object["eventType"] = eventType
    json_object["values"] = values
    json_object["idName"] = idName
    json_object["unit"] = unit
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_update_last_parked_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_update_last_parked_location", response.text)

    return response
def lastPark_location_fetch_elements(self, attributeName, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_fetch_last_parked_location")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    if "attributeName_modelCode" in tc:
        complete_url = str(base_url + endpoint) + "?attributeName={attributeName}&modelCode={modelCode}".replace('{attributeName}', attributeName).replace('{modelCode}', modelCode)
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
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_fetch_last_parked_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_fetch_last_parked_location", response.text)

    return response
def lastPark_location_delete_elements(self, attributeName, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_delete_last_parked_location")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{attributeName}', attributeName).replace('{modelCode}', modelCode)
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
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_delete_last_parked_location', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_delete_last_parked_location", response.text)

    return response

# ------------------------------------------
# Telemetry master data API Reusable Modules
# ------------------------------------------
def Telemetry_master_data_add_new_event(self, eventType, eventName, eventCategory, modelCode, attributeList1, attributeList2, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_master_data_add_new_event")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["telemetryData"]["eventType"] = eventType
    json_object["telemetryData"]["eventName"] = eventName
    json_object["telemetryData"]["eventCategory"] = eventCategory
    json_object["telemetryData"]["modelCode"] = modelCode
    json_object["telemetryData"]["eventCategory"] = eventCategory
    json_object["telemetryData"]["eventCategory"] = eventCategory

    if "add_single_attribute" in tc:
        json_object["telemetryData"]["attributeList"][0] = attributeList1
    elif "add_multiple_attribute" in tc:
        json_object["telemetryData"]["attributeList"][0] = attributeList1
        json_object["telemetryData"]["attributeList"].append(attributeList2)

    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_master_data_add_new_event', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_master_data_add_new_event", response.text)

    return response

def Telemetry_master_data_update_event(self, eventType, eventName, eventCategory, modelCode, attributeList1, attributeList2, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_master_data_update_event")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["telemetryData"]["eventType"] = eventType
    json_object["telemetryData"]["eventName"] = eventName
    json_object["telemetryData"]["eventCategory"] = eventCategory
    json_object["telemetryData"]["modelCode"] = modelCode
    json_object["telemetryData"]["eventCategory"] = eventCategory
    json_object["telemetryData"]["eventCategory"] = eventCategory
    if "update_single_attribute" in tc:
        json_object["telemetryData"]["attributeList"][0] = attributeList1
    elif "update_multiple_attribute" in tc:
        json_object["telemetryData"]["attributeList"][0] = attributeList1
        json_object["telemetryData"]["attributeList"].append(attributeList2)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_master_data_update_event', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_master_data_update_event", response.text)

    return response

def Telemetry_master_data_get_event(self, eventType, offset, limit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_master_data_get_event_details")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{eventType}', eventType).replace('{offset}', offset).replace('{limit}', limit)
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
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_master_data_get_event_details', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_master_data_get_event_details", response.text)

    return response

def Telemetry_master_data_delete_event(self, eventType, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_master_data_delete_event")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["eventType"] = eventType
    json_object["modelCode"] = modelCode
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_master_data_delete_event', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_master_data_delete_event", response.text)

    return response

# Telemetry master data- Reusable function

def master_data_add_new_event(self, eventType, eventName, eventCategory, modelCode, attributeList1, attributeList2, tc):

    print("----------------------------------------------------------")

    # Call API to add event
    if tc == "add_single_attribute":
        response = Telemetry_master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_single_attribute"
        )
    elif tc == "add_multiple_attribute":
        response = Telemetry_master_data_add_new_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "add_multiple_attribute"
        )
    else:
        assert False, f"Invalid test case flag 'tc': {tc}. Use 'add_single_attribute' or 'add_multiple_attribute'."

    # --- Create/Idempotency handling ---
    if response.status_code == 200:
        response_body = response.json()
        if response_body.get("message") == "Data Saved Successfully":
            testResult(self, "passed",
                       "Telemetry Master Data - New event should saved successfully",
                       "Telemetry Master Data - New event is saved successfully")
            assert True
        else:
            testResult(self, "failed",
                       "Telemetry Master Data - New event should saved successfully",
                       f"Unexpected success message: {response_body.get('message')}")
            assert False, f"Unexpected success message: {response_body.get('message')}"
    elif response.status_code == 400:
        response_body = response.json()
        errors = response_body.get("errors", [])
        if errors and errors[0].get("errorCode") == "15565" and errors[0].get("message") == "Data Already exist with given Event Type":
            testResult(self, "passed",
                       "Telemetry Master Data - Already event exist",
                       "Telemetry Master Data - Already event exist")
            assert True
        else:
            testResult(self, "failed",
                       "Telemetry Master Data - Already event exist",
                       f"Unexpected 400 response: {response_body}")
            assert False, f"Unexpected 400 response: {response_body}"
    else:
        assert False, f"Create failed: Expected 200 or 400, got {response.status_code} ({getattr(response, 'text', '')})"

    # --- Fetch and validate ---
    response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
    assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

    response_body = response.json()
    if response_body.get("message") == "Data Fetched Successfully":
        telemetry_list = response_body.get("telemetryData", [])
        assert telemetry_list, "No telemetry data returned for the eventType"

        event = telemetry_list[0]
        eventType_actual = event.get("eventType")
        eventName_actual = event.get("eventName")
        eventCategory_actual = event.get("eventCategory")
        modelCode_actual = event.get("modelCode")
        actual_params = event.get("attributeList", []) or []

        # Header validation (normalize to strings to avoid type mismatches)
        headers_match = (
            str(eventType_actual) == str(eventType) and
            str(eventName_actual) == str(eventName) and
            str(eventCategory_actual) == str(eventCategory) and
            str(modelCode_actual) == str(modelCode)
        )

        expected_attributes = []

        if headers_match:
            # Decide which attributes to validate based on 'tc'
            if tc == "add_single_attribute":
                expected_attributes = [attributeList1]
            elif tc == "add_multiple_attribute":  # "add_multiple_attribute"
                expected_attributes = [attributeList1, attributeList2]

            missing = []

            for expected in expected_attributes:
                found = any(
                    str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                    str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                    str(actual.get("elementId")) == str(expected.get("elementId")) and
                    str(actual.get("idName")) == str(expected.get("idName")) and
                    str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                    str(actual.get("description")) == str(expected.get("description")) and
                    # Compare nested areaList[0].areaId and areaName safely
                    str((actual.get("areaList") or [{}])[0].get("areaId")) == str((expected.get("areaList") or [{}])[0].get("areaId")) and
                    str((actual.get("areaList") or [{}])[0].get("areaName")) == str((expected.get("areaList") or [{}])[0].get("areaName"))
                    for actual in actual_params
                )
                if not found:
                    missing.append(expected.get("attributeName", "<unknown>"))

            if not missing:
                if tc == "add_single_attribute":
                    testResult(self, "passed",
                               "Expected telemetry attribute found in API response",
                               "Validation successful")
                else:
                    testResult(self, "passed",
                               "Both expected telemetry attributes found in API response",
                               "Validation successful")
                assert True
            else:
                if tc == "add_single_attribute":
                    testResult(self, "failed",
                               "Expected telemetry attribute missing in API response",
                               f"Missing attribute: {missing[0]}")
                    assert False, f"Missing attribute: {missing[0]}"
                else:
                    testResult(self, "failed",
                               "Some expected telemetry attributes missing in API response",
                               f"Missing attributes: {', '.join(missing)}")
                    assert False, f"Missing attributes: {', '.join(missing)}"
        else:
            testResult(self, "failed",
                       "Event header details should match expected values",
                       f"Mismatch in event details: "
                       f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                       f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
            assert False, (
                f"Header mismatch: Expected "
                f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
            )
    else:
        assert False, f'Unexpected fetch message: {response_body.get("message")}'

def master_data_update_event(self, eventType, eventName, eventCategory, modelCode, attributeList1, attributeList2, tc):

    print("----------------------------------------------------------")

    # Call API to add event
    if tc == "update_single_attribute":
        response = Telemetry_master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_single_attribute"
        )
    elif tc == "update_multiple_attribute":
        response = Telemetry_master_data_update_event(
            self, eventType, eventName, eventCategory, modelCode,
            attributeList1, attributeList2, "update_multiple_attribute"
        )
    else:
        assert False, f"Invalid test case flag 'tc': {tc}. Use 'update_single_attribute' or 'update_multiple_attribute'."

    # --- Create/Idempotency handling ---
    if response.status_code == 200:
        response_body = response.json()
        if response_body.get("message") == "Data Updated Successfully":
            testResult(self, "passed",
                       "Telemetry Master Data - Event should updated successfully",
                       "Telemetry Master Data - Event is updated successfully")
            assert True
        else:
            testResult(self, "failed",
                       "Telemetry Master Data - Event should updated successfully",
                       f"Unexpected success message: {response_body.get('message')}")
            assert False, f"Unexpected success message: {response_body.get('message')}"
    else:
        assert False, f"Update failed: Expected 200, got {response.status_code}"

    # --- Fetch and validate ---
    response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")
    assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

    response_body = response.json()
    if response_body.get("message") == "Data Fetched Successfully":
        telemetry_list = response_body.get("telemetryData", [])
        assert telemetry_list, "No telemetry data returned for the eventType"

        event = telemetry_list[0]
        eventType_actual = event.get("eventType")
        eventName_actual = event.get("eventName")
        eventCategory_actual = event.get("eventCategory")
        modelCode_actual = event.get("modelCode")
        actual_params = event.get("attributeList", []) or []

        # Header validation
        headers_match = (
            str(eventType_actual) == str(eventType) and
            str(eventName_actual) == str(eventName) and
            str(eventCategory_actual) == str(eventCategory) and
            str(modelCode_actual) == str(modelCode)
        )

        expected_attributes = []

        if headers_match:
            # Decide which attributes to validate based on 'tc'
            if tc == "update_single_attribute":
                expected_attributes = [attributeList1]
            elif tc == "update_multiple_attribute":  # "add_multiple_attribute"
                expected_attributes = [attributeList1, attributeList2]

            missing = []

            for expected in expected_attributes:
                found = any(
                    str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                    str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                    str(actual.get("elementId")) == str(expected.get("elementId")) and
                    str(actual.get("idName")) == str(expected.get("idName")) and
                    str(actual.get("changeMode")) == str(expected.get("changeMode")) and
                    str(actual.get("description")) == str(expected.get("description")) and
                    # Compare nested areaList[0].areaId and areaName safely
                    str((actual.get("areaList") or [{}])[0].get("areaId")) == str((expected.get("areaList") or [{}])[0].get("areaId")) and
                    str((actual.get("areaList") or [{}])[0].get("areaName")) == str((expected.get("areaList") or [{}])[0].get("areaName"))
                    for actual in actual_params
                )
                if not found:
                    missing.append(expected.get("attributeName", "<unknown>"))

            if not missing:
                if tc == "update_single_attribute":
                    testResult(self, "passed",
                               "Expected telemetry attribute found in API response",
                               "Validation successful")
                else:
                    testResult(self, "passed",
                               "Both expected telemetry attributes found in API response",
                               "Validation successful")
                assert True
            else:
                if tc == "update_single_attribute":
                    testResult(self, "failed",
                               "Expected telemetry attribute missing in API response",
                               f"Missing attribute: {missing[0]}")
                    assert False, f"Missing attribute: {missing[0]}"
                else:
                    testResult(self, "failed",
                               "Some expected telemetry attributes missing in API response",
                               f"Missing attributes: {', '.join(missing)}")
                    assert False, f"Missing attributes: {', '.join(missing)}"
        else:
            testResult(self, "failed",
                       "Event header details should match expected values",
                       f"Mismatch in event details: "
                       f"Expected (Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                       f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})")
            assert False, (
                f"Header mismatch: Expected "
                f"(Type={eventType}, Name={eventName}, Category={eventCategory}, Model={modelCode}) "
                f"Got (Type={eventType_actual}, Name={eventName_actual}, Category={eventCategory_actual}, Model={modelCode_actual})"
            )
    else:
        assert False, f'Unexpected fetch message: {response_body.get("message")}'

def master_data_delete_event(self, eventType, modelCode, tc):

    print("----------------------------------------------------------")

    # Call API to delete event
    response = Telemetry_master_data_delete_event(self, eventType, modelCode, "valid")

    # delete 1006- adding multiple attributes
    # Call API to add event
    response1 = Telemetry_master_data_delete_event(self, "1006", modelCode, "valid")

    if response.status_code == 200:
        response_body = response.json()
        if response_body["message"] == "Data Deleted Successfully.":
            testResult(self, "passed",
                       "Telemetry Master Data - Event should deleted successfully",
                       "Telemetry Master Data - Event is deleted successfully")
            assert True
        else:
            testResult(self, "failed",
                       "Telemetry Master Data - Event should deleted successfully",
                       "Telemetry Master Data - Event is not deleted successfully")
            assert False
    else:
        print("Response status code is not 200. Rather then found: ", response.status_code)
        assert False

    # Fetch event details
    response = Telemetry_master_data_get_event(self, eventType, "0", "10", "valid")

    if response.status_code == 204:
        testResult(self, "passed",
                   "After deletion there should not be any data for the event",
                   "After deletion there is no data for the event")
        assert True
    else:
        testResult(self, "failed",
                   "After deletion there should not be any data for the event",
                   "After deletion still data exist for the event in cloud")
        assert False


#Telemetry- last park element reusable function

def lastPark_location_save_telemetry_elements(self, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7, parameter8, parameter9, parameter10, parameter11, parameter12, parameter13, parameter14, parameter15):

    print("----------------------------------------------------------")

    expected_params = [parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7,
                       parameter8, parameter9, parameter10, parameter11, parameter12, parameter13,
                       parameter14, parameter15]

    # Step 1: Create telemetry elements
    response = lastPark_location_create_elements(self, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6, parameter7,
                       parameter8, parameter9, parameter10, parameter11, parameter12, parameter13,
                       parameter14, parameter15, "valid")

    # Validate response
    if response.status_code == 200:
        response_body = response.json()
        assert response_body.get("message") == "Model code '1234' updated successfully.", \
            f"Unexpected message: {response_body}"
    elif response.status_code == 400:
        response_body = response.json()
        if (response_body["errors"][0][
            "message"] == "Telemetry element with modelCode and attributeName already exists"
                and response_body["errors"][0]["errorCode"] == "1515"):
            testResult(self, "passed", "Telemetry parameters already exist", "Telemetry parameters already exist")
            assert True
        else:
            assert False, f"Unexpected error response: {response_body}"
    else:
        assert False, f"Unexpected status code: {response.status_code}"

    # Step 2: Fetch telemetry elements
    response = lastPark_location_fetch_elements(self, "", "", "valid")
    assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"

    response_body = response.json()
    assert response_body.get("message") == "Data fetched successfully", \
        f"Unexpected fetch message: {response_body}"

    actual_params = response_body.get("responseData", [])

    # check for missing params
    missing = []
    for expected in expected_params:
        if not any(
                str(actual.get("attributeName")) == str(expected.get("attributeName")) and
                str(actual.get("modelCode")) == str(expected.get("modelCode")) and
                str(actual.get("elementId")) == str(expected.get("elementId"))
                for actual in actual_params):
            missing.append(expected.get("attributeName"))

    if not missing:
        testResult(self, "passed",
                   "All expected telemetry parameters found in API response",
                   "Validation successful")
        assert True
    else:
        testResult(self, "failed",
                   "Some expected telemetry parameters missing in API response",
                   f"Missing attributes: {', '.join(missing)}")
        assert False, f"Missing attributes: {', '.join(missing)}"

def lastPark_location_update_telemetry_elements(self, elementId, attributeName, modelCode, eventType, values, idName, unit):

    print("----------------------------------------------------------")

    # Step 1: Update telemetry parameters
    response = lastPark_location_update_elements(
        self, attributeName, modelCode, elementId, eventType, values, idName, unit, "valid"
    )

    # Validate update response
    assert response.status_code == 200, f"Update failed: Expected 200, got {response.status_code}"
    response_body = response.json()
    if response_body.get("message") == "Data updated successfully":
        assert True
        testResult(self, "passed",
                   "Last Park location telemetry parameters should be updated/configured successfully",
                   "Last park Location telemetry parameters are updated/configured successfully")
    else:
        print(f"Unexpected update message: {response_body}")
        testResult(self, "failed",
               "Last Park location telemetry parameters should be updated/configured successfully",
               "Last park Location telemetry parameters are not updated/configured successfully")

    # Step 2: Fetch telemetry parameters
    response = lastPark_location_fetch_elements(self, attributeName, modelCode, "attributeName_modelCode")
    assert response.status_code == 200, f"Fetch failed: Expected 200, got {response.status_code}"
    response_body = response.json()
    if response_body.get("message") == "Data fetched successfully":
        assert True
    else:
        print(f"Unexpected fetch message: {response_body}")
        assert False

    # Extract actual values
    data = response_body.get("responseData", [{}])[0]
    elementId_actual = str(data.get("elementId"))
    attributeName_actual = str(data.get("attributeName"))
    modelCode_actual = str(data.get("modelCode"))
    eventType_actual = str(data.get("eventType"))
    values_actual = str(data.get("values"))
    idName_actual = str(data.get("idName"))
    unit_actual = str(data.get("unit"))

    # Compare expected vs actual
    mismatches = []
    if elementId_actual != elementId: mismatches.append(f"elementId: expected {elementId}, got {elementId_actual}")
    if attributeName_actual != attributeName: mismatches.append(
        f"attributeName: expected {attributeName}, got {attributeName_actual}")
    if modelCode_actual != modelCode: mismatches.append(f"modelCode: expected {modelCode}, got {modelCode_actual}")
    if eventType_actual != eventType: mismatches.append(f"eventType: expected {eventType}, got {eventType_actual}")
    if values_actual != values: mismatches.append(f"values: expected {values}, got {values_actual}")
    if idName_actual != idName: mismatches.append(f"idName: expected {idName}, got {idName_actual}")
    if unit_actual != unit: mismatches.append(f"unit: expected {unit}, got {unit_actual}")

    if not mismatches:
        testResult(self, "passed",
                   "Last Park Location telemetry parameters should be present in API response",
                   "All expected telemetry parameters found in API response")
        assert True
    else:
        testResult(self, "failed",
                   "Last Park Location telemetry parameters should be present in API response",
                   f"Mismatches found: {', '.join(mismatches)}")
        assert False, f"Mismatches found: {', '.join(mismatches)}"

def lastPark_location_delete_telemetry_elements(self, attributeName, modelCode ):

    print("----------------------------------------------------------")

    # Step 1: Delete telemetry parameters
    response = lastPark_location_delete_elements(self, attributeName, modelCode, "valid")

    # Validate delete response
    assert response.status_code == 200, f"Delete failed: Expected 200, got {response.status_code}"
    response_body = response.json()

    if response_body.get("message") == "Telemetry elements deleted successfully.":
        testResult(self, "passed",
                   "Last Park location telemetry parameters should be deleted successfully",
                   "Telemetry parameters deleted successfully")
    else:
        testResult(self, "failed",
                   "Last Park location telemetry parameters should be deleted successfully",
                   f"Unexpected delete message: {response_body.get('message')}")

    # Step 2: Fetch telemetry parameters after deletion
    response = lastPark_location_fetch_elements(self, attributeName, modelCode, "attributeName_modelCode")

    if response.status_code == 204:
        testResult(self, "passed",
                   "Last Park Location telemetry parameters should not be present in API response",
                   "Telemetry parameters are not present in API response after deletion")
        assert True
    else:
        testResult(self, "failed",
                   "Last Park Location telemetry parameters should not be present in API response",
                   f"Telemetry parameters still present. Status code: {response.status_code}")
        assert False, f"Expected 204 after deletion, got {response.status_code}"