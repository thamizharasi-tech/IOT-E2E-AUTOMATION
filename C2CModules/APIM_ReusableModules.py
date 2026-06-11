import ast
import json
import time

import requests

from C2CModules.resuse_modules import verify_message_in_log, save_api_resp_into_file
from C2CModules.e2e_testData import tripId_code
from C2CModules.testResults import testResult
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# APIM-Telemetry Modules
# ---------------------------------


def getTelemetryCurrValue(self, systemId,testcaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get System Telemetry Curr Values")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if "telemetryCurrValues" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)
    elif "telemetryValuesForHandles" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/body/handles"
    elif "telemetryValuesForHorn" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/body/horn"
    elif "telemetryValuesForTailLight" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/body/tail-light"
    elif "telemetryValuesForHeadLight" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/body/head-light"
    elif "telemetryValuesForHazardLight" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/body/hazard-light"
    elif "telemetryValuesForHighBeamLightState" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/high-beam-lights-state"
    elif "telemetryValuesForIndicator" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/indicator"
    elif "telemetryValuesForSideStand" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/side-stand"
    elif "telemetryValuesForBatteryReadings" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/battery"
    elif "telemetryValuesForBatteryLevel" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/battery/level"
    elif "telemetryValuesForBatteryTemperature" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/battery/temperature"
    elif "telemetryValuesForBatteryBMSTemperature" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}',systemId)+"/battery/bms-temperature"
    elif "telemetryValuesForLocation" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/location"
    elif "telemetryValuesForIgnitionStatus" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/engine/ignition"
    elif "telemetryValuesForEngineMobilize" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/engine/mobilize"
    elif "telemetryValuesForTyrePressure" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/pressure"
    elif "telemetryValuesForFrontRightTyrePressure" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/front/right/pressure"
    elif "telemetryValuesForFrontLeftTyrePressure" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/front/left/pressure"
    elif "telemetryValuesForRearRightTyrePressure" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/rear/right/pressure"
    elif "telemetryValuesForRearLeftTyrePressure" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/rear/left/pressure"
    elif "telemetryValuesForRearCriticalPressureThreshold" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/rear/critical-pressure-threshold"
    elif "telemetryValuesForFrontCriticalPressureThreshold" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/body/tires/front/critical-pressure-threshold"
    elif "telemetryValuesForEngineOdometer" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/engine/odometer"
    elif "telemetryValuesForRangeRemaining" in testcaseName:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId)+"/range-remaining"

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)
    # Act: convert dict to json by json.dumps() for body data and send request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get Telemetry Handles Value', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Telemetry Handles Value", response.text)

    return response


#-----------------------------------------------------------------------------
#APIM- Trip Modules
#-----------------------------------------------------------------------------
# AssetManagement_trip-info-by-tripId
def assetManagement_trip_info_by_tripId(self, trip_id):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-info-by-tripId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{tripIdValue}', trip_id).replace('\n', '')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-info-by-tripId",
                                                "AssetManagement_trip_AuthToken")
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip-info-by-tripId', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip-info-by-tripId", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body


# AssetManagement_trip-waypoints-by-tripid
def assetManagement_trip_waypoints_by_tripid(self, trip_id):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-waypoints-by-tripid")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{tripId}', trip_id).replace('\n', '')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-waypoints-by-tripid",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip-waypoints-by-tripid', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip-waypoints-by-tripid", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body


# AssetManagement_trip-waypoints-by-systemId
def assetManagement_trip_waypoints_by_systemId(self, startDate, endDate, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-waypoints-by-systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = str(base_url + endpoint).replace('{startDate}', startDate)
    completeurl = str(url).replace('{endDate}', endDate)
    complete_url = str(completeurl).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-waypoints-by-systemId",
                                                "AssetManagement_trip_AuthToken")
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip-waypoints-by-systemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip-waypoints-by-systemId", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body

def get_tridId_from_log(self):
    print("Read the trip id from c2c log file")
    ls = verify_message_in_log(self, tripId_code, tripId_code)

    if tripId_code in str(ls[0]):
        print(str(ls[0]))
        trip_id = str(ls[0]).split('trip_id: ')
        trip_id = str(trip_id[1])
        print(f"Trip Id should be generated in 'systemId_timestamp' format")
        testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                   "Trip Id is generated in 'systemId_timestamp' format")
        print("Trip Id : ", trip_id)
    if str(ls[0]) == "Error":
        ls = verify_message_in_log(self, 'Trip_id: ', 'Trip_id: ')
        print(ls)
        trip_id = str(ls[0]).split('Trip_id: ')
        trip_id = str(trip_id[1])
        print(f"Trip Id should be generated in 'systemId_timestamp' format")
        testResult(self, "passed", "Telemetry message should be published to cloud via Hub ",
                   "Trip Id is generated in 'systemId_timestamp' format")
        print("Trip Id : ", trip_id)
        if str(ls[0]) == "Error":
            print("Trip Id is not generated or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip Id should be generated in 'systemId_timestamp' format",
                       "Trip Id is not generated or device logs are not updated. pls refer device "
                       "logs in detail ")
            trip_id = ""
    return trip_id

# Trip_DriverScoreCard_driverScore
def Trip_DriverScoreCard_impactScoreBySystemId(self, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Vehicle Score")
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
    print(header_x)

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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "DriverScoreCard_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_driverScore",
                                                "DriverScoreCard_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('Get Vehicle Score', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Vehicle Score", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body




#---------------------------------------------------------------------------------
#APIM-Telemetry Location Modules
#---------------------------------------------------------------------------------

# TelemetryLocation_saveVehicleLocation
def TelemetryLocation_saveVehicleLocation(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                              ruleExpression, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_saveVehicleLocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geoId}', geoId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

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

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

# TelemetryLocation_updateVehicleLocation
def TelemetryLocation_updateVehicleLocation(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                ruleExpression,name):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_updateVehicleLocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{geoId}', geoId).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["notification"] = notification
    json_object["isEdgeEnabled"] = isEdgeEnabled
    json_object["ruleId"] = ruleId
    json_object["isActive"] = isActive
    json_object["ruleExpression"] = ruleExpression
    json_object["name"] = name
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

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

# TelemetryLocation_getVehicleLocation
def TelemetryLocation_getVehicleLocation(self,systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_getVehicleLocation")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}',systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

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

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

# TelemetryLocation_deleteVehicleLocation
def TelemetryLocation_deleteVehicleLocation(self, vehicleMappingId):
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
    print(header_x)

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

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# Telemetry_Location_nearestPOIlocation
def Telemetry_Location_nearestPOIlocation(self, latitude, longitude, radius,testcaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Points Of Interest")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for request

    # Url :
    complete_url = str(base_url + endpoint)
    if "getNearestLocationBy_radiusLatLong" in testcaseName:
        complete_url = str(base_url + endpoint)+"?radius={radius}&latitude={latitude}&longitude={longitude}".replace('{radius}',radius).replace('{latitude}',latitude).replace('{longitude}',longitude)

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

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
    save_api_resp_into_file('Get Points Of Interest', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Points Of Interest", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

#------------------------------------------------------------------------------------
#APIM-Notify connect Modules
#------------------------------------------------------------------------------------
# Notification Service Controller -Subscribe
def notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName, destinationType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_subscribe")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filterValues"][0]["systemId"] = systemId
    json_object["filterValues"][0]["vin"] = vin
    json_object["category"][0]["endPoint"] = endPoint
    json_object["category"][0]["categoryName"] = categoryName
    json_object["category"][0]["destinationType"] = destinationType
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
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_subscribe', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_subscribe", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body



# Notification Service Controller - Details by System Id
def notificationServiceController_details_by_systemId(self, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_details_by_systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}',systemId)
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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_details_by_systemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_details_by_systemId", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

# Notification Service Controller -Un-Subscribe
def notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName, destinationType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_unsubscribe")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filterValues"][0]["systemId"] = systemId
    json_object["filterValues"][0]["vin"] = vin
    json_object["category"][0]["endPoint"] = endPoint
    json_object["category"][0]["categoryName"] = categoryName
    json_object["category"][0]["destinationType"] = destinationType
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
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_unsubscribe', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_unsubscribe", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body

#Get notofications
def notificationServiceController_getNotifications(self,type,subscriber,testcaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_get_notifications")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if "getNotificationsByType" in testcaseName:
        complete_url = str(base_url + endpoint)+"?type={type}".replace('{type}',type)
    elif "getNotificationsBySubscriber" in testcaseName:
        complete_url = str(base_url + endpoint)+"?subscriber={subscriber}".replace('{subscriber}',subscriber)
    elif "getNotificationsBy_TypeSubscriber" in testcaseName:
        complete_url = str(base_url + endpoint)+"?type={type}&subscriber={subscriber}".replace('{type}',type).replace('{subscriber}',subscriber)
    else:
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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_unsubscribe', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_unsubscribe", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body
#------------------------------------------------------------------------------
#APIM- Command&Control Modules
#------------------------------------------------------------------------------
# APIIM CommandControl_Request : horn
def commandControl_Request_APIIM_horn(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_horn")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "horn-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_horn', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_horn", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response


# APIIM CommandControl_Request : head-light
def commandControl_Request_APIIM_headlight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_headlight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "headlight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_headlight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_headlight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response







# APIIM CommandControl_Request : hazard-light
def commandControl_Request_APIIM_hazardlight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_hazardlight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "hazardlight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_hazardlight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_hazardlight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response



# APIIM CommandControl_Request : flash-light
def commandControl_Request_APIIM_flashlight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_flashlight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "flashlight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_flashlight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_flashlight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response




# APIIM CommandControl_Request : emergency-light
def commandControl_Request_APIIM_emergencylight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_emergencylight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "emergencylight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_emergencylight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_emergencylight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response



# APIIM CommandControl_Request : ambient light
def commandControl_Request_APIIM_ambientlight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_ambientlight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "ambientlight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_ambientlight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_ambientlight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response


# APIIM CommandControl_Request : ambient reading light
def commandControl_Request_APIIM_readinglight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_readinglight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "readinglight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_readinglight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_readinglight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response




# APIIM CommandControl_Request : tail-light
def commandControl_Request_APIIM_taillight(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_taillight")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "taillight-on":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_taillight', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_taillight", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response



# APIIM CommandControl_Request : buzz-bike
def commandControl_Request_APIIM_Buzzbike(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_buzzbike")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "BUZZ-BIKE-ON":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','ON')
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_buzzbike', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_buzzbike", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response



# APIIM CommandControl_Request : ignition
def commandControl_Request_APIIM_ignition(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_ignition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "HANDLE-LOCK":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','HANDLE-LOCK')
    if testCaseName == "HANDLE-UNLOCK":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'HANDLE-UNLOCK')
    if testCaseName == "IGNITION-ON":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'IGNITION-ON')
    if testCaseName == "IGNITION-OFF":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'IGNITION-OFF')
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_ignition', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_ignition", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response



# APIIM CommandControl_Request : immobilize
def commandControl_Request_APIIM_immobilize(self, appid, systemId,  testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "APIIM_CommandControl_Request_immobilize")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if testCaseName == "IMMOBILIZE":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}','IMMOBILIZE')
    if testCaseName == "MOBILIZE":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', 'MOBILIZE')

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)
    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('APIIM_CommandControl_Request_immobilize', response.text)
    save_api_resp_in_excel(self, "API_Data", "APIIM_CommandControl_Request_immobilize", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    return response

#-----------------------------------------------------------------------------------
#APIM-Vehicle Metadata Modules
#-----------------------------------------------------------------------------------

# Vehicle_get-all-vehicle-details
def vehicle_getAll_vehicle_details(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get All vehicles")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get All vehicles', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get All vehicles", response.text)

    return response


# Vehicle_get-vehicle-meta-data-by-vin
def vehicle_get_vehicle_meta_data_by_vin(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Vehicle Data By VIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{vin}', vin)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get Vehicle Data By VIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Vehicle Data By VIN", response.text)

    return response

# Find VIN by Model
def vehicle_get_vehicle_meta_data_vins_by_model(self, model):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Find VIN by Model")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Find VIN by Model', response.text)
    save_api_resp_in_excel(self, "API_Data", "Find VIN by Model", response.text)

    return response

# Vehicle_get-vehicle-meta-data-by-deviceId
def vehicle_get_vehicle_meta_data_by_deviceId(self, deviceId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "findVehicleDetailsByDeviceId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{deviceId}', deviceId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('findVehicleDetailsByDeviceId', response.text)
    save_api_resp_in_excel(self, "API_Data", "findVehicleDetailsByDeviceId", response.text)

    return response


# Vehicle_update-vehicle-meta-data-by-vin
def vehicle_update_vehicle_meta_data_by_vin(self, vin, make, brand, trim, chassis_number, engine_type, model, year, manufacturing_plant, manufacturing_country, manufacturing_date, manufacturing_location, vehicle_registration, vehicle_registration_date):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Update Vehicle Data By VIN")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["make"] = make
    json_object["brand"] = brand
    json_object["trim"] = trim
    json_object["chassis_number"] = chassis_number
    json_object["engine_type"] = engine_type
    json_object["model"] = model
    json_object["year"] = year
    json_object["manufacturing_plant"] = manufacturing_plant
    json_object["manufacturing_country"] = manufacturing_country
    json_object["manufacturing_date"] = manufacturing_date
    json_object["manufacturing_location"] = manufacturing_location
    json_object["vehicle_registration"] = vehicle_registration
    json_object["vehicle_registration_date"] = vehicle_registration_date
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Update Vehicle Data By VIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "Update Vehicle Data By VIN", response.text)

    return response

#------------------------------------------------------------------------------------
#APIM- Device Metadata Modules
#------------------------------------------------------------------------------------
# Vehicle_get-vehicle-meta-data-by-deviceId
def vehicle_get_device_meta_data(self, deviceId,testcaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Devices")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    if "getDevicesBydeviceId" in testcaseName:
        complete_url = str(base_url + endpoint)+"/{deviceId}".replace('{deviceId}', deviceId)
    else:
        complete_url = str(base_url + endpoint)

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get Devices', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Devices", response.text)

    return response
# Device metadata : update-device-lifecycle-state
def device_meta_data_update_lifecycle_state(self, deviceId,lifecycleState):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Update Device Lifecycle State")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{deviceId}', deviceId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["newState"] = lifecycleState

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Update Device Lifecycle State', response.text)
    save_api_resp_in_excel(self, "API_Data", "Update Device Lifecycle State", response.text)

    return response

#--------------------------------------------------------------------------------
#APIM - Vehicle Service,DTC Modules
#--------------------------------------------------------------------------------
def dtc_processDTC(self, dtcCode, systemId, subsystemId, deviceId, action):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Process DTC")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{dtc-code}',dtcCode).replace('{action}',action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["dtcCode"] = dtcCode
    json_object["systemId"] = systemId
    json_object["subSystemId"] = subsystemId
    json_object["deviceId"] = deviceId

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Process DTC', response.text)
    save_api_resp_in_excel(self, "API_Data", "Process DTC", response.text)

    return response

#Book vehicle service appointment
def vehicle_service_book_appointment(self, systemId, accountId, territoryId, workTypeGroupId, startTime, endTime,quoteId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Book Appointment")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{accountId}',accountId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["territoryId"] = territoryId
    json_object["accountId"] = accountId
    json_object["workTypeGroupId"] = workTypeGroupId
    json_object["startTime"] = startTime
    json_object["endTime"] = endTime
    json_object["quoteId"] = quoteId

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Book Appointment', response.text)
    save_api_resp_in_excel(self, "API_Data", "Book Appointment", response.text)

    return response

#get dealers available schedule
def vehicle_service_get_dealers_available_schedule(self, accountId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Schedules")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request
    # Url :
    complete_url = str(base_url + endpoint).replace('{accountId}',accountId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get Schedules', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Schedules", response.text)

    return response

#get dealers appointments
def vehicle_service_get_dealers_appointments_history(self, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "get Appointments")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request
    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}',systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('get Appointments', response.text)
    save_api_resp_in_excel(self, "API_Data", "get Appointments", response.text)

    return response

#get estimate details
def vehicle_service_get_estimate_details(self, systemId,quoteId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get Estimate Details")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request
    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}',systemId).replace('{quoteID}',quoteId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get Estimate Details', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get Estimate Details", response.text)

    return response