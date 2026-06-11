import ast
import json
import requests
import time
import jwt
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
import os

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel
from C2CModules.ces_token_generation import JwtService



def IdentifyToken_getOEMUserId(self, firstName, lastName, username, password, tc):
    # Read API test data from Excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getOEMUserId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["userInfo"]["firstName"] = firstName
    json_object["userInfo"]["lastName"] = lastName
    json_object["username"] = username
    json_object["password"] = password
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
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getOEMUserIdp",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet
    save_api_resp_into_file('IdentifyToken_getOEMUserId', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getOEMUserId", response.text)

    return response


def IdentifyToken_getOEMAuthToken(self, username, password, tc):
    # Read API test data from Excel sheet
    data = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getOEMAuthToken")
    base_url = str(data["Base Url"])
    endpoint = str(data["Endpoint"])
    headers = str(data["Headers"]).replace('\n', '')
    payload = str(data["Payload"]).replace('\n', '')

    # Complete URL
    complete_url = str(base_url + endpoint)
    print("Complete URL: ", complete_url)

    # Headers
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    json_object["username"] = username
    json_object["password"] = password
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
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getOEMAuthToken",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")
        

    # Save test result in Excel sheet
    save_api_resp_into_file('IdentifyToken_getOEMAuthToken', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getOEMAuthToken", response.text)

    return response

def IdentifyToken_generateQCId(self, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_generateQCId")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["oemAuthToken"] = oemAuthToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_generateQCId",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_generateQCId', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_generateQCId", response.text)

    return response

def IdentifyToken_getQCId(self, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getQCId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{oemAuthToken}', oemAuthToken)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getQCId",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getQCId', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getQCId", response.text)

    return response
    
def IdentifyToken_enrollUserAuth_PIN(self, authData, authType, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_enrollUserAuth_PIN")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["authData"] = authData
    json_object["authType"] = authType
    json_object["oemAuthToken"] = oemAuthToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_enrollUserAuth_PIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_enrollUserAuth_PIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_enrollUserAuth_PIN", response.text)

    return response
    
def IdentifyToken_enrollUserAuth_Biometrics(self, authImagePathUrl, authType, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_enrollUserAuth_Biometrics")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["authImagePathUrl"] = authImagePathUrl
    json_object["authType"] = authType
    json_object["oemAuthToken"] = oemAuthToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_enrollUserAuth_Biometrics",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_enrollUserAuth_Biometrics', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_enrollUserAuth_Biometrics", response.text)

    return response
    
def IdentifyToken_generateQCId_token(self, appData, authData, authType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_generateQCId_token")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["appData"] = appData
    json_object["authData"] = authData
    json_object["authType"] = authType
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_generateQCId_token",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_generateQCId_token', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_generateQCId_token", response.text)

    return response

def IdentifyToken_bindVehicle_with_user(self, qcToken, vins, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_bindVehicle_with_user")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qcToken"] = qcToken
    json_object["vins"] = vins
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_bindVehicle_with_user",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_bindVehicle_with_user', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_bindVehicle_with_user", response.text)

    return response
    
def IdentifyToken_bindVehicle(self, bindToken, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_bindVehicle")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["bindToken"] = bindToken
    json_object["oemAuthToken"] = oemAuthToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_bindVehicle",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_bindVehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_bindVehicle", response.text)

    return response
    
def IdentifyToken_bindVehicleStatus(self, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_bindVehicleStatus")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{oemAuthToken}', oemAuthToken)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_bindVehicleStatus",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_bindVehicleStatus', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_bindVehicleStatus", response.text)

    return response
    
def IdentifyToken_getOEMUserInfo(self, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getOEMUserInfo")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{oemAuthToken}', oemAuthToken)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getOEMUserInfo",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getOEMUserInfo', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getOEMUserInfo", response.text)

    return response
    
def IdentifyToken_updateOEMUserInfo(self, oemAuthToken, dob, gender, addressLine1, addressLine2, addressLine3, city, state, countryCode,  postCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_updateOEMUserInfo")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{oemAuthToken}', oemAuthToken)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["dob"] = dob
    json_object["gender"] = gender
    json_object["addressLine1"] = addressLine1
    json_object["addressLine2"] = addressLine2
    json_object["addressLine3"] = addressLine3
    json_object["city"] = city
    json_object["state"] = state
    json_object["countryCode"] = countryCode
    json_object["postCode"] = postCode
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_updateOEMUserInfo",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_updateOEMUserInfo', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_updateOEMUserInfo", response.text)

    return response
    
def IdentifyToken_authenticateUser_by_Biometric(self, systemId, authType, authImagePathUrl, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_authenticateUser_by_Biometric")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["authType"] = authType
    json_object["authImagePathUrl"] = authImagePathUrl
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_authenticateUser_by_Biometric",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_authenticateUser_by_Biometric', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_authenticateUser_by_Biometric", response.text)

    return response
    
def IdentifyToken_getQCId_by_Biometric(self, systemId, authType, authImagePathUrl, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getQCId_by_Biometric")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["systemId"] = systemId
    json_object["authType"] = authType
    json_object["authImagePathUrl"] = authImagePathUrl
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getQCId_by_Biometric",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getQCId_by_Biometric', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getQCId_by_Biometric", response.text)

    return response
    
def IdentifyToken_getUserInfo(self, publicKey, qcToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getUserInfo")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["publicKey"] = publicKey
    json_object["qcToken"] = qcToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getUserInfo",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getUserInfo', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getUserInfo", response.text)

    return response
    
def IdentifyToken_verifyQCIdToken(self, qcToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_verifyQCIdToken")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qcToken"] = qcToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_verifyQCIdToken",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_verifyQCIdToken', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_verifyQCIdToken", response.text)

    return response
    
def IdentifyToken_getUserCreationStatus(self, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getUserCreationStatus")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{oemAuthToken}', oemAuthToken)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getUserCreationStatus",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getUserCreationStatus', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getUserCreationStatus", response.text)

    return response
    
def IdentifyToken_tokenService_verifyQCIdToken(self, qcToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_tokenService_verifyQCIdToken")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qcToken"] = qcToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_tokenService_verifyQCIdToken",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_tokenService_verifyQCIdToken', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_tokenService_verifyQCIdToken", response.text)

    return response
    
def IdentifyToken_saveUserPreferences(self, qc_id, subscription1, subscription2, subscription3, subscription4, name, lat, long, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_saveUserPreferences")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qc_id"] = qc_id
    json_object["preferenceData"]["subscriptions"][0] = subscription1
    json_object["preferenceData"]["subscriptions"][1] = subscription2
    json_object["preferenceData"]["subscriptions"][2] = subscription3
    json_object["preferenceData"]["subscriptions"][3] = subscription4
    json_object["preferenceData"]["name"] = name
    json_object["preferenceData"]["home_location"]["lat"] = lat
    json_object["preferenceData"]["home_location"]["long"] = long
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_saveUserPreferences",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_saveUserPreferences', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_saveUserPreferences", response.text)

    return response
    
def IdentifyToken_unbindVehicle(self, bindToken, oemAuthToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_unbindVehicle")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["bindToken"] = bindToken
    json_object["oemAuthToken"] = oemAuthToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_unbindVehicle",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_unbindVehicle', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_unbindVehicle", response.text)

    return response
    
def IdentifyToken_unbindVehicle_by_VIN(self, qcToken, vins, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_unbindVehicle_by_VIN")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qcToken"] = qcToken
    json_object["vins"] = vins
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_unbindVehicle_by_VIN",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_unbindVehicle_by_VIN', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_unbindVehicle_by_VIN", response.text)

    return response
    
def IdentifyToken_resetPassword(self, username, password, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_resetPassword")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["password"] = password
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_resetPassword",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_resetPassword', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_resetPassword", response.text)

    return response
    
def IdentifyToken_deleteUser(self, username, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_deleteUser")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_deleteUser",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_deleteUser', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_deleteUser", response.text)

    return response
    
def IdentifyToken_getAllUsers(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "IdentifyToken_getAllUsers")
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "IdentifyToken_getAllUsers",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('IdentifyToken_getAllUsers', response.text)
    save_api_resp_in_excel(self, "API_Data", "IdentifyToken_getAllUsers", response.text)

    return response

#------------------------------------------------------------------------------------------------------
#----------------------------------------JPM API-------------------------------------------------------
#------------------------------------------------------------------------------------------------------

def JPM_API_debit(self, description, merchantTransactionId, transactionType, paymentToken,  tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "JPM_API_debit")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    jwt_service = JwtService("C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\privateKey.pem",
                             "C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\publicKey.pem",
                             "0c88bc5d-c591-4b07-aaf5-b08da08f29ed")
    token = jwt_service.generate_token()

    print("Generated Token:", token)

    header_x = ast.literal_eval(headers)
    header_x["Authorization"] = f'Bearer {token}'
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["description"] = description
    json_object["merchantTransactionId"] = merchantTransactionId
    json_object["transactionType"] = transactionType
    json_object["paymentToken"] = paymentToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "JPM_API_debit",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('JPM_API_debit', response.text)
    save_api_resp_in_excel(self, "API_Data", "JPM_API_debit", response.text)

    return response
    
def JPM_API_capture(self, description, merchantTransactionId, transactionType, id, amount, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "JPM_API_capture")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    jwt_service = JwtService("C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\privateKey.pem",
                             "C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\publicKey.pem",
                             "0c88bc5d-c591-4b07-aaf5-b08da08f29ed")
    token = jwt_service.generate_token()

    print("Generated Token:", token)

    header_x = ast.literal_eval(headers)
    header_x["Authorization"] = f'Bearer {token}'
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["description"] = description
    json_object["merchantTransactionId"] = merchantTransactionId
    json_object["transactionType"] = transactionType
    json_object["referenceTransaction"]["id"] = id
    json_object["amount"] = amount
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "JPM_API_capture",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('JPM_API_capture', response.text)
    save_api_resp_in_excel(self, "API_Data", "JPM_API_capture", response.text)

    return response
    
def JPM_API_healthCheck(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "JPM_API_healthCheck")
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "JPM_API_healthCheck",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('JPM_API_healthCheck', response.text)
    save_api_resp_in_excel(self, "API_Data", "JPM_API_healthCheck", response.text)

    return response

#------------------------------------------------------------------------------------------
#----------------------------------Payment Service - API-----------------------------------
#------------------------------------------------------------------------------------------

def PaymentService_authorize(self, qcIdToken, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PaymentService_authorize")
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
    header_x["Authorization"] = f'Bearer {token}'
    header_x = header_update(header_x, tc)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["qcIdToken"] = qcIdToken
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "PaymentService_authorize",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PaymentService_authorize', response.text)
    save_api_resp_in_excel(self, "API_Data", "PaymentService_authorize", response.text)

    return response
    
def PaymentService_capture(self, transactionId, total, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PaymentService_capture")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["transactionId"] = transactionId
    json_object["total"] = total
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "PaymentService_capture",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PaymentService_capture', response.text)
    save_api_resp_in_excel(self, "API_Data", "PaymentService_capture", response.text)

    return response
    
def PaymentService_save_chargingSummary(self, sessionId, quantity, rate, amount, cost, tax, currency, merchantName, timestamp, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PaymentService_save_chargingSummary")
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
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["sessionId"] = sessionId
    json_object["quantity"] = quantity
    json_object["rate"] = rate
    json_object["amount"] = amount
    json_object["cost"] = cost
    json_object["tax"] = tax
    json_object["currency"] = currency
    json_object["merchantName"] = merchantName
    json_object["timestamp"] = timestamp
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "PaymentService_save_chargingSummary",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PaymentService_save_chargingSummary', response.text)
    save_api_resp_in_excel(self, "API_Data", "PaymentService_save_chargingSummary", response.text)

    return response
    
def PaymentService_fetch_chargingSummary(self, sessionId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PaymentService_fetch_chargingSummary")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # Url :
    complete_url = str(base_url + endpoint).replace('{sessionId}', sessionId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
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
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "TokenPayment-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "PaymentService_fetch_chargingSummary",
                                                "TokenPayment-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PaymentService_fetch_chargingSummary', response.text)
    save_api_resp_in_excel(self, "API_Data", "PaymentService_fetch_chargingSummary", response.text)

    return response


