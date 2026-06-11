import ast
import json
import time
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel, XlsxReader, save_data_in_excel


# SOTA API reusable modules :

# SOTA-CreatePresignUrl

def SOTA_createPresignUrl(self, filename, system, model_name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreatePresignUrl")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_filename":
        del json_object["filename"]
    else:
        json_object["filename"] = filename
    if tc == "no_system":
        del json_object["system"]
    else:
        json_object["system"] = system
    if tc == "no_model":
        del json_object["model-name"]
    else:
        json_object["model-name"] = model_name
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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreatePresignUrl",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreatePresignUrl', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreatePresignUrl", response.text)

    print("API response status code is :", response.status_code)

    # Validate response status code
    if response.status_code == 200:
        # Parse API response into JSON
        response = response.json()

    return response


# SOTA-uploadPackage

def SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                       isFull, downloadConsent, installConsent, rebootConsent, packageName,
                       packageVersion, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-uploadPackage")
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
    print("Header :", header_x)

    # Payload :
    # print(payload)
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["system"] = system
    json_object["description"] = description
    json_object["isDiffImage"] = isDiffImage
    # json_object["isBase"] = isBase
    # json_object["isFull"] = isFull
    json_object["downloadConsent"] = downloadConsent
    json_object["installConsent"] = installConsent
    json_object["rebootConsent"] = rebootConsent
    json_object["packageName"] = packageName
    if "no_model" in tc:
        del json_object["model"]
    if "no_system" in tc:
        del json_object["system"]
    if "no_description" in tc:
        del json_object["description"]
    if "no_isDiffImage" in tc:
        del json_object["isDiffImage"]
    if "no_packageName" in tc:
        del json_object["packageName"]
    if "no_downloadConsent" in tc:
        del json_object["downloadConsent"]
    if "no_installConsent" in tc:
        del json_object["installConsent"]
    if "no_rebootConsent" in tc:
        del json_object["rebootConsent"]
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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadPackage",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-uploadPackage', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-uploadPackage", response.text)

    print("API response status code is :", response.status_code)

    return response


# SOTA-CreateScript

def SOTA_CreateScript(self, model, system, scriptName, command, appName, targetVersion, notes, preconditions,
                      tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreateScript")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["system"] = system
    json_object["scriptName"] = scriptName
    json_object["preconditions"][0] = preconditions
    json_object["command"] = command
    json_object["appName"] = appName
    json_object["targetVersion"] = targetVersion
    json_object["notes"] = notes
    if "no_model" in tc:
        del json_object["model"]
    elif "no_system" in tc:
        del json_object["system"]
    elif "no_scriptName" in tc:
        del json_object["scriptName"]
    elif "no_preconditions" in tc:
        del json_object["preconditions"]
    elif "no_command" in tc:
        del json_object["command"]
    elif "no_appName" in tc:
        del json_object["appName"]
    elif "no_targetVersion" in tc:
        del json_object["targetVersion"]
    elif "no_notes" in tc:
        del json_object["notes"]

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateScript",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreateScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreateScript", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-uploadFile

def SOTA_uploadFile(self, upload_url, filepath, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-uploadFile")
    # base_url = str(dict["Base Url"])
    # endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    # payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    print(upload_url)
    # payload = {'file': filepath}
    # print(filepath)
    response = requests.put(upload_url, data=filepath, headers=header_x)
    print("API response : ", response.text)

    # try:
    #     # Parse API response into JSON
    #     response_body = response.json()
    #
    #     if response_body["Message"] == "User is not authorized to access this resource":
    #         print("\n")
    #         # Generate token
    #         token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
    #         update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadFile",
    #                                             "SOTA-GetToken")
    #         time.sleep(60)
    #         response = requests.put(upload_url, data=filepath, headers=headers)
    #         print("API response : ", response.text)
    # except:
    #     print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    # save_api_resp_into_file('SOTA-uploadFile', response.text)
    # save_api_resp_in_excel(self, "API_Data", "SOTA-uploadFile", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListPackages

def SOTA_ListPackages(self, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListPackages")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    if "{pageNo}" in endpoint or "{pageSize}" in endpoint:
        complete_url = str(base_url + endpoint).replace('{pageNo}', pageNo).replace(
            '{pageSize}', pageSize)
    elif "pageNumber" in endpoint or "pageSize" in endpoint:
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=" + str(pageNo)).replace(
            'pageSize=10', "pageSize=" + pageSize)
    else:
        complete_url = str(base_url + endpoint)

    if "removeQueryParams_from_url" in tc:
        # Remove query params from the url
        complete_url = str(base_url + endpoint).split('?')[0]

    if tc == "queryParams_status":
        complete_url = str(base_url + endpoint).replace('status=SUCCESS,FAILURE', "status=SUCCESS").replace(
            '{status=}', "SUCCESS")
    if tc == "queryParams_model":
        if "model=" in endpoint:
            complete_url = str(base_url + endpoint).replace('{model}', "adp")
        else:
            complete_url = str(base_url + endpoint).replace('?', "?&model=adp&")

    print("Complete URL : ", complete_url)

    # Update Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListPackages",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListPackages', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListPackages", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListScripts

def SOTA_ListScripts(self, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListScripts")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    print(pageNo, pageSize)

    complete_url = str(base_url + endpoint)
    if "?pageNumber=1" in complete_url or "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", 'pageNumber=' + str(pageNo))
    if "pageSize=10" in complete_url:
        complete_url = complete_url.replace("&pageSize=10", '&pageSize=' + str(pageSize))
    if "{pageNo}" in complete_url or "{pageSize}" in complete_url:
        complete_url = str(base_url + endpoint) + "&pageNumber={pageNo}&pageSize={pageSize}".replace('{pageNo}',
                                                                                                     pageNo).replace(
            '{pageSize}', pageSize)

    if "no_pagesNumber" in tc:
        complete_url = complete_url + "&pageSize={pageSize}".replace('{pageSize}', pageSize)
    elif "no_pageSize" in tc:
        complete_url = complete_url + "&pageNumber={pageNo}".replace('{pageNo}', pageNo)
    elif "no_pageNoandpageSize" in tc:
        complete_url = complete_url

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScripts",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListScripts', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListScripts", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-CreateSchedule

def SOTA_CreateSchedule(self, vins, scriptId, startDate, endDate, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-CreateSchedule")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_vin":
        del json_object["vins"]
    else:
        json_object["vins"][0] = vins
    if tc == "no_scriptId":
        del json_object["scriptId"]
    else:
        json_object["scriptId"] = scriptId
    if tc == "no_startDate":
        del json_object["period"]["startDate"]
    else:
        json_object["period"]["startDate"] = startDate
    if tc == "no_endDate":
        del json_object["period"]["endDate"]
    else:
        json_object["period"]["endDate"] = endDate
    if tc == "no_period":
        del json_object["period"]
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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateSchedule",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-CreateSchedule', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-CreateSchedule", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListSchedules

def SOTA_ListSchedules(self, pageNo, pageSize, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListSchedules")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :

    complete_url = str(base_url + endpoint)
    if "?pageNumber=1" in complete_url or "pageNumber=1" in complete_url:
        complete_url = complete_url.replace("pageNumber=1", 'pageNumber=' + str(pageNo))
    if "pageSize=10" in complete_url:
        complete_url = complete_url.replace("&pageSize=10", '&pageSize=' + str(pageSize))
    if "{pageNo}" in complete_url or "{pageSize}" in complete_url:
        complete_url = str(base_url + endpoint) + "&pageNumber={pageNo}&pageSize={pageSize}".replace('{pageNo}',
                                                                                                     pageNo).replace(
            '{pageSize}', pageSize)

    if "no_pagesNumber" in tc:
        complete_url = complete_url + "&pageSize={pageSize}".replace('{pageSize}', pageSize)
    elif "no_pageSize" in tc:
        complete_url = complete_url + "&pageNumber={pageNo}".replace('{pageNo}', pageNo)
    elif "no_pageNoandpageSize" in tc:
        complete_url = complete_url

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListSchedules",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListSchedules', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListSchedules", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-List ScheduleVin

def SOTA_ListScheduleVin(self, scheduleId, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListScheduleVin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', scheduleId)

    if tc == "invalid_pageNo_lessthanZero":
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=-1")
    elif tc == "invalid_pageSize_lessthanZero":
        complete_url = str(base_url + endpoint).replace('pageSize=3', "pageSize=-1")
    elif tc == "invalid_pageNo":
        complete_url = str(base_url + endpoint).replace('pageNumber=1', "pageNumber=xy")
    elif tc == "invalid_pageSize":
        complete_url = str(base_url + endpoint).replace('pageSize=3', "pageSize=xy")

    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["vins"][0] = vin
    if "no_vin" in tc:
        del json_object["vins"]
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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScheduleVin",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListScheduleVin', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListScheduleVin", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-vehicle Onboard
def SOTA_VehicleOnboard(self, model, name, partNo, sn, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-VehicleOnboard")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["model"] = model
    json_object["vehicles"][0]["ecus"][0]["name"] = name
    json_object["vehicles"][0]["ecus"][0]["partNo"] = partNo
    json_object["vehicles"][0]["ecus"][0]["sn"] = sn
    json_object["vehicles"][0]["vin"] = vin

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-VehicleOnboard",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-VehicleOnboard', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-VehicleOnboard", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-GetPreconditions

def SOTA_GetPreconditions(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-GetPreconditions")
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
    print("Header :", header_x)

    # print(header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-GetPreconditions",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-GetPreconditions', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-GetPreconditions", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListApps

def SOTA_ListApps(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListApps")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{modelName}', model)
    if "no_model" in tc:
        complete_url = str(base_url + endpoint).replace('{modelName}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListApps",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListApps', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListApps", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListModels1

def SOTA_ListModels1(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListModels1")
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
    print("Header :", header_x)
    # print(header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels1",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListModels1', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListModels1", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-ListModels

def SOTA_ListModels(self, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-ListModels")
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
    print("Header :", header_x)
    # print(header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-ListModels', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-ListModels", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-UpdatePackageDescription

def SOTA_UpdatePackageDescription(self, packageId, desc, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-UpdatePackageDescription")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    complete_url = str(base_url + endpoint).replace('{PackageId}', packageId)

    if "no_packageId" in tc:
        complete_url = str(base_url + endpoint).replace('{PackageId}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object['description'] = desc
    if "no_description" in tc:
        del json_object['description']
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-UpdatePackageDescription",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-UpdatePackageDescription', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-UpdatePackageDescription", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-EditScriptNotes

def SOTA_EditScriptNotes(self, scriptId, releasenote, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-EditScriptNotes")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scriptId}', scriptId).replace('{reqId}', scriptId)
    if "no_scriptId" in tc:
        complete_url = str(base_url + endpoint).replace('{scriptId}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object['release-note'] = releasenote
    if "no_release-note" in tc:
        del json_object['release-note']
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("\n")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-EditScriptNotes",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.patch(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-EditScriptNotes', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-EditScriptNotes", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-DeletePackage

def SOTA_DeletePackage(self, packageId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeletePackage")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{PackageId}', str(packageId))
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeletePackage",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeletePackage', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeletePackage", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-DeleteScript

def SOTA_DeleteScript(self, scriptId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeleteScript")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{reqId}', scriptId)
    if "no_scriptId" in tc:
        complete_url = str(base_url + endpoint).replace('{reqId}', "")
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteScript",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeleteScript', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeleteScript", response.text)
    print("API response status code is :", response.status_code)

    return response


# SOTA-DeleteScript_scheduleId

def SOTA_deleteSchedule(self, scheduleId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-DeleteSchedule")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{scheduleId}', scheduleId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteSchedule",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-DeleteSchedule', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-DeleteSchedule", response.text)
    print("API response status code is :", response.status_code)

    return response


def SOTA_getScriptModel(self, temp):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "SOTA-GetScriptModel")
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
    header_x = header_update(header_x, temp)
    print("Header :", header_x)

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
            token_gen_reus_mod(self, "API_Data", "SOTA-GetToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-GetScriptModel",
                                                "SOTA-GetToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('SOTA-GetScriptModel', response.text)
    save_api_resp_in_excel(self, "API_Data", "SOTA-GetScriptModel", response.text)

    return response


# ----------------------------------------
# Reusable modules
# ----------------------------------------
def get_model_by_getListOfModelsCount_api(self):
    # get model
    response = SOTA_ListModels(self, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        data_len = len(response_body["responseData"]["dataList"])
        if data_len >= 1:
            for i in range(data_len):
                model = response_body["responseData"]["dataList"][i]
                if model == "adp":
                    model = "adp"
                    break
                else:
                    model = response_body["responseData"]["dataList"][0]

            print("Module : ", model)

        else:
            print(" => module datalist is empty")
            model = ""
            assert False
    return model


def get_packageId_from_packageDetails_api(self):
    # call api reusable module
    global packageId
    response = SOTA_ListPackages(self, str(1), str(10), "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        if len(response_body["responseData"]["dataList"]) >= 1:
            packageId = response_body["responseData"]["dataList"][0]["packageId"]
        else:
            print("datalist is empty")
            packageId = ""
    return packageId


def get_ScriptId_from_ScriptDetails_api(self):
    # call api reusable module
    response = SOTA_ListScripts(self, str(1), str(10), "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        if len(response_body["responseData"]["dataList"]) >= 1:
            refId = response_body["responseData"]["dataList"][0]["scriptId"]
            print("Script Id : ", response_body["responseData"]["dataList"][0]["scriptId"])
        else:
            print("datalist is empty")
            refId = ""
    return refId


def get_ScheduledId_from_ScheduleDetails_api(self):
    # call api reusable module
    response = SOTA_ListSchedules(self, str(1), str(10), "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        if len(response_body["responseData"]["dataList"]) >= 1:
            scheduleId = response_body["responseData"]["dataList"][0]["scheduleId"]
            print("Schedule Id : ", response_body["responseData"]["dataList"][0]["scheduleId"])
        else:
            print("datalist is empty")
            scheduleId = ""

    return scheduleId


def get_preCondition_from_preconditionDetails_api(self):
    # call api reusable module
    global precondition
    response = SOTA_GetPreconditions(self, "valid")
    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    # Parse API response into JSON
    response_body = response.json()
    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        if len(response_body["responseData"]["dataList"]) >= 1:
            precondition = response_body["responseData"]["dataList"][0]["precondition"]
            print("precondition : ", precondition)
        else:
            print("datalist is empty")
            precondition = ""
    return precondition


def get_verisons_from_versionDetails_api(self, model):
    appName = appVersion = ""
    # call api reusable module
    response = SOTA_ListApps(self, model, "valid")

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    # Validate response
    if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
        # message = response_body["responseData"]["message"]
        # print('Message : ', message)
        if len(response_body["responseData"]["dataList"]) >= 1:
            ecu = response_body["responseData"]["dataList"][0]
            if "IVI" in ecu:
                if len(response_body["responseData"]["dataList"][0]["IVI"]) >= 1:
                    appName = response_body["responseData"]["dataList"][0]["IVI"][0]["appName"]
                    appVersion = response_body["responseData"]["dataList"][0]["IVI"][0]["appVersion"]

            elif "TCU" in ecu:
                if len(response_body["responseData"]["dataList"][0]["TCU"]) >= 1:
                    appName = response_body["responseData"]["dataList"][0]["TCU"][0]["appName"]
                    appVersion = response_body["responseData"]["dataList"][0]["TCU"][0]["appVersion"]
        else:
            print("datalist is empty")

    return appName, appVersion
