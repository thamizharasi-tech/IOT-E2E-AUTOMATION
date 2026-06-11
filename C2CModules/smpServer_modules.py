import ast
import json
import requests

from C2CModules.e2e_testData import deviceType_TCU, deviceType_VT, deviceType_IVI
from C2CModules.resuse_modules import *
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# SMP Server/UI - getVINdetails
def smpServer_getVINdetails(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GetVINdetails")
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

    # Payload :
    json_object = json.loads(payload)
    # print(json_object)
    json_object["vin"][0] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GetVINdetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GetVINdetails", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# SMP Server/UI - getSKUupdateList
def smpServer_getSKUupdateList(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GetSKUupdateList")
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

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GetSKUupdateList', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GetSKUupdateList", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - getFeatureUpdateList
def smpServer_getFeatureUpdateList(self):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GetFeatureUpdateList")
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

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GetFeatureUpdateList', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GetFeatureUpdateList", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - VinGetuPvChipsetSpIdlist
def smpServer_VinGetuPvChipsetSpIdlist(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_VinGetuPvChipsetSpIdlist")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["systemsVinRequest"]["vin"] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_VinGetuPvChipsetSpIdlist', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_VinGetuPvChipsetSpIdlist", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - VinGetSKUIdlist
def smpServer_VinGetSKUIdlist(self, pvChipsetSpId, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_VinGetSKUIdlist")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["skuByPvChSpAndVinRequest"]["pvChipsetSpId"] = pvChipsetSpId
    json_object["skuByPvChSpAndVinRequest"]["vin"] = vin
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_VinGetSKUIdlist', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_VinGetSKUIdlist", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - VinUpdateSKU
def smpServer_VinUpdateSKU(self, pvChipsetSpId, vin, skuId, deviceType):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_VinUpdateSKU")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["vinSkuRequest"]["pvChipsetSpId"] = pvChipsetSpId
    json_object["vinSkuRequest"]["vin"] = vin
    json_object["vinSkuRequest"]["skuId"] = skuId
    json_object["vinSkuRequest"]["system"] = deviceType
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_VinUpdateSKU', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_VinUpdateSKU", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - createGroup
def smpServer_createGroup(self, name, vinNo):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_CreateGroup")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["groupRequest"]["group"]["groupName"] = name
    json_object["groupRequest"]["group"]["criteria"][0]["criteriaValues"][0] = vinNo
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_CreateGroup', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_CreateGroup", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - GrpGetuPvChipsetSpIdlist
def smpServer_GrpGetuPvChipsetSpIdlist(self, groupId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GrpGetuPvChipsetSpIdlist")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["request"]["groupId"] = groupId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GrpGetuPvChipsetSpIdlist', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GrpGetuPvChipsetSpIdlist", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - GrpGetSKUIdlist
def smpServer_GrpGetSKUIdlist(self, pvChipsetSpId, groupId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GrpGetSKUIdlist")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["request"]["pvChipsetSpId"] = pvChipsetSpId
    json_object["request"]["groupId"] = groupId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GrpGetSKUIdlist', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GrpGetSKUIdlist", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - GrpUpdateSKU
def smpServer_GrpUpdateSKU(self, deviceType, pvChipsetSpId, skuId, groupId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GrpUpdateSKU")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["skuRequest"]["vehicleGroupId"] = groupId
    json_object["skuRequest"]["system"] = deviceType
    json_object["skuRequest"]["pvChipsetSpId"] = pvChipsetSpId
    json_object["skuRequest"]["skuId"] = skuId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GrpUpdateSKU', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GrpUpdateSKU", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - GetFilterValuesbyGroup
def smpServer_GetFilterValuesbyGroup(self, groupId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GetFilterValuesbyGroup")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["request"]["groupId"] = groupId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GetFilterValuesbyGroup', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GetFilterValuesbyGroup", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body


# SMP Server/UI - GetFeaturesforselectedFilters
def smpServer_GetFeaturesforselectedFilters(self, pvChipsetSpId, groupId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_GetFeaturesforselectedFilters")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["request"]["groupId"] = groupId
    json_object["request"]["pvChipsetSpId"] = pvChipsetSpId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_GetFeaturesforselectedFilters', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_GetFeaturesforselectedFilters", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body

# SMP Server/UI - SendUpdateFeatureRequest
def smpServer_SendUpdateFeatureRequest(self, groupId,newGroupName,pvChipsetSpId,deviceType, pvChipset,pvChipsetsp,featureID,featureName,isBundle,device,action):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SMP_SendUpdateFeatureRequest")
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

    # Payload :
    json_object = json.loads(payload)
    json_object["featureRequest"]["group"]["groupId"] = groupId
    json_object["featureRequest"]["group"]["groupName"] = newGroupName
    json_object["featureRequest"]["group"]["associatedDeviceNo"] = "1"

    if device == deviceType_TCU or device == deviceType_VT:
        json_object["featureRequest"]["pvChipsetSpId"] = pvChipsetSpId
        json_object["featureRequest"]["system"] = deviceType
        json_object["featureRequest"]["chipset"] = pvChipset
        json_object["featureRequest"]["sp"] = pvChipsetsp
        json_object["featureRequest"]["updateFeatures"][0]["featureId"] = featureID
        json_object["featureRequest"]["updateFeatures"][0]["featureName"] = featureName
        json_object["featureRequest"]["updateFeatures"][0]["isBundle"] = isBundle
        json_object["featureRequest"]["updateFeatures"][0]["action"] = action

    elif device == deviceType_IVI:
        try:
            json_object["featureRequest"]["pvChipsetSpId"] = pvChipsetSpId
            json_object["featureRequest"]["system"] = deviceType_IVI
            json_object["featureRequest"]["chipset"] = pvChipset
            json_object["featureRequest"]["sp"] = pvChipsetsp
            json_object["featureRequest"]["updateFeatures"][0]["featureId"] = featureID
            json_object["featureRequest"]["updateFeatures"][0]["featureName"] = featureName
            json_object["featureRequest"]["updateFeatures"][0]["isBundle"] = isBundle
            json_object["featureRequest"]["updateFeatures"][0]["action"] = action
            json_object["featureRequest"]["updateFeatures"][0]["description"] = "description"
        except:
            json_object["featureRequest"]["pvChipsetSpId"] = pvChipsetSpId
            json_object["featureRequest"]["system"] = deviceType_IVI
            json_object["featureRequest"]["chipset"] = pvChipset
            json_object["featureRequest"]["sp"] = pvChipsetsp
            json_object["featureRequest"]["updateFeatures"][1]["featureId"] = featureID
            json_object["featureRequest"]["updateFeatures"][1]["featureName"] = featureName
            json_object["featureRequest"]["updateFeatures"][1]["isBundle"] = isBundle
            json_object["featureRequest"]["updateFeatures"][1]["action"] = action

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SMP_SendUpdateFeatureRequest', response.text)
    save_api_resp_in_excel(self, "API_Data", "SMP_SendUpdateFeatureRequest", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body

# licensecleanup
def license_cleanup(self, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LicenseCleanup")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{vinNo}',vin)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LicenseCleanup', response.text)
    save_api_resp_in_excel(self, "API_Data", "LicenseCleanup", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse HTTP response body to json format
    response_body = response.json()

    return response_body
