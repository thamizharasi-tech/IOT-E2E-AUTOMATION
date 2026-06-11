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

# Vehicle_update-vehicle-meta-data
def vehicle_update_vehicle_meta_data(self, vin, model, engineType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_update-vehicle-meta-data")
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

    year = "2023"
    make = "toyota"
    manufacturing_date = "04-03-2023"
    manufacturing_location = "detroit"
    manufacturing_plant = "detroit"
    manufacturing_country = "USA"
    vehicle_registration = "REG123"
    vehicle_registration_date = "04-07-2023"
    fleet_id = "fleet_123"
    driver_id = "driver_123"

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["year"] = year
    json_object["make"] = make
    json_object["engine_type"] = engineType
    json_object["manufacturing_date"] = manufacturing_date
    json_object["manufacturing_location"] = manufacturing_location
    json_object["manufacturing_plant"] = manufacturing_plant
    json_object["manufacturing_country"] = manufacturing_country
    json_object["vehicle_registration"] = vehicle_registration
    json_object["vehicle_registration_date"] = vehicle_registration_date
    json_object["fleet_id"] = fleet_id
    json_object["driver_id"] = driver_id
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_update-vehicle-meta-data",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_update-vehicle-meta-data', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_update-vehicle-meta-data", response.text)

    return response


def vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                    manufacturing_location, manufacturing_plant, manufacturing_country,
                                    vehicle_registration, vehicle_registration_date, fleet_id, driver_id, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_update-vehicle-meta-data")
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
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["year"] = year
    json_object["make"] = make
    json_object["engine_type"] = engine_type
    json_object["manufacturing_date"] = manufacturing_date
    json_object["manufacturing_location"] = manufacturing_location
    json_object["manufacturing_plant"] = manufacturing_plant
    json_object["manufacturing_country"] = manufacturing_country
    json_object["vehicle_registration"] = vehicle_registration
    json_object["vehicle_registration_date"] = vehicle_registration_date
    json_object["fleet_id"] = fleet_id
    json_object["driver_id"] = driver_id
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_update-vehicle-meta-data",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_update-vehicle-meta-data', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_update-vehicle-meta-data", response.text)

    return response


# Vehicle_get-vehicle-meta-data
def vehicle_get_vehicle_metadata(self, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_get-vehicle-meta-data")
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
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get-vehicle-meta-data",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_get-vehicle-meta-data', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_get-device-meta-data", response.text)

    return response


# Vehicle_get-device-meta-data
def vehicle_get_device_metadata(self, deviceId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_get-device-meta-data")
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
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get-device-meta-data",
                                                "Vehicle-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_get-device-meta-data', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_get-device-meta-data", response.text)

    return response


# Vehicle_GetVinsbyModelNew
def vehicle_get_vinsbyModelNew(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinsbyModelNew")
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
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsbyModelNew",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle-GetVinsbyModelNew', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinsbyModelNew", response.text)

    return response


# Vehicle-GetVinCountByAllModels
def vehicle_get_vinCount_byAllModels(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinCountByAllModels")
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
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinCountByAllModels",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle-GetVinCountByAllModels', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinCountByAllModels", response.text)

    return response


# Vehicle-GetVinsByModel
def vehicle_get_vins_byModel(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinsByModel")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{modelName}', model)
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

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle-GetVinsByModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinsByModel", response.text)

    return response


# Vehicle-GetVinsByModel
def vehicle_get_vins_byModel_v3(self, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3")
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
    header_x = header_update(header_x, tc)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel_v3",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle-GetVinsByModel_v3', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3", response.text)

    return response


# Vehicle-GetVinsByModel
def vehicle_get_vinsByModel_v3(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{vin}', vin).replace("\n", "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    for i in range(5):
        response = requests.get(complete_url, headers=header_x)
        print("API response : ", response.text)

        try:
            # Parse API response into JSON
            response_body = response.json()

            if response_body["Message"] == "User is not authorized to access this resource":
                print("Token generation : ")
                # Generate token
                token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
                time.sleep(5)
                update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel_v3",
                                                    "Vehicle-AuthToken")
                time.sleep(120)
                response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
                print("API response : ", response.text)
        except:
            print("\n")

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_resp_into_file('Vehicle-GetVinsByModel_v3', response.text)
        save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3", response.text)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseData"]["message"] == "Success")
            print("\n")
            break
        elif response_body["responseCode"] == str(13201):
            print("response Code is not 1200. Rather found : " + str(response_body))
            time.sleep(30)
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

    return response_body

def vehicle_get_vinsByModel_v3_regional_state(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3_regional")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{vin}', vin).replace("\n", "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    for i in range(5):
        response = requests.get(complete_url, headers=header_x)
        print("API response : ", response.text)

        try:
            # Parse API response into JSON
            response_body = response.json()

            if response_body["Message"] == "User is not authorized to access this resource":
                print("Token generation : ")
                # Generate token
                token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
                time.sleep(5)
                update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel_v3",
                                                    "Vehicle-AuthToken")
                time.sleep(120)
                response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
                print("API response : ", response.text)
        except:
            print("\n")

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_resp_into_file('Vehicle-GetVinsByModel_v3', response.text)
        save_api_resp_in_excel(self, "API_Data", "Vehicle-GetVinsByModel_v3", response.text)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseData"]["message"] == "Success")
            print("\n")
            break
        elif response_body["responseCode"] == str(13201):
            print("response Code is not 1200. Rather found : " + str(response_body))
            time.sleep(30)
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

    return response_body


# ---------------------------------
# RE API Modules
# ---------------------------------

# Vehicle_update-vehicle-meta-data
def vehicle_update_metadata(self, vin, engineType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_update_metadata")
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

    model = "tvsice"
    year = "2023"
    make = "RoyalEnfield"
    brand = "RoyalEnfield"
    trim = "RE"
    chassisNumber = "12345"
    manufacturing_date = "04-03-2023"
    manufacturing_location = "Chennai"
    manufacturing_plant = "Chennai"
    manufacturing_country = "India"
    vehicle_registration = "VINREG123"
    vehicle_registration_date = "04-07-2023"
    fleetId = "REfleet123"
    driverId = "REdriver123"
    vehicleFuelType1 = 6
    vehicleFuelType2 = 10

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["year"] = year
    json_object["make"] = make
    json_object["brand"] = brand
    json_object["trim"] = trim
    json_object["chassisNumber"] = chassisNumber
    json_object["engineType"] = engineType
    json_object["manufacturingDate"] = manufacturing_date
    json_object["manufacturingLocation"] = manufacturing_location
    json_object["manufacturingPlant"] = manufacturing_plant
    json_object["manufacturingCountry"] = manufacturing_country
    json_object["vehicleRegistration"] = vehicle_registration
    json_object["vehicleRegistrationDate"] = vehicle_registration_date
    json_object["fleetId"] = fleetId
    json_object["driverId"] = driverId
    json_object["vehicleFuelType"][0] = vehicleFuelType1
    json_object["vehicleFuelType"][1] = vehicleFuelType2
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(60)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_update_metadata",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_update_metadata', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_update_metadata", response.text)

    return response

# Vehicle-GetVehicleMetadata
def vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make, systemId, style, operationalState, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Get_Vehicle_Metadata")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)
    if "vehicle_meta_by_systemId" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize) + "&systemId={systemId}".replace('{systemId}', systemId)
    elif "vehicle_meta_by_make" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize) + "&make={make}".replace('{make}', make)
    elif "vehicle_meta_by_model" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&model={model}".replace('{model}', model)
    elif "vehicle_meta_by_year" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&year={year}".replace('{year}', year)
    elif "vehicle_meta_by_systemId_lifeCycleState" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&systemId={systemId}&lifeCycleState={lifeCycleState}".replace('{systemId}', systemId).replace('{lifeCycleState}', lifeCycleState)
    elif "vehicle_meta_by_systemId_lifeCycleState_model" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&systemId={systemId}&lifeCycleState={lifeCycleState}&model={model}".replace('{systemId}', systemId).replace('{lifeCycleState}', lifeCycleState).replace('{model}', model)
    elif "vehicle_meta_by_regionCode" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&regionCode={regionCode}".replace('{regionCode}', regionCode)
    elif "vehicle_meta_by_systemId_lifeCycleState_model_make" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&systemId={systemId}&lifeCycleState={lifeCycleState}&model={model}&make={make}".replace('{systemId}', systemId).replace('{lifeCycleState}', lifeCycleState).replace('{model}', model).replace('{make}', make)
    elif "vehicle_meta_by_systemId_lifeCycleState_model_make_style" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',pageSize) + "&systemId={systemId}&lifeCycleState={lifeCycleState}&model={model}&make={make}&style={style}".replace('{systemId}', systemId).replace('{lifeCycleState}', lifeCycleState).replace('{model}', model).replace('{make}', make).replace('{style}', style)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Get_Vehicle_Metadata",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get_Vehicle_Metadata', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get_Vehicle_Metadata", response.text)

    return response

def vehicle_get_vehicle_connection_state_global(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_get_vehicleConnectionState_global")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get_vehicleConnectionState_global",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_get_vehicleConnectionState_global', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_get_vehicleConnectionState_global", response.text)

    return response

def vehicle_get_vehicle_connection_state_regional(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_get_vehicleConnectionState_regional")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get_vehicleConnectionState_regional",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_get_vehicleConnectionState_regional', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_get_vehicleConnectionState_regional", response.text)

    return response

def vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, tc):
    # Read api test data from excel sheet
    if tc == "valid" or tc == "regional":
        dict = read_api_data_from_excel(self, "API_Data", "Get_Vehicle_Metadata")
    elif tc == "global":
        dict = read_api_data_from_excel(self, "API_Data", "Get_Vehicle_Metadata_global")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize) + "&systemId={systemId}".replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)

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
            token_gen_reus_mod(self, "API_Data", "Vehicle-AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Get_Vehicle_Metadata",
                                                "Vehicle-AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Get_Vehicle_Metadata', response.text)
    save_api_resp_in_excel(self, "API_Data", "Get_Vehicle_Metadata", response.text)

    return response

def fetch_vehicle_model_by_systemId(self, systemId):

    pageNo = "1"
    pageSize = "10"
    # Call api reusable module
    response = vehicle_get_vehicle_metadata_new(self, pageNo, pageSize, systemId, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    response_body = response.json()

    model = response_body["responseData"]["vehicleDetails"][0]["model"]

    return model

def validate_vehicle_metadata_by_systemId(self, OnboardingType, chipsetType, deviceState):
    status = ''
    print("=============================================================")
    try:

        if deviceState == "global":

            print("Read VIN & System Id from device for validations")

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN : =>  ", vin)

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")

            response = vehicle_get_vinsByModel_v3(self, vin)
            if response["responseData"]["data"]["vin"] == vin:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")
            print("Validate System Id @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be mapped to System Id successfully",
                           "VIN is mapped to System Id successfully")
            else:
                status = 'FAIL'
                testResult(self, "verificationFailed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

            print("---------------------------------------------------------")
            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["lifecycleState"] == "ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "GLOBAL_ACTIVE" or response["responseData"]["data"]["lifecycleState"] == "REHOMED":
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

            if status == 'FAIL':
                testResult(self, "failed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

        if deviceState == "regional":

            print("Read VIN & System Id from device for validations")

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN : =>  ", vin)

            print("---------------------------------------------------------")
            print("Validate VIN @ Cloud post device on-boarding/provisioning : ")

            response = vehicle_get_vinsByModel_v3_regional_state(self, vin)
            if response["responseData"]["data"]["vin"] == vin:
                testResult(self, "passed", "VIN should be added/onboarded successfully",
                           "VIN is added/onboarded successfully")
            else:
                testResult(self, "verificationFailed", "VIN should be added/onboarded successfully",
                           "VIN is not added/onboarded successfully")

            print("---------------------------------------------------------")
            print("Validate System Id @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["systemId"] == systemId:
                testResult(self, "passed", "VIN should be mapped to System Id successfully",
                           "VIN is mapped to System Id successfully")
            else:
                status = 'FAIL'
                testResult(self, "verificationFailed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")

            print("---------------------------------------------------------")
            print("Validate Life Cycle State @ Cloud post device on-boarding/provisioning : ")

            if response["responseData"]["data"]["lifecycleState"] == "ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "REGIONAL_ACTIVE" or response["responseData"]["data"][
                "lifecycleState"] == "PRE_REGIONAL_ACTIVE":
                testResult(self, "passed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is set to ACTIVE")
            else:
                testResult(self, "failed", "Life Cycle State should be set to ACTIVE",
                           "Life Cycle State is not set to ACTIVE")

            if status == 'FAIL':
                testResult(self, "failed", "VIN should be mapped to System Id successfully",
                           "VIN is not mapped to System Id.")
    except:
        testResult(self, "failed", "Cloud Validation ",
                   "cloud validation failed, Refer logs for more details")

    print("=============================================================")