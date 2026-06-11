import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# TelemetryLocation_assignGeofenceToVehicle
def TelemetryLocation_assignGeofenceToVehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                              ruleExpression, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_assignGeofenceToVehicle")
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
    json_object["geoId"] = geoId
    json_object["mapping"][0]["notification"] = notification
    json_object["mapping"][0]["isEdgeEnabled"] = isEdgeEnabled
    json_object["mapping"][0]["ruleId"] = ruleId
    json_object["mapping"][0]["isActive"] = isActive
    json_object["mapping"][0]["ruleExpression"] = ruleExpression
    json_object["mapping"][0]["systemId"] = systemId
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
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryLocation_assignGeofenceToVehicle",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryLocation_assignGeofenceToVehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryLocation_assignGeofenceToVehicle", response.text)

    return response


# Telemetry_Location_bySystemId
def Telemetry_Location_bySystemId(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_bySystemId")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_bySystemId",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_bySystemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_bySystemId", response.text)

    return response


# Telemetry_Location_byGeofenceId
def Telemetry_Location_byGeofenceId(self, geoId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_byGeofenceId")
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
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_byGeofenceId",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_byGeofenceId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_byGeofenceId", response.text)

    return response


# Telemetry_Location_byGeoIdGefoNameIsActive
def Telemetry_Location_byGeoIdGefoNameIsActive(self, geoId, geoName, isActive,tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_byGeoIdGefoNameIsActive")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId).replace('{geofenceName}', geoName).replace(
        '{status}', isActive)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_byGeoIdGefoNameIsActive",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_byGeoIdGefoNameIsActive', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_byGeoIdGefoNameIsActive", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# Telemetry_Location_updateLocationForVehicle
def Telemetry_Location_updateLocationForVehicle(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                ruleExpression, vehicleStatus, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_updateLocationForVehicle")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["notification"] = notification
    json_object["isEdgeEnabled"] = isEdgeEnabled
    json_object["ruleId"] = ruleId
    json_object["isActive"] = isActive
    json_object["ruleExpression"] = ruleExpression
    json_object["vehicleStatus"] = vehicleStatus
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
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_updateLocationForVehicle",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_updateLocationForVehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_updateLocationForVehicle", response.text)

    return response


# Telemetry_Location_nearestPOIlocation
def Telemetry_Location_nearestPOIlocation(self, latitude, longitude, radius, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_nearestPOIlocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for request

    # Url :
    complete_url = str(base_url + endpoint).replace('{latitude}', str(latitude)).replace('{longitude}', str(longitude)).replace(
        '{radius}', str(radius))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_nearestPOIlocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_nearestPOIlocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_nearestPOIlocation", response.text)

    return response




# ---------------------------------
# API Modules - NEW
# ---------------------------------

# TelemetryLocation_saveVehicleLocation
def TelemetryLocation_saveVehicleLocation(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                              ruleExpression, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_saveVehicleLocation")
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
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["geoId"] = geoId
    json_object["mapping"][0]["notification"] = notification
    json_object["mapping"][0]["isEdgeEnabled"] = isEdgeEnabled
    json_object["mapping"][0]["ruleId"] = ruleId
    json_object["mapping"][0]["isActive"] = isActive
    json_object["mapping"][0]["ruleExpression"] = ruleExpression
    json_object["mapping"][0]["systemId"] = systemId
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
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryLocation_saveVehicleLocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryLocation_saveVehicleLocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryLocation_saveVehicleLocation", response.text)

    return response

# TelemetryLocation_updateVehicleLocation
def TelemetryLocation_updateVehicleLocation(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                ruleExpression, vehicleStatus, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_updateVehicleLocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geofenceId}', geoId).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["notification"] = notification
    json_object["isEdgeEnabled"] = isEdgeEnabled
    json_object["ruleId"] = ruleId
    json_object["isActive"] = isActive
    json_object["ruleExpression"] = ruleExpression
    json_object["vehicleStatus"] = vehicleStatus
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
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryLocation_updateVehicleLocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryLocation_updateVehicleLocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryLocation_updateVehicleLocation", response.text)

    return response

# TelemetryLocation_getVehicleLocation
def TelemetryLocation_getVehicleLocation(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_getVehicleLocation")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryLocation_getVehicleLocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryLocation_getVehicleLocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryLocation_getVehicleLocation", response.text)

    return response

# TelemetryLocation_deleteVehicleLocation
def TelemetryLocation_deleteVehicleLocation(self, vehicleMappingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_deleteVehicleLocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{vehicleMappingId}', vehicleMappingId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryLocation_deleteVehicleLocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryLocation_deleteVehicleLocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryLocation_deleteVehicleLocation", response.text)

    return response


# Telemetry_Location_nearestPOIlocation
def Telemetry_Location_nearestPOIlocation(self, latitude, longitude, radius, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Telemetry_Location_nearestPOIlocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for request

    # Url :
    complete_url = str(base_url + endpoint).replace('{latitude}', str(latitude)).replace('{longitude}', str(longitude)).replace(
        '{radius}', str(radius))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TelemetryLocation_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Location_nearestPOIlocation",
                                                "TelemetryLocation_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Telemetry_Location_nearestPOIlocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "Telemetry_Location_nearestPOIlocation", response.text)

    return response
