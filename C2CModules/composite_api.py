import ast
import json
import time
import requests
import os

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult

folder_path = "C:\Car2Cloud_E2ETesting"

# -----------------------------------------------------
# Vehicle Composite API's reusable modules
# -----------------------------------------------------

def vehicle_composite_api_to_fetch_vehicle_alert_count(self, regionCode, countryCode, engineType, model, year, tc):

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_vehicleAlertCount")
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
    json_object["regionCode"][0] = regionCode
    json_object["countryCode"][0] = countryCode
    json_object["engineType"][0] = engineType
    json_object["model"][0] = model
    json_object["year"][0] = year
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Composite_API_vehicleAlertCount', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_vehicleAlertCount", response.text)

    return response

def vehicle_composite_api_to_fetch_vehicle_status_count(self, regionCode, countryCode, engineType, model, year, tc):

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_vehicleCount")
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
    json_object["regionCode"][0] = regionCode
    json_object["countryCode"][0] = countryCode
    json_object["engineType"][0] = engineType
    json_object["model"][0] = model
    json_object["year"][0] = year
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Composite_API_vehicleCount', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_vehicleCount", response.text)

    return response

def vehicle_composite_api_to_fetch_vehicle_location(self, regionCode, countryCode, engineType, model, year, offset, limit, tc):

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_vehicleLocation")
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
    json_object["regionCode"][0] = regionCode
    json_object["countryCode"][0] = countryCode
    json_object["engineType"][0] = engineType
    json_object["model"][0] = model
    json_object["year"][0] = year
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Composite_API_vehicleLocation', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_vehicleLocation", response.text)

    return response

def vehicle_composite_api_to_fetch_vehicle_location_by_systemId(self, systemId, tc):

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_fetch_vehicle_location_by_systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
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
    save_api_resp_into_file('Composite_API_fetch_vehicle_location_by_systemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_fetch_vehicle_location_by_systemId", response.text)

    return response

# API operation to get telemetry info
def get_telemetry_data(self, countOnly, name, condition, value, systemId, offset, limit, tc):
    # Arrange: Test data (url,header and payload) for GET request
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_telemetry")
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
    json_object["countOnly"] = countOnly
    json_object["systemId"] = systemId
    json_object["name"] = name
    json_object["condition"] = condition
    json_object["value"] = value
    json_object["offset"] = offset
    json_object["limit"] = limit
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Composite_API_telemetry', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_telemetry", response.text)

    return response

def get_telemetry_history_details(self, systemId, eventType, start, stop, offset, limit, tc):
    # Arrange: Test data (url,header and payload) for GET request
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_telemetryHistory")
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
    json_object["systemId"] = systemId
    json_object["eventType"] = eventType
    json_object["start"] = start
    json_object["stop"] = stop
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Composite_API_telemetryHistory', response.text)
    save_api_resp_in_excel(self, "API_Data", "Composite_API_telemetryHistory", response.text)

    return response

# ---------------------------------------
# Telemetry History & Data COMPOSITE API Reusable Modules
# ---------------------------------------

def vehicle_alert_count(self, regionCode, countryCode, engineType, model, year, tc):
    try:
        response = vehicle_composite_api_to_fetch_vehicle_alert_count(self, regionCode, countryCode, engineType, model, year, tc)
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        records = response_body["vehicles"]["records"]
        emergency = response_body["alerts"]["Emergency"]
        D0 = response_body["alerts"]["D0"]
        D1 = response_body["alerts"]["D1"]
        D2 = response_body["alerts"]["D2"]

        if records > 0:
            testResult(self, "passed", "Vehicle Alert Count data should be fetched successfully",
                   "Vehicle Alert Count data is fetched successfully")
        else:
            testResult(self, "failed", "Vehicle Alert Count data should be fetched successfully",
                   "Failed to fetch vehicle alert count data. See API response for details")
    except Exception:
        testResult(self, "failed", "Vehicle Alert Count data should be fetched successfully",
               "Failed to fetch vehicle alert count data. See API response for details")
    print("----------------------------------------------------------")

def vehicle_status_count(self, regionCode, countryCode, engineType, model, year, tc):
    try:
        response = vehicle_composite_api_to_fetch_vehicle_status_count(self, regionCode, countryCode, engineType, model, year, tc)
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        records = response_body["vehicles"]["records"]
        statuses = ["HALT", "NO_GPS", "RUNNING", "INACTIVE", "IDLE", "DEAD", "OFFLINE"]
        for status in statuses:
            _ = response_body["status"][status]

        if records > 0:
            testResult(self, "passed", "Vehicle Status Count data should be fetched successfully",
                   "Vehicle Status Count data is fetched successfully")
        else:
            testResult(self, "failed", "Vehicle Status Count data should be fetched successfully",
                   "Failed to fetch vehicle status count data. See API response for details")
    except Exception:
        testResult(self, "failed", "Vehicle Status Count data should be fetched successfully",
               "Failed to fetch vehicle status count data. See API response for details")
    print("----------------------------------------------------------")

def vehicle_location(self, regionCode, countryCode, engineType, model, year, offset, limit, tc):
    try:
        response = vehicle_composite_api_to_fetch_vehicle_location(self, regionCode, countryCode, engineType, model, year, offset, limit, tc)
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        message = response_body["message"]
        totalRecords = response_body["totalRecords"]

        for item in response_body["vehicleLocationResponses"]:
            systemId = item["systemId"]
            vin = item["vin"]
            model = item["model"]
            group = item["group"]
            lastTrackedStr = item["lastTrackedStr"]
            lastTracked = item["lastTracked"]
            status = item["status"]
            address = item["address"]
            lat = item["location"]["lat"]
            lng = item["location"]["lng"]

        if totalRecords > 0 and message == "Data Fetched Successfully":
            testResult(self, "passed", "Vehicle Location data should be fetched successfully",
                   "Vehicle Location data is fetched successfully")
        else:
            testResult(self, "failed", "Vehicle Location data should be fetched successfully",
                   "Failed to fetch vehicle location data. See API response for details")
    except Exception:
        testResult(self, "failed", "Vehicle Location data should be fetched successfully",
               "Failed to fetch vehicle location data. See API response for details")
    print("----------------------------------------------------------")

def vehicle_location_by_systemId(self, systemId, tc):
    try:
        response = vehicle_composite_api_to_fetch_vehicle_location_by_systemId(self, systemId, tc)
        assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

        response_body = response.json()
        systemId_actual = response_body["systemId"]
        vin = response_body["vin"]
        model = response_body["model"]
        group = response_body["group"]
        lastTrackedStr = response_body["lastTrackedStr"]
        lastTracked = response_body["lastTracked"]
        status = response_body["status"]
        address = response_body["address"]
        lat = response_body["location"]["lat"]
        lng = response_body["location"]["lng"]

        if systemId == systemId_actual:
            testResult(self, "passed", "Vehicle Location data should be fetched successfully",
                   "Vehicle Location data is fetched successfully")
        else:
            testResult(self, "failed", "Vehicle Location data should be fetched successfully",
                   "System ID mismatch in response")
    except Exception:
        testResult(self, "failed", "Vehicle Location data should be fetched successfully",
               "Failed to fetch vehicle location data. See API response for details")
    print("----------------------------------------------------------")

def telemetry_history(self, systemId, eventType, start, stop, offset, limit, tc):
    # Call reusable module
    response = get_telemetry_history_details(self, systemId, eventType, start, stop, offset, limit, "valid")

    if response.status_code == 200:

        # Parse API response into JSON
        response_body = response.json()

        status_p = status_f = ""
        message = response_body["message"]
        if message == "Data Fetched Successfully":
            dataList_len = len(response_body["telemetryHistoryDataList"])
            if dataList_len >= 1:
                for i in range(dataList_len):
                    trip_id = response_body["telemetryHistoryDataList"][i]["meta"]["trip_id"]
                    device_id = response_body["telemetryHistoryDataList"][i]["meta"]["device_id"]
                    system_id = response_body["telemetryHistoryDataList"][i]["meta"]["system_id"]
                    sequence_no = response_body["telemetryHistoryDataList"][i]["meta"]["sequence_no"]
                    packet_status = response_body["telemetryHistoryDataList"][i]["meta"]["packet_status"]
                    sub_system_id = response_body["telemetryHistoryDataList"][i]["meta"]["sub_system_id"]
                    data = response_body["telemetryHistoryDataList"][i]["data"]

                    dataList_len1 = len(data)
                    if dataList_len1 >= 1:
                        for j in range(dataList_len1):
                            id = response_body["telemetryHistoryDataList"][i]["data"][j]["id"]
                            name = response_body["telemetryHistoryDataList"][i]["data"][j]["name"]
                            area = response_body["telemetryHistoryDataList"][i]["data"][j]["area"]
                            area_name = response_body["telemetryHistoryDataList"][i]["data"][j]["area_name"]
                            value = response_body["telemetryHistoryDataList"][i]["data"][j]["value"]
                            unit = response_body["telemetryHistoryDataList"][i]["data"][j]["unit"]
                    else:
                        print("Data array is empty")
                        assert False

                    print("------------------------------------------------")
                    print("system_id : ", system_id)
                    print("Trip Id : ", trip_id)
                    print("Sequence No. : ", sequence_no)
                    print("Packet Status : ", packet_status)
                    print("data : ", data)
                    testResult(self, "passed",
                           "Validate that sequence number is zero value if Trip is not ACTIVE and packet status is LIVE if network is up",
                           "The sequence number is zero value if Trip is not ACTIVE and packet status is LIVE if network is up. pls refer "
                           "cloud logs for detailed info")
            else:
                assert False
        elif message == "No data available":
            print("No data available")
            assert False
        else:
            assert False
    else:
        assert False

def telemetry_data(self, countOnly, name, condition, value, systemId, offset, limit, tc):
    # Call reusable module
    response = get_telemetry_data(self, countOnly, name, condition, value, systemId, offset, limit, tc)

    if response.status_code == 200:

        # Parse API response into JSON
        response_body = response.json()

        status_p = status_f = ""
        message = response_body["message"]
        if message == "Data Fetched Successfully":
            totalRecords = response_body["totalRecords"]
            print("------------------------------------")
            print("Total Records :", totalRecords)
            print("------------------------------------")
            dataList_len = len(response_body["telemetryCurrvalues"])
            print(dataList_len)
            if tc == "valid_countOnly_true":
                if dataList_len == 0 and totalRecords >=1:
                    testResult(self, "passed",
                           "Validate that telemetry curr values/data count is fetched based on the count flag & the condition/criteria",
                           "Only telemetry curr values/data count is fetched based on the set count flag - True & the condition/criteria successfully")
                else:
                    testResult(self,  "failed",
                           "Validate that telemetry curr values/data count is fetched based on the count flag & the condition/criteria",
                           "Failed to fetch telemetry curr values/data count or also fetched telemetry cur values based on the count flag & the condition/criteria successfully")

            elif tc == "valid_countOnly_false":
                if dataList_len >= 1 and totalRecords >=1:
                    for i in range(dataList_len):
                        id = response_body["telemetryCurrvalues"][i]["id"]
                        elementId = response_body["telemetryCurrvalues"][i]["elementId"]
                        areaId = response_body["telemetryCurrvalues"][i]["areaId"]
                        systemId = response_body["telemetryCurrvalues"][i]["systemId"]
                        value = response_body["telemetryCurrvalues"][i]["value"]
                        createdBy = response_body["telemetryCurrvalues"][i]["createdBy"]
                        createdTime = response_body["telemetryCurrvalues"][i]["createdTime"]
                        updatedBy = response_body["telemetryCurrvalues"][i]["updatedBy"]
                        updatedTime = response_body["telemetryCurrvalues"][i]["updatedTime"]

                        print("------------------------------------------------")
                        print("system_id : ", systemId)
                        print("Id : ", id)
                        print("elementId : ", elementId)
                        print("value : ", value)
                        testResult(self, "passed",
                               "Validate that telemetry curr values/data is fetched based on the count flag & the condition/criteria",
                               "The telemetry curr values/data is fetched based on the count flag & the condition/criteria successfully")

                else:
                    print("telemetryCurrvalues - data array is empty")
                    assert False
            else:
                print("invalid test case")
                assert False
        else:
            print("telemetryCurrvalues - data array is empty")
            assert False
    else:
        print("API response Status is not 200")
        assert False


#--------------------------------------------------------
#--------Composite API(Graphql)--------------------------
#--------------------------------------------------------

def getVehicleLocationBySystemId(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getVehicleLocationBySystemId_payload = """
                query GetVehicleLocationBySystemId{
    getVehicleLocationBySystemId(systemId: <systemId>) {
        systemId
        vin
        model
        group
        lastTrackedStr
        lastTracked
        status
        address
        location {
            lat
            lng
        }
    }
}

             """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getVehicleLocationBySystemId_payload.replace('<systemId>', '"' + systemId + '"')

    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})

    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Vehicle Location by SystemId data should be fetched Successfully",
                   "Failed to fetch vehicle Location by SystemId data. Http Status is not 200")

        # Validate response body
        systemId_actual = response_body["data"]["getVehicleLocationBySystemId"]["systemId"]
        vin = response_body["data"]["getVehicleLocationBySystemId"]["vin"]
        model = response_body["data"]["getVehicleLocationBySystemId"]["model"]
        group = response_body["data"]["getVehicleLocationBySystemId"]["group"]
        lastTrackedStr = response_body["data"]["getVehicleLocationBySystemId"]["lastTrackedStr"]
        lastTracked = response_body["data"]["getVehicleLocationBySystemId"]["lastTracked"]
        status = response_body["data"]["getVehicleLocationBySystemId"]["status"]
        address = response_body["data"]["getVehicleLocationBySystemId"]["address"]
        location = response_body["data"]["getVehicleLocationBySystemId"]["location"]

        if systemId_actual == systemId:
            print("-------------------------------")
            print("VIN - ", vin)
            print("Model - ", model)
            print("Group - ", group)
            print("Last Tracked Str - ", lastTrackedStr)
            print("Last Tracked - ", lastTracked)
            print("Status - ", status)
            print("Address - ", address)
            print("Location - ", location)
            print("-------------------------------")
            testResult(self, "passed",
                   "Vehicle Location by SystemId data should be fetched Successfully",
                   "Vehicle Location by SystemId data is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Vehicle Location by SystemId data should be fetched Successfully",
                   "Failed to fetch vehicle location by SystemId data. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Vehicle Location by SystemId data should be fetched Successfully",
               "Failed to fetch vehicle Location by SystemId data. Response code is not 200")
    print("----------------------------------------------------------")


def getVehicleLocations(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getVehicleLocations_payload = """
                    query VehicleLocations {
        vehicleLocations(
            vehicleLocationFilter: {
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                model: <model>
                year: <year>
                variant: null
                search: null
                group: null
                vehicleStatus: null
                alertStatus: null
            }
            offset: 0
            limit: 10
        ) {
            offset
            limit
            totalRecords
            message
            vehicleLocationResponses {
                systemId
                vin
                model
                group
                lastTrackedStr
                lastTracked
                status
                address
                location {
                    lat
                    lng
                }
            }
        }
    }

                 """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getVehicleLocations_payload.replace('<regionCode>', '"' + regionCode + '"')
    payload_query = payload_query.replace('<countryCode>', '"' + countryCode + '"')
    payload_query = payload_query.replace('<engineType>', '"' + engineType + '"')
    payload_query = payload_query.replace('<model>', '"' + model + '"')
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x, json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Vehicle Locations data should be fetched Successfully",
                   "Failed to fetch vehicle Locations data. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["vehicleLocations"]["offset"]
        limit = response_body["data"]["vehicleLocations"]["limit"]
        totalRecords = response_body["data"]["vehicleLocations"]["totalRecords"]
        message = response_body["data"]["vehicleLocations"]["message"]

        if totalRecords > 0:
            testResult(self, "passed",
                   "Vehicle Locations data should be fetched Successfully",
                   "Vehicle Locations data is fetched Successfully")
        else:
            testResult(self,"failed",
                   "Vehicle Locations data should be fetched Successfully",
                   "Failed to fetch vehicle locations data. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Vehicle Locations data should be fetched Successfully",
               "Failed to fetch vehicle Locations data. Response code is not 200")
    print("----------------------------------------------------------")


def getActiveActiveAlertCountsForVehicles(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getActiveActiveAlertCountsForVehicles_payload = """
                    query ActiveAlertCountsForVehicles {
        activeAlertCountsForVehicles(
            vehicleGlobalFilter: {
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                model: <model>
                year: <year>
                variant: null
            }
        ) {
            vehicles
            status
            alerts
        }
    }

                    """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getActiveActiveAlertCountsForVehicles_payload.replace('<regionCode>', '"' + regionCode + '"')
    payload_query = payload_query.replace('<countryCode>', '"' + countryCode + '"')
    payload_query = payload_query.replace('<engineType>', '"' + engineType + '"')
    payload_query = payload_query.replace('<model>', '"' + model + '"')
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Active Alerts for Vehicles data should be fetched Successfully",
                   "Failed to fetch vehicle active alert count data. Http Status is not 200")

        # Validate response body
        records = response_body["data"]["activeAlertCountsForVehicles"]["vehicles"]["records"]
        Emergency = response_body["data"]["activeAlertCountsForVehicles"]["alerts"]["Emergency"]
        D0 = response_body["data"]["activeAlertCountsForVehicles"]["alerts"]["D0"]
        D1 = response_body["data"]["activeAlertCountsForVehicles"]["alerts"]["D1"]
        D2 = response_body["data"]["activeAlertCountsForVehicles"]["alerts"]["D2"]

        if records > 0:
            testResult(self, "passed",
                   "Active Vehicle Alert Count data should be fetched Successfully",
                   "Active Vehicle Alert Count data is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Active Vehicle Alert Count data should be fetched Successfully",
                   "Failed to fetch Active vehicle alert count data. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Active Alerts for Vehicles data should be fetched Successfully",
               "Failed to fetch vehicle active alert count data. Response code is not 200")
    print("----------------------------------------------------------")


def getVehicleCountsByStatus(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getVehicleCountsByStatus_payload = """
                    query VehicleCountsByStatus {
        vehicleCountsByStatus(
            vehicleGlobalFilter: {
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                model: <model>
                year: <year>
                variant: null
            }
        ) {
            vehicles
            status
            alerts
        }
    }

                 """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getVehicleCountsByStatus_payload.replace('<regionCode>', '"' + regionCode + '"')
    payload_query = payload_query.replace('<countryCode>', '"' + countryCode + '"')
    payload_query = payload_query.replace('<engineType>', '"' + engineType + '"')
    payload_query = payload_query.replace('<model>', '"' + model + '"')
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Vehicle Count by Status should be fetched Successfully",
                   "Failed to fetch vehicle status count data. Http Status is not 200")

        # Validate response body
        records = response_body["data"]["vehicleCountsByStatus"]["vehicles"]["records"]
        HALT = response_body["data"]["vehicleCountsByStatus"]["status"]["HALT"]
        NO_GPS = response_body["data"]["vehicleCountsByStatus"]["status"]["NO_GPS"]
        RUNNING = response_body["data"]["vehicleCountsByStatus"]["status"]["RUNNING"]
        INACTIVE = response_body["data"]["vehicleCountsByStatus"]["status"]["INACTIVE"]
        IDLE = response_body["data"]["vehicleCountsByStatus"]["status"]["IDLE"]
        DEAD = response_body["data"]["vehicleCountsByStatus"]["status"]["DEAD"]
        OFFLINE = response_body["data"]["vehicleCountsByStatus"]["status"]["OFFLINE"]

        if records > 0:
            testResult(self,"passed",
                   "Vehicle Count by Status should be fetched Successfully",
                   "Vehicle Count by Status is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Vehicle Count by Status should be fetched Successfully",
                   "Failed to fetch vehicle Status count data. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Vehicle Count by Status should be fetched Successfully",
               "Failed to fetch vehicle status count data. Response code is not 200")
    print("----------------------------------------------------------")


def viewAlertCounts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    viewAlertCounts_payload = """
                    query ViewAlertCounts {
        viewAlertCounts(
            alertDataFilterDTO: {
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                model: <model>
                year: <year>
                variant: null
                startTime: null
                endTime: null
            }
        ) {
            nonDTC
            DTC
            D0
            D1
            D2
            D3
            crashCount
            emergencyCount
        }
    }
    """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = viewAlertCounts_payload.replace('<regionCode>', '"' + regionCode + '"')
    payload_query = payload_query.replace('<countryCode>', '"' + countryCode + '"')
    payload_query = payload_query.replace('<engineType>', '"' + engineType + '"')
    payload_query = payload_query.replace('<model>', '"' + model + '"')
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x, json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Vehicle Alert Count data should be fetched Successfully",
                   "Failed to fetch vehicle alert count data. Http Status is not 200")

        # Validate response body
        nonDTC = response_body["data"]["viewAlertCounts"]["nonDTC"]
        DTC = response_body["data"]["viewAlertCounts"]["DTC"]
        D0 = response_body["data"]["viewAlertCounts"]["D0"]
        D1 = response_body["data"]["viewAlertCounts"]["D1"]
        D2 = response_body["data"]["viewAlertCounts"]["D2"]
        crashCount = response_body["data"]["viewAlertCounts"]["crashCount"]
        emergencyCount = response_body["data"]["viewAlertCounts"]["emergencyCount"]

        if nonDTC > 0 or DTC > 0 or crashCount > 0 or emergencyCount > 0:
            testResult(self, "passed",
                   "Vehicle Alert Count data should be fetched Successfully",
                   "Vehicle Alert Count data is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Vehicle Alert Count data should be fetched Successfully",
                   "Failed to fetch vehicle alert count data. Refer api response for failure details")
    else:
        testResult(self, "failed",
               "Vehicle Alert Count data should be fetched Successfully",
               "Failed to fetch vehicle alert count data. Response code is not 200")

        print("----------------------------------------------------------")


def viewNonDTCAlertDetailsForVehicle(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    viewNonDTCAlertDetailsForVehicle_payload = """
                    query ViewNonDTCAlertDetailsForVehicle {
        viewNonDTCAlertDetailsForVehicle(
            systemId: <systemId>
            alertStatus: "ALL"
            startDate: null
            endDate: null
            offset: 0
            limit: 100
            category: "ALL"
        ) {
            offset
            limit
            totalRecords
            message
            nonDTCList {
                nonDTCType
                date
                ignitionStatus
                severity
                alertStatus
                location {
                    longitude
                    latitude
                }
            }
        }
    }

                 """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = viewNonDTCAlertDetailsForVehicle_payload.replace('<systemId>', '"' + systemId + '"')
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)
        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Non DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view Non DTC Alert Details For Vehicle. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["viewNonDTCAlertDetailsForVehicle"]["offset"]
        limit = response_body["data"]["viewNonDTCAlertDetailsForVehicle"]["limit"]
        totalRecords = response_body["data"]["viewNonDTCAlertDetailsForVehicle"]["totalRecords"]
        message = response_body["data"]["viewNonDTCAlertDetailsForVehicle"]["message"]

        if totalRecords > 0 or message == "Data Fetched Successfully":
            testResult(self, "passed",
                   "Non DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Non DTC Alert Details For Vehicle data is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Non DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view Non DTC Alert Details For Vehicle. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Non DTC Alert Details For Vehicle data should be fetched Successfully",
               "Failed to view Non DTC Alert Details For Vehicle. Response code is not 200")
    print("----------------------------------------------------------")


def viewDTCAlertDetailsForVehicle(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    viewDTCAlertDetailsForVehicle_payload = """
                    query ViewDTCAlertDetailsForVehicle {
        viewDTCAlertDetailsForVehicle(
            systemId: <systemId>
            dtcStatus: "ALL"
            endDate: null
            startDate: null
            offset: 0
            limit: 100
        ) {
            offset
            limit
            totalRecords
            message
            dTCList {
                dtc
                dtcCode
                dtcInfo
                firstOccurrence
                lastOccurrence
                runningTime
                noOfOccurrences
                dtcStatus
                ticketStatus
            }
        }
    }
                 """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = viewDTCAlertDetailsForVehicle_payload.replace('<systemId>', '"' + systemId + '"')
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)
        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view DTC Alert Details For Vehicle. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["viewDTCAlertDetailsForVehicle"]["offset"]
        limit = response_body["data"]["viewDTCAlertDetailsForVehicle"]["limit"]
        totalRecords = response_body["data"]["viewDTCAlertDetailsForVehicle"]["totalRecords"]
        message = response_body["data"]["viewDTCAlertDetailsForVehicle"]["message"]

        if totalRecords > 0 or message == "Data Fetched Successfully":
            testResult(self,"passed",
                   "DTC Alert Details For Vehicle data should be fetched Successfully",
                   "DTC Alert Details For Vehicle data is fetched Successfully")
        else:
            testResult(self,"failed",
                   "DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view DTC Alert Details For Vehicle. Refer api response for failure details")


    else:
        testResult(self,"failed",
               "DTC Alert Details For Vehicle data should be fetched Successfully",
               "Failed to view DTC Alert Details For Vehicle. Response code is not 200")
    print("----------------------------------------------------------")


def viewVehicleDetailsWithAlerts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    viewVehicleDetailsWithAlerts_payload = """query ViewVehicleDetailsWithAlerts {
        viewVehicleDetailsWithAlerts(
            vehicleDetailsWithAlertsFilterDTO: {
                model: <model>
                variant: null
                year: <year>
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                vehicleStatus: null
                alertType: "ALL"
            }
            offset: 0
            limit: 100
        ) {
            offset
            limit
            totalRecords
            message
            vehiclesList {
                systemId
                vin
                model
                group
                lastTracked
                status
                vehicleHealth
                kmsTravelled
                dtcCount
                nonDTCCount
            }
        }
    }
    """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = viewVehicleDetailsWithAlerts_payload.replace('<regionCode>', '"' + regionCode + '"')
    payload_query = payload_query.replace('<countryCode>', '"' + countryCode + '"')
    payload_query = payload_query.replace('<engineType>', '"' + engineType + '"')
    payload_query = payload_query.replace('<model>', '"' + model + '"')
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)
        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "DTC Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view DTC Alert Details For Vehicle. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["viewVehicleDetailsWithAlerts"]["offset"]
        limit = response_body["data"]["viewVehicleDetailsWithAlerts"]["limit"]
        totalRecords = response_body["data"]["viewVehicleDetailsWithAlerts"]["totalRecords"]
        message = response_body["data"]["viewVehicleDetailsWithAlerts"]["message"]

        if totalRecords > 0 or message == "Data Fetched Successfully":
            testResult(self, "passed",
                   "Alert Details For Vehicle data should be fetched Successfully",
                   "Alert Details For Vehicle data is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Alert Details For Vehicle data should be fetched Successfully",
                   "Failed to view Alert Details For Vehicle. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "Alert Details For Vehicle data should be fetched Successfully",
               "Failed to view Alert Details For Vehicle. Response code is not 200")
    print("----------------------------------------------------------")


def viewDtcTimeSeriesCounts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    viewDtcTimeSeriesCounts_payload = """
                    query ViewDtcTimeSeriesCounts {
        viewDtcTimeSeriesCounts(
            dtcStatsDataFilterDTO: {
                regionCode: <regionCode>
                countryCode: <countryCode>
                engineType: <engineType>
                model: <model>
                year: <year>
                variant: null
                duration: null
            }
        )
    }

                 """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = viewDtcTimeSeriesCounts_payload.replace('<regionCode>', regionCode)
    payload_query = payload_query.replace('<countryCode>', countryCode)
    payload_query = payload_query.replace('<engineType>', engineType)
    payload_query = payload_query.replace('<model>', model)
    payload_query = payload_query.replace('<year>', year)
    print(payload_query)

    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Dtc Time Series Counts data should be fetched Successfully",
                   "Failed to view Dtc Time Series Counts . Http Status is not 200")

        # Validate response body
        stats = response_body["data"]["viewDtcTimeSeriesCounts"]["stats"]

        if stats != "":
            testResult(self, "passed",
                   "Dtc Time Series Counts data should be fetched Successfully",
                   "Dtc Time Series Counts data is fetched Successfully")
        else:
            testResult("failed",
                   "Dtc Time Series Counts data should be fetched Successfully",
                   "Failed to view Dtc Time Series Counts. Refer api response for failure details")


    else:
        testResult(self,"failed",
               "Dtc Time Series Counts data should be fetched Successfully",
               "Failed to view Dtc Time Series Counts. Response code is not 200")
    print("----------------------------------------------------------")


def getTripDetails(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getTripDetails_payload = """
            query GetTripDetails {
        getTripDetails(
            systemId: <systemId>
            startDate: null
            endDate: null
            offset: 0
            limit: 100
        ) {
            offset
            limit
            totalRecords
            message
            tripList {
                tripId
                systemId
                tripStatus
                tripStartDate
                tripEndDate
                tripDuration
                distance
                runningTime
                idlingTime
                overspeedCount
                averageSpeed
                topSpeed
                harshBreakers
                harshAcceleration
                navigation
                tripStartLoc {
                    longitude
                    latitude
                    altitude
                }
                tripEndLoc {
                    longitude
                    latitude
                    altitude
                }
            }
        }
    }
     """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getTripDetails_payload.replace('<systemId>', '"' + systemId + '"')
    response = requests.post(url=complete_url, headers=header_x, json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)
        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "Trip Details should be fetched Successfully",
                   "Failed to fetch trip details. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["getTripDetails"]["offset"]
        limit = response_body["data"]["getTripDetails"]["limit"]
        totalRecords = response_body["data"]["getTripDetails"]["totalRecords"]
        message = response_body["data"]["getTripDetails"]["message"]

        tripId = tripStartDate = tripEndDate = ''

        if totalRecords > 0 or message == "Success":
            tripList_len = len(response_body["data"]["getTripDetails"]["tripList"])
            if tripList_len >= 1:
                for i in range(tripList_len):
                    tripId = response_body["data"]["getTripDetails"]["tripList"][i]["tripId"]
                    tripStatus = response_body["data"]["getTripDetails"]["tripList"][i]["tripStatus"]
                    tripStartDate = response_body["data"]["getTripDetails"]["tripList"][i]["tripStartDate"]
                    tripEndDate = response_body["data"]["getTripDetails"]["tripList"][i]["tripEndDate"]
                    if tripStatus == "Completed":
                        break
            else:
                print("No trip is listed for this vehicle")

            testResult(self,"passed",
                   "Trip Details should be fetched Successfully",
                   "Trip Details is fetched Successfully")
        else:
            testResult(self, "failed",
                   "Trip Details should be fetched Successfully",
                   "Failed to fetch trip details. Refer api response for failure details")

    else:
        testResult(self,"failed",
               "Trip Details should be fetched Successfully",
               "Failed to fetch trip details. Response code is not 200")
    print("----------------------------------------------------------")

    return tripId, tripStartDate, tripEndDate


def getTripReplayDetailsWithPagination(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getTripReplayDetailsWithPagination_payload = """
            query GetTripReplayDetailsWithPagination {
        getTripReplayDetailsWithPagination(
            systemId: <systemId>
            tripId: <tripId>
            startDate: <startDate>
            endDate: <endDate>
        ) {
            offset
            limit
            totalRecords
            message
            tripId
        }
    }


            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getTripReplayDetailsWithPagination_payload.replace('<systemId>', '"' + systemId + '"')

    tripId, tripStartDate, tripEndDate = getTripDetails(self, cloudEnv, systemId, tc)

    payload_query = payload_query.replace('<tripId>', '"' + tripId + '"')
    payload_query = payload_query.replace('<startDate>', str(tripStartDate))
    payload_query = payload_query.replace('<endDate>', str(tripEndDate))
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
                response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Trip Details should be fetched Successfully",
                   "Failed to fetch trip details. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["getTripDetails"]["offset"]
        limit = response_body["data"]["getTripDetails"]["limit"]
        totalRecords = response_body["data"]["getTripDetails"]["totalRecords"]
        message = response_body["data"]["getTripDetails"]["message"]

        if totalRecords > 0 or message == "Success":
            testResult(self,"passed",
                   "Trip Details should be fetched Successfully",
                   "Trip Details is fetched Successfully")
        else:
            testResult(self,"failed",
                   "Trip Details should be fetched Successfully",
                   "Failed to fetch trip details. Refer api response for failure details")
    else:
        testResult(self, "failed",
               "Trip Details should be fetched Successfully",
               "Failed to fetch trip details. Response code is not 200")
    print("----------------------------------------------------------")


def getTripReplayDetails(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getTripReplayDetails_payload = """
            query GetTripReplayDetails {
        getTripReplayDetails(
            systemId: <systemId>
            tripId: <tripId>
            startDate: <startDate>
            endDate: <endDate>
        ) {
            tripId
            plotPoints {
                time
                longitude
                latitude
                direction
                altitude
            }
            alerts {
                harshBreaks {
                    time
                    longitude
                    latitude
                    direction
                    altitude
                }
                harshAcceleration {
                    time
                    longitude
                    latitude
                    direction
                    altitude
                }
                overSpeed {
                    time
                    longitude
                    latitude
                    direction
                    altitude
                }
            }
        }
    }


            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getTripReplayDetails_payload.replace('<systemId>', '"' + systemId + '"')

    tripId, tripStartDate, tripEndDate = getTripDetails(self, cloudEnv, systemId, tc)

    payload_query = payload_query.replace('<tripId>', '"' + tripId + '"')
    payload_query = payload_query.replace('<startDate>', str(tripStartDate))
    payload_query = payload_query.replace('<endDate>', str(tripEndDate))
    print(payload_query)

    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Trip Replay Details should be fetched Successfully",
                   "Failed to fetch trip replay details. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["getTripReplayDetails"]["offset"]
        limit = response_body["data"]["getTripReplayDetails"]["limit"]
        totalRecords = response_body["data"]["getTripReplayDetails"]["totalRecords"]
        message = response_body["data"]["getTripReplayDetails"]["message"]

        if totalRecords > 0 or message == "Success":
            testResult(self,"passed",
                   "Trip Replay Details should be fetched Successfully",
                   "Trip Replay Details is fetched Successfully")
        else:
            testResult(self,"failed",
                   "Trip Replay Details should be fetched Successfully",
                   "Failed to fetch trip replay details. Refer api response for failure details")
    else:
        testResult("failed",
               "Trip Replay Details should be fetched Successfully",
               "Failed to fetch trip replay details. Response code is not 200")
    print("----------------------------------------------------------")


def deleteTrip(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    deleteTrip_payload = """
            query DeleteTrip {
                deleteTrip(
                    systemId: <systemId>
                    tripId: <tripId>
                )
            }
            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = deleteTrip_payload.replace('<systemId>', '"' + systemId + '"')

    tripId, tripStartDate, tripEndDate = getTripDetails(self, cloudEnv, systemId, tc)

    payload_query = payload_query.replace('<tripId>', '"' + tripId + '"')
    # payload_query = payload_query.replace('<startDate>', str(tripStartDate))
    # payload_query = payload_query.replace('<endDate>', str(tripEndDate))
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x, json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Trip should be deleted Successfully",
                   "Failed to delete trip details. Http Status is not 200")

        # Validate response body
        message = response_body["data"]["deleteTrip"]

        if message == "Trips deleted successfully.":
            testResult(self,"passed",
                   "Trip should be deleted Successfully",
                   "Trip  is deleted Successfully")
        else:
            testResult(self,"failed",
                   "Trip should be deleted Successfully",
                   "Failed to delete trip details. Refer api response for failure details")
    else:
        testResult(self,"failed",
               "Trip should be deleted Successfully",
               "Failed to delete trip details. Response code is not 200")
    print("----------------------------------------------------------")


def mergeTrips(self, cloudEnv, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    mergeTrips_payload = """
            query MergeTrips {
                mergeTrips(systemId: "IMknCfR6qBhVmWVFyWHfS", tripIds: "IMknCfR6qBhVmWVFyWHfS_1755469304544,IMknCfR6qBhVmWVFyWHfS_1755469304544")
            }

            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)
    response = requests.post(url=complete_url, headers=header_x, json={"query": mergeTrips_payload})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "Trips should be merged Successfully",
                   "Failed to merge trips. Http Status is not 200")

        # Validate response body
        offset = response_body["data"]["getTripDetails"]["offset"]
        limit = response_body["data"]["getTripDetails"]["limit"]
        totalRecords = response_body["data"]["getTripDetails"]["totalRecords"]
        message = response_body["data"]["getTripDetails"]["message"]

        if totalRecords > 0 or message == "Success":
            testResult(self,"passed",
                   "Trips should be merged Successfully",
                   "Trips Merged Successfully")
        else:
            testResult(self,"failed",
                   "Trips should be merged Successfully",
                   "Failed to merge trips. Refer api response for failure details")
    else:
        testResult(self,"failed",
               "Trips should be merged Successfully",
               "Failed to merge trips. Response code is not 200")
    print("----------------------------------------------------------")


def getVehicleOverviewBySystemId(self, cloudEnv, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getVehicleOverviewBySystemId_payload = """
            query MergeTrips {
                getVehicleOverviewBySystemId(systemId: <systemId>) {
                    systemId
                    batteryLevel
                    isLocked
                    connectedStatus
                    signalStrength
                    odo
                    ignition
                    range
                    mileage
                    lastSyncTime
                    vehicleMode
                    charge {
                        soc
                        range
                    }
                    chargingStatus {
                        timeElapsed
                        timeRemaining
                        chargeType
                    }
                    vehicleLocationData {
                        lat
                        lng
                        gps
                        gsm
                        direction
                        lastSyncTime
                    }
                    vehicleStatus
                    vehicleSettings {
                        abs
                        hillHold
                        traction
                        regen
                        cruiseControl
                        jumblePIN
                    }
                    clusterSettings {
                        distance
                        temperature
                        time
                        language
                    }
                    rideModeConfig {
                        mode
                        custom {
                            abs
                            tc
                            pow
                            tm
                            rc
                            rb
                        }
                    }
                    trips {
                        trip
                        ResetTimestamp
                        Distance
                        Duration
                        MaxSpeed
                        AverageSpeed
                        Instant
                        averageEfficiency
                        totalEnergy
                    }
                    geofence {
                        type
                        radius
                        geoCoordinates
                    }
                    ota {
                        currentVersion
                        updatedTimeStamp
                        newVersion {
                            versionDetails
                            versionDescription
                        }
                    }
                    tpms {
                        frontPressure
                        rearPressure
                        frontTemp
                        rearTemp
                        Battery
                    }
                }
            }

            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": getVehicleOverviewBySystemId_payload})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult("failed",
                   "Vehicle Overview By SystemId should be fetched Successfully",
                   "Failed to fetch Vehicle Overview By SystemId. Http Status is not 200")

        # Validate response body
        systemId = response_body["data"]["getVehicleOverviewBySystemId"]["systemId"]
        batteryLevel = response_body["data"]["getVehicleOverviewBySystemId"]["batteryLevel"]
        isLocked = response_body["data"]["getVehicleOverviewBySystemId"]["isLocked"]
        connectedStatus = response_body["data"]["getVehicleOverviewBySystemId"]["connectedStatus"]
        signalStrength = response_body["data"]["getVehicleOverviewBySystemId"]["signalStrength"]
        odo = response_body["data"]["getVehicleOverviewBySystemId"]["odo"]
        ignition = response_body["data"]["getVehicleOverviewBySystemId"]["ignition"]
        vehicleMode = response_body["data"]["getVehicleOverviewBySystemId"]["vehicleMode"]

        if systemId != "":
            testResult(self,"passed",
                   "Vehicle Overview By SystemId should be fetched Successfully",
                   "Vehicle Overview By SystemId is fetched Successfully")
        else:
            testResult(self,"failed",
                   "Vehicle Overview By SystemId should be fetched Successfully",
                   "Failed to fetch Vehicle Overview By SystemId. Refer api response for failure details")


    else:
        testResult(self,"failed",
               "Vehicle Overview By SystemId should be fetched Successfully",
               "Failed to fetch Vehicle Overview By SystemId. Response code is not 200")
    print("----------------------------------------------------------")


def getGeoFenceBySystemId(self, cloudEnv, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getGeoFenceBySystemId_payload = """       
            query GetGeoFenceBySystemId {
                getGeoFenceBySystemId(systemId: <systemId>) {
                    geoId
                    geofenceType
                    radius
                    name
                    active
                    geoCoordinates
                }
            }

            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    response = requests.post(url=complete_url, headers=header_x
                             , json={"query": getGeoFenceBySystemId_payload})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self, "failed",
                   "GeoFence By SystemId should be fetched Successfully",
                   "Failed to fetch GeoFence By SystemId. Http Status is not 200")

        # Validate response body
        geoId = response_body["data"]["getGeoFenceBySystemId"]["geoId"]
        geofenceType = response_body["data"]["getGeoFenceBySystemId"]["geofenceType"]
        radius = response_body["data"]["getGeoFenceBySystemId"]["radius"]
        name = response_body["data"]["getGeoFenceBySystemId"]["name"]
        active = response_body["data"]["getGeoFenceBySystemId"]["active"]
        geoCoordinates = response_body["data"]["getGeoFenceBySystemId"]["geoCoordinates"]

        if geoId != "":
            testResult(self, "passed",
                   "GeoFence By SystemId should be fetched Successfully",
                   "GeoFence By SystemId is fetched Successfully")
        else:
            testResult(self,"failed",
                   "GeoFence By SystemId should be fetched Successfully",
                   "Failed to fetch GeoFence By SystemId. Refer api response for failure details")


    else:
        testResult(self, "failed",
               "GeoFence By SystemId should be fetched Successfully",
               "Failed to fetch GeoFence By SystemId. Response code is not 200")
    print("----------------------------------------------------------")


def getGeoFencesBySystemId(self, cloudEnv, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Composite_API_with_graphql")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    getGeoFencesBySystemId_payload = """       
                query GetGeoFencesBySystemId {
        getGeoFencesBySystemId(
            systemId: <systemId>
            geoId: null
            name: null
        ) {
            geoId
            geofenceType
            radius
            name
            active
            geoCoordinates
        }
    }

            """

    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    payload_query = getGeoFencesBySystemId_payload.replace('<systemId>', '"' + systemId + '"')
    print(payload_query)
    response = requests.post(url=complete_url, headers=header_x,
                             json={"query": payload_query})
    print("response status code: ", response.status_code)
    if response.status_code == 200:
        print("response : ", response.content)

        # Step 1: Decode the binary data to a string
        decoded_data = response.content.decode('utf-8')

        # Step 2: Convert the string to a JSON object
        response_body = json.loads(decoded_data)

        if '"httpStatus":500' in str(response_body) or '"httpStatus":502' in str(
                response_body) or '"httpStatus":400' in str(response_body) or 'errorCode' in str(
            response_body) or "BAD_REQUEST" in str(response_body):
            testResult(self,"failed",
                   "GeoFences By SystemId should be fetched Successfully",
                   "Failed to fetch GeoFences By SystemId. Http Status is not 200")

        # Validate response body
        data_len = len(response_body["data"]["getGeoFencesBySystemId"])
        if data_len >= 1:
            for i in range(data_len):
                geoId = response_body["data"]["getGeoFencesBySystemId"][i]["geoId"]
                geofenceType = response_body["data"]["getGeoFencesBySystemId"][i]["geofenceType"]
                radius = response_body["data"]["getGeoFencesBySystemId"][i]["radius"]
                name = response_body["data"]["getGeoFencesBySystemId"][i]["name"]
                active = response_body["data"]["getGeoFencesBySystemId"][i]["active"]
                geoCoordinates = response_body["data"]["getGeoFencesBySystemId"][i]["geoCoordinates"]
        elif data_len == 0:
            print("No geofence is assigned/mapped to this vehicle, hence marking this test case as pass")
            geoId = "1"
        else:
            geoId = response_body["data"]["getGeoFencesBySystemId"]["geoId"]
            geofenceType = response_body["data"]["getGeoFencesBySystemId"]["geofenceType"]
            radius = response_body["data"]["getGeoFencesBySystemId"]["radius"]
            name = response_body["data"]["getGeoFencesBySystemId"]["name"]
            active = response_body["data"]["getGeoFencesBySystemId"]["active"]
            geoCoordinates = response_body["data"]["getGeoFencesBySystemId"]["geoCoordinates"]

        if geoId != "":
            testResult(self,"passed",
                   "GeoFences By SystemId should be fetched Successfully",
                   "GeoFences By SystemId is fetched Successfully")
        else:
            testResult(self,"failed",
                   "GeoFences By SystemId should be fetched Successfully",
                   "Failed to fetch GeoFences By SystemId. Refer api response for failure details")
    else:
        testResult(self,"failed",
               "GeoFences By SystemId should be fetched Successfully",
               "Failed to fetch GeoFences By SystemId. Response code is not 200")
    print("----------------------------------------------------------")