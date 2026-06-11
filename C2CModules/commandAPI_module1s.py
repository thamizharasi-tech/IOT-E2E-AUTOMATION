import ast
import json
import time

import requests

from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel, read_API_common_data
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel


# CommandControl_Request_addTemplate
def CommandControl_Request_addTemplate(self, baseTemplateId, name, description, testCaseName):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]

    # Payload :
    json_object = json.loads(payload)
    if "missing_name" in testCaseName:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in testCaseName:
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
def CommandControl_Request_getTemplateInfo(self, baseTemplateId, template_id, name, testCaseName):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]

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
def CommandControl_Request_updateTemplate(self, baseTemplateId, name, description, template_id,testCaseName):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_name" in testCaseName:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in testCaseName:
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
def CommandControl_Request_addModelTemplate(self, appId, model, modelYear, class1, style, templateId, testCaseName):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in testCaseName:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_model" in testCaseName:
        del json_object["model"]
    else:
        json_object["model"] = model
    if "missing_class" in testCaseName:
        del json_object["class"]
    else:
        json_object["class"] = class1
    if "missing_style" in testCaseName:
        del json_object["style"]
    else:
        json_object["style"] = style
    json_object["modelYear"] = modelYear
    if "missing_templateId" in testCaseName:
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
def CommandControl_Request_updateModelTemplate(self, appId, model, modelYear, class1, style, templateId,baseTemplateId,testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_updateModelTemplate")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{baseTemplateId}",baseTemplateId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in testCaseName:
        del json_object["appId"]
    else:
        json_object["appId"] = appId

    if "missing_class" in testCaseName:
        del json_object["class"]
    else:
        json_object["class"] = class1
    if "missing_style" in testCaseName:
        del json_object["style"]
    else:
        json_object["style"] = style
    if "missing_ModelYear" in testCaseName:
        del json_object["modelYear"]
    else:
        json_object["modelYear"] = modelYear
    if "missing_model" in testCaseName:
        del json_object["model"]
    else:
        json_object["model"] = model
    if "missing_templateId" in testCaseName:
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
def CommandControl_Request_getModelTemplate(self, model, testCaseName):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
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
def CommandControl_Request_addOEM(self, appId, name, description,defaultTemplateId,testCaseName ):
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
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in testCaseName:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_name" in testCaseName:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in testCaseName:
        del json_object["description"]
    else:
        json_object["description"] = description
    if "missing_defaultTemplateId" in testCaseName:
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
def CommandControl_Request_updateOEM(self, oemId,appId, name, description,defaultTemplateId, testCaseName ):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_updateOEM")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{oemId}",oemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    if "missing_appId" in testCaseName:
        del json_object["appId"]
    else:
        json_object["appId"] = appId
    if "missing_name" in testCaseName:
        del json_object["name"]
    else:
        json_object["name"] = name
    if "missing_description" in testCaseName:
        del json_object["description"]
    else:
        json_object["description"] = description
    if "missing_defaultTemplateId" in testCaseName:
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
def CommandControl_Request_getOEM(self,oemId, testCaseName):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "CommandControl_Request_getOEM")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for GET request

    # Url :
    complete_url = str(base_url + endpoint).replace("{oemId}",oemId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    if "invalid_apiKey" == testCaseName:
        header_x["api-key"] = 'xyz'
    elif "empty_apiKey" in testCaseName:
        header_x["api-key"] = ''
    elif "no_apiKey" in testCaseName:
        del header_x["api-key"]
    elif "empty_x-requestor" in testCaseName:
        header_x["x-requestor"] = ''
    elif "no_x-requestor" in testCaseName:
        del header_x["x-requestor"]
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





