import ast
import json
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel

# API Operation to create initial config
def App_data_usage_getAppDataUsage(self, systemId,appID, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "App_data_usage_getAppUsage")
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
    print("Headers: ", header_x)

    # Payload
    #json_object = json.loads(payload)
    #payload = json_object
    #print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('App_data_usage_getAppUsage', response.text)
    save_api_resp_in_excel(self, "API_Data", "App_data_usage_getAppUsage", response.text)

    return response

def App_data_usage_getAppUsageDetails(self, systemId, offset,limit, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "App_data_usage_getAppUsageDetails")
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
    print("Headers: ", header_x)

    # Payload
    #json_object = json.loads(payload)
    #payload = json_object
    #print("Payload: ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('App_data_usage_getAppUsageDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "App_data_usage_getAppUsageDetails", response.text)

    return response
