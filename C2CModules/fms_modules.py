import ast
import json
import time
import os
import requests
from datetime import datetime, timezone, date, timedelta

from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *
from C2CModules.resuse_modules import verify_message_in_log, save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.primary_IVI_device_modules import pull_files_from_primary_IVI
from C2CModules.api_modules import header_update


# ---------------------------------
# API Modules
# ---------------------------------

# AssetManagement_trip-info
def assetManagement_trip_info_by_date(self, startDate, endDate):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = str(base_url + endpoint).replace('{startDate}', startDate)
    complete_url = str(url).replace('{endDate}', endDate)
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
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-info",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip-info', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip-info", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert (response_body["responseData"]["message"] == "Success")
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body


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
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x, data=payload)
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
            time.sleep(120)
            # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
            # time.sleep(60)
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
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x, data=payload)
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
            time.sleep(120)
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
    response = requests.get(complete_url, headers=header_x, data=payload)
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
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            # time.sleep(60)
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


# AssetManagement_latest-trip-meta
def assetManagement_latest_trip_meta(self, vin, systemId, status):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest-trip-meta")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["vin"] = vin
    json_object["systemId"] = systemId
    json_object["status"] = status
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-meta",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            # time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest-trip-meta', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest-trip-meta", response.text)

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


# AssetManagement_latest-trip-details
def assetManagement_latest_trip_details(self, vin, systemId, status):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest-trip-details")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["vin"] = vin
    json_object["systemId"] = systemId
    json_object["status"] = status
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-details",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(120)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            # time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest-trip-details', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest-trip-details", response.text)

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


# ---------------------------------
# NEW API Modules
# ---------------------------------

# AssetManagement_trip-info
def assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = str(base_url + endpoint).replace('{startDate}', startDate)
    complete_url = str(url).replace('{endDate}', endDate).replace('{pageNo}', pageNo).replace('pageNo=0',
                                                                                              'pageNo=' + str(
                                                                                                  pageNo)).replace(
        '{pageSize}', pageSize).replace('pageSize=10', 'pageSize=' + str(pageSize)).replace('pageSize=10',
                                                                                            'pageSize=' + str(pageSize))
    print("Complete URL : ", complete_url)

    # Header :
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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-info",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip-info', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip-info", response.text)

    return response


# AssetManagement_trip-info-by-tripId
def assetManagement_trip_info_by_tripId_new(self, trip_id, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-info-by-tripId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{tripIdValue}', trip_id).replace('{pageNo}', pageNo).replace(
        'pageNo=0', 'pageNo=' + str(pageNo)).replace('{pageSize}', pageSize).replace('pageSize=10',
                                                                                     'pageSize=' + str(pageSize))

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

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

    return response


# AssetManagement_trip-waypoints-by-tripid
def assetManagement_trip_waypoints_by_tripid_new(self, trip_id, tc):
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
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=payload)
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

    return response


# AssetManagement_trip-waypoints-by-systemId
def assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip-waypoints-by-systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = str(base_url + endpoint).replace('{startDate}', startDate)
    completeurl = str(url).replace('{endDate}', endDate)
    print(completeurl)

    if "{pageNo}" in completeurl:
        complete_url = str(completeurl).replace('{pageNo}', pageNo).replace(
            '{pageSize}', pageSize).replace('{systemId}', systemId)
    else:
        pageNo1 = 'pageNo=' + str(pageNo)
        pageSize1 = 'pageSize=' + str(pageSize)
        print(pageNo1, pageSize1)
        complete_url = str(completeurl).replace('pageNo=0', pageNo1).replace('pageSize=10', pageSize1).replace(
            '{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=payload)
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

    return response


# AssetManagement_latest-trip-meta
def assetManagement_latest_trip_meta_new(self, vin, systemId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest-trip-meta")
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
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vin"] = vin
    json_object["systemId"] = systemId
    json_object["status"] = status
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
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-meta",
                                                "AssetManagement_trip_AuthToken")
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest-trip-meta', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest-trip-meta", response.text)

    return response


# AssetManagement_latest-trip-details
def assetManagement_latest_trip_details_new(self, vin, systemId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest-trip-details")
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
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vin"] = vin
    json_object["systemId"] = systemId
    json_object["status"] = status
    # if "without_systemId" == tc:
    # del json_object["systemId"]
    # if "without_vin" == tc:
    # del json_object["vin"]
    if "without_vin_sys" == tc:
        del json_object["vin"]
        del json_object["systemId"]
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
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-details",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest-trip-details', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest-trip-details", response.text)

    return response


# ---------------------------------
# Modules
# ---------------------------------
def get_tridId_from_log(self):
    print("Read the trip id from c2c log file")
    ls = verify_message_in_log(self, tripId_code, tripId_code)

    if tripId_code in str(ls[0]):
        print(str(ls[0]))
        trip_id = str(ls[0]).split('trip_id: ')
        trip_id = str(trip_id[1]).replace(' ', '')
        print(f"Trip Id should be generated in 'systemId_timestamp' format")
        testResult(self, "verificationPassed", "Telemetry message should be published to cloud via Hub ",
                   "Trip Id is generated in 'systemId_timestamp' format")
        print("Trip Id : ", trip_id)
    if str(ls[0]) == "Error":
        ls = verify_message_in_log(self, 'Trip_id:', 'Trip_id:')
        trip_id = str(ls[0]).split('Trip_id:')
        print(ls)
        try:
            trip_id = str(trip_id[1]).replace(' ', '')
        except:
            trip_id = ""

        if str(ls[0]) == "Error" or trip_id == "":
            print(
                "Trip Id is not generated or not found in device logs. pls refer device files & logs for detailed info")
            trip_id = ""

    return trip_id


# ------------------------------------------------------------
# calculate fuel consumed based on trip start & end fuel level
# ------------------------------------------------------------
def calculate_fuel_consumed(self, trip_start_fuel_level, trip_end_fuel_level):
    # Fuel Usage = Fuel end - Fuel start
    try:
        fuel_consumed1 = float(trip_start_fuel_level - trip_end_fuel_level)
        fuel_consumed = float(fuel_consumed1 / 1000)
    except:
        fuel_consumed1 = float(trip_start_fuelLevel_value_ev - trip_end_fuelLevel_value_ev)  # coverting into litters
        fuel_consumed = float(fuel_consumed1 / 1000)
    return fuel_consumed


# ------------------------------------------------------------
# calculate CO2 emission
# ------------------------------------------------------------
def calculate_CO2_emission(self, fuel_usage, fuel_constant):
    # CO2(kg) = Fuel Usage * Fuel Constant
    try:
        CO2_emission = float(fuel_usage * fuel_constant)
    except:
        CO2_emission = float(trip_summary_fuelConsumed_value_ev * trip_Fuel_Constant_ev)

    return CO2_emission


# ------------------------------------------------------------
# calculate trip distance based on trip start & end odo meter value
# ------------------------------------------------------------
def calculate_trip_distance(self, cloudEnv, trip_start_odo, trip_end_odo):
    # Trip distance = ODO End – ODO Start
    if cloudEnv not in ["GCP-QA5", "PRE-PROD","GCP-QA8"]:
        try:
            trip_distance = float((trip_end_odo - trip_start_odo) / 1000)
        except:
            trip_distance = float(trip_end_odometer_value - trip_start_odometer_value) / 1000  # coverting into Km's
    else:
        trip_distance = float(trip_end_odo - trip_start_odo)

    return trip_distance


# ------------------------------------------------------------
# calculate trip fuel efficiency
# ------------------------------------------------------------
def calculate_trip_fuel_efficiency(self, trip_distance, trip_fuel_usage):
    # Fuel Efficiency = Trip Distance/ Fuel Usage
    try:
        fuel_efficiency = float(trip_distance / trip_fuel_usage)

    except ZeroDivisionError:
        fuel_efficiency = 0.0

    except:
        fuel_efficiency = 0.0

    return fuel_efficiency


# ------------------------------------------------------------
# calculate trip duration based on trip start & end time stamp
# ------------------------------------------------------------
def calculate_trip_duration(self, trip_start_time, trip_end_time):
    # Trip duration = (Trip End  time – Trip Start time)/3600000 [ to covert ms to hrs]
    try:
        trip_duration = float((trip_end_time - trip_start_time) / 3600000)

    except ZeroDivisionError:
        trip_duration = 0.0
    except:
        trip_duration = 0.0

    return trip_duration


# ------------------------------------------------------------
# calculate average speed
# ------------------------------------------------------------
def calculate_average_speed(self, trip_distance, trip_duration):
    # Avg Speed = Trip distance/ Trip Duration
    try:
        avg_speed = float(trip_distance / trip_duration)

    except ZeroDivisionError:
        avg_speed = 0.0

    except:
        avg_speed = float(trip_summary_tripDistance_value_ev / trip_summary_tripDuration_value_ev)  # km/hr

    return avg_speed


# ------------------------------------------------------------
# calculate battery consumed
# ------------------------------------------------------------
def calculate_battery_consumed(self, trip_start_battery_level, trip_end_battery_level):
    # batteryConsumed = (battery_level_end - battery_level_start) / 1000(inkwh)
    try:
        battery_consumed = float((trip_start_battery_level - trip_end_battery_level) / 1000)  # kwh
        if battery_consumed < 0:
            battery_consumed = battery_consumed * (-1)

    except ZeroDivisionError:
        battery_consumed = 0.0

    except:
        battery_consumed = float(trip_summary_tripDistance_value_ev / trip_summary_tripDuration_value_ev) / 1000

    return battery_consumed


# ------------------------------------------------------------
# calculate battery consumed based on battery SOC level
# ------------------------------------------------------------
def calculate_batterySOClevel_consumed(self, trip_start_battery_level, trip_end_battery_level):
    # batteryConsumed = (battery_level_end - battery_level_start) / 1000(inkwh)
    try:

        battery_consumed = float((trip_start_battery_level - trip_end_battery_level))  # %
        if battery_consumed < 0:
            battery_consumed = battery_consumed * (-1)

    except ZeroDivisionError:
        battery_consumed = 0.0

    except:
        battery_consumed = float(trip_summary_tripDistance_value_ev / trip_summary_tripDuration_value_ev) / 1000

    return battery_consumed


# ------------------------------------------------------------
# calculate battery efficiency
# ------------------------------------------------------------
def calculate_trip_battery_efficiency(self, trip_distance, battery_consumed):
    # trip_battery_efficiency = Trip distance/batteryConsumed
    try:
        battery_efficiency = float(trip_distance / battery_consumed)

    except ZeroDivisionError:
        battery_efficiency = 0.0
    except:
        battery_efficiency = float(trip_summary_tripDistance_value_ev) / float(trip_summary_batteryConsumed_value_ev)

    return battery_efficiency


# ------------------------------------------------------------
# calculate battery efficiency based on battery SOC level
# ------------------------------------------------------------
def calculate_trip_batterySOClevel_efficiency(self, trip_distance, battery_consumed):
    # trip_battery_efficiency = Trip distance/batteryConsumed
    batterySOClevelConstant = 41.86
    try:
        battery_efficiency = float(trip_distance / ((batterySOClevelConstant * battery_consumed) / 100))

    except ZeroDivisionError:
        battery_efficiency = 0.0
    except:
        battery_efficiency = float(trip_summary_tripDistance_value_ev) / float(
            batterySOClevelConstant * trip_summary_batteryConsumed_value_ev) / 100

    return battery_efficiency


# ------------------------------------------------------------
# Read Trip Id from trip file
# ------------------------------------------------------------

def read_tripId_from_Trip_waypoints(self, onboarding_Type, chipset_type, option):
    pull_files_from_primary_IVI(self, onboarding_Type, chipset_type, option)
    file = os.listdir('C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\Trip_waypoints')[0]
    file = file.split('_')
    filename = file[0] + "_" + file[1]
    print(filename)
    return filename


# ------------------------------------------------------------
# RE API Modules
# ------------------------------------------------------------

# AssetManagement_latest-trip-meta
def latest_trip_meta(self, systemId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest_trip_meta")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["status"] = status
    if "without_systemId" in tc:
        del json_object["systemId"]
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest_trip_meta",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(120)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            # time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest_trip_meta', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest_trip_meta", response.text)

    return response


# AssetManagement_latest-trip-details
def latest_trip_details(self, systemId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_latest_trip_details")
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
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["status"] = status
    # if "without_systemId" == tc:
    # del json_object["systemId"]
    # if "without_vin" == tc:
    # del json_object["vin"]
    if "without_vin_sys" == tc:
        # del json_object["vin"]
        del json_object["systemId"]
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
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest_trip_details",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_latest_trip_details', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_latest_trip_details", response.text)

    return response


def trip_vehicleUsageDetails(self, systemId, startDate, endDate, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Vehicle_get_vehicleUsageDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{startDate}', startDate).replace(
        '{endDate}', endDate)
    if "without_start_end_time" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('&startDate={startDate}',
                                                                                        "").replace(
            '&endDate={endDate}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get_vehicleUsageDetails",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Vehicle_get_vehicleUsageDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "Vehicle_get_vehicleUsageDetails", response.text)

    return response


# AssetManagement_trip_event
def trip_event(self, systemId, tripId, startDate, endDate, mergeId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip_event")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    tripId = tripId.replace('\n', '')
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', tripId).replace(
        '{startDate}', startDate).replace('{endDate}', endDate)
    if "without_date" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', tripId).replace(
            '{startDate}', "").replace('{endDate}', "")
    elif "without_systemId" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', "").replace('{tripId}', tripId).replace(
            '{startDate}', startDate).replace('{endDate}', endDate)
    elif "without_tripId" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', "").replace(
            '{startDate}', startDate).replace('{endDate}', endDate)
    elif "without_mergeId" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', "").replace(
            '{startDate}', startDate).replace('{endDate}', endDate).replace('{mergeId}', "")

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip_event",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip_event', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip_event", response.text)

    return response


# AssetManagement_trip_manage
def trip_manage(self, action, systemId, mergeId, tripId1, tripId2, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip_manage")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{action}', action)
    if "without_action" in tc:
        complete_url = str(base_url + endpoint).replace('{action}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["mergeGroups"][0]["mergeId"] = mergeId
    json_object["mergeGroups"][0]["tripId"][0] = tripId1
    json_object["mergeGroups"][0]["tripId"][1] = tripId2
    if "without_systemId" in tc:
        del json_object["systemId"]
    elif "without_tripId" in tc:
        del json_object["mergeGroups"][0]["tripId"][0]
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
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip_manage",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip_manage', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip_manage", response.text)

    return response


def trip_aggregated_summary(self, systemId, mergeId, startDate, endDate, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip_aggregated_summary")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{startDate}', startDate).replace(
        '{endDate}', endDate)

    if "without_startEndDate" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{startDate}', "").replace(
            '{endDate}', "")
    elif "without_systemId" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', "").replace('{startDate}', startDate).replace(
            '{endDate}', endDate)
    elif "no_systemId" in tc:
        complete_url = str(base_url + endpoint).replace('&systemId={systemId}', "").replace('{startDate}',
                                                                                            startDate).replace(
            '{endDate}', endDate)
    elif "mergeId" in tc:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{startDate}',
                                                                                        startDate).replace('{endDate}',
                                                                                                           endDate) + "&mergeId={mergeId}".replace(
            '{mergeId}', mergeId)
    print("Complete URL : ", complete_url)
    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip_aggregated_summary",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip_aggregated_summary', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip_aggregated_summary", response.text)

    return response


def trip_info(self, pageNo, pageSize, systemId, tripId, startDate, endDate, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_get_trip_info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    #tripId = tripId.replace('\n', '')
    #tripId =
    complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}', pageSize)

    if "systemId" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',
                                                                                    pageSize) + "&systemId={systemId}".replace(
            '{systemId}', systemId)

    elif "tripId" in tc:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',
                                                                                    pageSize) + "&systemId={systemId}&tripId={tripId}".replace(
            '{systemId}', systemId).replace('{tripId}', tripId)

    elif "trip_details_based_on_date":
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace('{pageSize}',
                                                                                    pageSize) + "&systemId={systemId}&startDate={startDate}&endDate={endDate}".replace(
            '{systemId}', systemId).replace('{startDate}', startDate).replace('{endDate}', endDate)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_get_trip_info",
                                                "AssetManagement_trip_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_get_trip_info', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_get_trip_info", response.text)

    return response

def get_trip_delete_details(self, systemId, tripId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip_deletion")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    tripId = tripId.replace('\n', '')
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{tripId}', tripId)

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip_deletion', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip_deletion", response.text)

    return response
# ------------------------------------------------------------
# RE REUSABLE Modules
# ------------------------------------------------------------


def read_latest_trip_meta_attribute_value(self, response, attribute):
    if attribute == "message":
        attribute_value = response["responseData"]["message"]
    elif attribute == "tripId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["tripId"]
    elif attribute == "parentTripId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["parentTripId"]
    elif attribute == "systemId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["systemId"]
    elif attribute == "subSystemId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["subSystemId"]
    elif attribute == "driverId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["driverId"]
    elif attribute == "fleetId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["fleetId"]
    elif attribute == "engineType":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["engineType"]
    elif attribute == "status":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["status"]
    elif attribute == "mergeId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["mergeId"]
    elif attribute == "vehicleFuelType":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["vehicleFuelType"]
    else:
        attribute_value = ""

    return attribute_value


def read_latest_trip_details_attribute_value(self, response, attribute):
    if attribute == "message":
        attribute_value = response["responseData"]["message"]
    elif attribute == "tripId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["tripId"]
    elif attribute == "parentTripId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["parentTripId"]
    elif attribute == "systemId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["systemId"]
    elif attribute == "subSystemId":
        attribute_value = response["responseData"]["data"]["trip"]["area"]["meta"]["subSystemId"]
    elif attribute == "driverId":
        attribute_value = response["responseData"]["data"]["trip"]["value"]["meta"]["driverId"]
    elif attribute == "fleetId":
        attribute_value = response["data"]["trip"]["meta"]["fleetId"]
    elif attribute == "engineType":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["engineType"]
    elif attribute == "status":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["status"]
    elif attribute == "mergeId":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["mergeId"]
    elif attribute == "vehicleFuelType":
        attribute_value = response["responseData"]["data"]["trip"]["meta"]["vehicleFuelType"]

    elif attribute == "tripStart_odometer":
        attribute_value = response["responseData"]["data"]["trip"]["tripStart"]["odometer"]
    elif attribute == "tripStart_batteryLevel":
        attribute_value = response["responseData"]["data"]["trip"]["tripStart"]["batteryLevel"]
    elif attribute == "tripStart_time":
        attribute_value = response["responseData"]["data"]["trip"]["tripStart"]["time"]
    elif attribute == "tripStart_location":
        attribute_value = response["responseData"]["data"]["trip"]["tripStart"]["location"]

    elif attribute == "tripEnd_odometer":
        attribute_value = response["responseData"]["data"]["trip"]["tripEnd"]["odometer"]
    elif attribute == "tripEnd_batteryLevel":
        attribute_value = response["responseData"]["data"]["trip"]["tripEnd"]["batteryLevel"]
    elif attribute == "tripEnd_time":
        attribute_value = response["responseData"]["data"]["trip"]["tripEnd"]["time"]
    elif attribute == "tripEnd_location":
        attribute_value = response["responseData"]["data"]["trip"]["tripEnd"]["location"]

    elif attribute == "tripSummary_tripDistance":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["tripDistance"]
    elif attribute == "tripSummary_tripDuration":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["tripDuration"]
    elif attribute == "tripSummary_avgSpeed":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["avgSpeed"]
    elif attribute == "tripSummary_batteryConsumed":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["batteryConsumed"]
    elif attribute == "tripSummary_tripBatteryEfficiency":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["tripBatteryEfficiency"]
    elif attribute == "tripSummary_maxSpeed":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["maxSpeed"]
    elif attribute == "tripSummary_violation_summary":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["violationSummary"]
    elif attribute == "tripSummary_violation_summary_ha":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["violationSummary"]["ha"]
    elif attribute == "tripSummary_violation_summary_hb":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["violationSummary"]["hb"]
    elif attribute == "tripSummary_violation_summary_overSpeed":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["violationSummary"]["overSpeed"]
    elif attribute == "tripSummary_idleTime":
        attribute_value = response["responseData"]["data"]["trip"]["tripSummary"]["idleTime"]
    else:
        attribute_value = ""

    return attribute_value


# AssetManagement_trip-details-by-tripId
def trip_details_by_tripId(self, trip_id, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "AssetManagement_trip_details_by_tripId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    trip_id = trip_id.replace('\n', '')
    complete_url = str(base_url + endpoint).replace('{tripId}', trip_id).replace('{systemId}', systemId)

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "AssetManagement_trip_AuthToken")
            time.sleep(10)
            update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip_details_by_tripId",
                                                "AssetManagement_trip_AuthToken")
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
            time.sleep(60)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('AssetManagement_trip_details_by_tripId', response.text)
    save_api_resp_in_excel(self, "API_Data", "AssetManagement_trip_details_by_tripId", response.text)

    return response


def read_trip_details_attribute_value(self, cloudEnv, response, attribute):
    if attribute == "message":
        attribute_value = response["message"]

    elif attribute == "tripId":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["tripId"]
    elif attribute == "parentTripId":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["parentTripId"]
    elif attribute == "systemId":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["systemId"]
    elif attribute == "subSystemId":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["area"]["meta"]["subSystemId"]
    elif attribute == "engineType":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["engineType"]
    elif attribute == "status":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["status"]
    elif attribute == "mergeId":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["mergeId"]
    elif attribute == "vehicleFuelType":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["meta"]["vehicleFuelType"]

    elif attribute == "tripStart_odometer":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripStart"]["odometer"]
    elif attribute == "tripStart_batteryLevel":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripStart"]["batteryLevel"]
    elif attribute == "tripStart_time":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripStart"]["time"]
    elif attribute == "tripStart_location":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripStart"]["location"]

    elif attribute == "tripEnd_odometer":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripEnd"]["odometer"]
    elif attribute == "tripEnd_batteryLevel":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripEnd"]["batteryLevel"]
    elif attribute == "tripEnd_time":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripEnd"]["time"]
    elif attribute == "tripEnd_location":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripEnd"]["location"]

    elif attribute == "tripSummary_tripDistance":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["tripDistance"]
    elif attribute == "tripSummary_tripDuration":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["tripDuration"]
    elif attribute == "tripSummary_avgSpeed":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["avgSpeed"]
    elif attribute == "tripSummary_batteryConsumed":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["batteryConsumed"]
    elif attribute == "tripSummary_tripBatteryEfficiency":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["tripBatteryEfficiency"]
    elif attribute == "tripSummary_maxSpeed":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["maxSpeed"]
    elif attribute == "tripSummary_violation_summary":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["violationSummary"]
    elif attribute == "tripSummary_violation_summary_ha":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["violationSummary"]["ha"]
    elif attribute == "tripSummary_violation_summary_hb":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["violationSummary"]["hb"]
    elif attribute == "tripSummary_violation_summary_overSpeed":
        if cloudEnv in ["GCP-QA2"]:
            attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["violationSummary"][
            "over_speed"]
        else:
            attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["violationSummary"][
                "overSpeed"]
    elif attribute == "tripSummary_idleTime":
        attribute_value = response["trips"]["tripSummaryDetails"][0]["trip"]["tripSummary"]["idleTime"]
    else:
        attribute_value = ""

    return attribute_value


def get_trip_summary_details(self, cloudEnv, systemId, tripId, tc):
    pageNo = "0"
    pageSize = "10"
    startDate = endDate = ""
    response1 = trip_info(self, pageNo, pageSize, systemId, tripId, startDate, endDate, "tripId")

    # Validate response status code
    assert (response1.status_code == 200), "Status code is not 200. Rather found : " + str(
        response1.status_code)

    # Parse API response into JSON
    response1_body = response1.json()

    trip_1_tripDistance = read_trip_details_attribute_value(self, cloudEnv, response1_body, "tripSummary_tripDistance")
    trip_1_tripDuration = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                            "tripSummary_tripDuration")

    trip_1_avgSpeed = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                        "tripSummary_avgSpeed")
    trip_1_maxSpeed = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                        "tripSummary_maxSpeed")

    trip_1_batteryConsumed = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                               "tripSummary_batteryConsumed")
    trip_1_tripBatteryEfficiency = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                                     "tripSummary_tripBatteryEfficiency")

    trip_1_idleTime = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                        "tripSummary_idleTime")

    trip_1_violation_summary_ha = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                                    "tripSummary_violation_summary_ha")
    trip_1_violation_summary_hb = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                                    "tripSummary_violation_summary_hb")
    trip_1_violation_summary_hc = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                                    "tripSummary_violation_summary_hc")
    trip_1_violation_summary_overSpeed = read_trip_details_attribute_value(self, cloudEnv, response1_body,
                                                                           "tripSummary_violation_summary_overSpeed")
    print('-------------------------------------------------------------')
    print("Trip Distance :", trip_1_tripDistance)
    print("Trip Duration :", trip_1_tripDuration)
    print("Average Speed :", trip_1_avgSpeed)
    print("Battery Consumed :", trip_1_batteryConsumed)
    print("Trip Battery Efficiency :", trip_1_tripBatteryEfficiency)
    # print("Fuel Consumed :", trip_1_fuelConsumed)
    # print("Trip Fuel Efficiency :", trip_1_tripFuelEfficiency)
    print("Max Speed :", trip_1_maxSpeed)
    print("Idle Time :", trip_1_idleTime)
    print("Violation Summary - HA :", trip_1_violation_summary_ha)
    print("Violation Summary - HB :", trip_1_violation_summary_hb)
    print("Violation Summary - HC :", trip_1_violation_summary_hc)
    print("Violation Summary - Over Speed :", trip_1_violation_summary_overSpeed)
    print('-------------------------------------------------------------')

    return trip_1_tripDistance, trip_1_tripDuration, trip_1_avgSpeed, trip_1_maxSpeed, trip_1_batteryConsumed, trip_1_tripBatteryEfficiency, trip_1_idleTime, trip_1_violation_summary_ha, trip_1_violation_summary_hb, trip_1_violation_summary_hc, trip_1_violation_summary_overSpeed


def vehicle_usage(self, cloudEnv, systemId):
    # Start & end date
    startDate = str(int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000000)
    endDate = str(int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000)

    print("System Id : ", systemId)
    print("Start Date : ", startDate)
    print("End Date : ", endDate)

    # Call vehicle usage reusable module
    response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["message"] == "Success":
        print("###################################################### ", '\n')
        data_len = len(response_body["vehicleUsage"]["trips"])
        print("No. of Trips : ", data_len)
        tripDistance_actual = tripDuration_actual = avgSpeed_actual = batteryConsumed_actual = tripBatteryEfficiency_actual = maxSpeed_actual = idleTime_actual = ha_actual = hb_actual = hc_actual = overSpeed_actual = hc = 0

        try:

            for i in range(data_len):
                trip_1 = response_body["vehicleUsage"]["trips"][i]
                print('-------------------------------------------------------------')
                print("Trip 1 Details : ")
                print('-------------------------------------------------------------')
                trip_1_tripDistance, trip_1_tripDuration, trip_1_avgSpeed, trip_1_maxSpeed, trip_1_batteryConsumed, trip_1_tripBatteryEfficiency, trip_1_idleTime, trip_1_violation_summary_ha, trip_1_violation_summary_hb, trip_1_violation_summary_hc, trip_1_violation_summary_overSpeed = get_trip_summary_details(
                    self, systemId, trip_1, "valid")

                tripDistance_actual = tripDistance_actual + trip_1_tripDistance
                tripDuration_actual = tripDuration_actual + trip_1_tripDuration
                avgSpeed_actual = tripDuration_actual + trip_1_avgSpeed
                batteryConsumed_actual = batteryConsumed_actual + trip_1_batteryConsumed
                tripBatteryEfficiency_actual = tripBatteryEfficiency_actual + trip_1_tripBatteryEfficiency
                maxSpeed_actual = maxSpeed_actual + trip_1_maxSpeed
                idleTime_actual = idleTime_actual + trip_1_idleTime
                ha_actual = ha_actual + trip_1_violation_summary_ha
                hb_actual = hb_actual + trip_1_violation_summary_hb
                hc_actual = hc_actual + trip_1_violation_summary_hc
                overSpeed_actual = overSpeed_actual + trip_1_violation_summary_overSpeed
        except:
            print("All trips does not have proper data, hence cannot be calculated")

        print("###################################################### ", '\n')

        print('-------------------------------------------------------------')
        print("Aggregated Trip Summary Details: ")
        print('-------------------------------------------------------------')

        try:
            print(tripDistance_actual, tripDuration_actual, batteryConsumed_actual, maxSpeed_actual)
            avgSpeed_actual = tripDistance_actual / tripDuration_actual
            tripBatteryEfficiency_actual = tripDistance_actual / batteryConsumed_actual
            maxSpeed_actual = maxSpeed_actual / data_len
        except:
            print("")

        # tripFuelEfficiency = response_body["vehicleUsage"]["aggregatedTripSummary"]["tripFuelEfficiency"]
        tripDistance = response_body["vehicleUsage"]["aggregatedTripSummary"]["tripDistance"]
        # fuelConsumed = response_body["vehicleUsage"]["aggregatedTripSummary"]["fuelConsumed"]

        tripDuration = response_body["vehicleUsage"]["aggregatedTripSummary"]["tripDuration"]
        avgSpeed = response_body["vehicleUsage"]["aggregatedTripSummary"]["avgSpeed"]
        batteryConsumed = response_body["vehicleUsage"]["aggregatedTripSummary"]["batteryConsumed"]

        tripBatteryEfficiency = response_body["vehicleUsage"]["aggregatedTripSummary"]["tripBatteryEfficiency"]
        maxSpeed = response_body["vehicleUsage"]["aggregatedTripSummary"]["maxSpeed"]
        idleTime = response_body["vehicleUsage"]["aggregatedTripSummary"]["idleTime"]

        ha = response_body["vehicleUsage"]["aggregatedTripSummary"]["violationSummary"]["ha"]
        hb = response_body["vehicleUsage"]["aggregatedTripSummary"]["violationSummary"]["hb"]
        # hc = response_body["vehicleUsage"]["aggregatedTripSummary"]["violationSummary"]["hc"]
        if cloudEnv in ["GCP-QA2"]:
            overSpeed = response_body["vehicleUsage"]["aggregatedTripSummary"]["violationSummary"]["over_speed"]
        else:
            overSpeed = response_body["vehicleUsage"]["aggregatedTripSummary"]["violationSummary"]["overSpeed"]

        # print("###################################################### ", '\n')
        print("Trip Distance :", tripDistance)
        print("Trip Duration :", tripDuration)
        print("Average Speed :", avgSpeed)
        print("Battery Consumed :", batteryConsumed)
        print("Trip Battery Efficiency :", tripBatteryEfficiency)
        # print("Fuel Consumed :", fuelConsumed)
        # print("Trip Fuel Efficiency :", tripFuelEfficiency)
        print("Max Speed :", maxSpeed)
        print("Idle Time :", idleTime)
        print("Violation Summary - HA :", ha)
        print("Violation Summary - HB :", hb)
        # print("Violation Summary - HC :", hc)
        print("Violation Summary - Over Speed :", overSpeed)
        print("###################################################### ", '\n')
    else:
        print("Fail to fetch vehicle usage details")
        assert False

    print('-------------------------------------------------------------')
    print("Validations : ")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Trip Distance : ", tripDistance_actual)
    print("Actual Aggregated Trip Summary - Trip Distance : ", tripDistance)
    if tripDistance_actual == tripDistance:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Trip Distance should be calculated based on trips",
                   "Aggregated Trip Summary - Trip Distance value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Trip Distance should be calculated based on trips",
                   "Aggregated Trip Summary - Trip Distance value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")

    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Trip Duration : ", tripDuration_actual)
    print("Actual Aggregated Trip Summary - Trip Duration : ", tripDuration)
    if tripDuration_actual == tripDuration:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Trip Duration should be calculated based on trips",
                   "Aggregated Trip Summary - Trip Duration value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Trip Duration should be calculated based on trips",
                   "Aggregated Trip Summary - Trip Duration value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Average Speed : ", avgSpeed_actual)
    print("Actual Aggregated Trip Summary - Average Speed : ", avgSpeed)
    if avgSpeed_actual == avgSpeed:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Average Speed should be calculated based on trips",
                   "Aggregated Trip Summary - Average Speed value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Average Speed should be calculated based on trips",
                   "Aggregated Trip Summary - Average Speed value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Maximum Speed : ", maxSpeed_actual)
    print("Actual Aggregated Trip Summary - Maximum Speed : ", maxSpeed)
    if maxSpeed_actual == maxSpeed:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Maximum Speed should be calculated based on trips",
                   "Aggregated Trip Summary - Maximum Speed value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Maximum Speed should be calculated based on trips",
                   "Aggregated Trip Summary - Maximum Speed value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Battery Consumed : ", batteryConsumed_actual)
    print("Actual Aggregated Trip Summary - Battery Consumed : ", batteryConsumed)
    if batteryConsumed_actual == batteryConsumed:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Battery Consumed should be calculated based on trips",
                   "Aggregated Trip Summary - Battery Consumed  value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Battery Consumed  should be calculated based on trips",
                   "Aggregated Trip Summary - Battery Consumed  value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Battery Efficiency : ", tripBatteryEfficiency_actual)
    print("Actual Aggregated Trip Summary - Battery Efficiency : ", tripBatteryEfficiency)
    if tripBatteryEfficiency_actual == tripBatteryEfficiency:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Battery Efficiency should be calculated based on trips",
                   "Aggregated Trip Summary - Battery Efficiency  value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Battery Efficiency  should be calculated based on trips",
                   "Aggregated Trip Summary - Battery Efficiency  value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Idle Time : ", idleTime_actual)
    print("Actual Aggregated Trip Summary - Idle Time : ", idleTime)
    if idleTime_actual == idleTime:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Idle Time should be calculated based on trips",
                   "Aggregated Trip Summary - Idle Time  value is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Idle Time  should be calculated based on trips",
                   "Aggregated Trip Summary - Idle Time  value is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Violation Summary - HA : ", ha_actual)
    print("Actual Aggregated Trip Summary - Violation Summary - HA : ", ha)
    if ha_actual == ha:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Violation Summary - HA should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - HA  count is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Violation Summary - HA  should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - HA  count is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Violation Summary - HB : ", hb_actual)
    print("Actual Aggregated Trip Summary - Violation Summary - HB : ", hb)
    if hb_actual == hb:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Violation Summary - HB should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - HB  count is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Violation Summary - HB  should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - HB  count is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    print('-------------------------------------------------------------')

    print("Expected Aggregated Trip Summary - Violation Summary - Over Speed : ", overSpeed_actual)
    print("Actual Aggregated Trip Summary - Violation Summary - Over Speed : ", overSpeed)
    if overSpeed_actual == overSpeed:
        testResult(self, "passed",
                   "Aggregated Trip Summary - Violation Summary - Over Speed should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - Over Speed  count is correct & stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")
    else:
        testResult(self, "verificationFailed",
                   "Aggregated Trip Summary - Violation Summary - Over Speed  should be calculated based on trips",
                   "Aggregated Trip Summary - Violation Summary - Over Speed  count is incorrect or not stored in the Cloud DB. pls refer "
                   "stub & device/cloud for detailed info")


# Trip info, merge, umerge, aggregation

# Step 1: get first 2 trips
def get_2_trip_id_summary(self, systemId):
    pageNo = "0"
    pageSize = "10"
    tripId = startDate = endDate = ""

    # Fetch trip data using the API
    response = trip_info(self, pageNo, pageSize, systemId, tripId, startDate, endDate, "systemId")
    assert response.status_code == 200, f"Failed to fetch trip info. Status code: {response.status_code}"

    response_body = response.json()
    if response_body.get("message") != "Success":
        print(f"Unexpected response message: {response_body.get('message')}")
        assert False

    # Extract completed trips
    tripSummaryDetails = response_body.get("trips", {}).get("tripSummaryDetails", [])
    trip_ids = []
    trip_summary = []

    for summary in tripSummaryDetails:
        try:
            meta = summary["trip"]["meta"]
            status = meta.get("status", "").lower()
            if status == "completed":
                trip_ids.append(meta.get("tripId", ""))
                trip_summary.append(summary["trip"].get("tripSummary", {}))
                if len(trip_ids) == 2:
                    break
        except (KeyError, TypeError) as error:
            print(f"Error parsing trip summary: {error}")
            continue

    if len(trip_ids) < 2:
        print("Fewer than 2 completed trips found.")
        assert False

    return trip_summary[0], trip_summary[1], trip_ids


# Step 2: Merge 2 trips
def merge_trips(self, action, systemId, mergeId, tripId1, tripId2):
    pageNo = "0"
    pageSize = "10"
    tripId = startDate = endDate = ""

    if action == "merge":

        # Call the trip_manage API to merge the trips
        response = trip_manage(self, action, systemId, mergeId, tripId1, tripId2, "valid")

        # Validate the API response status code
        assert response.status_code == 200, f"Failed to merge trips. Status code: {response.status_code}"

        # Parse the API response into JSON
        response_body = response.json()

        # Validate the response message
        if response_body["message"] == "Trips merged successfully.":
            print("Trips have been merged successfully.")
            testResult(self, "passed", "Trips should be merged successfully", "Trips merged successfully")
            assert True
        elif response_body.get("message", "").startswith("Trips merged successfully."):
            print("Trips have been merged successfully.")
            testResult(self, "passed", "Trips should be merged successfully", "Trips merged successfully")
            assert True
        else:
            print("Trip merge failed.")
            testResult(self, "failed", "Trips should be merged successfully", "Trips are not merged")

    elif action == "unmerge":

        response1 = trip_manage(self, action, systemId, mergeId, tripId1, tripId2, "valid")
        # Validate the API response status code
        assert response1.status_code == 200, "Status code is not 200. Rather found: " + str(response1.status_code)

        # Parse the API response into JSON format
        response_body = response1.json()

        if response_body["message"] == "Trips unmerged successfully.":
            # step 4: Trip unmerge
            response = trip_info(self, pageNo, pageSize, systemId, tripId, startDate, endDate, "systemId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["message"] == "Success":
                data_len = len(response_body["trips"]["tripSummaryDetails"])

                # Validate presence of trip data
                if data_len >= 1:
                    mergeId = None  # Initialize mergeId

                    for i in range(data_len):
                        tripId = response_body["trips"]["tripSummaryDetails"][i]["trip"]["meta"]["tripId"]

                        # Check if the tripId matches either tripId1 or tripId2
                        if tripId == tripId1 or tripId == tripId2:
                            mergeId = response_body["trips"]["tripSummaryDetails"][i]["trip"]["meta"]["mergeId"]
                            break

                    # mergeId should be zero after unmerge the trips
                    if mergeId == 0 or mergeId == str(0):
                        testResult(self, "passed", "TripId's should be unmerged successfully",
                                   "TripId's unmerged successfully")
                        assert True
                    else:
                        testResult(self, "failed", "TripId's should be unmerged successfully",
                                   f"Trip is still merged. MergeId: {mergeId}")
                        assert False
                else:
                    print("No trips found in the response.")
                    assert False
            else:
                print("Trip unmerge operation failed.")
                assert False
    else:
        print("Invalid action")


# Step 3: Get mergeId from the trip Info API
def get_merge_id(self, systemId, tripId1, tripId2):
    pageNo = "0"
    pageSize = "10"  # Adjust page size if needed
    tripId = startDate = endDate = ""

    # Fetch trip info using the API
    response = trip_info(self, pageNo, pageSize, systemId, tripId, startDate, endDate, "systemId")
    assert response.status_code == 200, f"Failed to fetch trip info. Status code: {response.status_code}"

    # Parse the API response
    response_body = response.json()
    assert response_body["message"] == "Success", f"Unexpected response message: {response_body['message']}"

    # Locate mergeId for the given trips
    for trip in response_body["trips"]["tripSummaryDetails"]:
        trip_meta = trip["trip"]["meta"]
        if trip_meta["tripId"] in [tripId1, tripId2]:
            mergeId = trip_meta.get("mergeId")
            if mergeId and mergeId != "0":
                print(f"Merged Trip ID Found: {mergeId}")
                return mergeId

    else:
        print("MergeId not found for the provided trips.")


# Step 4: Fetch aggregated summary from the GET API
def fetch_aggregated_summary(self, cloudEnv, systemId, mergeId):
    today_date = date.today()
    startDate = today_date.strftime("%m-%d-%Y")
    endDate = startDate

    # Call the API
    response = trip_aggregated_summary(self, systemId, mergeId, startDate, endDate, "mergeId")

    # Validate API response
    assert response.status_code == 200, f"Status code is not 200. Found: {response.status_code}"

    # Parse API response into JSON format
    response_body = response.json()

    if cloudEnv not in ["GCP-QA3", "GCP-QA2", "RE-UAT", "RE-DM1"]:
        actual_aggregated_trip_summary = response_body["tripDetail"]["mergedTrips"][0]["aggregatedTripSummary"]
    else:
        actual_aggregated_trip_summary = response_body["tripDetail"]["mergedTrips"]["aggregatedTripSummary"]

    return actual_aggregated_trip_summary


# Step 5: Calculate expected aggregated values
def calculate_expected_aggregated_summary(cloudEnv, trip1_distance, trip2_distance, trip1_duration, trip2_duration,
                                          trip1_battery_consumed, trip2_battery_consumed, trip1_idle_time,
                                          trip2_idle_time, trip1_ha, trip2_ha, trip1_hb, trip2_hb,
                                          trip1_over_speed, trip2_over_speed):
    expected_trip_distance = trip1_distance + trip2_distance
    expected_trip_duration = trip1_duration + trip2_duration
    expected_avg_speed = expected_trip_distance / expected_trip_duration if expected_trip_duration > 0 else 0
    expected_battery_consumed = trip1_battery_consumed + trip2_battery_consumed
    expected_efficiency = expected_trip_distance / expected_battery_consumed if expected_battery_consumed > 0 else 0
    expected_idle_time = trip1_idle_time + trip2_idle_time
    expected_ha = trip1_ha + trip2_ha
    expected_hb = trip1_hb + trip2_hb
    expected_overspeed = trip1_over_speed + trip2_over_speed

    result = {
        "tripDistance": expected_trip_distance,
        "tripDuration": expected_trip_duration,
        "avgSpeed": expected_avg_speed,
        "batteryConsumed": expected_battery_consumed,
        "tripBatteryEfficiency": expected_efficiency,
        "idleTime": expected_idle_time,
        "ha": expected_ha,
        "hb": expected_hb,
    }

    if cloudEnv in ["GCP-QA2"]:
        result["over_speed"] = expected_overspeed
    else:
        result["overSpeed"] = expected_overspeed

    return result


# Step 7: Validate aggregated summary
def validate_aggregated_summary(cloudEnv, expected_summary, actual_summary):
    print("==> Expected Aggregated Summary: ", expected_summary)

    print("==> Actual Aggregated Summary: ", actual_summary)

    # Status and error tracking
    status = "PASS"
    result = []

    # Compare Trip Distance
    if expected_summary["tripDistance"] == actual_summary["tripDistance"]:
        result.append(
            f"Trip Distance Match: Expected {expected_summary['tripDistance']}, Found {actual_summary['tripDistance']}")
        status = "PASS"

    # Compare Trip Duration
    if expected_summary["tripDuration"] == actual_summary["tripDuration"]:
        result.append(
            f"Trip Duration Match: Expected {expected_summary['tripDuration']}, Found {actual_summary['tripDuration']}")
        status = "PASS"

    # Compare Average Speed
    if expected_summary["avgSpeed"] == actual_summary["avgSpeed"]:
        result.append(
            f"Avg Speed Match: Expected {expected_summary['avgSpeed']}, Found {actual_summary['avgSpeed']}")
        status = "PASS"

    # Compare Battery Consumed
    if expected_summary["batteryConsumed"] == actual_summary["batteryConsumed"]:
        result.append(
            f"Battery Consumed Match: Expected {expected_summary['batteryConsumed']}, Found {actual_summary['batteryConsumed']}")
        status = "PASS"

    # Compare Battery Efficiency
    if expected_summary["tripBatteryEfficiency"] == float(actual_summary["tripBatteryEfficiency"]):
        result.append(
            f"Battery Efficiency Match: Expected {expected_summary['tripBatteryEfficiency']}, Found {actual_summary['tripBatteryEfficiency']}")
        status = "PASS"

    # Compare Idle Time
    if expected_summary["idleTime"] == actual_summary["idleTime"]:
        result.append(
            f"Idle Time Match: Expected {expected_summary['idleTime']}, Found {actual_summary['idleTime']}")
        status = "PASS"

    # Compare Harsh Accelerations (HA)
    if expected_summary["ha"] == actual_summary["violationSummary"]["ha"]:
        result.append(
            f"Harsh Acceleration Match: Expected {expected_summary['ha']}, Found {actual_summary['violationSummary']['ha']}")
        status = "PASS"

    # Compare Harsh Braking (HB)
    if expected_summary["hb"] == actual_summary["violationSummary"]["hb"]:
        result.append(
            f"Harsh Brakes Match: Expected {expected_summary['hb']}, Found {actual_summary['violationSummary']['hb']}")
        status = "PASS"

    # Compare Overspeed Events
    if cloudEnv in ["GCP-QA2"]:
        if expected_summary["over_speed"] == actual_summary["violationSummary"]["over_speed"]:
            result.append(
                f"Overspeed Match: Expected {expected_summary['over_speed']}, Found {actual_summary['violationSummary']['over_speed']}")
            status = "PASS"
    else:
        if expected_summary["overSpeed"] == actual_summary["violationSummary"]["overSpeed"]:
            result.append(
                f"Overspeed Match: Expected {expected_summary['overSpeed']}, Found {actual_summary['violationSummary']['overSpeed']}")
            status = "PASS"

    # Validation Results
    if status == "PASS":
        print("[PASS] Aggregated Trip Summary validation successful.")
        for res in result:
            print(f"[RESULT] {res}")
    else:
        print("[FAIL] Aggregated Trip Summary validation failed.")

        assert False


def trip_delete(self, systemId, tc):
    # Get/Read trip Id with Completed status for delete
    try:
        trip1_summary, trip2_summary, trip_ids = get_2_trip_id_summary(self, systemId)
    except AssertionError:
        print("Failed to retrieve two completed trip summaries.")
        # self.result.set_result(TestResults.failed)
        return

    if not trip_ids or len(trip_ids) < 2:
        print("Completed trip IDs not found.")
        # self.result.set_result(TestResults.failed)
        return

    tripId = trip_ids[0]
    print("Trip Id:", tripId)

    # Call trip delete reusable module
    response = get_trip_delete_details(self, systemId, tripId, tc)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["message"] == "Trips deleted successfully.":
        print("###################################################### ", '\n')
        print("Trip is deleted successfully")
        print("###################################################### ", '\n')
        assert True
    else:
        print("Fail to delete Trip ")
        assert False

    # Verify Delete status

    pageNo = "0"
    pageSize = "10"
    searchTripId = startDate = endDate = ""

    # Fetch trip data using the API
    response = trip_info(self, pageNo, pageSize, systemId, searchTripId, startDate, endDate, "systemId")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    tripSummaryDetails_len = len(response_body["trips"]["tripSummaryDetails"])

    trip_found = False
    if tripSummaryDetails_len >= 1:
        for i in range(tripSummaryDetails_len):
            status_actual = response_body["trips"]["tripSummaryDetails"][i]["trip"]["meta"]["status"]
            tripId_actual = response_body["trips"]["tripSummaryDetails"][i]["trip"]["meta"]["tripId"]
            if tripId_actual == tripId and status_actual == "DELETED":
                print("Trip is deleted successfully and the trip status updated as DELETED")
                trip_found = True
                break
    else:
        print("No Trip exists with Deleted Status or Status is not update ")
        assert False

    if trip_found:
        print("Trip status is updated as DELETED successfully ")
        assert True
    else:
        print("No Trip exists with Deleted Status or Status is not update ")
        assert False