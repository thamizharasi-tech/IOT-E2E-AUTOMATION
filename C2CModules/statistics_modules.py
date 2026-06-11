import ast
import json
import time
import requests

from C2CModules.api_modules import pageNo_pageSize_update, header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# Statistic - monthly-trip-summaries-vin
def Statistics_Monthly_trip_summaries_vin(self, fromMonth, toMonth):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-MonthlyTripSummariesVin")
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
    json_object['fromMonth'] = fromMonth
    json_object['toMonth'] = toMonth
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesVin",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-MonthlyTripSummariesVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-MonthlyTripSummariesVin", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# Statistic - monthly-trip-summaries-fleet
def Statistics_Monthly_trip_summaries_fleet(self, fromMonth, toMonth):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet")
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
    json_object['fromMonth'] = fromMonth
    json_object['toMonth'] = toMonth
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-MonthlyTripSummariesFleet', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# Statistic - daily-trip-summaries-vin
def Statistics_daily_trip_summaries_vin(self, fromDate, toDate):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-DailyTripSummariesVin")
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
    json_object['fromDate'] = fromDate
    json_object['toDate'] = toDate
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesVin",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-DailyTripSummariesVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-DailyTripSummariesVin", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# Statistic - daily-trip-summaries-fleet
def Statistics_daily_trip_summaries_fleet(self, fromDate, toDate):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-DailyTripSummariesFleet")
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
    json_object['fromDate'] = fromDate
    json_object['toDate'] = toDate
    payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesFleet",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-DailyTripSummariesFleet', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-DailyTripSummariesFleet", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# New api modules
# Statistics-DailyTripSummariesFleet_byFleetId
def Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-DailyTripSummariesFleet_byFleetId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    complete_url = pageNo_pageSize_update(complete_url, tc)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "no_fromDate" in tc:
        del json_object['fromDate']
    else:
        json_object['fromDate'] = fromDate
    if "no_toDate" in tc:
        del json_object['toDate']
    else:
        json_object['toDate'] = toDate
    if "no_fleetId" in tc:
        del json_object['fleetId']
    else:
        json_object['fleetId'] = fleetId

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
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesFleet_byFleetId",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-DailyTripSummariesFleet_byFleetId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-DailyTripSummariesFleet_byFleetId", response.text)

    return response


# Statistics-MonthlyTripSummariesFleet_byFleetId
def Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet_byFleetId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    complete_url = pageNo_pageSize_update(complete_url, tc)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "no_fromMonth" in tc:
        del json_object['fromMonth']
    else:
        json_object['fromMonth'] = fromMonth
    if "no_toMonth" in tc:
        del json_object['toMonth']
    else:
        json_object['toMonth'] = toMonth
    if "no_fleetId" in tc:
        del json_object['fleetId']
    else:
        json_object['fleetId'] = fleetId
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
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet_byFleetId",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-MonthlyTripSummariesFleet_byFleetId', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet_byFleetId", response.text)

    return response


# Statistics-DailyTripSummariesVin_byVin
def Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-DailyTripSummariesVin_byVin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    complete_url = pageNo_pageSize_update(complete_url, tc)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "no_fromDate" in tc:
        del json_object['fromDate']
    else:
        json_object['fromDate'] = fromDate
    if "no_toDate" in tc:
        del json_object['toDate']
    else:
        json_object['toDate'] = toDate
    if "no_fleetId" in tc:
        del json_object['fleetId']
    else:
        json_object['fleetId'] = fleetId
    if "no_systemId" in tc:
        del json_object['systemId']
    else:
        json_object['systemId'] = systemId
    if "no_vin" in tc:
        del json_object['vin']
    else:
        json_object['vin'] = vin
    if "no_fuelType" in tc:
        del json_object['fuelType']
    else:
        json_object['fuelType'] = fuelType
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
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesVin_byVin",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-DailyTripSummariesVin_byVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-DailyTripSummariesVin_byVin", response.text)

    return response


# Statistics-MonthlyTripSummariesVin_byVin
def Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId, fuelType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Statistics-MonthlyTripSummariesVin_byVin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint)
    complete_url = pageNo_pageSize_update(complete_url, tc)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "no_fromMonth" in tc:
        del json_object['fromMonth']
    else:
        json_object['fromMonth'] = fromMonth
    if "no_toMonth" in tc:
        del json_object['toMonth']
    else:
        json_object['toMonth'] = toMonth
    if "no_fleetId" in tc:
        del json_object['fleetId']
    else:
        json_object['fleetId'] = fleetId
    if "no_systemId" in tc:
        del json_object['systemId']
    else:
        json_object['systemId'] = systemId
    if "no_vin" in tc:
        del json_object['vin']
    else:
        json_object['vin'] = vin
    if "no_fuelType" in tc:
        del json_object['fuelType']
    else:
        json_object['fuelType'] = fuelType
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
            token_gen_reus_mod(self, "API_Data", "Statistics_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesVin_byVin",
                                                "Statistics_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Statistics-MonthlyTripSummariesVin_byVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "Statistics-MonthlyTripSummariesVin_byVin", response.text)

    return response


