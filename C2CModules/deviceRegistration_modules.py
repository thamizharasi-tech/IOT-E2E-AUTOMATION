import ast
import csv
import json
import random
import time

import requests

from C2CModules.api_modules import header_update
from C2CModules.e2e_testData import deviceIdFlag, reqDeviceId_tcu, reqDeviceId_ivi
from C2CModules.resuse_modules import *
from C2CModules.testResults import testResult
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# Registration-DeviceReg - E2E
def registration_DeviceReg(self, deviceType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = base_url + endpoint
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])

    if deviceType == "TCU":
        if deviceIdFlag == "Yes":
            deviceId = reqDeviceId_tcu
        else:
            deviceId = "QA_TEST_TCU_" + random_id
    elif deviceType == "IVI":
        if deviceIdFlag == "Yes":
            deviceId = reqDeviceId_ivi
        else:
            deviceId = "QA_TEST_IVI_" + random_id

    # Payload :
    json_object = json.loads(payload)
    print(json_object)
    json_object[0]['device_type'] = deviceType
    json_object[0]["device_id"] = deviceId
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
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration-DeviceReg", "Registration-RequestToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration-DeviceReg', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration-DeviceReg", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()
    # Validate api response body contents
    assert (response_body["responseCode"] == "1200")
    assert (response_body["responseMessage"] == "SUCCESS")
    reqId = response_body["responseData"]["requestId"]
    print("Request Id :", reqId)
    assert (response_body["responseData"]["status"] == "SUBMITTED")
    assert (response_body["responseData"]["message"] == "Request Submitted for registration!")
    return response_body


# Registration_getCount
def registration_getCount(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration_getCount")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Read reqId from Registration_DeviceReg api resp from Excel sheet
    dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
    api_resp = str(dict1["Actual API Response"])
    # print(api_resp)
    json_object = json.loads(api_resp)
    reqId = json_object["responseData"]["requestId"]
    print("Request Id :", reqId)

    # Url :
    url = base_url + endpoint
    complete_url = url.replace('{requestId}', reqId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)
    time.sleep(90)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken_GETmethod")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getCount",
                                                "Registration-RequestToken_GETmethod")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration_getCount', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration_getCount", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate api response body contents
    assert (response_body["responseData"]["totalCount"] == 1)
    assert (response_body["responseData"]["status"] == "Completed")
    print("Success Count : ", response_body["responseData"]["successCount"])
    print("Failure Count : ", response_body["responseData"]["failCount"])
    if response_body["responseData"]["successCount"] == 1:
        print("successCount is set to :=> ", response_body["responseData"]["successCount"])
        testResult(self, "passed", 'New Device Registration', 'New Device is registered successfully')
        print('\n')
        # assert True
    elif response_body["responseData"]["failCount"] == 1:
        print("failCount is set to :=> ", response_body["responseData"]["failCount"])
        testResult(self, "failed", 'New Device Registration', 'New Device is not registered successfully')
    assert (response_body["responseData"]["failCount"] == 0)
    assert (response_body["responseData"]["message"] == "Successfully generated the registration data.")
    return response_body


# Registration_getDetails
def registration_getDetails(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration_getDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Read reqId from Registration_DeviceReg api resp from Excel sheet
    dict1 = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
    api_resp = str(dict1["Actual API Response"])
    # print(api_resp)
    json_object = json.loads(api_resp)
    reqId = json_object["responseData"]["requestId"]
    print("Request Id :", reqId)

    # Url :
    url = base_url + endpoint
    complete_url = url.replace('{requestId}', reqId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken_GETmethod")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getDetails",
                                                "Registration-RequestToken_GETmethod")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration_getDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration_getDetails", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate api response body contents
    if response_body["responseMessage"] == "SUCCESS" or response_body["responseMessage"] == "Success":
        # print(f"Response Message is SUCCESS")
        assert True
        assert (response_body["responseMessage"] == "Success")
    else:
        print(str(response_body["responseMessage"]))

    device_id = response_body["responseData"][0]["device_id"]
    status = response_body["responseData"][0]["status"]
    url = response_body["responseData"][0]["url"]
    systemId = response_body["responseData"][0]["system_id"]
    deviceType = response_body["responseData"][0]["device_type"]
    certificateDetails = response_body["responseData"][0]["certificateDetails"]["certificate"]
    PrivateKeyDetails = response_body["responseData"][0]["certificateDetails"]["privateKey"]
    return response_body


# Registration-DeviceReg - API for negative test cases
def Registration_DeviceReg_API(self, device_type, device_id, attestationMechanism):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "DeviceRegistration", "Registration-DeviceReg")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = base_url + endpoint
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    random_id = ' '.join([str(random.randint(10, 9999)).zfill(7) for _ in range(1)])

    # Payload :
    json_object = json.loads(payload)
    print(json_object)
    json_object[0]['device_type'] = device_type
    json_object[0]["device_id"] = device_id
    json_object[0]["attestationMechanism"] = attestationMechanism
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    return response


# -------------------
# New Modules for negative testing
# -------------------


# Registration-DeviceReg - API for negative test cases
def deviceRegistration_post(self, device_type, device_id, attestationMechanism, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration-DeviceReg")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = base_url + endpoint
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    print(json_object)
    if tc == "no_deviceType":
        del json_object[0]['device_type']
    else:
        json_object[0]['device_type'] = device_type
    if tc == "no_deviceId":
        del json_object[0]["device_id"]
    else:
        json_object[0]["device_id"] = device_id
    if tc == "no_attestationMechanism":
        del json_object[0]["attestationMechanism"]
    else:
        json_object[0]["attestationMechanism"] = attestationMechanism
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
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration-DeviceReg", "Registration-RequestToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration-DeviceReg', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration-DeviceReg", response.text)

    return response


# Registration_getCount
def deviceRegistration_getCount(self, reqId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration_getCount")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = base_url + endpoint
    if tc == "no_requestId":
        reqId = ""
        complete_url = url.replace('{requestId}', reqId)
    elif tc == "incorrect_requestId":
        reqId = str(reqId).replace("1", "2").replace("b", "a")
        complete_url = url.replace('{requestId}', reqId)
    elif tc == "invalid_requestId":
        l = len(reqId)
        reqId = reqId[:l - 2]
        complete_url = url.replace('{requestId}', reqId)
    else:
        complete_url = url.replace('{requestId}', reqId)

    print("Request Id :", reqId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)
    time.sleep(90)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken_GETmethod")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getCount",
                                                "Registration-RequestToken_GETmethod")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration_getCount', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration_getCount", response.text)

    return response


# Registration_getDetails
def deviceRegistration_getDetails(self, reqId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Registration_getDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    url = base_url + endpoint
    if tc == "no_requestId":
        reqId = ""
        complete_url = url.replace('{requestId}', reqId)
    elif tc == "incorrect_requestId":
        reqId = str(reqId).replace("1", "2").replace("b", "a")
        complete_url = url.replace('{requestId}', reqId)
    elif tc == "invalid_requestId":
        l = len(reqId)
        reqId = reqId[:l - 2]
        complete_url = url.replace('{requestId}', reqId)
    else:
        complete_url = url.replace('{requestId}', reqId)

    print("Request Id :", reqId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Registration-RequestToken_GETmethod")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getDetails",
                                                "Registration-RequestToken_GETmethod")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Registration_getDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "Registration_getDetails", response.text)

    return response


#--------------------------------------------------------------------------------------------------------------
#------------------------------------------RE Reusable Modules-------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


#device rehoming

def deviceRehoming(self, systemId, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Device_rehoming")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Device_rehoming")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Device_rehoming",
                                                "Device_rehoming")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Device_rehoming', response.text)
    save_api_resp_in_excel(self, "API_Data", "Device_rehoming", response.text)

    return response

def deviceRehoming_status(self, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Device_rehoming_status")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Device_rehoming_status")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "Device_rehoming_status",
                                                "Device_rehoming_status")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Device_rehoming_status', response.text)
    save_api_resp_in_excel(self, "API_Data", "Device_rehoming_status", response.text)

    return response

def supplier_feed(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DeviceRegistration_supplier_feed_API")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    files = [
        ('file', ('supplier_feed.csv', open(r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files/supplier_feed.csv', 'rb'), 'text/csv'))
    ]

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.request("POST", complete_url, headers=header_x, data=payload, files=files)
    print("API response :", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DeviceRegistration_supplier_feed_API', response.text)
    save_api_resp_in_excel(self, "API_Data", "DeviceRegistration_supplier_feed_API", response.text)

    return response

def EOL_deviceReplacement(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "EOL_Device_Replacement")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "EOL_Device_Replacement")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "EOL_Device_Replacement",
                                                "EOL_Device_Replacement")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('EOL_Device_Replacement', response.text)
    save_api_resp_in_excel(self, "API_Data", "EOL_Device_Replacement", response.text)

    return response

def EOL_deviceRevoke(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "EOL_Device_Revoke")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "EOL_Device_Revoke")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "EOL_Device_Revoke",
                                                "EOL_Device_Revoke")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('EOL_Device_Revoke', response.text)
    save_api_resp_in_excel(self, "API_Data", "EOL_Device_Revoke", response.text)

    return response

def supplier_feed_status(self, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "DeviceRegistration_supplier_feed_status_tracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["tracking_id"][0] = trackingId
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('DeviceRegistration_supplier_feed_status_tracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "DeviceRegistration_supplier_feed_status_tracking", response.text)

    return response

# Write data to the CSV file dynamically
def write_to_csv(self, imei, iccid):
    # Define the file path
    file_path = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\bootstrap_files\supplier_feed.csv"

    rows = []

    # Read the original file and update only specific columns
    with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        # Copy header
        headers = reader.fieldnames

        for row in reader:
            # Dynamically generate new imei and iccid
            row["device_imei"] = imei
            row["iccid"] = iccid
            rows.append(row)  # Append the updated row

    # Write the updated rows to a new file
    with open(file_path, mode="w", newline="", encoding="utf-8") as updated_csv_file:
        writer = csv.DictWriter(updated_csv_file, fieldnames=headers)

        # Write header
        writer.writeheader()

        # Write updated rows
        writer.writerows(rows)

    print(f"IMEI and ICCID saved to {file_path}")

def supplier_feed_for_mno(self):

    print("\n------------------------------START------------------------------\n")

    """

    This test is validating the Supplier Feed functionality. (positive scenario)

    :return: return test status

    Validate Supplier Feed

    """
    #print("=========GENERATE AND UPDATE IMEI AND ICCID IN CSV========")
    #imei = "IMEI" + str(random.randint(1, 1000))
    #iccid = "ICCID" + str(random.randint(1, 1000))

    #print("IMEI: ", imei)
    #print("ICCID: ", iccid)

    #write_to_csv(self, imei, iccid)

    print("\n------------------SUPPLIER FEED------------------\n")

    response = supplier_feed(self, "valid")

    # Parse API response into JSON

    response_body = response.json()

    # Validate response status code

    if response.status_code == 200:

        # Validate response body

        if response_body["message"] == "Supplier feed Saved Successfully":
            if response_body["supplierFeed"][0]["iccid"]:
                if response_body["supplierFeed"][0]["mnoStatus"] == "Success":
                    trackingId = response_body["supplierFeed"][0]["trackingId"]
                    testResult(self, "passed",

                               "Validate that Supplier feed saved successfully",
                               "Supplier feed saved successfully, pls refer api response for detailed info")
                else:
                    print("Response message is expected but trackingId is not in response body")
                    assert True
            else:
                print("Response message is expected but trackingId is not in response body")
                assert True

        else:

            testResult(self, "failed",

                   "Validate that Supplier feed is saved successfully",

                   "Supplier feed is not saved, pls refer api response for detailed info")

    elif response.status_code == 400:

        # Validate response body

        if response_body["errors"][0]["message"] == "device imei is already exits":

            testResult(self, "passed",

                   "Validate that Supplier feed is saved or already exists in DB",

                   "Supplier feed is already exits, pls refer api response for detailed info")

        else:

            testResult(self, "failed",

                   "Validate that Supplier feed is saved successfully",

                   "Supplier feed is not saved or does not exits, pls refer api response for detailed info")

    else:

        testResult(self, "failed",

               "Validate that Supplier feed is saved successfully",

               "Supplier data is not saved, pls refer api response for detailed info")

    # verify supplier feed status on the cloud side
    response = supplier_feed_status(self, trackingId, "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # Parse API response into JSON
    response_body = response.json()
    # Validate response body
    if response_body["message"] == "Data fetched successfully":
        if response_body["supplierFeed"][0]["mnoStatus"] == "Success" and response_body["supplierFeed"][0]["iccid"]:
            trackingId_actual = response_body["supplierFeed"][0]["trackingId"]
            if trackingId == trackingId_actual:
                testResult(self, "passed", "Supplier Feed data should be saved successfully",
                           "Supplier Feed data saved successfully")
            # self.result.set_result(TestResults.passed)
    elif response_body["message"] != "Data fetched successfully":
        # print(response_body["responseData"]["message"])
        testResult(self, "failed", "Supplier Feed data should be saved successfully",
                   "Supplier Feed data failed to save" + " Reason for failure is : " +
                   response_body["message"])
        # self.result.set_result(TestResults.failed)
    else:
        print("Something went wrong. Please check the api response for more info", response_body)
        # self.result.set_result(TestResults.failed)
        assert False

def EOL_Pre_Provisioning_API(self, vin, mcu, bin, vcu, model, region, country, modelDescription, plant, assemblyLine, shift, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "EOL_Pre_Provisioning_API")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Read payload from the text file
    json_object = json.loads(payload)
    json_object[0]["vin"] = vin
    json_object[0]["mcu"] = mcu
    json_object[0]["bin"] = bin
    json_object[0]["vcu"] = vcu
    json_object[0]["model"] = model
    json_object[0]["region"] = region
    json_object[0]["country"] = country
    json_object[0]["modelDescription"] = modelDescription
    json_object[0]["plant"] = plant
    json_object[0]["assemblyLine"] = assemblyLine
    json_object[0]["shift"] = shift
    json_object[0]["modelCode"] = modelCode
    payload = json_object

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('EOL_Pre_Provisioning_API', response.text)
    save_api_resp_in_excel(self, "API_Data", "EOL_Pre_Provisioning_API", response.text)

    return response

def EOL_Activation_API(self, systemId, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "EOL_Activation_API")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header:
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    # print(payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('EOL_Activation_API', response.text)
    save_api_resp_in_excel(self, "API_Data", "EOL_Activation_API", response.text)

    return response



