import ast
import json
import requests
import time

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel
from C2CModules.testResults import testResult



def DigitalPin_reset_PIN(self, systemId, action, id, user_id, value, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_reset_PIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}',action)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["id"] = id
    json_object["user_id"] = user_id
    json_object["value"] = value
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_reset_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_reset_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_reset_PIN", response.text)

    return response


def DigitalPin_revoke_PIN(self, systemId, action, id, user_id, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_revoke_PIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}',action)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["id"] = id
    json_object["user_id"] = user_id
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_revoke_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_revoke_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_revoke_PIN", response.text)

    return response

def DigitalPin_share_PIN(self, systemId, id, user_id, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_share_PIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["id"] = id
    json_object["user_id"] = user_id
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_share_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_share_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_share_PIN", response.text)

    return response


def DigitalPin_statusTracking(self, trackingId, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_statusTracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_statusTracking",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_statusTracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_statusTracking", response.text)

    return response


def DigitalPin_reset_PIN_global(self, systemId, action, id, user_id, value, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_reset_PIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}',action)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["id"] = id
    json_object["user_id"] = user_id
    json_object["value"] = value
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_reset_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_reset_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_reset_PIN", response.text)

    return response

def DigitalPin_revoke_PIN_global(self, systemId, action, id, user_id, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_revoke_PIN")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}',action)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["id"] = id
    json_object["user_id"] = user_id
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_revoke_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_revoke_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_revoke_PIN", response.text)

    return response

def DigitalPin_statusTracking_global(self, trackingId, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DigitalPin_statusTracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload: ", payload)

    # Send POST request
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response: ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "DigitalPin_statusTracking",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('DigitalPin_statusTracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "DigitalPin_statusTracking", response.text)

    return response