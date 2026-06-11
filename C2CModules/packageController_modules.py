import ast
import json
import time
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# -------------------
# API Modules
# -------------------

# PackageController_PackageUpgrade : API operation to save a vehicle to package assignment
def packageController_packageUpgrade(self, systemId, vin, packageId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageUpgrade")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_packageId":
        del json_object["packageId"]
    else:
        json_object["packageId"] = packageId
    if tc == "no_vin":
        del json_object["vin"]
    else:
        json_object["vin"] = vin
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
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageUpgrade",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageUpgrade', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageUpgrade", response.text)

    return response


# PackageController_PackageAssignmentDetails : API operation to get a vehicle from package assignment details for
# specific systemId
def packageController_packageAssignmentDetails(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageAssignmentDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAssignmentDetails",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageAssignmentDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageAssignmentDetails", response.text)


    return response


# PackageController_PackageIdDetails : API operation to get package details
def packageController_packageIdDetails(self, packageId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageIdDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{packageId}', str(packageId))
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageIdDetails",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageIdDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageIdDetails", response.text)

    return response


# PackageController_PackageAllDetails : API operation to get all packages
def packageController_packageAllDetails(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageAllDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint)
    if tc == "invalid_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", "pageNumber=#@")
    elif tc == "empty_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", "pageNumber=")
    elif tc == "no_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1&", "")

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
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAllDetails",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageAllDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageAllDetails", response.text)

    return response


# PackageController_categoryDetails : API operation to get all category
def packageController_categoryDetails(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_CategoryDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint)
    if tc == "invalid_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", "pageNumber=#@")
    elif tc == "empty_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", "pageNumber=")
    elif tc == "no_pageNo" and "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1&", "")

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
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_CategoryDetails",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_CategoryDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_CategoryDetails", response.text)

    return response


# PackageController_PackageFailureDetails : API operation to get package failure details
def packageController_packageFailureDetails(self, systemId, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageFailureDetails")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId).replace('{trackingId}', trackingId)
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
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageFailureDetails",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageFailureDetails', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageFailureDetails", response.text)

    return response


# PackageController_PackageAssignmentStatusUpdate : API operation to edit the status of vehicle to package assignment
def packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "PackageController_PackageAssignmentStatusUpdate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    # systemId = get_SystemId(self, deviceType_IVI)
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_packageId":
        del json_object["updates"][0]["packageId"]
    else:
        json_object["updates"][0]["packageId"] = packageId
    if tc == "no_status":
        del json_object["updates"][0]["status"]
    else:
        json_object["updates"][0]["status"] = status
    if tc == "no_trackingId":
        del json_object["updates"][0]["trackingId"]
    else:
        json_object["updates"][0]["trackingId"] = trackingId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation :")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "PackageController_AuthToken")
            time.sleep(5)

            update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAssignmentStatusUpdate",
                                                "PackageController_AuthToken")
            time.sleep(60)
            response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('PackageController_PackageAssignmentStatusUpdate', response.text)
    save_api_resp_in_excel(self, "API_Data", "PackageController_PackageAssignmentStatusUpdate", response.text)

    return response


# ----------------------------
# Modules
# ----------------------------
def read_packageId(self, response, package_name):
    packageId = ''
    data_len = len(response["responseData"]["dataList"])
    for i in range(data_len):
        name = response["responseData"]["dataList"][int(i)]["name"]
        if name == package_name:
            packageId = response["responseData"]["dataList"][int(i)]["id"]
            break
    return packageId


def read_packageStatus_byTrackingId(self, response, trackingId):
    packageId = ''
    data_len = len(response["responseData"]["dataList"])
    for i in range(data_len):
        name = response["responseData"]["dataList"][int(i)]["trackingId"]
        if name == trackingId:
            packageId = response["responseData"]["dataList"][int(i)]["packageId"]
            status = response["responseData"]["dataList"][int(i)]["status"]
            break
    return packageId, status


def read_packageStatus_byPackageId(self, response, packageId):
    data_len = len(response["responseData"]["dataList"])
    for i in range(data_len):
        package_Id = response["responseData"]["dataList"][int(i)]["packageId"]
        if package_Id == packageId:
            status = response["responseData"]["dataList"][int(i)]["status"]
            break
    return status
