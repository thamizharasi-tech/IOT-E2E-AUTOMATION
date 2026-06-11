import ast
import json
import time

import requests

from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# Telemetry Persistence
def Telemetry_Persistence(self, systemId, vin, eventType, start, stop):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "TelemetryPersistence_history")
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
    json_object["systemId"] = systemId
    json_object["vin"] = vin
    json_object["eventType"] = eventType
    json_object["start"] = start
    json_object["stop"] = stop
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
            token_gen_reus_mod(self, "API_Data", "TelemetryPersistence_AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryPersistence_history",
                                                "TelemetryPersistence_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('TelemetryPersistence_history', response.text)
    save_api_resp_in_excel(self, "API_Data", "TelemetryPersistence_history", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body
