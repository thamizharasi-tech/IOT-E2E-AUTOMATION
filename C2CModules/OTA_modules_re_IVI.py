import ast
import json
import os
import subprocess
import time

import requests

from C2CModules.e2e_testData import C2CtestReport_otaPath, b2c_batchPath, b2c_ivi_adbSerialNo
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel

ota_beforeOTA_path = os.path.join(C2CtestReport_otaPath, r'beforeOTA')
ota_afterOTA_path = os.path.join(C2CtestReport_otaPath, r'afterOTA')
fota_packageId_file = "fota_packageId.txt"


# -----------------------
# FOTA API Modules:
# -----------------------

# FOTA-get_vehicle_ecus:

def ota_get_vehicle_ecus(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_vehicle_ecus")
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_vehicle_ecus', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_vehicle_ecus", response.text)

    return response


# FOTA-generate_presigned_url:

def ota_generate_presigned_url(self, model, packageName, fileName, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_generate_presigned_url")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).replace('{packageName}', packageName).replace(
        '{fileName}', fileName).replace('{action}', action)
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_generate_presigned_url', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_generate_presigned_url", response.text)

    return response


# FOTA-create_package:

def ota_create_package(self, packageName, model, ecuName, packageType, sourceVersion, targetVersion, fileName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_create_package")
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
    json_object["model"] = model
    json_object["packageName"] = packageName
    json_object["fileName"] = fileName
    json_object["ecuName"] = ecuName
    json_object["packageType"] = packageType
    json_object["sourceVersion"] = sourceVersion
    json_object["targetVersion"] = targetVersion
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_create_package', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_create_package", response.text)

    return response


# FOTA-get_package_info_by_packageId:

def ota_get_package_info_by_packageId(self, packageId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_package_info_by_packageId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{packageId}', packageId)
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_package_info_by_packageId', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_package_info_by_packageId", response.text)

    return response


# FOTA-get_package_info_by_model:

def ota_get_package_info_by_model(self, model, ecuName, pageNumber, pageSize, sort, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_package_info_by_model")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model).replace('{ecuName}', ecuName).replace(
        '{pageNumber}', pageNumber).replace('{pageSize}', pageSize).replace('{sort}', sort)
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_package_info_by_model', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_package_info_by_model", response.text)

    return response


# FOTA-create_campaign:

def ota_create_campaign(self, name, model, packageId, type, startDate, endDate, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_create_campaign")
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

    # test data
    precondition = [
        {
            "key": "batteryMin",
            "value": "15.0"
        },
        {
            "key": "batteryMax",
            "value": "100.0"
        }
    ]
    releaseNotes = [
        {
            "title": "HU",
            "briefDescription": "HU 7 upgrade",
            "description": "New upgrade",
            "language": "en-US"
        }
    ]
    steps = [
        {
            "packageId": packageId,
            "sequentialUpdatesRequired": "true",
            "rollbackRequired": "true",
            "signRequired": "true",
            "encryptionRequired": "true",
            "consent": {
                "download": "false",
                "install": "false",
                "reboot": "false"
            }
        }
    ]

    vehicleProperties = {
        "systemIds": [systemId]
    }

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["name"] = name
    json_object["type"] = type
    json_object["startDate"] = startDate
    json_object["endDate"] = endDate

    json_object["precondition"] = precondition
    json_object["releaseNotes"] = releaseNotes
    json_object["steps"] = steps
    json_object["vehicleProperties"] = vehicleProperties

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_create_campaign', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_create_campaign", response.text)

    return response


# FOTA-update_campaign:

def ota_update_campaign(self, campaignId, name, model, packageId, type, startDate, endDate, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_update_campaign")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # test data
    precondition = [
        {
            "key": "batteryMin",
            "value": "15.0"
        },
        {
            "key": "batteryMax",
            "value": "100.0"
        }
    ]
    releaseNotes = [
        {
            "title": "HU",
            "briefDescription": "HU 7 upgrade",
            "description": "New upgrade",
            "language": "en-US"
        }
    ]
    steps = [
        {
            "packageId": packageId,
            "sequentialUpdatesRequired": "true",
            "rollbackRequired": "true",
            "signRequired": "true",
            "encryptionRequired": "true",
            "consent": {
                "download": "false",
                "install": "false",
                "reboot": "false"
            }
        }
    ]

    vehicleProperties = {
        "systemIds": [systemId]
    }

    # Payload :
    json_object = json.loads(payload)
    json_object["campaignId"] = campaignId
    json_object["model"] = model
    json_object["name"] = name
    json_object["type"] = type
    json_object["startDate"] = startDate
    json_object["endDate"] = endDate

    json_object["precondition"] = precondition
    json_object["releaseNotes"] = releaseNotes
    json_object["steps"] = steps
    json_object["vehicleProperties"] = vehicleProperties

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_update_campaign', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_update_campaign", response.text)

    return response


# FOTA-updating_campaign_status(action-approve):

def ota_updating_campaign_status(self, campaignId, action, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_update_campaign_status")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{campaignId}', campaignId).replace('{action}', action)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_update_campaign_status', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_update_campaign_status", response.text)

    return response


# FOTA-get_campaign_info:

def ota_get_campaign_info(self, campaignId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_campaign_info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{campaignId}', campaignId)
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_campaign_info', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_campaign_info", response.text)

    return response


# FOTA-ota_get_all_campaign_info:

def ota_get_all_campaign_info(self, pageNumber, pageSize, sort, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_all_campaign_info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{pageNumber}', str(pageNumber)).replace('{pageSize}',
                                                                                             str(pageSize)).replace(
        '{sort}', sort)
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_all_campaign_info', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_all_campaign_info", response.text)

    return response


# FOTA-trigger_campaign:

def ota_trigger_campaign(self, campaignId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_trigger_campaign")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{campaignId}', str(campaignId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_trigger_campaign', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_trigger_campaign", response.text)

    return response


# FOTA-blacklists_vehicles:

def ota_blacklists_vehicles(self, systemId, reason, date, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_blacklists_vehicles")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["reason"] = reason
    json_object["date"] = date
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_blacklists_vehicles', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_blacklists_vehicles", response.text)

    return response


# FOTA-get_blacklists_vehicles:

def ota_get_blacklists_vehicles(self, systemId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_blacklists_vehicles")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('{status}', str(status))
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_blacklists_vehicles', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_blacklists_vehicles", response.text)

    return response


# FOTA-revoke_blacklists_vehicles:

def ota_revoke_blacklists_vehicles(self, systemId, reason, date, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_revoke_blacklists_vehicles")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["reason"] = reason
    json_object["date"] = date
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_revoke_blacklists_vehicles', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_revoke_blacklists_vehicles", response.text)

    return response


# FOTA-get_campaign_consent_info:

def ota_get_campaign_consent_info(self, systemId, campaignId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_campaign_consent_info")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', str(systemId)).replace('{campaignId}',
                                                                                         str(campaignId))
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_campaign_consent_info', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_campaign_consent_info", response.text)

    return response


# FOTA-get_campaign_status:

def ota_get_campaign_vehicle_status(self, campaignId, pageNumber, pageSize, sort, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_get_campaign_vehicle_status")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{campaignId}', str(campaignId)).replace('{pageNumber}',
                                                                                             str(pageNumber)).replace(
        '{pageSize}', str(pageSize)).replace('{sort}', str(sort))
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

    # Save test result in Excel sheet @ desired cell
    save_api_resp_into_file('ota_get_campaign_vehicle_status', response.text)
    save_api_resp_in_excel(self, "API_Data", "ota_get_campaign_vehicle_status", response.text)

    return response


# FOTA-package_upload:

def ota_package_upload(self, presigned_url, file, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "ota_package_upload")
    headers = str(dict["Headers"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(presigned_url).replace(" ", "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = response = requests.put(complete_url, headers=header_x, data=open(file, 'rb').read())
    print("API response status code : ", response.status_code)

    return response


# -----------------------
# FOTA Modules:
# -----------------------

def read_ecu_details_of_vehicle(self, systemId, attribute):
    response = ota_get_vehicle_ecus(self, systemId, "valid")

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    if message == "Success":
        if attribute == "model":
            value = response_body["vehicle"]["model"]
        elif attribute == "state":
            value = response_body["vehicle"]["state"]
    else:
        print("Incorrect message")
        value = ''
        assert False
    return value


def create_package(self, packageName, model, ecuName, packageType, sourceVersion, targetVersion, fileName, file, tc):
    # generate pre-signed url for package upload
    response = ota_generate_presigned_url(self, model, packageName, fileName, "UPLOAD", tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    if message == "Success":
        presignedUrl = response_body["presignedUrlInfo"]["presignedUrl"]
    else:
        print("Incorrect message")
        presignedUrl = ''
        assert False

    # upload package
    print("File : ", file)
    response = ota_package_upload(self, presignedUrl, file, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    time.sleep(15)
    # create package
    response = ota_create_package(self, packageName, model, ecuName, packageType, sourceVersion, targetVersion,
                                  fileName, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    if message == "Success":
        packageId = response_body["packageInfo"]["packageId"]
    else:
        print("Incorrect message")
        packageId = ''
        assert False

    packageId_file = os.path.join(ota_beforeOTA_path, fota_packageId_file)
    print("packageId_file : ", packageId_file)

    text_file = open(packageId_file, "w+")
    text_file.write(str(packageId))
    text_file.close()

    return packageId


def verify_uploaded_package_details(self, packageId, packageName, model, ecuName, packageType, sourceVersion,
                                    targetVersion, fileName, tc):
    #  get package info by packageId
    response = ota_get_package_info_by_packageId(self, packageId, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    datalen = len(response_body["packages"])
    if datalen >= 1:
        for i in range(datalen):
            if message == "Success":
                packageId_actual = response_body["packages"][i]["packageId"]
                packageName_actual = response_body["packages"][i]["packageName"]
                fileName_actual = response_body["packages"][i]["fileName"]
                model_actual = response_body["packages"][i]["model"]
                ecuName_actual = response_body["packages"][i]["ecuName"]
                packageType_actual = response_body["packages"][i]["packageType"]
                targetVersion_actual = response_body["packages"][i]["targetVersion"]
                sourceVersion_actual = response_body["packages"][i]["sourceVersion"]

                if int(packageId_actual) == int(packageId):
                    break
    else:
        print("Package list is empty")
        assert False

    if packageName_actual == packageName and fileName_actual == fileName and model_actual == model and ecuName_actual == ecuName and packageType_actual == packageType and sourceVersion_actual == sourceVersion and targetVersion_actual == targetVersion:
        print("Details are same as that of configured during package creation")
        assert True
    else:
        print("Mismatch in details or package id does not exists/listed. pls check api response")
        print("packageId_actual : ", packageId_actual)
        print("packageName_actual : ", packageName_actual)
        print("fileName_actual : ", fileName_actual)
        print("model_actual : ", model_actual)
        print("ecuName_actual : ", ecuName_actual)
        print("packageType_actual : ", packageType_actual)
        print("sourceVersion_actual : ", sourceVersion_actual)
        print("targetVersion_actual : ", targetVersion_actual)
        assert False


def read_pacakgeId_from_file(self):
    packageId_file = os.path.join(ota_beforeOTA_path, fota_packageId_file)
    print("packageId_file : ", packageId_file)

    text_file = open(packageId_file, "r")
    packageId = text_file.read()
    text_file.close()
    return packageId


# create campaign for uploaded package
def create_campaign(self, name, model, packageId, type, startDate, endDate, systemId, tc):
    # call create campaign api module
    response = ota_create_campaign(self, name, model, packageId, type, startDate, endDate, systemId, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    if message == "Success":
        campaignId = response_body["campaign"]["campaignId"]
    else:
        print("Incorrect message")
        campaignId = ''
        assert False
    return campaignId


def verify_campaign_details(self, campaignId, packageId, name, model, type1, startDate, endDate, systemId,
                            campaignStatus, tc):
    #  get campaign info by campaignId
    response = ota_get_campaign_info(self, campaignId, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]

    if message == "Success":
        campaignId_actual = response_body["campaign"]["campaignId"]
        type_actual = response_body["campaign"]["type"]
        startDate_actual = response_body["campaign"]["startDate"]
        endDate_actual = response_body["campaign"]["endDate"]
        model_actual = response_body["campaign"]["model"]
        systemId_actual = response_body["campaign"]["vehicleProperties"]["systemIds"][0]
        campaignStatus_actual = response_body["campaign"]["campaignStatus"]
        name_actual = response_body["campaign"]["name"]
        packageId_actual = response_body["campaign"]["steps"][0]["package"]["packageId"]
        packageName_actual = response_body["campaign"]["steps"][0]["package"]["packageName"]
        fileName_actual = response_body["campaign"]["steps"][0]["package"]["fileName"]
        packageType_actual = response_body["campaign"]["steps"][0]["package"]["packageType"]
        sourceVersion_actual = response_body["campaign"]["steps"][0]["package"]["sourceVersion"]
        targetVersion_actual = response_body["campaign"]["steps"][0]["package"]["targetVersion"]

    else:
        print("Package list is empty")
        assert False

    if int(packageId_actual) == int(
            packageId) and campaignId_actual == campaignId and name_actual == name and model_actual == model and type_actual == type1 and int(
        startDate_actual) == int(startDate) and int(endDate_actual) == int(endDate) and str(systemId_actual) == str(
        systemId):
        print("Details are same as that of configured during package creation")
        if campaignStatus_actual == campaignStatus:
            print("Campaign Status is : " + campaignStatus_actual)
        assert True
    else:
        print("Mismatch in details. pls check api response")
        print("campaignId_actual : ", campaignId_actual)
        print("campaignStatus_actual : ", campaignStatus_actual)
        print("name_actual : ", name_actual)
        print("model_actual : ", model_actual)
        print("type_actual : ", type_actual)
        print("startDate_actual : ", startDate_actual)
        print("endDate_actual : ", endDate_actual)
        print("systemId_actual : ", systemId_actual)
        print("packageId_actual : ", packageId_actual)
        print("packageName_actual : ", packageName_actual)
        print("fileName_actual : ", fileName_actual)
        print("packageType_actual : ", packageType_actual)
        print("sourceVersion_actual : ", sourceVersion_actual)
        print("targetVersion_actual : ", targetVersion_actual)
        assert False


# Approve Campaign
def approve_campaign(self, campaignId, action, tc):
    #  call api module
    response = ota_updating_campaign_status(self, campaignId, action, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]

    if message == "Success":
        print("Campaign is approved successfully")
    else:
        print("Failed to approve campaign")
        assert False


def verify_campaign_vehicle_status(self, systemId, campaignId, pageNumber, pageSize, sort, tc):
    #  get campaign status for vehicle
    response = ota_get_campaign_vehicle_status(self, campaignId, pageNumber, pageSize, sort, tc)

    # Validate response status code
    if response.status_code == 200:
        assert True
    else:
        print("Status code is not 200. Rather found : " + str(response.status_code))
        assert False

    # Parse API response into JSON
    response_body = response.json()

    # Read pre-signed url from api response body
    message = response_body["message"]
    datalen = len(response_body["campaignVehicleStatus"])
    if datalen >= 1:
        for i in range(datalen):
            if message == "Success":
                systemId_actual = response_body["campaignVehicleStatus"][i]["systemId"]
                batchId_actual = response_body["campaignVehicleStatus"][i]["batchId"]
                status_actual = response_body["campaignVehicleStatus"][i]["status"]
                lastUpdatedTime_actual = response_body["campaignVehicleStatus"][i]["lastUpdatedTime"]
                if int(systemId_actual) == int(systemId):
                    break
        print("systemId_actual : ", systemId_actual)
        print("batchId_actual : ", batchId_actual)
        print("status_actual : ", status_actual)
        print("lastUpdatedTime_actual : ", lastUpdatedTime_actual)
    else:
        print("Campaign Vehicle list is empty")
        assert False
    return status_actual


def verify_device_cloud_status(self, option, systemId, campaignId, tc):
    print("=======================================================================================================")

    if option == "beforeFOTAupdate":
        try:
            # get firmware Version
            firmwareVer_beforeFOTA = subprocess.call(
                [b2c_batchPath + 'C2C_OTACommands.bat',
                 b2c_ivi_adbSerialNo, "FOTA_before"], timeout=60)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('\n')

    if option == "afterFOTAupdate":

        print('-------------------------------------------------')
        print("Cloud Side Final E2E Validation Results :            ")
        print('-------------------------------------------------')
        # print('\n')

        for i in range(30):
            status = verify_campaign_vehicle_status(self, systemId, campaignId, "0", "10", "updatedTime%2Cdesc",
                                                    "valid")
            if status == "SUCCESS":
                testResult(self, "passed", "Campaign vehicle status for desired systemId should be 'SUCCESS'",
                           "Campaign vehicle status for desired systemId is " + status + " ")
                break
            else:
                time.sleep(120)

        print("=======================================================================================================")

        try:
            # get firmware Version
            firmwareVer_afterFOTA = subprocess.call(
                [b2c_batchPath + 'C2C_OTACommands.bat',
                 b2c_ivi_adbSerialNo, "FOTA_after"], timeout=60)
            time.sleep(5)
        except subprocess.TimeoutExpired:
            print('\n')

        # Meta build Version
        with open(os.path.join(ota_beforeOTA_path, r'ver_info.txt'),
                  "r") as file:
            json_data = json.load(file)
            Meta_Build_ID_beforeFOTAupdate = json_data['Metabuild_Info']['Meta_Build_ID']
            Version_beforeFOTAupdate_ver = json_data['Version']

        with open(os.path.join(ota_afterOTA_path, r'ver_info.txt'),
                  "r") as file:
            json_data = json.load(file)
            Meta_Build_ID_afterFOTAupdate = json_data['Metabuild_Info']['Meta_Build_ID']
            Version_afterFOTAupdate_ver = json_data['Version']

        # Device Slot
        currentSlot_beforeFOTAupdate = \
            open(os.path.join(ota_beforeOTA_path, r'currentSlot.txt'),
                 "r").read()

        currentSlot_afterFOTAupdate = \
            open(os.path.join(ota_afterOTA_path, r'currentSlot.txt'),
                 "r").read()

        # Device Unix name
        uname_beforeFOTAupdate = \
            open(os.path.join(ota_beforeOTA_path, r'uname-a.txt'),
                 "r").read()

        uname_afterFOTAupdate = \
            open(os.path.join(ota_beforeOTA_path, r'uname-a.txt'),
                 "r").read()

        print("=======================================================================================================")
        print('-------------------------------------------------')
        print("Device Side Details Before & After FOTA Update : ")
        print('-------------------------------------------------')
        # print('\n')
        print("BEFORE FOTA UPDATE : ")
        print('---------------------')
        print("Firmware - Meta build ID before FOTA update : ", Meta_Build_ID_beforeFOTAupdate)
        print("Firmware - Version before FOTA update : ", Version_beforeFOTAupdate_ver)
        print("Firmware - details before FOTA update : ", uname_beforeFOTAupdate)
        print("Current Slot before FOTA update : ", currentSlot_beforeFOTAupdate)
        # print('\n')
        print('---------------------')
        print("AFTER FOTA UPDATE :  ")
        print('---------------------')
        print("Firmware - Meta build ID after FOTA update : ", Meta_Build_ID_afterFOTAupdate)
        print("Firmware - Version before FOTA update : ", Version_afterFOTAupdate_ver)
        print("Firmware - details after FOTA update : ", uname_afterFOTAupdate)
        print("Current Slot after FOTA update : ", currentSlot_afterFOTAupdate)

        print('---------------------------------------')
        print("Device Side Final E2E Validation Results : ")
        print('---------------------------------------')

        if Meta_Build_ID_beforeFOTAupdate != Meta_Build_ID_afterFOTAupdate or Version_beforeFOTAupdate_ver != Version_afterFOTAupdate_ver or uname_beforeFOTAupdate != uname_afterFOTAupdate:
            testResult(self, "passed", "Firmware Metabuild Id/Version/details should be updated successfully on device",
                       "Firmware Metabuild Id/Version/details is updated successfully on device")
        else:
            testResult(self, "verificationFailed",
                       "Firmware Metabuild/Version/details should be updated successfully on device",
                       "Firmware Metabuild Id/Version/details is same.")

        if currentSlot_beforeFOTAupdate != currentSlot_afterFOTAupdate:
            testResult(self, "passed", "Current slot should be updated successfully on device",
                       "Current slot is updated successfully on device")
        else:
            testResult(self, "verificationFailed", "Current slot should be updated successfully on device",
                       "Current slot is not updated on device")

        print("=======================================================================================================")
        if status == "SUCCESS" and currentSlot_beforeFOTAupdate != currentSlot_afterFOTAupdate:
            testResult(self, "passed", "OTA should be successful",
                       "OTA is success ")
        else:
            testResult(self, "failed", "OTA should be successful",
                       "OTA failed")
    print("=======================================================================================================")