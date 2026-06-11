import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import *
from C2CModules.vehicle_state import *

folder_path = "C:\Car2Cloud_E2ETesting"


# ---------------------------------
# API Modules
# ---------------------------------

# Geofence Creation
def Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type, poiFlag, tag, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
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
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["name"] = name
    json_object["geometryType"] = geometryType
    json_object["radius"] = radius
    json_object["coordinates"][0][0] = long
    json_object["coordinates"][0][1] = lat
    json_object["isActive"] = isActive
    json_object["tolerance"] = tolerance
    json_object["type"] = type
    json_object["poiFlag"] = poiFlag
    json_object["tag"] = tag
    if tc == "no_name":
        del json_object["name"]
    elif tc == "no_geometryType":
        del json_object["geometryType"]
    elif tc == "no_radius":
        del json_object["radius"]
    elif tc == "polygon_geofence":
        json_object["coordinates"] = [
            [77.2290, 28.6100],
            [77.2310, 28.6070],
            [77.2311, 28.6072],
            [77.2312, 28.6073],
            [77.2313, 28.6074],
            [77.2290, 28.6100]
        ]
    elif tc == "no_IsActive":
        del json_object["isActive"]
    elif tc == "no_tolerance":
        del json_object["tolerance"]
    elif tc == "no_type":
        del json_object["type"]
    elif tc == "no_poiFlag":
        del json_object["poiFlag"]
    elif tc == "no_tag":
        del json_object["tag"]
    elif tc == "no_latitude":
        del json_object["coordinates"][0][1]
    elif tc == "no_longitude":
        del json_object["coordinates"][0][0]
    elif tc == "no_coordinates":
        del json_object["coordinates"][0]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_createGeofence",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_createGeofence', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_createGeofence", response.text)

    return response


# Geofence - Update
def Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type, poiFlag,
                            tag, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_updateGeofence")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_contentType" in tc:
        header_x["Content-Type"] = "xyz"
    elif "null_contentType" in tc:
        header_x["Content-Type"] = None
    elif "no_contentType" in tc:
        del header_x["Content-Type"]
    else:
        header_x["Content-Type"] = "application/com.c2c.telemetry.location.dto.v1.request.locationrequestnew.v1+json"
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["name"] = name
    json_object["geometryType"] = geometryType
    json_object["radius"] = radius
    json_object["coordinates"][0][0] = long
    json_object["coordinates"][0][1] = lat
    json_object["isActive"] = isActive
    json_object["tolerance"] = tolerance
    json_object["type"] = type
    json_object["poiFlag"] = poiFlag
    json_object["tag"] = tag
    if tc == "no_name":
        del json_object["name"]
    elif tc == "no_geometryType":
        del json_object["geometryType"]
    elif tc == "no_radius":
        del json_object["radius"]
    elif tc == "no_coordinates":
        del json_object["coordinates"]
    elif tc == "no_IsActive":
        del json_object["isActive"]
    elif tc == "no_tolerance":
        del json_object["tolerance"]
    elif tc == "no_type":
        del json_object["type"]
    elif tc == "no_poiFlag":
        del json_object["poiFlag"]
    elif tc == "no_tag":
        del json_object["tag"]
    elif tc == "no_latitude":
        del json_object["coordinates"][0][1]
    elif tc == "no_longitude":
        del json_object["coordinates"][0][0]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_updateGeofence",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_updateGeofence', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_updateGeofence", response.text)

    return response


# Geofence - Delete
def Geofence_deleteGeofence(self, geoId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_deleteGeofence")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId)
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
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_deleteGeofence",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_deleteGeofence', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_deleteGeofence", response.text)

    return response


# Geofence - get geofence list
def Geofence_getGeofences(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_getGeofences")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint)
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
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_deleteGeofence",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_getGeofences', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_getGeofences", response.text)

    return response


# RE-API Modules:
# Geofence - get geofence list
def geofence_getGeofence_by_systemId(self, systemId, offset, limit, isActive, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_getGeofence_by_systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace("{systemId}", systemId).replace("{offset}", offset).replace(
        "{limit}", limit).replace("{isActive}", isActive)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apikey_length" in tc:
        header_x["api-key"] = 'Y2NzZXJ2aWNlQDc4O'
    header_x = header_update(header_x, tc)
    # print("Header : ", header_x)

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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_getGeofence_by_systemId",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_getGeofence_by_systemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_getGeofence_by_systemId", response.text)

    return response


# TelemetryLocation_saveVehicleLocation
def geofence_map_geofence_to_vehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                     ruleExpression, systemId, name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_map_geofence_to_vehicle")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apikey_length" in tc:
        header_x["api-key"] = 'Y2NzZXJ2aWNlQDc4O'
    header_x = header_update(header_x, tc)
    # print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["geoId"] = geoId
    json_object["mapping"][0]["notification"] = notification
    json_object["mapping"][0]["isEdgeEnabled"] = isEdgeEnabled
    json_object["mapping"][0]["ruleId"] = ruleId
    json_object["mapping"][0]["isActive"] = isActive
    json_object["mapping"][0]["ruleExpression"] = ruleExpression
    json_object["mapping"][0]["systemId"] = systemId
    json_object["mapping"][0]["name"] = name
    if "no_isActive" in tc:
        del json_object["mapping"][0]["isActive"]
    elif "no_systemId" in tc:
        del json_object["mapping"][0]["systemId"]
    elif "no_mapping" in tc:
        del json_object["mapping"]
    elif "null_mapping" in tc:
        json_object["mapping"] = None
    elif "null_notification" in tc:
        json_object["mapping"][0]["notification"] = ""
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_map_geofence_to_vehicle",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_map_geofence_to_vehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_map_geofence_to_vehicle", response.text)

    return response


def geofence_getGeofence_by_vehicleMappingId(self, vehicleMappingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_getGeofence_by_vehicleMappingId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace("{vehicleMappingId}", vehicleMappingId).replace(' ', '')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    # print("Header : ", header_x)

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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_getGeofence_by_vehicleMappingId",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_getGeofence_by_vehicleMappingId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_getGeofence_by_vehicleMappingId", response.text)

    return response


# Geofence - Delete
def geofence_deleteGeofence_by_vehicleMappingId(self, Id, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_deleteGeofence_by_vehicleMappingId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{vehicleMappingId}', Id).replace(' ', '')
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
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_deleteGeofence_by_vehicleMappingId",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_deleteGeofence_by_vehicleMappingId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_deleteGeofence_by_vehicleMappingId", response.text)

    return response


def Geofence_getGeofences_new(self, offset, limit, name, geoId, isActive, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_getGeofence")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{offset}', offset).replace('{limit}', limit).replace('{geoName}',
                                                                                                          name).replace(
        '{isActive}', isActive).replace('{geoId}', geoId)
    if "geoName" in tc:
        complete_url = str(base_url + endpoint).replace('{offset}', offset).replace('{limit}', limit).replace(
            '{geoName}', name).replace("&isActive={isActive}&geoId={geoId}", "")
    elif "isActive" in tc:
        complete_url = str(base_url + endpoint).replace('{offset}', offset).replace('{limit}', limit).replace(
            '{geoName}', name).replace('{isActive}', isActive).replace("&geoId={geoId}", "")

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
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_deleteGeofence",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_getGeofence', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_getGeofence", response.text)

    return response


# TelemetryLocation_saveVehicleLocation
def geofence_update_geofence_to_vehicle(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                        ruleExpression, name, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_update_geofence_to_vehicle")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{geoId}', geoId)
    if tc == "geofence_enable_disable":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{geoId}', geoId) + "?action={action}".replace(
            '{action}', action)

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apikey_length" in tc:
        header_x["api-key"] = 'Y2NzZXJ2aWNlQDc4O'
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["notification"] = notification
    json_object["isEdgeEnabled"] = isEdgeEnabled
    json_object["ruleId"] = ruleId
    json_object["isActive"] = isActive
    json_object["ruleExpression"] = ruleExpression
    json_object["name"] = name
    if "no_isActive" in tc:
        del json_object["isActive"]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Geofence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Geofence_update_geofence_to_vehicle",
                                                "Geofence_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_update_geofence_to_vehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_update_geofence_to_vehicle", response.text)

    return response


# geofence precondition
def geofence_save_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2,
                               statePreconditions3, tc):
    # Read API test data from Excel
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_save_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Construct URL and headers
    complete_url = base_url + endpoint
    print("Complete URL:", complete_url)

    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:", header_x)

    # Prepare payload
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["action"] = action

    if cloudEnv not in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8"]:
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
        json_object["precondition"]["statePreconditions"][2] = statePreconditions3
    else:
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2

    payload = json_object
    print("Payload:", payload)

    # Send POST request
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response:", response.text)

    # Save response
    save_api_resp_into_file('Geofence_save_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_save_precondition", response.text)

    return response


def geofence_update_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2,
                                 statePreconditions3, tc):
    # Read API test data from Excel
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_update_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Construct URL and headers
    complete_url = base_url + endpoint
    print("Complete URL:", complete_url)

    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:", header_x)

    # Prepare payload
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["action"] = action

    if cloudEnv not in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8"]:
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
        json_object["precondition"]["statePreconditions"][2] = statePreconditions3
    else:
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2

    payload = json_object
    print("Payload:", payload)

    # Send PUT request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response:", response.text)

    # Save response
    save_api_resp_into_file('Geofence_update_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_update_precondition", response.text)

    return response


def geofence_get_precondition(self, model, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Geofence_get_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send DELETE request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Geofence_get_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "Geofence_get_precondition", response.text)

    return response


# Geofence reusable modules

def geofence_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3,
                          tc):
    # Call appropriate API based on test case
    if tc == "save_precondition":
        response = geofence_save_precondition(
            self, cloudEnv, model, action,
            statePreconditions1, statePreconditions2, statePreconditions3, "valid"
        )
    elif tc == "update_precondition":
        response = geofence_update_precondition(
            self, cloudEnv, model, action,
            statePreconditions1, statePreconditions2, statePreconditions3, "valid"
        )

    # Validate response status
    if response.status_code == 200:
        response_body = response.json()
        if tc == "save_precondition":
            if response_body.get("message") == "Data Saved Successfully":
                print("Geofence precondition data saved successfully.")
            else:
                print("Failed to save geofence precondition.")
                assert False
        elif tc == "update_precondition":
            if response_body.get("message") == "Data Updated Successfully":
                print("Geofence precondition data updated successfully.")
            else:
                print("Failed to update geofence precondition.")
                assert False
    elif response.status_code == 400:
        response_body = response.json()
        error = response_body["errors"][0]
        if error["errorCode"] == "15586" and error["message"] == "Data already exists in db for Model & Action":
            print("Geofence precondition data already exists in DB for the model.")
    else:
        print(f"Unexpected response status code: {response.status_code}")
        assert False

    # Fetch saved precondition
    response = geofence_get_precondition(self, model, action, "valid")
    if response.status_code != 200:
        print(f"API request failed with status {response.status_code}")
        assert False

    response_body = response.json()
    if response_body.get("model") == model and response_body.get("action") == action:
        print("----------------------------------------------------------")
        print(f"Message: {response_body.get('message')}")
        print("----------------------------------------------------------")

        preconditions = response_body.get("preConditions", {}).get("statePreconditions")
        if not preconditions:
            print("No preConditions found in response body.")
            return

        print(f"Fetched Precondition: {preconditions}")

        # Extract individual preconditions
        ignition = preconditions[0]
        vehicle_mode = preconditions[1]
        park_mode = preconditions[2] if cloudEnv not in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5",
                                                         "PRE-PROD", "GCP-QA8"] else None

        # Validate ignition
        if ignition["attribute"] == "ignition" and ignition["operator"] == "eq" and ignition["value"][0] == "ON":
            expected_modes = {"PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE", "NORMAL_MODE"}
            fetched_modes = set(vehicle_mode["value"])

            # Validate vehicle mode
            if vehicle_mode["attribute"] == "vehicleMode" and vehicle_mode[
                "operator"] == "in" and expected_modes == fetched_modes:
                if cloudEnv not in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8"]:
                    # Validate park mode
                    if park_mode["attribute"] == "parkMode" and park_mode["operator"] == "eq" and park_mode["value"][
                        0] == "OFF":
                        testResult(self, "passed",
                                   "Geofence precondition data should be saved and fetched successfully.",
                                   "Geofence precondition data is saved successfully.")
                    else:
                        testResult(self, "failed",
                                   "Geofence precondition data should be saved and fetched successfully.",
                                   "Geofence precondition data is NOT saved successfully.")
                else:
                    pass  # Skipped for GCP-QA3 and DM1
            else:
                print(f"Vehicle Mode mismatch! Expected: {expected_modes}, Fetched: {fetched_modes}")
                testResult(self, "failed", "Precondition mismatch",
                           "Geofence conditions do not match expected values.")
        else:
            print(f"Ignition mismatch! Expected: ON, Fetched: {ignition['value']}")
            testResult(self, "failed", "Precondition mismatch",
                       "Ignition condition does not match expected value.")

def geofence_enable_disable(self, systemId, notification, isEdgeEnabled, ruleId, isActive,
                                        ruleExpression, name, action, tc):
    # read geoId
    geoId_file = os.path.join(folder_path, 'geoId.txt')
    print("Geofence Id File : ", geoId_file)

    with open(geoId_file, "r", encoding="utf-8") as f:
        geoId = f.read().strip()  # <-- strip to remove \n, spaces

    # read vehicleMappingId  (FIX: use the correct file)
    vehicleMappingId_file = os.path.join(folder_path, 'vehicleMappingId.txt')
    print("Vehicle Mapping Id File : ", vehicleMappingId_file)

    with open(vehicleMappingId_file, "r", encoding="utf-8") as f:
        vehicleMappingId = f.read().strip()  # <-- strip to remove \n, spaces


    response = geofence_update_geofence_to_vehicle(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                        ruleExpression, name, action, "geofence_enable_disable")

    if response.status_code == 200:
        assert True
    else:
        print("Response status code is not 200. Rather than found: ", response.status_code)
        assert False

    response_body = response.json()

    if tc == "disable":
        if response_body["message"] == "DISABLE initiated in the device":
            vehicleMappingId_actual = response_body["responseData"]["vehicleMappingId"]
            if vehicleMappingId_actual == vehicleMappingId:
                assert True
                testResult(self, "passed", "Geofence should be disbaled", "Geofence is disbaled")
            else:
                assert False
        else:
            assert False
    elif tc == "enable":
        if response_body["message"] == "ENABLE initiated in the device":
            vehicleMappingId_actual = response_body["responseData"]["vehicleMappingId"]
            if vehicleMappingId_actual == vehicleMappingId:
                assert True
            else:
                assert False
        else:
            assert False
    else:
        assert False

    # Call API reusable module
    response = geofence_getGeofence_by_systemId(self, systemId, "1", "10", isActive, "valid")

    # Validate response status code
    assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
    response_body = response.json()

    # Validate response body
    if response_body["message"] == "Data Fetched Successfully":
        geofences = response_body["responseData"]["geofences"]
        found = False

        for geofence in geofences:
            isEdgeEnabled = geofence["isEdgeEnabled"]
            actual_geoId = geofence["geofence"]["geoId"]


            if actual_geoId == geoId and str(isEdgeEnabled) == "1":
                found = True

                if "isAssociated" in geofence:
                    isAssociated = geofence["isAssociated"]
                    if tc == "disable":
                        if bool(isAssociated) == False:
                            testResult(self, "passed",
                                       f"Geofence with geoId '{geoId}' and {systemId} should be disabled and should fetch with status {isAssociated}.",
                                       f"Geofence with geoId '{geoId}' and {systemId} is successfully disabled and fetched with status {isAssociated}.")
                        else:
                            testResult(self, "failed",
                                       f"Geofence with geoId '{geoId}' and {systemId} should be disabled and should fetch with status {isAssociated}.",
                                       f"Geofence with geoId '{geoId}' and {systemId} is not successfully disabled and fetched with status {isAssociated}.")
                    if tc == "enable":
                        if bool(isAssociated) == True:
                            testResult(self, "passed",
                                       f"Geofence with geoId '{geoId}' and {systemId} should be enabled and should fetch with status {isAssociated}.",
                                       f"Geofence with geoId '{geoId}' and {systemId} is successfully enabled and fetched with status {isAssociated}.")
                        else:
                            testResult(self, "failed",
                                       f"Geofence with geoId '{geoId}' and {systemId} should be enabled and should fetch with status {isAssociated}.",
                                       f"Geofence with geoId '{geoId}' and {systemId} is not successfully enabled and fetched with status {isAssociated}.")
                elif "geofenceStatus" in geofence:
                    device_status = geofence["geofenceStatus"]
                    if device_status == "UPDATED_IN_DEVICE":
                        testResult(self, "passed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' is successfully created and fetched with status {device_status}.")
                    else:
                        testResult(self, "failed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' has unexpected status {device_status}.")
                else:
                    testResult(self, "failed",
                               "Newly created geofence should be listed & fetched successfully",
                               f"Geofence with geoId '{geoId}' has no recognizable status field.")
                break

        if not found:
            testResult(self, "failed",
                       "Newly created geofence should be listed & fetched successfully",
                       f"No matching geofence found for geoId: {geoId}. Refer to device/cloud logs or API response.")
    else:
        print(f"Unexpected response message: {response_body['message']}")
        testResult(self, "failed",
                   "Newly created geofence should be listed & fetched successfully",
                   f"Unexpected response message: {response_body['message']}. Refer to device & cloud logs for more details.")


def create_circle_polygon_geofence(self, onboardingType, chipsetType, name, geometryType, radius, long, lat, isActive,
        tolerance, type1, poiFlag, tag, notification, isEdgeEnabled, ruleId,
                                 ruleExpression, tc):
    print("----------------------------------------------------------")
    print("Geofence - Cloud Precondition")
    print("----------------------------------------------------------")

    # Set ignition ON via stub
    run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, 'ignition_on_alert')
    time.sleep(5)

    print("----------------------------------------------------------")
    print("* * * * * * * * GET CURRENT VEHICLE MODE * * * * * * * * *")
    print("----------------------------------------------------------")

    systemId = read_vehicleJsonFile(self, "system_id")
    cloudEnv = read_cloud_env(self)

    currentState, connectionState, speed, vehicleMode, parkMode, rideMode, ignition, deviceActivationState, rodeState = vehicle_state_info(
        self, cloudEnv, systemId, "regional"
    )

    if ignition == "ON" and vehicleMode in ["NORMAL_MODE", "PRIVACY_MODE", "INCOGNITO_MODE", "VACATION_MODE"]:
        testResult(self, "passed",
                   "Cloud precondition should satisfy to create the geofence",
                   "Cloud precondition is satisfied to create the geofence")
        assert True
    else:
        testResult(self, "failed",
                   "Cloud precondition should satisfy to create the geofence",
                   "Cloud precondition is not satisfied to create the geofence")
        assert False

    print("----------------------------------------------------------")
    print("Create new geofence with predefined input/data")
    print("----------------------------------------------------------")

    # Create geofence
    if tc == "circle":
        response = Geofence_createGeofence(
            self, name, geometryType, radius, long, lat, isActive,
            tolerance, type1, poiFlag, tag, "valid"
        )
    elif tc == "polygon":
        # Create geofence
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "polygon_geofence")
    else:
        print("Invalid Testcases")

    assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
    response_body = response.json()

    if response_body["message"] == "Data Saved Successfully":
        geoId = response_body["responseData"]["geoId"]
        print("----------------------------------------------------------")
        print("Geofence Id:", geoId)
        print("----------------------------------------------------------")
        testResult(self, "passed",
                   "New geofence should be created successfully",
                   "New geofence is created successfully")
    else:
        testResult(self, "failed",
                   "New geofence should be created successfully",
                   f"New geofence is not created. Reason: {response_body['responseData']['message']}")
        assert False

    #Save geoId
    geoId_file = os.path.join(folder_path, 'geoId.txt')
    print("Geofence Id File : ", geoId_file)

    text_file = open(geoId_file, "w+")
    text_file.write(str(geoId))
    text_file.close()

    print("----------------------------------------------------------")
    print("Map Geofence with Vehicle")
    print("----------------------------------------------------------")

    # Map geofence to vehicle
    response = geofence_map_geofence_to_vehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                 ruleExpression, systemId, name, "valid")

    assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
    response_body = response.json()

    mapping_msg = response_body["geofenceMappings"][0]["message"]
    if mapping_msg == "Geofence creation Initiated in the device":
        vehicleMappingId = response_body["geofenceMappings"][0]["vehicleMappingId"]
        print("----------------------------------------------------------")
        print("Vehicle Mapping Id:", vehicleMappingId)
        print("Message:", mapping_msg)
        print("----------------------------------------------------------")
        testResult(self, "passed",
                   "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                   "Geofence creation is initiated and mapped to Vehicle successfully")
    else:
        testResult(self, "failed",
                   "Geofence creation should be initiated in device and mapped to Vehicle successfully",
                   f"Failed to initiate or map geofence. Reason: {mapping_msg}")
        assert False

    # Save vehicleMappingId
    vehicleMappingId_file = os.path.join(folder_path, 'vehicleMappingId.txt')
    print("Vehicle Mapping Id File : ", vehicleMappingId_file)

    text_file = open(vehicleMappingId_file, "w+")
    text_file.write(str(vehicleMappingId))
    text_file.close()

    print("----------------------------------------------------------")
    print("Validation of Geofence Creation at Device:")
    print("----------------------------------------------------------")

    # Pull logs for validation
    print("Pull/Fetch device logs for validation:")
    pull_logs_from_IVI_device(self, onboardingType, chipsetType)
    print("Logs are fetched from device to host machine @ desired location")
    print("----------------------------------------------------------")

    # Define expected log messages
    conf_msg = "configuration data ="
    msgType_16650 = '"message_type": 16650'
    msg_266 = "Message type: 266 : Encoding type : 2"
    flush_msg = "Flush geofence table success"
    msg_268 = "Message type: 268 : Encoding type : 2"
    msg_267 = "Message type: 267 : Encoding type : 1"

    # Validate geofence configuration message
    ls = verify_message_in_log(self, conf_msg, conf_msg)
    if conf_msg in str(ls[0]):
        print("=> Device received required geofence details from cloud successfully")
        testResult(self, "passed",
                   "Device should receive geofence details from cloud",
                   "Device received geofence details successfully. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> Device failed to receive geofence details from cloud")
        testResult(self, "verificationFailed",
                   "Device should receive geofence details from cloud",
                   "Device failed to receive geofence details. Refer to device logs.")

    print("----------------------------------------------------------")

    # Validate geoId presence
    ls = verify_message_in_log(self, geoId, geoId)
    if geoId in str(ls[0]):
        print("=> GeoId is present and matches POST API creation")
        testResult(self, "passed",
                   "GeoId should match POST API creation",
                   "GeoId matches POST API creation. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> GeoId is missing or mismatched")
        testResult(self, "verificationFailed",
                   "GeoId should match POST API creation",
                   "GeoId missing or mismatched. Refer to device logs.")

    print("----------------------------------------------------------")

    # Validate geofence creation request message
    ls = verify_message_in_log(self, msg_266, msg_266)
    if msg_266 in str(ls[0]):
        print("=> Device received geofence creation request from cloud")
        testResult(self, "passed",
                   "Device should receive geofence creation request from cloud",
                   "Device received geofence creation request successfully. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> Device failed to receive geofence creation request")
        testResult(self, "verificationFailed",
                   "Device should receive geofence creation request from cloud",
                   "Device failed to receive geofence creation request. Refer to device logs.")

    print("----------------------------------------------------------")

    # Validate acknowledgement message
    ls = verify_message_in_log(self, msg_267, msg_267)
    if msg_267 in str(ls[0]):
        print("=> Device sent acknowledgement to cloud")
        testResult(self, "passed",
                   "Device should send acknowledgement to cloud",
                   "Device sent acknowledgement successfully. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> Device failed to send acknowledgement to cloud")
        testResult(self, "verificationFailed",
                   "Device should send acknowledgement to cloud",
                   "Device failed to send acknowledgement. Refer to device logs.")

    print("----------------------------------------------------------")

    # Validate geofence table flush
    ls = verify_message_in_log(self, flush_msg, flush_msg)
    if msg_268 in str(ls[0]):
        print("=> Device flushed geofence table successfully")
        testResult(self, "passed",
                   "Device should flush geofence table",
                   "Device flushed geofence table successfully. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> Device failed to flush geofence table")
        testResult(self, "verificationFailed",
                   "Device should flush geofence table",
                   "Device failed to flush geofence table. Refer to device logs.")

    print("----------------------------------------------------------")

    # Validate final response message
    ls = verify_message_in_log(self, msg_268, msg_268)
    if msg_268 in str(ls[0]):
        print("=> Device sent final response to cloud")
        testResult(self, "passed",
                   "Device should send final response to cloud",
                   "Device sent final response successfully. Refer to device logs.")
        print("c2c logs line data:", ls[0])
    elif str(ls[0]) == "Error":
        print("=> Device failed to send final response to cloud")
        testResult(self, "verificationFailed",
                   "Device should send final response to cloud",
                   "Device failed to send final response. Refer to device logs.")

    print("----------------------------------------------------------")
    print("----------------------------------------------------------")
    print("Cloud Side Validations: Fetch Geofence List to verify newly created geofence details")
    print("----------------------------------------------------------")

    # Call API reusable module
    response = geofence_getGeofence_by_systemId(self, systemId, "1", "10", isActive, "valid")

    # Validate response status code
    assert response.status_code == 200, f"Status code is not 200. Rather found: {response.status_code}"
    response_body = response.json()

    # Validate response body
    if response_body["message"] == "Data Fetched Successfully":
        geofences = response_body["responseData"]["geofences"]
        found = False

        for geofence in geofences:
            isEdgeEnabled = geofence["isEdgeEnabled"]
            actual_geoId = geofence["geofence"]["geoId"]

            if actual_geoId == geoId and str(isEdgeEnabled) == "1":
                found = True

                if "deviceStatus" in geofence:
                    device_status = geofence["deviceStatus"]
                    if str(device_status) == "1":
                        testResult(self, "passed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' is successfully created and fetched with status {device_status}.")
                    else:
                        testResult(self, "failed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' has unexpected status {device_status}.")
                elif "geofenceStatus" in geofence:
                    device_status = geofence["geofenceStatus"]
                    if device_status == "SAVED_IN_DEVICE":
                        testResult(self, "passed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' is successfully created and fetched with status {device_status}.")
                    else:
                        testResult(self, "failed",
                                   "Newly created geofence should be listed & fetched successfully",
                                   f"Geofence with geoId '{geoId}' has unexpected status {device_status}.")
                else:
                    testResult(self, "failed",
                               "Newly created geofence should be listed & fetched successfully",
                               f"Geofence with geoId '{geoId}' has no recognizable status field.")
                break

        if not found:
            testResult(self, "failed",
                       "Newly created geofence should be listed & fetched successfully",
                       f"No matching geofence found for geoId: {geoId}. Refer to device/cloud logs or API response.")
    else:
        print(f"Unexpected response message: {response_body['message']}")
        testResult(self, "failed",
                   "Newly created geofence should be listed & fetched successfully",
                   f"Unexpected response message: {response_body['message']}. Refer to device & cloud logs for more details.")

    print("----------------------------------------------------------")
