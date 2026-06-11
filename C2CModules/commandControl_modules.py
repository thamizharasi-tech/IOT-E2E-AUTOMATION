import ast
import json
import time
import requests

from C2CModules.api_modules import header_update
from C2CModules.e2e_testData import telemetry_msg_id_published2Cloud
from C2CModules.primary_IVI_device_modules import pull_logs_from_IVI_device, \
    verify_msg_details_pub2Cloud
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.testResults import testResult
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel, read_API_common_data
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# ---------------------------------
# API Modules
# ---------------------------------

# CommandControl_Request
def commandControl_Request(self, appid, name, area, value, vin):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI, drimaes_ivi_chipset)

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    # json_object["a]ppid"] = appid
    json_object["name"] = name
    json_object["payload"][0]["area"] = area
    json_object["payload"][0]["value"] = value
    json_object["target"]["vins"][0] = vin
    json_object["appid"] = appid

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request", response.text)

    return response


# CommandControl_Tracking
def commandControl_Tracking(self, trackingId):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Tracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Tracking",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Tracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Tracking", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
        assert True
    else:
        print("response Code is not 1200. Rather found : " + str(response_body["message"]))
        assert False

    return response_body


# CommandControl_Request_addTemplate
def CommandControl_Request_addTemplate(self, baseTemplateId, name, description, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_addTemplate")
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
    if "missing_name" in tc:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in tc:
        del json_object["description"]
    else:
        json_object["description"] = description

    json_object["baseTemplateId"] = baseTemplateId

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_addTemplate",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_addTemplate', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_addTemplate", response.text)

    return response


# CommandControl_Request_getTemplateInfo
def CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_getTemplateInfo")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{baseTemplateId}', str(baseTemplateId)).replace("{template_id}",
                                                                                                     str(template_id)).replace(
        "{name}", name)
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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_getTemplateInfo",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_getTemplateInfo', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_getTemplateInfo", response.text)

    return response


# CommandControl_Request_updateTemplate
def CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_updateTemplate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace('{template_id}', template_id)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_name" in tc:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in tc:
        del json_object["description"]
    else:
        json_object["description"] = description
    json_object["baseTemplateId"] = baseTemplateId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_updateTemplate",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_updateTemplate', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_updateTemplate", response.text)

    return response


# CommandControl_Request_addModelTemplate
def CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_addModelTemplate")
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
    if "missing_appId" in tc:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_model" in tc:
        del json_object["model"]
    else:
        json_object["model"] = model
    if "missing_class" in tc:
        del json_object["class"]
    else:
        json_object["class"] = class1
    if "missing_style" in tc:
        del json_object["style"]
    else:
        json_object["style"] = style
    json_object["modelYear"] = modelYear
    if "missing_templateId" in tc:
        del json_object["templateId"]
    else:
        json_object["templateId"] = templateId

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_addModelTemplate",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_addModelTemplate', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_addModelTemplate", response.text)

    return response


# CommandControl_Request_updateModelTemplate
def CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style, templateId, baseTemplateId,
                                               tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_updateModelTemplate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{baseTemplateId}", baseTemplateId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in tc:
        del json_object["appId"]
    else:
        json_object["appId"] = appId

    if "missing_class" in tc:
        del json_object["class"]
    else:
        json_object["class"] = class1
    if "missing_style" in tc:
        del json_object["style"]
    else:
        json_object["style"] = style
    if "missing_ModelYear" in tc:
        del json_object["modelYear"]
    else:
        json_object["modelYear"] = modelYear
    if "missing_model" in tc:
        del json_object["model"]
    else:
        json_object["model"] = model
    if "missing_templateId" in tc:
        del json_object["templateId"]
    else:
        json_object["templateId"] = templateId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_updateModelTemplate",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_updateModelTemplate', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_updateModelTemplate", response.text)

    return response


# CommandControl_Request_getModelTemplate
def CommandControl_Request_getModelTemplate(self, model, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_getModelTemplate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace('{model}', model)
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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_getModelTemplate",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_getModelTemplate', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_getModelTemplate", response.text)

    return response


# CommandControl_Request_addOEM
def CommandControl_Request_addOEM(self, appId, name, description, defaultTemplateId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_addOEM")
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
    if "missing_appId" in tc:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_name" in tc:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in tc:
        del json_object["description"]
    else:
        json_object["description"] = description
    if "missing_defaultTemplateId" in tc:
        del json_object["defaultTemplateId"]
    else:
        json_object["defaultTemplateId"] = defaultTemplateId

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_addOEM",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_addOEM', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_addOEM", response.text)

    return response


# CommandControl_Request_updateOEM
def CommandControl_Request_updateOEM(self, oemId, appId, name, description, defaultTemplateId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_updateOEM")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{oemId}", oemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in tc:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_name" in tc:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in tc:
        del json_object["description"]
    else:
        json_object["description"] = description
    if "missing_defaultTemplateId" in tc:
        del json_object["defaultTemplateId"]
    else:
        json_object["defaultTemplateId"] = defaultTemplateId

    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_updateOEM",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_updateOEM', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_updateOEM", response.text)

    return response


# CommandControl_Request_getOEM
def CommandControl_Request_getOEM(self, oemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_getOEM")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace("{oemId}", oemId)
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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request_getOEM",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request_getOEM', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request_getOEM", response.text)

    return response


# CommandControl_liveTracking
def CommandControl_liveTracking(self, name, systemId, frequency, value, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_liveTracking_updateFrequency")
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
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "no_commandName":
        del json_object["name"]
    else:
        json_object["name"] = name
    if tc == "no_systemId":
        del json_object["systemId"]
    else:
        json_object["systemId"] = systemId
    if tc == "no_frequency":
        del json_object["frequency"]
    elif tc == "invalid_frequency":
        json_object["frequency"] = frequency
    else:
        json_object["frequency"] = int(frequency)
    if tc == "no_value":
        del json_object["value"]
    elif tc == "invalid_value":
        json_object["value"] = value
    else:
        json_object["value"] = int(value)
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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_liveTracking_updateFrequency",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_liveTracking_updateFrequency', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_liveTracking_updateFrequency", response.text)

    return response


# ---------------------------------
# Wrapper API Modules
# ---------------------------------

# CommandControl_BuzzBike
def commandControl_wrapper(self, systemId, command, appid):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", command)
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{sysId}', systemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", command,
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file(command, response.text)
    save_api_resp_in_excel(self, "API_Data", command, response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    return response_body


# CommandControl_remote-operation
def commandControl_remoteOperation(self, command, systemId, eventName, appid):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", command)
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{event-name}', eventName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["appid"] = appid
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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", command,
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file(command, response.text)
    save_api_resp_in_excel(self, "API_Data", command, response.text)

    return response


# ---------------------------------
# Modules
# ---------------------------------

def get_commandCtrl_trackingId(self, response):
    trackingId = response["responseData"]['trackingId']
    print("Command Control - Tracking Id : ", trackingId)
    return trackingId


def verify_commandCtrl_apiResp_status(self, response):
    print("Tracking Status :", response["responseData"]["trackingStatus"])
    status = response["responseData"]["data"][0]["status"]
    print("Status : ", status)
    if status == 103:
        assert True
    else:
        print("status is not 103. Rather found : " + str(status))
        assert False
    return status


def verify_commandCtrl_msg_in_deviceLogs(self, OnboardingType, chipsetType, msg_type, msg_attribute):
    # ===========================================================================================
    # Pull logs & verify command & control msg
    # ===========================================================================================
    print("Pull/Fetch device logs for validation : ")
    i = 1
    while i <= 10:
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
        status = verify_msg_details_pub2Cloud(self, msg_type, msg_attribute)
        print("Status : ", status)
        if status == "Found":
            break
        i = i + 1
        time.sleep(5)

    print("Logs are fetched from device to host machine @ desired location and verified ")
    if status == "Found":
        print(
            f"Command & control message published to cloud' {telemetry_msg_id_published2Cloud} with {msg_type} '")
        testResult(self, "passed", "Command & control message should be published to cloud via Hub ",
                   "Command & control message is published to cloud and device logs are updated accordingly, pls refer "
                   "device logs for detailed info")

    elif status == "NotFound":
        print(
            "Command & control message is not published to cloud or device logs are not updated or logs have been rotated. pls refer device logs in detail")
        testResult(self, "verificationFailed", "Command & control message should be published to cloud via Hub ",
                   "Command & control message is not published to cloud or device logs are not updated or logs have been rotated. pls refer device "
                   "logs in detail ")

    print("----------------------------------------------------------")


# header_validation_For_commandRequest
def commandControl_Request_header_validation(self, appid, name, area, value, vin, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    # vin = getVIN(self, "tel", deviceType_IVI, drimaes_ivi_chipset)

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

    # Payload :
    json_object = json.loads(payload)
    # json_object["appid"] = appid
    json_object["name"] = name
    json_object["payload"][0]["area"] = area
    json_object["payload"][0]["value"] = value
    json_object["target"]["vins"][0] = vin
    json_object["appid"] = appid

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            # print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Request', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Request", response.text)

    return response


# header_validation_For_commandTracking
def commandControl_Tracking_header_validation(self, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Tracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header :", header_x)

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
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Tracking",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Tracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Tracking", response.text)

    return response


# ---------------------------------
# RE API Modules
# ---------------------------------

# CommandControl_Request
def commandControl_Service_Request(self, name, systemId, appId, area, value, timeout, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Service_Request")
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
    print("Headers: ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["name"] = name
    if "invalid_command_name" in tc:
        json_object["name"] = "xyz"
    if "without_command_name" in tc:
        del json_object["name"]
    json_object["systemId"] = systemId
    if "invalid_systemId" in tc:
        json_object["systemId"] = "xyz"
    if "without_systemId" in tc:
        del json_object["systemId"]
    json_object["appId"] = appId
    if "invalid_appId" in tc:
        json_object["appId"] = "xyz"
    if "without_appId" in tc:
        del json_object["appId"]
    json_object["input"][0]["area"] = area
    json_object["input"][0]["value"] = value
    json_object["timeout"] = timeout

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
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Service_Request",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Service_Request', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Service_Request", response.text)

    return response


# CommandControl_Tracking
def commandControl_Service_Tracking(self, trackingId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Service_Tracking")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{trackingId}', trackingId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "CommandControl_AuthToken")
            time.sleep(5)
            update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Service_Tracking",
                                                "CommandControl_AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('CommandControl_Service_Tracking', response.text)
    save_api_resp_in_excel(self, "API_Data", "CommandControl_Service_Tracking", response.text)

    return response

def command_save_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, isCritical, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Command_save_precondition")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header) for DELETE request

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers: ", header_x)

    # Payload
    json_object = json.loads(payload)
    if cloudEnv not in ["GCP-QA3", "DM1"]:
        json_object["model"] = model
        json_object["action"] = action
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
        json_object["precondition"]["statePreconditions"][2] = statePreconditions3
    else:
        json_object["model"] = model
        json_object["action"] = action
        json_object["isCritical"] = isCritical
        json_object["precondition"]["statePreconditions"][0] = statePreconditions1
        json_object["precondition"]["statePreconditions"][1] = statePreconditions2
        json_object["precondition"]["statePreconditions"][2] = statePreconditions3
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Command_save_precondition', response.text)
    save_api_resp_in_excel(self, "API_Data", "Command_save_precondition", response.text)

    return response

# ---------------------------------
# RE REUSABLE Modules
# ---------------------------------
def read_commandCtrl_trackingId(self, response):
    status = response["commandResponse"]['Status']
    trackingId = response["commandResponse"]['trackingId']
    message = response["message"]
    print("Command Control - Status : ", status)
    print("Command Control - Tracking Id : ", trackingId)
    print("Command Control - Message : ", message)
    return trackingId


def verify_commandCtrl_status(self, response):
    commandTrackingId = response["command"]["commandTrackingId"]
    appId = response["command"]["appId"]
    name = response["command"]["name"]
    systemId = response["command"]["systemId"]
    area = response["command"]["payload"][0]["area"]
    value = response["command"]["payload"][0]["value"]
    commandIssuedTime = response["command"]["commandIssuedTime"]
    status = response["command"]["status"]
    statusUpdatedTime = response["command"]["statusUpdatedTime"]
    message = response["message"]
    print("Command Tracking Id :", commandTrackingId)
    print("Command Status :", status)
    return status

def command_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, isCritical, tc):

    # Call API reusable module
    response = command_save_precondition(self, cloudEnv, model, action, statePreconditions1, statePreconditions2, statePreconditions3, isCritical, "valid")

    # Validate response status code
    if response.status_code == 200:
        response_body = response.json()

        if response_body.get("message") == f"Precondition saved for the following combination - Model: {model} & Command: {action}":
            print("Command precondition data saved successfully.")
        else:
            print("Failed to save command precondition.")
            assert False
    elif response.status_code == 400:
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "15586" and response_body["errors"][0]["message"] == "Data already exists in db for Model & Action":
            print("Command precondition data already exist on db for the model")
    else:
        print("Response status code is not 200. Rather than found: ", response.status_code)
        assert False