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

# Trip_DriverScoreCard_impactScore
def Trip_DriverScoreCard_impactScore(self, parameter, operation, value):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore")
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
    json_object["expression"][0]["parameter"] = parameter
    json_object["expression"][0]["operation"] = operation
    json_object["expression"][0]["value"] = value
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
            token_gen_reus_mod(self, "API_Data", "DriverScoreCard_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_impactScore",
                                                "DriverScoreCard")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Trip_DriverScoreCard_impactScore', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore", response.text)

    return response


# Trip_DriverScoreCard_impactScore
def Trip_DriverScoreCard_impactScore_HAHBHC(self, HA_parameter, HA_operation, HA_value, HB_parameter, HB_operation,
                                            HB_value, HC_parameter, HC_operation, HC_value):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore_HAHBHC")
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
    json_object["expression"][0]["parameter"] = HA_parameter
    json_object["expression"][0]["operation"] = HA_operation
    json_object["expression"][0]["value"] = HA_value
    json_object["expression"][1]["parameter"] = HB_parameter
    json_object["expression"][1]["operation"] = HB_operation
    json_object["expression"][1]["value"] = HB_value
    json_object["expression"][2]["parameter"] = HC_parameter
    json_object["expression"][2]["operation"] = HC_operation
    json_object["expression"][2]["value"] = HC_value
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
            token_gen_reus_mod(self, "API_Data", "DriverScoreCard_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_impactScore_HAHBHC",
                                                "DriverScoreCard")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Trip_DriverScoreCard_impactScore_HAHBHC', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore_HAHBHC", response.text)

    return response


# Trip_DriverScoreCard_impactScoreBySystemId
def Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', tripId).replace('\n',
                                                                                                                '')
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
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId",
                                                "DriverScoreCard_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('Trip_DriverScoreCard_impactScoreBySystemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId", response.text)

    return response


# Trip_DriverScoreCard_driverScore
def Trip_DriverScoreCard_impactScoreBySystemId(self, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_driverScore")
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
    save_api_resp_into_file('Trip_DriverScoreCard_driverScore', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_driverScore", response.text)

    return response


def calculate_impactScore(self, tripScoreCrad_HA, HA_operation, HA_value,
                          tripScoreCrad_HB, HB_operation, HB_value, tripScoreCrad_HC,
                          HC_operation, HC_value):
    score = ''
    if HA_operation == HB_operation == HC_operation == 'multiplication':
        score_HA = float(HA_value) * float(tripScoreCrad_HA)
        score_HB = float(HB_value) * float(tripScoreCrad_HB)
        score_HC = float(HC_value) * float(tripScoreCrad_HC)

    score = score_HA + score_HB + score_HC
    return score


# -------------------------------------------
# Reusable modules for Negative scenarios
# -------------------------------------------

def Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Update Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_parameter":
        del json_object["expression"][0]["parameter"]
    else:
        json_object["expression"][0]["parameter"] = parameter
    if tc == "no_operation":
        del json_object["expression"][0]["operation"]
    else:
        json_object["expression"][0]["operation"] = operation
    if tc == "no_value":
        del json_object["expression"][0]["value"]
    else:
        json_object["expression"][0]["value"] = value

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
            token_gen_reus_mod(self, "API_Data", "DriverScoreCard_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_impactScore",
                                                "DriverScoreCard")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Trip_DriverScoreCard_impactScore', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_impactScore", response.text)

    return response


def Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', tripId).replace('\n',
                                                                                                                '')
    print("Complete URL : ", complete_url)

    # Update Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

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
            token_gen_reus_mod(self, "API_Data", "DriverScoreCard_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId",
                                                "DriverScoreCard_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Trip_DriverScoreCard_impactScoreBySystemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_impactScoreBySystemId", response.text)

    return response


def Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Trip_DriverScoreCard_driverScore")
    base_url = str(dict["Base Url"])
    headers = str(dict["Headers"]).replace('\n', '')
    endpoint = str(dict["Endpoint"])

    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Update Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

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
    save_api_resp_into_file('Trip_DriverScoreCard_driverScore', response.text)
    save_api_resp_in_excel(self, "API_Data", "Trip_DriverScoreCard_driverScore", response.text)
    # Validate response status code
    assert (
            response.status_code == 403), "Status " \
                                          "code is " \
                                          "not 403. " \
                                          "Rather " \
                                          "found " \
                                          ": " + str(
        response.status_code)
    return response_body
