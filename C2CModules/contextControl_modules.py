import ast
import json
import time
import requests

from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ContextControl
def context_Control(self, block_id, reason_code, enable, frequency, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ContextControl")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object['config'][0]['block_id'] = block_id
    json_object['config'][0]['reason_code'] = reason_code
    json_object['config'][0]['enable'] = enable
    json_object['config'][0]['frequency'] = frequency
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
            token_gen_reus_mod(self, "API_Data", "ContextControl_getToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "ContextControl",
                                                "ContextControl_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('ContextControl', response.text)
    save_api_resp_in_excel(self, "API_Data", "ContextControl", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()


    return response_body

# ContextControl
def context_Control_for_telemetry_location(self, systemId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Context_control_telemetry_location")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
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
            token_gen_reus_mod(self, "API_Data", "ContextControl_getToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "ContextControl",
                                                "ContextControl_getToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('ContextControl', response.text)
    save_api_resp_in_excel(self, "API_Data", "ContextControl", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()


    return response_body

# ContextControl_getDetails
def ContextControl_getDetails(self, messageId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ContextControl_getDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{messageId}', messageId)
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

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "ContextControl_getToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "ContextControl_getDetails",
                                                "ContextControl_getToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('ContextControl_getDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "ContextControl_getDetails", response.text)

    return response
