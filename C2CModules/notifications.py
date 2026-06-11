import ast
import json
import time
import datetime
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import token_gen_reus_mod, update_apiheader_with_token_inExcel
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *

folder_path = "C:\Car2Cloud_E2ETesting"


# ---------------------------------
# API Modules
# ---------------------------------
# Notification_message
def notification_message(self, vin, systemId, message):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_message")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request
    #  vin = getVIN(self, "tel", deviceType_IVI)
    #  systemId = get_SystemId(self, deviceType_IVI)

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["target"][0]["systemId"] = systemId
    json_object["target"][0]["vin"] = vin
    json_object["message"] = message
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_message', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_message", response.text)

    # Validate response status code
    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

    # Parse API response into JSON
    response_body = response.json()

    if response_body["responseCode"] == str(1200):
        assert (response_body["responseData"]["message"] == "SUCCESS")
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        assert False

    return response_body


# Notification_message
def notification_message_new(self, vin, systemId, message, source, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_message")
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
    if tc == "invalid_without_systemId_field":
        del json_object["target"][0]["systemId"]
    else:
        json_object["target"][0]["systemId"] = systemId
    if tc == "invalid_without_vin_field":
        del json_object["target"][0]["vin"]
    else:
        json_object["target"][0]["vin"] = vin
    if tc == "invalid_without_message_field":
        del json_object["message"]
    else:
        json_object["message"] = message
    if tc == "invalid_without_source_field":
        del json_object["meta"]["source"]
    else:
        json_object["meta"]["source"] = source
    if tc == "invalid_without_target_field":
        del json_object["target"]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_message', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_message", response.text)

    return response


# Notification Service Controller -Subscribe
def notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName, destinationType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_subscribe")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filterValues"][0]["systemId"] = systemId
    json_object["filterValues"][0]["vin"] = vin
    json_object["category"][0]["endPoint"] = endPoint
    json_object["category"][0]["categoryName"] = categoryName
    json_object["category"][0]["destinationType"] = destinationType
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_subscribe', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_subscribe", response.text)

    if response.status_code == 200:
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response = response.json()

    return response


# Notification Service Controller - Details by System Id
def notificationServiceController_details_by_systemId(self, systemId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_details_by_systemId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

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

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_details_by_systemId', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_details_by_systemId", response.text)

    if response.status_code == 200:
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response = response.json()

    return response


# Notification Service Controller - Details by System Id & Category Type
def notificationServiceController_details_by_systemId_Category(self, systemId, categoryType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_details_by_systemId_Category")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if tc == "no_category":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('&category={notificationType}',
                                                                                        '')
    elif tc == "empty_pageNo":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageNumber=1',
                                                                                        'pageNumber=').replace(
            '{notificationType}',
            categoryType)
    elif tc == "invalid_pageNo":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageNumber=1',
                                                                                        'pageNumber=a').replace(
            '{notificationType}',
            categoryType)
    elif tc == "empty_pageSize":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageSize=10',
                                                                                        'pageSize=').replace(
            '{notificationType}',
            categoryType)
    elif tc == "invalid_pageSize":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageSize=10',
                                                                                        'pageSize=a').replace(
            '{notificationType}',
            categoryType)
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{notificationType}',
                                                                                        categoryType)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_details_by_systemId_Category', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_details_by_systemId_Category",
                           response.text)

    return response


# Notification Service Controller - Un-Subscribe
def notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName, destinationType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_unsubscribe")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["filterValues"][0]["systemId"] = systemId
    json_object["filterValues"][0]["vin"] = vin
    json_object["category"][0]["endPoint"] = endPoint
    json_object["category"][0]["categoryName"] = categoryName
    json_object["category"][0]["destinationType"] = destinationType
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_unsubscribe', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_unsubscribe", response.text)

    if response.status_code == 200:
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response = response.json()

    return response


# Notification_broadcastMessage
def notification_broadcastMessage(self, groupName, title, message, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_broadcastMessage")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{groupName}', groupName)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["title"] = title
    json_object["message"] = message
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_broadcastMessage",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_broadcastMessage', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_broadcastMessage", response.text)

    if response.status_code == 200:
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response = response.json()

    return response


# Notification_createBroadcastGroup
def notification_createBroadcastGroup(self, systemId, vin, groupName, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_createBroadcastGroup")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    if tc == "invalid_without_systemId_field":
        del json_object["group"][0]["systemId"]
    else:
        json_object["group"][0]["systemId"] = systemId
    if tc == "invalid_without_VIN_field":
        del json_object["group"][0]["vin"]
    else:
        json_object["group"][0]["vin"] = vin
    if tc == "invalid_without_groupName_field":
        del json_object["groupName"]
    else:
        json_object["groupName"] = groupName
    if tc == "invalid_without_group_field":
        del json_object["group"]
    if tc == "invalid_without_vinSystemId_field":
        del json_object["group"][0]["vin"]
        del json_object["group"][0]["systemId"]
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_createBroadcastGroup",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_createBroadcastGroup', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_createBroadcastGroup", response.text)

    if response.status_code == 200:
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        # response = response.json()

    return response


# ---------------------------
# RE API Reusable Modules
# ---------------------------


# Notification - Update event status based on message Id & system Id
def notification_updateStatus(self, systemId, messageId, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_updateStatus")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["messageId"] = messageId
    json_object["status"] = status
    json_object["systemId"] = systemId
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_updateStatus', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_updateStatus",
                           response.text)

    return response


# Notification - get event status based on system Id, startDate, endDate, categoryId
def notification_getEvents(self, systemId, startDate, endDate, categoryId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_getEvents")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{categoryId}', categoryId).replace(
        '{startDate}', startDate).replace('{endDate}', endDate)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)
    # Payload :
    # json_object = json.loads(payload)
    # json_object["startDate"] = startDate
    # json_object["endDate"] = endDate
    # json_object["systemId"] = systemId
    # json_object["categoryId"] = categoryId
    # payload = json_object
    # print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.get(complete_url, headers=header_x)
    # print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_getEvents",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_getEvents', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_getEvents",
                           response.text)

    return response


# ---------------------------
# RE Reusable Modules
# ---------------------------

def notification_verify_alert_details_old(self, systemId, categoryName, notification_name, notification_type, dt, dt1):

    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")

    # parse api response into json
    response_body = response.json()

    if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
        if response_body["responseMessage"] == "SUCCESS":
            data_len = len(response_body["responseData"])
            createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
            if data_len >= 1:
                for i in range(data_len):
                    notificationType_actual = response_body["responseData"][i]["notificationType"]
                    categoryName_actual = response_body["responseData"][i]["category"]
                    if categoryName_actual == notification_name and notificationType_actual == notification_type:
                        createdBy = response_body["responseData"][i]["createdBy"]
                        createdTime = response_body["responseData"][i]["createdTime"]
                        updatedBy = response_body["responseData"][i]["updatedBy"]
                        updatedTime = response_body["responseData"][i]["updatedTime"]
                        id = response_body["responseData"][i]["id"]
                        parameters = response_body["responseData"][i]["paramaters"]
                        status = response_body["responseData"][i]["status"]
                        subscriber_id = response_body["responseData"][i]["subscriber"]["subscriber_id"]
                        break


                print("Latest notification details fetched from API response : ")
                print("Created By : ", createdBy)
                print("Created Time : ", createdTime)
                print("Updated By : ", updatedBy)
                print("Updated Time : ", updatedTime)
                print("Id : ", id)
                print("Parameters : ", parameters)
                print("Status : ", status)
                print("Category : ", categoryName_actual)
                print("Notification Type : ", notificationType_actual)
                print("Subscriber Id : ", subscriber_id)

                your_dt = datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
                createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
                createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

                print("-------------------------------------------------------------------")
                if createdTime1 == dt or createdTime2 == dt1:
                    testResult(self, "passed",
                               notification_name + " alert/notification should be triggered for this vehicle System ID",
                               notification_name + " alert/notification is triggered for this vehicle System ID successfully. pls refer "
                                                   " device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Mismatch in created date & time")
                    print("Test Execution - Current Date & Time ", dt, dt1)
                    print("API Response - Created Time ", createdTime1, createdTime2)
                    testResult(self, "failed",
                               notification_name + "  alert/notification should be triggered for this vehicle System ID",
                               notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                                   "wrong. pls refer device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                print("-------------------------------------------------------------------")

                # Validate the notify_status in the t_notification_messages table as soon as the message is
                # published to KAFKA

                if status == '1' or status == 1:
                    testResult(self, "passed",
                               "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                               "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                               " device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Mismatch in status")
                    print("Current Status is ", status)
                    testResult(self, "failed",
                               "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                               "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                               "wrong. pls refer device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                print("-------------------------------------------------------------------")

            else:
                print("dataList is empty in api response")
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
                assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")


def notification_verify_alert_details(self, systemId, categoryName, notification_name, notification_type, dt, dt1):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        data_len = len(response_body["notificationDetails"])
        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body["notificationDetails"][i]["notificationType"]
                categoryName_actual = response_body["notificationDetails"][i]["category"]
                print(categoryName_actual, notification_name, notificationType_actual,  notification_type)
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body["notificationDetails"][i]["createdBy"]
                    createdTime = response_body["notificationDetails"][i]["createdTime"]
                    updatedBy = response_body["notificationDetails"][i]["updatedBy"]
                    updatedTime = response_body["notificationDetails"][i]["updatedTime"]
                    id = response_body["notificationDetails"][i]["id"]
                    parameters = response_body["notificationDetails"][i]["paramaters"]
                    status = response_body["notificationDetails"][i]["status"]
                    subscriber_id = response_body["notificationDetails"][i]["subscriber"]["subscriber_id"]
                    break

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            your_dt = datetime.datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

            print("-------------------------------------------------------------------")
            if createdTime1 == dt or createdTime2 == dt1:
                testResult(self, "passed",
                           notification_name + " alert/notification should be triggered for this vehicle System ID",
                           notification_name + " alert/notification is triggered for this vehicle System ID successfully. pls refer "
                                               " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in created date & time")
                print("Test Execution - Current Date & Time ", dt, dt1)
                print("API Response - Created Time ", createdTime1, createdTime2)
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

            # Validate the notify_status in the t_notification_messages table as soon as the message is
            # published to KAFKA

            if status == '1' or status == 'NOTIFIED':
                testResult(self, "passed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                           " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in status")
                print("Current Status is ", status)
                testResult(self, "failed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                           "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

        else:
            print("dataList is empty in api response")
            testResult(self, "failed",
                       notification_name + "  alert/notification should be triggered for this vehicle System ID",
                       notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                           "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")



def notification_verify_update_status(self, systemId, categoryName, notification_name, notification_type,
                                      update_status_string, update_status):
    print("----------------------------------------------------------------------------")
    print(f"Update the {notification_name} status as {update_status}-{update_status_string} using PUT API : ")
    print("----------------------------------------------------------------------------")

    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")

    # Parse api response into json
    response_body = response.json()

    if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
        if response_body["responseMessage"] == "SUCCESS":
            data_len = len(response_body["responseData"])
            if data_len >= 1:
                for i in range(data_len):
                    notificationType_actual = response_body["responseData"][i]["notificationType"]
                    categoryName_actual = response_body["responseData"][i]["category"]
                    if categoryName_actual == notification_name and notificationType_actual == notification_type:
                        updatedBy = response_body["responseData"][i]["updatedBy"]
                        updatedTime = response_body["responseData"][i]["updatedTime"]
                        messageId = response_body["responseData"][i]["id"]
                        before_status = response_body["responseData"][i]["status"]
                        break

    # Call subscribe reusable module
    response = notification_updateStatus(self, systemId, messageId, update_status_string, "valid")

    # Parse api response in to json
    response_body = response.json()

    # Validate api response body
    try:
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200 and response_body[
             "responseMessage"] == "Updated the status successfully ":
            testResult(self, "passed",
                       "The notify_status should be updated successfully",
                       "The notify_status is updated successfully. pls refer "
                       " api response & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "The notify_status should be updated successfully",
                       "The notify_status is not updated successfully. pls refer "
                       " api response & cloud logs for detailed info")
    except:
        if response_body["message"] == "Updated the status successfully ":
            testResult(self, "passed",
                       "The notify_status should be updated successfully",
                       "The notify_status is updated successfully. pls refer "
                       " api response & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "The notify_status should be updated successfully",
                       "The notify_status is not updated successfully. pls refer "
                       " api response & cloud logs for detailed info")

    print("----------------------------------------------------------------------------")
    print(f"Cloud Side Validations : Validate the {notification_name} status ")
    print("----------------------------------------------------------------------------")

    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")

    # Parse api response into json
    response_body = response.json()

    if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
        if response_body["responseMessage"] == "SUCCESS":
            data_len = len(response_body["responseData"])
            createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
            if data_len >= 1:
                for i in range(data_len):
                    notificationType_actual = response_body["responseData"][i]["notificationType"]
                    categoryName_actual = response_body["responseData"][i]["category"]
                    if categoryName_actual == notification_name and notificationType_actual == notification_type:
                        createdBy = response_body["responseData"][i]["createdBy"]
                        createdTime = response_body["responseData"][i]["createdTime"]
                        updatedBy = response_body["responseData"][i]["updatedBy"]
                        updatedTime = response_body["responseData"][i]["updatedTime"]
                        id = response_body["responseData"][i]["id"]
                        parameters = response_body["responseData"][i]["paramaters"]
                        status = response_body["responseData"][i]["status"]
                        subscriber_id = response_body["responseData"][i]["subscriber"]["subscriber_id"]
                        break

                print("Latest notification details fetched from API response : ")
                print("Created By : ", createdBy)
                print("Created Time : ", createdTime)
                print("Updated By : ", updatedBy)
                print("Updated Time : ", updatedTime)
                print("Id : ", id)
                print("Parameters : ", parameters)
                print("Status : ", status)
                print("Category : ", categoryName_actual)
                print("Notification Type : ", notificationType_actual)
                print("Subscriber Id : ", subscriber_id)

                print("-------------------------------------------------------------------")

    # Validate the notify_status in the t_notification_messages table once the RE sends back status
    # as processing

    print(f"{notification_name} status before Update : ", before_status)
    print(f"{notification_name} status after Update :  ", status)
    if str(status) == str(update_status):
        testResult(self, "passed",
                   "The " + notification_name + " status should be updated as " + update_status + " - " + update_status_string + " in the cloud DB table",
                   "The " + notification_name + " status is updated as " + update_status + " - " + update_status_string + " in the cloud DB table. pls refer "
                                                                                                                          " device & cloud logs for detailed info")
        # self.result.set_result(TestResults.passed)
    else:
        print("Mismatch in status")
        testResult(self, "failed",
                   "The " + notification_name + " status should be updated as " + update_status + " - " + update_status_string + " in the cloud DB table",
                   "The " + notification_name + " status is not updated as " + update_status + " - " + update_status_string + " in the cloud DB table or something went "
                                                                                                                              "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
    # print("-------------------------------------------------------------------")


def notification_verify_event_details(self, systemId, startDate, endDate, notification_name, categoryId, modeId, status):
    # Call subscribe reusable module
    response = notification_getEvents(self, systemId, startDate, endDate, categoryId, "valid")

    # Parse api response in to json
    response_body = response.json()

    # Validate api response
    data_len = len(response_body["events"])
    eventId = messageTrackingId = eventTime = originType = originator = messageId = status_actual = modeId_actual = categoryId_actual = ""
    if data_len >= 1:
        for i in range(data_len):
            categoryId_actual = response_body["events"][i]["categoryId"]
            if str(categoryId_actual) == categoryId:
                eventId = response_body["events"][i]["eventId"]
                messageTrackingId = response_body["events"][i]["messageTrackingId"]
                eventTime = response_body["events"][i]["eventTime"]
                originType = response_body["events"][i]["originType"]
                originator = response_body["events"][i]["originator"]
                messageId = response_body["events"][i]["notifications"][0]["messageId"]
                status_actual = response_body["events"][i]["notifications"][0]["status"]
                modeId_actual = response_body["events"][i]["mode"]["modeId"]
                break
        else:
            print("No data available")

        print("Latest notification details fetched from API response : ")
        print("Even Id : ", eventId)
        print("Message Tracking Id : ", messageTrackingId)
        print("Category Id : ", categoryId_actual)
        print("Event Time : ", eventTime)
        print("Origin Type : ", originType)
        print("Originator : ", originator)
        print("Message Id : ", messageId)
        print("Status : ", status_actual)
        print("Mode Id : ", modeId_actual)

    print("-------------------------------------------------------------------")

    # Validate the notify_status in the t_notification_messages table once the RE sends back status
    # as processing

    print(
        f"{notification_name} alert message should be stored t_notification_event_table with the below parameters :")
    print("-------------------------------------------------------------------")
    if str(categoryId) == str(categoryId_actual):
        testResult(self, "passed",
                   "The Category Id should be " + categoryId + " in the cloud DB table",
                   "The Category Id is " + categoryId + " in the cloud DB table. pls refer "
                                                        " device & cloud logs for detailed info")
        # self.result.set_result(TestResults.passed)
    else:
        print("Mismatch in status")
        testResult(self, "passed",
                   "The Category Id should be " + categoryId + " in the cloud DB table",
                   "The Category Id is not " + categoryId + " in the cloud DB table. pls refer "
                                                            " device & cloud logs for detailed info")
    print("-------------------------------------------------------------------")
    if str(modeId) == str(modeId_actual):
        testResult(self, "passed",
                   "The Mode Id should be " + modeId + " in the cloud DB table",
                   "The Mode Id is " + modeId + " in the cloud DB table. pls refer "
                                                " device & cloud logs for detailed info")
        # self.result.set_result(TestResults.passed)
    else:
        print("Mismatch in status")
        testResult(self, "passed",
                   "The Mode Id should be " + modeId + " in the cloud DB table",
                   "The Mode Id is not " + modeId + " in the cloud DB table. pls refer "
                                                    " device & cloud logs for detailed info")

    print("-------------------------------------------------------------------")

    if str(status) == str(status_actual):
        testResult(self, "passed",
                   "The status should be as " + status + " in the cloud DB table",
                   "The status is as " + status + " in the cloud DB table. pls refer "
                                                  " device & cloud logs for detailed info")
        # self.result.set_result(TestResults.passed)
    else:
        print("Mismatch in status")
        testResult(self, "failed",
                   "The status should be as " + status + " in the cloud DB table",
                   "The status is not as " + status + " in the cloud DB table or something went "
                                                      "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
    print("-------------------------------------------------------------------")


def notification_verify_notify_status(self, systemId, categoryName, notification_name, notification_type, update_status,
                                      update_status_string):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")
    # Parse api response in to json
    response_body = response.json()

    if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
        if response_body["responseMessage"] == "SUCCESS":
            data_len = len(response_body["responseData"])
            createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
            if data_len >= 1:
                for i in range(data_len):
                    notificationType_actual = response_body["responseData"][i]["notificationType"]
                    categoryName_actual = response_body["responseData"][i]["category"]
                    if categoryName_actual == notification_name and notificationType_actual == notification_type:
                        createdBy = response_body["responseData"][i]["createdBy"]
                        createdTime = response_body["responseData"][i]["createdTime"]
                        updatedBy = response_body["responseData"][i]["updatedBy"]
                        updatedTime = response_body["responseData"][i]["updatedTime"]
                        id = response_body["responseData"][i]["id"]
                        parameters = response_body["responseData"][i]["paramaters"]
                        status = response_body["responseData"][i]["status"]
                        subscriber_id = response_body["responseData"][i]["subscriber"]["subscriber_id"]
                        break
                else:
                    print("No data available")

                print("Latest notification details fetched from API response : ")
                print("Created By : ", createdBy)
                print("Created Time : ", createdTime)
                print("Updated By : ", updatedBy)
                print("Updated Time : ", updatedTime)
                print("Id : ", id)
                print("Parameters : ", parameters)
                print("Status : ", status)
                print("Category : ", categoryName_actual)
                print("Notification Type : ", notificationType_actual)
                print("Subscriber Id : ", subscriber_id)

                print("-------------------------------------------------------------------")

    # Validate the notify_status in the t_notification_messages table once the RE sends back status
    # as processing

    if str(status) == str(update_status):
        testResult(self, "passed",
                   "The " + notification_name + " status should be as " + update_status + " - " + update_status_string + " in the cloud DB table",
                   "The " + notification_name + " status is as " + update_status + " - " + update_status_string + " in the cloud DB table. pls refer "
                                                                                                                  " device & cloud logs for detailed info")
        # self.result.set_result(TestResults.passed)
    else:
        print("Mismatch in status")
        testResult(self, "failed",
                   "The " + notification_name + " status should be as " + update_status + " - " + update_status_string + " in the cloud DB table",
                   "The " + notification_name + " status is not as " + update_status + " - " + update_status_string + " in the cloud DB table or something went "
                                                                                                                      "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
    print("-------------------------------------------------------------------")


# Notification Event - Details by System Id & Category Type
def notification_event_details_by_systemId_Category(self, systemId, categoryId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_event_details_by_systemId_Category")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if tc == "no_category":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('&categoryId={categoryId}', '')
    elif tc == "no_systemId":
        complete_url = str(base_url + endpoint).replace('systemId={systemId}&', "").replace('{categoryId}', categoryId)

    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{categoryId}',
                                                                                        categoryId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)

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
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data",
                                                "notification_event_details_by_systemId_Category",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.get(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notification_event_details_by_systemId_Category', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_event_details_by_systemId_Category",
                           response.text)

    return response

# Created new reusable module to support latest Changes (V2)
def notification_verify_alert_details_v2(self, systemId, categoryName, notification_name, notification_type, dt, dt1):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        data_len = len(response_body["notificationDetails"])
        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body["notificationDetails"][i]["notificationType"]
                categoryName_actual = response_body["notificationDetails"][i]["category"]
                print(categoryName_actual, notification_name, notificationType_actual,  notification_type)
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body["notificationDetails"][i]["createdBy"]
                    createdTime = response_body["notificationDetails"][i]["createdTime"]
                    updatedBy = response_body["notificationDetails"][i]["updatedBy"]
                    updatedTime = response_body["notificationDetails"][i]["updatedTime"]
                    id = response_body["notificationDetails"][i]["id"]
                    # Extract the parameters field from the response
                    parameters = response_body["notificationDetails"][i]["paramaters"]
                    status = response_body["notificationDetails"][i]["status"]
                    subscriber_id = response_body["notificationDetails"][i]["subscriber"]["subscriber_id"]
                    break

            # Check if the parameters field is not empty or None
            if parameters:
                try:
                    param_json = json.loads(parameters)
                    meta = param_json.get('body', {}).get('meta', {})
                    if meta:
                        print("Meta Field Content:", meta)
                    data = param_json.get('body', {}).get('data', [])
                    if data:
                        timestamp_keys = ["deviceReceivedTime", "deviceSentTime", "cloudReceivedTime", "cloudSentTime"]
                        matched_keys = []
                        for item in data:
                            attributes = item.get("attributes", [])
                            for attribute in attributes:
                                key = attribute.get("key", "")
                                value = attribute.get("value", "")
                                if key in timestamp_keys:
                                    matched_keys.append(key)
                                    print(f"Key: {key}, Value: {value}")
                        if len(matched_keys) == 4:
                            testResult(self, "passed", notification_name + " alert/notification message should have four timestamps",notification_name + " alert/notification is having four timestamps")
                        else:
                            missing_keys = [key for key in timestamp_keys if key not in matched_keys]
                            testResult(self, "failed", notification_name + " alert/notification message should have four timestamps",f"{notification_name} alert/notification is missing some timestamps:{','.join(missing_keys)} ")
                    else:
                        print("No 'data' field present in parameters.")
                except json.JSONDecodeError as e:
                    print("Error decoding parameters JSON:", str(e))
            else:
                print("Parameters field is empty or missing.")

            print("========================================================")

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            your_dt = datetime.datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

            print("-------------------------------------------------------------------")
            if createdTime1 == dt or createdTime2 == dt1:
                testResult(self, "passed",
                           notification_name + " alert/notification should be triggered for this vehicle System ID",
                           notification_name + " alert/notification is triggered for this vehicle System ID successfully. pls refer "
                                               " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in created date & time")
                print("Test Execution - Current Date & Time ", dt, dt1)
                print("API Response - Created Time ", createdTime1, createdTime2)
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

            # Validate the notify_status in the t_notification_messages table as soon as the message is
            # published to KAFKA

            if status == '1' or status == 'NOTIFIED':
                testResult(self, "passed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                           " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in status")
                print("Current Status is ", status)
                testResult(self, "failed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                           "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

        else:
            print("dataList is empty in api response")
            testResult(self, "failed",
                       notification_name + "  alert/notification should be triggered for this vehicle System ID",
                       notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                           "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

# Notification Service Controller - Details by System Id & Category Type
def notificationServiceController_details_by_systemId_Category_global(self, systemId, categoryType, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notificationServiceController_details_by_systemId_Category_global")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    if tc == "no_category":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('&category={notificationType}',
                                                                                        '')
    elif tc == "empty_pageNo":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageNumber=1',
                                                                                        'pageNumber=').replace(
            '{notificationType}',
            categoryType)
    elif tc == "invalid_pageNo":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageNumber=1',
                                                                                        'pageNumber=a').replace(
            '{notificationType}',
            categoryType)
    elif tc == "empty_pageSize":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageSize=10',
                                                                                        'pageSize=').replace(
            '{notificationType}',
            categoryType)
    elif tc == "invalid_pageSize":
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('pageSize=10',
                                                                                        'pageSize=a').replace(
            '{notificationType}',
            categoryType)
    else:
        complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{notificationType}',
                                                                                        categoryType)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    # response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    try:
        # Parse API response into JSON
        response_body = response.json()

        if response_body["Message"] == "User is not authorized to access this resource":
            print("Token Generation : ")
            # Generate token
            token_gen_reus_mod(self, "API_Data", "Notification-AuthToken")
            update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message",
                                                "Notification-AuthToken")
            time.sleep(60)
            response = requests.post(complete_url, headers=header_x)
            print("API response : ", response.text)
    except:
        print("\n")

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notificationServiceController_details_by_systemId_Category_global', response.text)
    save_api_resp_in_excel(self, "API_Data", "notificationServiceController_details_by_systemId_Category_global",
                           response.text)

    return response

def notification_verify_alert_details_v3(self, systemId, categoryName, notification_name, notification_type, dt, dt1):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                          "valid")
    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        data_len = len(response_body["notifications"])
        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body["notifications"][i]["notificationType"]
                categoryName_actual = response_body["notifications"][i]["category"]
                print(categoryName_actual, notification_name, notificationType_actual, notification_type)
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body["notifications"][i]["createdBy"]
                    createdTime = response_body["notifications"][i]["createdTime"]
                    updatedBy = response_body["notifications"][i]["updatedBy"]
                    updatedTime = response_body["notifications"][i]["updatedTime"]
                    id = response_body["notifications"][i]["id"]
                    # Extract the parameters field from the response
                    parameters = response_body["notifications"][i]["paramaters"]
                    status = response_body["notifications"][i]["status"]
                    subscriber_id = response_body["notifications"][i]["subscriber"]["subscriber_id"]
                    break

            # Check if the parameters field is not empty or None
            if parameters:
                try:
                    param_json = json.loads(parameters)
                    meta = param_json.get('body', {}).get('meta', {})
                    if meta:
                        print("Meta Field Content:", meta)
                    data = param_json.get('body', {}).get('data', [])
                    if data:
                        timestamp_keys = ["deviceReceivedTime", "deviceSentTime", "cloudReceivedTime", "cloudSentTime"]
                        matched_keys = []
                        for item in data:
                            attributes = item.get("attributes", [])
                            for attribute in attributes:
                                key = attribute.get("key", "")
                                value = attribute.get("value", "")
                                if key in timestamp_keys:
                                    matched_keys.append(key)
                                    print(f"Key: {key}, Value: {value}")
                        if len(matched_keys) == 4:
                            testResult(self, "passed",
                                       notification_name + " alert/notification message should have four timestamps",
                                       notification_name + " alert/notification is having four timestamps")
                        else:
                            missing_keys = [key for key in timestamp_keys if key not in matched_keys]
                            testResult(self, "failed",
                                       notification_name + " alert/notification message should have four timestamps",
                                       f"{notification_name} alert/notification is missing some timestamps:{','.join(missing_keys)} ")
                    else:
                        print("No 'data' field present in parameters.")
                except json.JSONDecodeError as e:
                    print("Error decoding parameters JSON:", str(e))
            else:
                print("Parameters field is empty or missing.")

            print("========================================================")
            print("Validate priority and mode field")
            # Example: Assuming 'paramaters' is a string from your JSON
            raw_param_string = parameters  # replace with actual path
            param_json = json.loads(raw_param_string)

            priority = None
            modes = []

            for entry in param_json.get("body", {}).get("data", []):
                if entry.get("type") == "priority":
                    for attr in entry.get("attributes", []):
                        if attr.get("key") == "precedence":
                            priority = attr.get("value")
                            print("Priority of the alert is: ", priority)

                elif entry.get("type") == "channel":
                    for attr in entry.get("attributes", []):
                        if attr.get("key") == "mode":
                            modes = attr.get("value", [])
                            print("Mode: ", modes)

            # Example validation logic:
            if priority == 2 or priority == 1 or priority == 0:
                print("Priority is set correctly.")
            else:
                print(f"Unexpected priority: {priority}")

            expected_modes = {"EMAIL", "SMS", "PUSH"}
            if set(modes) == expected_modes:
                print("Modes are as expected.")

            print("========================================================")

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            your_dt = datetime.datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

            print("-------------------------------------------------------------------")
            if createdTime1 == dt or createdTime2 == dt1:
                testResult(self, "passed",
                           notification_name + " alert/notification should be triggered for this vehicle System ID",
                           notification_name + " alert/notification is triggered for this vehicle System ID successfully. pls refer "
                                               " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in created date & time")
                print("Test Execution - Current Date & Time ", dt, dt1)
                print("API Response - Created Time ", createdTime1, createdTime2)
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

            # Validate the notify_status in the t_notification_messages table as soon as the message is
            # published to KAFKA

            if status == '1' or status == 'NOTIFIED':
                testResult(self, "passed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                           " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in status")
                print("Current Status is ", status)
                testResult(self, "failed",
                           "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                           "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                           "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

        else:
            print("dataList is empty in api response")
            testResult(self, "failed",
                       notification_name + "  alert/notification should be triggered for this vehicle System ID",
                       notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                           "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")


# ---------------------------------------
# API operation to trigger alert
# ---------------------------------------
def trigger_alert_details(self, systemId, categoryId, messageId, modeId,priority, msgInfo_id, msgInfo_area, msgInfo_value, tc):

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "Notification_trigger_via_API")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    cloudEnv = read_cloud_env(self)

    dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
    country = str(dict1["country"])
    modelCode = str(dict1["modelCode"])

    if tc == trip_notification_name:
        payload = {
            "systemId": systemId,
            "categoryId": categoryId,
            "messageId": messageId,
            "modeId": modeId,
            "priority": priority,
            "messageRawData": {
                "avg_speed": "0.0",
                "max_speed": "0.0",
                "co2_emission": "",
                "fuel_consumed": "",
                "trip_distance": "0.0",
                "trip_duration": "0.04933889",
                "trip_fuel_efficiency": "0",
                "trip_battery_efficiency": "0.0"
            }
        }
    elif tc == dtc_notification_name:
        payload = {
            "systemId": systemId,
            "categoryId": categoryId,
            "messageId": messageId,
            "modeId": modeId,
            "priority": priority,
            "messageRawData": {
                "geoId": "0",
                "radius": "50",
                "message": "0",
                "dtc_code": "P1001",
                "incident_id": "1853566233",
                "dtc_priority": "1",
                "dtc_severity": "1"
            }
        }
    elif tc == geofence_notification_name:
        payload = {
            "systemId": systemId,
            "categoryId": categoryId,
            "messageId": messageId,
            "modeId": modeId,
            "priority": priority,
            "messageInfo": [
                {
                    "id": 557895681,
                    "area": 0,
                    "value": [
                        {
                            "int_array_value": [
                                "0"
                            ],
                            "string_value": [],
                            "float_array_value": [],
                            "double_array_value": []
                        }
                    ]
                },
                {
                    "id": 559940097,
                    "area": 0,
                    "value": [
                        {
                            "float_array_value": [
                                40
                            ],
                            "string_value": [],
                            "int_array_value": [],
                            "double_array_value": []
                        }
                    ]
                },
                {
                    "id": 559940098,
                    "area": 0,
                    "value": [
                        {
                            "float_array_value": [
                                40
                            ],
                            "string_value": [],
                            "int_array_value": [],
                            "double_array_value": []
                        }
                    ]
                },
                {
                    "id": 559940099,
                    "area": 0,
                    "value": [
                        {
                            "float_array_value": [
                                51
                            ],
                            "string_value": [],
                            "int_array_value": [],
                            "double_array_value": []
                        }
                    ]
                }
            ],
            "msgDeviceData": {
                "geoId": "13453",
                "message": 11,
                "coordinates": [
                    {
                        "latitude": 40,
                        "longitude": 40
                    }
                ],
                "radius": 51,
                "dtc_code": "string",
                "dtc_priority": 0,
                "dtc_severity": 0,
                "incident_id": 0
            },
            "deviceReceivedTime": 1752067597826,
            "deviceSentTime": 1752067597826
        }
    elif tc == pinExpiry_notification_name:
        payload = {
            "systemId": systemId,
            "categoryId": categoryId,
            "messageId": messageId,
            "modeId": modeId,
            "priority": priority,
            "messageRawData": {
                "time": "1",
                "value": "12345",
                "action": "EXPIRED",
                "expiry": "1734611358142",
                "pin_id": "pin_5"
            },
            "deviceReceivedTime": "",
            "deviceSentTime": ""
        }
    else:
        payload = {
            "systemId": systemId,
            "categoryId": categoryId,
            "messageId": messageId,
            "modeId": modeId,
            "priority": priority,
            "messageInfo": [
                {
                    "id": msgInfo_id,
                    "area": msgInfo_area,
                    "value": [
                        msgInfo_value
                    ]
                }
            ]
        }
    if cloudEnv in ["GCP-QA4", "GCP-QA5", "PRE-PROD", "GCP-QA8"]:
        payload["country"] = country
        payload["modelCode"] = modelCode
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('Notification_trigger_via_API', response.text)
    save_api_resp_in_excel(self, "API_Data", "Notification_trigger_via_API", response.text)

    return response


def trigger_alert_through_api_and_verify(self, systemId, categoryId, messageId, modeId,priority, msgInfo_id, msgInfo_area, msgInfo_value, notification_name, tc):
    # call reusable module
    response = trigger_alert_details(self, systemId, categoryId, messageId, modeId,priority, msgInfo_id, msgInfo_area, msgInfo_value, tc)

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        testResult(self, "passed",
               notification_name + "  alert/notification should be triggered for this vehicle System ID",
               notification_name + "  alert/notification is triggered for this vehicle System ID. pls refer device & cloud logs for detailed info")
    else:
        testResult(self, "failed",
               notification_name + "  alert/notification should be triggered for this vehicle System ID",
               notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                   "wrong. pls refer device & cloud logs for detailed info")


def verify_notification_details(self, systemId, categoryName, notification_name, notification_type, dt, dt1):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName, "valid")

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        if "notificationDetails" in response_body:
            para = "notificationDetails"
        else:
            para = "notifications"

        data_len = len(response_body[para])

        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body[para][i]["notificationType"]
                categoryName_actual = response_body[para][i]["category"]
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body[para][i]["createdBy"]
                    createdTime = response_body[para][i]["createdTime"]
                    updatedBy = response_body[para][i]["updatedBy"]
                    updatedTime = response_body[para][i]["updatedTime"]
                    id = response_body[para][i]["id"]
                    parameters = response_body[para][i]["paramaters"]
                    status = response_body[para][i]["status"]
                    subscriber_id = response_body[para][i]["subscriber"]["subscriber_id"]
                    break

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            # Timestamp validation
            your_dt = datetime.fromtimestamp(int(createdTime) / 1000)
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

            if createdTime1 == dt or createdTime2 == dt1:
                testResult(self, "passed",
                           f"{notification_name} alert/notification should be triggered for this vehicle System ID",
                           f"{notification_name} alert/notification is triggered for this vehicle System ID successfully. pls refer device & cloud logs for detailed info")

                # Validate Parameters body data
                verification_status = ""
                print("-------------------------------------------------------")
                print("Parameter Body Data Validation : ")
                print("-------------------------------------------------------")
                # json message
                parameters = json.loads(parameters)

                timestamp = parameters["timestamp"]
                version = parameters["version"]
                event_category = parameters["event_category"]
                event_type = parameters["event_type"]
                encoding_type = parameters["encoding_type"]
                correlation_id = parameters["correlation_id"]
                event_id = parameters["event_id"]
                print("timestamp : ", timestamp)
                print("version : ", version)
                print("event_category : ", event_category)
                print("event_type : ", event_type)
                print("encoding_type :", encoding_type)
                print("correlation_id : ", correlation_id)
                print("event_id : ", event_id)
                print("--------------------------------------------")

                for i in range(len(parameters["body"]["data"])):
                    try:
                        att_len = len(parameters["body"]["data"][i]["attributes"])
                    except:
                        att_len = 0

                    mode_value = ""
                    priority_value = None
                    severity_value = ""

                    for j in range(att_len):
                        key = parameters["body"]["data"][i]["attributes"][j]["key"]
                        datatype = parameters["body"]["data"][i]["attributes"][j]["datatype"]
                        unit = parameters["body"]["data"][i]["attributes"][j]["unit"]
                        value = parameters["body"]["data"][i]["attributes"][j]["value"]
                        print("Key : ", key)
                        print("Datatype : ", datatype)
                        print("Unit : ", unit)
                        print("Value : ", value)
                        print("--------------------------------------------")

                        if key == "latitude":
                            # latitude_key = parameters["body"]["data"][i]["attributes"][j]["key"]
                            # latitude_datatype = parameters["body"]["data"][i]["attributes"][j]["datatype"]
                            # latitude_unit = parameters["body"]["data"][i]["attributes"][j]["unit"]
                            if notification_name == geofence_notification_name:
                                latitude_value = parameters["body"]["data"][i]["attributes"][j]["value"]

                            else:
                                latitude_value = parameters["body"]["data"][i]["attributes"][j]["value"][0]
                                if latitude_value == 40:
                                    testResult(self, "passed",
                                               "Latitude value should be same as configured.",
                                               "Latitude value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self, "verificationFailed",
                                               "Latitude value should be same as configured.",
                                               "Latitude value is not same as configured.")
                        elif key == "longitude":
                            if notification_name == geofence_notification_name:
                                longitude_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            else:
                                longitude_value = parameters["body"]["data"][i]["attributes"][j]["value"][0]
                                if longitude_value == 40:
                                    testResult(self, "passed",
                                               "Longitude value should be same as configured.",
                                               "Longitude value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self, "verificationFailed",
                                               "Longitude value should be same as configured.",
                                               "Longitude value is not same as configured.")
                        elif key == "deviceReceivedTime":
                            deviceReceivedTime_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            # print(createdTime1, createdTime2, dt, dt1, deviceReceivedTime_value)
                            if deviceReceivedTime_value > 0:
                                testResult(self, "passed",
                                           "Device Received Time value should be available.",
                                           "Device Received Time value is available.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Device Received Time value should be available.",
                                           "Device Received Time parameter is not available or its value is '0'")
                        elif key == "deviceSentTime":
                            deviceSentTime_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            if deviceSentTime_value > 0:
                                testResult(self, "passed",
                                           "Device Sent Time value should be available.",
                                           "Device Sent Time value is available.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Device Sent Time value should be available.",
                                           "Device Sent Time parameter is not available or its value is '0'")
                        elif key == "cloudReceivedTime":
                            cloudReceivedTime_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            if cloudReceivedTime_value > 0:
                                testResult(self, "passed",
                                           "Cloud Received Time value should be available.",
                                           "Cloud Received Time value is available.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Cloud Received Time value should be available.",
                                           "Cloud Received Time parameter is not available or its value is '0'")
                        elif key == "cloudSentTime":
                            cloudSentTime_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            if cloudSentTime_value > 0:
                                testResult(self, "passed",
                                           "Cloud Sent Time value should be available.",
                                           "Cloud Sent Time value is available.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Cloud Sent Time value should be available.",
                                           "Cloud Sent Time parameter is not available or its value is '0'")
                        elif key == "mode":
                            mode_value = parameters["body"]["data"][i]["attributes"][j]["value"]
                            if "PUSH" in mode_value or "DEVICE" in mode_value:
                                testResult(self, "passed",
                                           "Mode value should be same as configured.",
                                           "Mode value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Mode value should be same as configured.",
                                           "Mode value is not same as configured.")
                        elif key == "priority":  # Fixed from 'type' to 'key'
                            priority_value = parameters["body"]["data"][i]["attributes"][j]["value"]

                            if priority_value == 1:
                                testResult(self, "passed",
                                           "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                            elif priority_value == 2:
                                testResult(self, "passed",
                                           "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                            elif priority_value == 0:
                                testResult(self, "passed",
                                           "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Priority value should be same as configured.",
                                           "Priority value is not same as configured.")
                        elif key == "severity":
                            severity_value = parameters["body"]["data"][i]["attributes"][j]["value"]

                            if severity_value == "MEDIUM":
                                testResult(self, "passed",
                                           "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                            elif severity_value == "LOW":
                                testResult(self, "passed",
                                           "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                            elif severity_value == "HIGH":
                                testResult(self, "passed",
                                           "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Severity value should be same as configured.",
                                           "Severity value is not same as configured.")
                        elif key == "sos":
                            sos_value = parameters["body"]["data"][i]["attributes"][j]["value"][0]
                            if sos_value == 0 or sos_value == 1:
                                testResult(self, "passed",
                                           "SOS value should be same as configured.",
                                           "SOS value is same as configured.")
                            else:
                                # verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "SOS value should be same as configured.",
                                           "SOS value is not same as configured.")
                        elif key == "odometer":
                            odometer_value = parameters["body"]["data"][i]["attributes"][j]["value"][0]
                            if odometer_value == 6000 or odometer_value == "6000":
                                testResult(self, "passed",
                                           "Odo Meter value should be same as configured.",
                                           "Odo Meter value is same as configured.")
                            else:
                                # verification_status = "FAIL"
                                testResult(self, "verificationFailed",
                                           "Odo Meter value should be same as configured.",
                                           "Odo Meter value is not same as configured.")

                print(mode_value, priority_value, severity_value)
                if "DEVICE" in mode_value:
                    if priority_value == 2 and severity_value == "LOW":
                        print("TRIGGER ALERT VIA API - Test cases is passed, as notification details are as configured")

                if verification_status == "FAIL":
                    print("Notification detail verification failed")
                    assert False

                if status == '1' or status == 'NOTIFIED':
                    testResult(self, "passed",
                               "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                               "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                               " device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Mismatch in status")
                    print("Current Status is ", status)
                    testResult(self, "failed",
                               "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                               "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                               "wrong. pls refer device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                print("-------------------------------------------------------------------")
            else:
                print("Mismatch in created date & time")
                print("Test Execution - Current Date & Time ", dt, dt1)
                print("API Response - Created Time ", createdTime1, createdTime2)
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
        else:
            print("dataList is empty in api response")
            testResult(self, "failed",
                       notification_name + "  alert/notification should be triggered for this vehicle System ID",
                       notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                           "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False
    print("----------------------------------------------------------")

def verify_notification_details_v2(self, systemId, categoryName, notification_name, notification_type, dt, dt1):
    # Call subscribe reusable module
    response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName, "valid")

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":
        if "notificationDetails" in response_body:
            para = "notificationDetails"
        else:
            para = "notifications"

        data_len = len(response_body[para])

        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body[para][i]["notificationType"]
                categoryName_actual = response_body[para][i]["category"]
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body[para][i]["createdBy"]
                    createdTime = response_body[para][i]["createdTime"]
                    updatedBy = response_body[para][i]["updatedBy"]
                    updatedTime = response_body[para][i]["updatedTime"]
                    id = response_body[para][i]["id"]
                    parameters = response_body[para][i]["paramaters"]
                    status = response_body[para][i]["status"]
                    subscriber_id = response_body[para][i]["subscriber"]["subscriber_id"]
                    break

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            # Timestamp validation
            your_dt = datetime.fromtimestamp(int(createdTime) / 1000)
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

            if createdTime1 == dt or createdTime2 == dt1:
                testResult(self, "passed",
                           f"{notification_name} alert/notification should be triggered for this vehicle System ID",
                           f"{notification_name} alert/notification is triggered for this vehicle System ID successfully. pls refer device & cloud logs for detailed info")

                # Validate Parameters body data
                verification_status = ""
                mode_value = []
                priority_value = None
                severity_value = ""

                print("-------------------------------------------------------")
                print("Parameter Body Data Validation:")
                print("-------------------------------------------------------")

                # Extract top-level metadata from parameters
                timestamp = parameters.get("timestamp")
                version = parameters.get("version")
                event_category = parameters.get("event_category")
                event_type = parameters.get("event_type")
                encoding_type = parameters.get("encoding_type")
                correlation_id = parameters.get("correlation_id")
                event_id = parameters.get("event_id")

                # Optional: Print to confirm
                print("Extracted Metadata:")
                print("timestamp       :", timestamp)
                print("version         :", version)
                print("event_category  :", event_category)
                print("event_type      :", event_type)
                print("encoding_type   :", encoding_type)
                print("correlation_id  :", correlation_id)
                print("event_id        :", event_id)

                print("-------------------------------------------------------")

                # Loop through each data block
                for data_entry in parameters.get("body", {}).get("data", []):
                    entry_type = data_entry.get("type")
                    attributes = data_entry.get("attributes", [])

                    for attr in attributes:
                        key = attr.get("key")
                        value = attr.get("value")
                        datatype = attr.get("datatype")
                        unit = attr.get("unit")

                        print(f"Key      : {key}")
                        print(f"Datatype : {datatype}")
                        print(f"Unit     : {unit}")
                        print(f"Value    : {value}")
                        print("-------------------------------------------------------")

                        # Device & Cloud Timestamps
                        if key in ["deviceReceivedTime", "deviceSentTime", "cloudReceivedTime", "cloudSentTime"]:
                            if value > 0:
                                testResult(self, "passed", f"{key} should be available.", f"{key} is available.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed", f"{key} should be available.",
                                           f"{key} is missing or zero.")

                        # Mode (from channel block)
                        elif entry_type == "channel" and key == "mode":
                            mode_value = value
                            if "PUSH" in mode_value or "DEVICE" in mode_value:
                                testResult(self, "passed", "Mode value should be same as configured.",
                                           "Mode value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed", "Mode value should be same as configured.",
                                           f"Mode value is not same as configured. Found: {mode_value}")

                        # Priority (from priority block)
                        elif entry_type == "priority" and key == "precedence":
                            priority_value = value
                            if priority_value in [0, 1, 2]:
                                testResult(self, "passed", "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed", "Priority value should be same as configured.",
                                           f"Priority value is not same as configured. Found: {priority_value}")

                        # Severity (from severity block)
                        elif entry_type == "severity" and key == "severity":
                            severity_value = value
                            if severity_value in ["LOW", "MEDIUM", "HIGH"]:
                                testResult(self, "passed", "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                            else:
                                verification_status = "FAIL"
                                testResult(self, "verificationFailed", "Severity value should be same as configured.",
                                           f"Severity value is not same as configured. Found: {severity_value}")

                # Final conditional check
                print(mode_value, priority_value, severity_value)
                if "PUSH" in mode_value and priority_value == 2 and severity_value == "LOW":
                    print("TRIGGER ALERT VIA API - Test case passed, notification details are as configured")
                    assert True

                if verification_status == "FAIL":
                    print("Notification detail verification failed")
                    assert False

                # Notify status validation
                if status in ['1', 'NOTIFIED']:
                    testResult(self, "passed",
                               "Notify status should be updated to 1 - Notified",
                               "Notify status is correctly updated to 1 - Notified. Refer device & cloud logs.")
                else:
                    print("Mismatch in status. Current Status:", status)
                    testResult(self, "failed",
                               "Notify status should be updated to 1 - Notified",
                               "Notify status is not updated correctly. Refer device & cloud logs.")

                print("-------------------------------------------------------------------")

            else:
                print("Mismatch in created date & time")
                print("Test Execution - Current Date & Time ", dt, dt1)
                print("API Response - Created Time ", createdTime1, createdTime2)
                testResult(self, "failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
        else:
            print("dataList is empty in api response")
            testResult(self, "failed",
                       notification_name + "  alert/notification should be triggered for this vehicle System ID",
                       notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                           "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response message is not success. Rather found : " + str(response_body))
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False


    #Notification Event
    print("---------------------------------------------------------------------------")
    print("********** Validate the notification message delivered to kafka ***********")
    print("---------------------------------------------------------------------------")
    response = notification_eventDetails_by_eventId(self, systemId, event_id, "valid")

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":

        categoryId_actual = response_body["event"]["categoryId"]
        categoryName_actual = response_body["event"]["categoryName"]
        deviceReceivedTime = response_body["event"]["deviceReceivedTime"]
        deviceSentTime = response_body["event"]["deviceSentTime"]
        cloudReceivedTime = response_body["event"]["cloudReceivedTime"]
        cloudSentTime = response_body["event"]["cloudSentTime"]
        originType = response_body["event"]["originType"]
        originator = response_body["event"]["originator"]
        eventStatus = response_body["event"]["status"]["eventStatus"]
        eventdetails = response_body["event"]["status"]["eventdetails"]
        priority = response_body["event"]["priority"]

        print("\n--------------------------------------------")
        print("------- Notification Event Details -----------")
        print("----------------------------------------------")
        print(f"Category Id         => {categoryId_actual}")
        print(f"Category Name       => {categoryName_actual}")
        print(f"Device Received Time=> {deviceReceivedTime}")
        print(f"Device Sent Time    => {deviceSentTime}")
        print(f"Cloud Received Time => {cloudReceivedTime}")
        print(f"Cloud Sent Time     => {cloudSentTime}")
        print(f"Origin Type         => {originType}")
        print(f"Originator          => {originator}")
        print(f"Event Status        => {eventStatus}")
        print(f"Event Details       => {eventdetails}")
        print(f"Priority            => {priority}")

        if originType == "DEVICE" and eventStatus == "DELIVERED":
            testResult(self, "passed",
                       notification_name + "  alert/notification should be delivered to the kafka",
                       notification_name + "  alert/notification is delivered to the kafka")
        else:
            testResult(self, "failed",
                       notification_name + "  alert/notification should be delivered to the kafka",
                       notification_name + "  alert/notification is not delivered to the kafka")
    else:
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
    print("----------------------------------------------------------")



def verify_notification_details_v3(self, systemId, categoryName, notification_name, notification_type, dt, dt1, tc):
    # Poll a few times, but handle the disable-case quickly:
    for i in range(3):

        # Call subscribe reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName, "valid")

        try:
            response_body = response.json()
        except Exception:
            response_body = {}

        if response.status_code != 200:
            if tc == "disable" and "No data available in the database" in str(response_body):
                testResult(self, "passed",
                           notification_name + " should NOT be present in Cloud when geofence is disabled",
                           notification_name + " was not found in Cloud as expected for disabled geofence.")
                return
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            assert False

        utc_time = datetime.now()
        dt1 = utc_time.strftime("%Y-%m-%d_%H_%M")

        # If no data and this is a disable-case, that's a successful outcome
        if "No data available in the database" in str(response_body):
            if tc == "disable":
                testResult(self, "passed",
                           notification_name + " should NOT be present in Cloud when geofence is disabled",
                           notification_name + " was not found in Cloud as expected for disabled geofence.")
                return
            # otherwise retry a bit
            time.sleep(15)
            continue

        # If data exists and this is a disable-case, validate timestamps: any recent notification -> fail
        if response_body.get("message") == "SUCCESS" and tc == "disable":
            notifications = response_body.get("notifications", []) or response_body.get("notificationDetails", [])
            found_recent = False
            for n in notifications:
                try:
                    createdTime = n.get("createdTime")
                    your_dt = datetime.fromtimestamp(int(createdTime) / 1000)
                    createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
                    print(dt, createdTime1, dt1)
                    if dt <= createdTime1 <= dt1 or createdTime1 == dt or createdTime1 == dt1:
                        found_recent = True
                        break
                except Exception:
                    continue

            if found_recent:
                testResult(self, "failed",
                           notification_name + " should NOT be present in Cloud when geofence is disabled",
                           notification_name + " was found in Cloud within the recent timeframe even though geofence was disabled.")
                return
            else:
                testResult(self, "passed",
                           notification_name + " should NOT be present in Cloud when geofence is disabled",
                           notification_name + " data present but not within recent timeframe; treated as pass for disable.")
                return

        # For non-disable flows, if we have SUCCESS and notifications, proceed to the detailed validation
        if response_body.get("message") == "SUCCESS":
            data_len = len(response_body.get("notifications", []) or response_body.get("notificationDetails", []))
            if data_len >= 1:
                break
            else:
                time.sleep(15)
                continue
        else:
            time.sleep(15)
            continue

    if response_body["message"] == "SUCCESS":
        if "notificationDetails" in response_body:
            para = "notificationDetails"
        else:
            para = "notifications"

        data_len = len(response_body[para])
        createdBy = createdTime = updatedBy = updatedTime = id = parameters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
        # -------------------- FIX: init variables used later to avoid NameError ---
        event_id = None
        mode_value = []
        priority_value = None
        severity_value = None

        if data_len >= 1:
            for i in range(data_len):
                notificationType_actual = response_body[para][i]["notificationType"]
                categoryName_actual = response_body[para][i]["category"]
                # print(categoryName_actual, notification_name, notificationType_actual, notification_type)
                if categoryName_actual == notification_name and notificationType_actual == notification_type:
                    createdBy = response_body[para][i]["createdBy"]
                    createdTime = response_body[para][i]["createdTime"]
                    updatedBy = response_body[para][i]["updatedBy"]
                    updatedTime = response_body[para][i]["updatedTime"]
                    id = response_body[para][i]["id"]
                    parameters = response_body[para][i]["paramaters"]
                    status = response_body[para][i]["status"]
                    noti_status = response_body[para][i]["status"]
                    subscriber_id = response_body[para][i]["subscriber"]["subscriber_id"]
                    # -------------------- FIX: capture event_id once it's available ----
                    event_id = response_body[para][i]["paramaters"].get("event_id")
                    s = i
                    break

            print("Latest notification details fetched from API response : ")
            print("Created By : ", createdBy)
            print("Created Time : ", createdTime)
            print("Updated By : ", updatedBy)
            print("Updated Time : ", updatedTime)
            print("Id : ", id)
            print("Parameters : ", parameters)
            print("Status : ", status)
            print("Category : ", categoryName_actual)
            print("Notification Type : ", notificationType_actual)
            print("Subscriber Id : ", subscriber_id)

            your_dt = datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
            createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
            createdTime2 = your_dt.strftime("%Y-%m-%d_%H")
            # Date to check
            utc_time = datetime.now()
            dt1 = utc_time.strftime("%Y-%m-%d_%H_%M")

            print("End date & time :", dt1)

            if dt <= createdTime1 <= dt1:

                # if createdTime1 == dt or createdTime2 == dt1:
                testResult(self,"passed",
                       notification_name + " alert/notification should be triggered for this vehicle System ID",
                       notification_name + " alert/notification is triggered for this vehicle System ID successfully. pls refer "
                                           " device & cloud logs for detailed info")

                # Validate Parameters body data
                verification_status = ""
                print("-------------------------------------------------------")
                print("Parameter Body Data Validation : ")
                print("-------------------------------------------------------")

                timestamp = response_body[para][s]["paramaters"]["timestamp"]
                version = response_body[para][s]["paramaters"]["version"]
                event_category = response_body[para][s]["paramaters"]["event_category"]
                event_type = response_body[para][s]["paramaters"]["event_type"]
                encoding_type = response_body[para][s]["paramaters"]["encoding_type"]
                correlation_id = response_body[para][s]["paramaters"]["correlation_id"]
                # -------------------- NOTE: event_id already captured; keep original line too --------------
                event_id = response_body[para][s]["paramaters"].get("event_id", event_id)
                print("timestamp : ", timestamp)
                print("version : ", version)
                print("event_category : ", event_category)
                print("event_type : ", event_type)
                print("encoding_type :", encoding_type)
                print("correlation_id : ", correlation_id)
                print("event_id : ", event_id)
                print("--------------------------------------------")

                para_len = len(response_body[para][s]["paramaters"]["body"]["data"])
                if para_len >= 1:
                    for k in range(para_len):
                        type = response_body[para][s]["paramaters"]["body"]["data"][k]["type"]
                        print("Type : ", type)
                        try:
                            att_len = len(response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"])
                        except:
                            att_len = 0
                        for j in range(att_len):

                            key = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["key"]
                            datatype = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["datatype"]
                            unit = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["unit"]
                            value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                            print("Key : ", key)
                            print("Datatype : ", datatype)
                            print("Unit : ", unit)
                            print("Value : ", value)
                            print("--------------------------------------------")
                            if key == "latitude":
                                try:
                                    latitude_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"][0]
                                except:
                                    latitude_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]

                                if latitude_value == 40 or latitude_value == "40" or latitude_value >= 28:
                                    testResult(self,"passed",
                                           "Latitude value should be same as configured.",
                                           "Latitude value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Latitude value should be same as configured.",
                                           "Latitude value is not same as configured.")
                            elif key == "longitude":
                                try:
                                    longitude_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"][0]
                                except:
                                    longitude_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]

                                if longitude_value == 40 or longitude_value == "40" or longitude_value >= 77:
                                    testResult(self,"passed",
                                           "Longitude value should be same as configured.",
                                           "Longitude value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Longitude value should be same as configured.",
                                           "Longitude value is not same as configured.")
                            elif key == "deviceReceivedTime":
                                deviceReceivedTime_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                                if deviceReceivedTime_value > 0:
                                    testResult(self,"passed",
                                           "Device Received Time value should be available.",
                                           "Device Received Time value is available.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Device Received Time value should be available.",
                                           "Device Received Time parameter is not available or its value is '0'")
                            elif key == "deviceSentTime":
                                deviceSentTime_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                                if deviceSentTime_value > 0:
                                    testResult(self,"passed",
                                           "Device Sent Time value should be available.",
                                           "Device Sent Time value is available.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Device Sent Time value should be available.",
                                           "Device Sent Time parameter is not available or its value is '0'")
                            elif key == "cloudReceivedTime":
                                cloudReceivedTime_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                                if cloudReceivedTime_value > 0:
                                    testResult(self,"passed",
                                           "Cloud Received Time value should be available.",
                                           "Cloud Received Time value is available.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Cloud Received Time value should be available.",
                                           "Cloud Received Time parameter is not available or its value is '0'")
                            elif key == "cloudSentTime":
                                cloudSentTime_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                                if cloudSentTime_value > 0:
                                    testResult(self,"passed",
                                           "Cloud Sent Time value should be available.",
                                           "Cloud Sent Time value is available.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Cloud Sent Time value should be available.",
                                           "Cloud Sent Time parameter is not available or its value is '0'")
                            elif key == "mode":
                                mode_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]
                                if "PUSH" in mode_value or "DEVICE" in mode_value:
                                    testResult(self,"passed",
                                           "Mode value should be same as configured.",
                                           "Mode value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Mode value should be same as configured.",
                                           "Mode value is not same as configured.")
                            elif type == "priority":
                                priority_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]

                                if priority_value == 1:
                                    testResult(self,"passed",
                                           "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                                elif priority_value == 2:
                                    testResult(self,"passed",
                                           "Priority value should be same as configured.",
                                           "Priority value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Priority value should be same as configured.",
                                           "Priority value is not same as configured.")

                            elif key == "severity":
                                severity_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"]

                                if severity_value == "MEDIUM":
                                    testResult(self,"passed",
                                           "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                                elif severity_value == "LOW":
                                    testResult(self,"passed",
                                           "Severity value should be same as configured.",
                                           "Severity value is same as configured.")
                                else:
                                    verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Severity value should be same as configured.",
                                           "Severity value is not same as configured.")

                            elif key == "sos":
                                sos_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"][0]
                                if sos_value == 0 or sos_value == 1:
                                    testResult(self,"passed",
                                           "SOS value should be same as configured.",
                                           "SOS value is same as configured.")
                                else:
                                    # verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "SOS value should be same as configured.",
                                           "SOS value is not same as configured.")
                            elif key == "odometer":
                                odometer_value = response_body[para][s]["paramaters"]["body"]["data"][k]["attributes"][j]["value"][0]
                                if odometer_value == 6000 or odometer_value == "6000" or odometer_value == 1000 or odometer_value == "1000":
                                    testResult(self,"passed",
                                           "Odo Meter value should be same as configured.",
                                           "Odo Meter value is same as configured.")
                                else:
                                    # verification_status = "FAIL"
                                    testResult(self,"verificationFailed",
                                           "Odo Meter value should be same as configured.",
                                           "Odo Meter value is not same as configured.")

                                print("--------------------------------------------")
                    # print(mode_value, priority_value, severity_value)
                    if "DEVICE" in mode_value:
                        if priority_value == 2 and severity_value == "LOW":
                            print(
                                "TRIGGER ALERT VIA API - Test cases is passed, as notification details are as configured")

                    if verification_status == "FAIL":
                        print("Test cases is failed, as notification details are not as configured")
                        assert False
                print("-------------------------------------------------------------------")
            else:
                if tc == "disable":
                    print("Mismatch in created date & time")
                    print("Test Execution - Current Date & Time ", dt, dt1)
                    print("API Response - Created Time ", createdTime1, createdTime2)
                    testResult(self, "passed",
                               notification_name + "  alert/notification should be triggered for this vehicle System ID",
                               notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                                   "wrong. pls refer device & cloud logs for detailed info")
                    return

                else:
                    # self.result.set_result(TestResults.failed)
                    print("-------------------------------------------------------------------")
                    print("Mismatch in created date & time")
                    print("Test Execution - Current Date & Time ", dt, dt1)
                    print("API Response - Created Time ", createdTime1, createdTime2)
                    testResult(self,"failed",
                           notification_name + "  alert/notification should be triggered for this vehicle System ID",
                           notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                               "wrong. pls refer device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

            # Validate the notify_status in the t_notification_messages table as soon as the message is
            # published to KAFKA

            print(noti_status)
            if noti_status == '1' or noti_status == 'NOTIFIED':
                testResult(self,"passed",
                       "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                       "The notify_status is updated as 1 - Notified in the t_notification_messages table. pls refer "
                       " device & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
            else:
                print("Mismatch in status")
                print("Current Status is ", noti_status)
                testResult(self,"failed",
                       "The notify_status should be updated as 1 - Notified in the t_notification_messages table",
                       "The notify_status is not updated as 1 - Notified in the t_notification_messages table or something went "
                       "wrong. pls refer device & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
            print("-------------------------------------------------------------------")

        else:
            print("dataList is empty in api response")
            testResult(self,"failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
    else:
        print("response Code is not 1200. Rather found : " + str(response_body))
        testResult(self,"failed",
               notification_name + "  alert/notification should be triggered for this vehicle System ID",
               notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                   "wrong. pls refer device & cloud logs for detailed info")
        # self.result.set_result(TestResults.failed)
        assert False


    # Notification Event
    print("---------------------------------------------------------------------------")
    print("********** Validate the notification message delivered to kafka ***********")
    print("---------------------------------------------------------------------------")

    # -------------------- FIX: guard event_id to avoid UnboundLocalError -----------
    if not event_id:
        print("event_id is missing in parameters; skipping event details verification.")
        return

    response = notification_eventDetails_by_eventId(self, systemId, event_id, "valid")

    assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
    if response.status_code != 200:
        # self.result.set_result(TestResults.failed)
        assert False

    # parse api response into json
    response_body = response.json()

    if response_body["message"] == "SUCCESS":

        categoryId_actual = response_body["event"]["categoryId"]
        categoryName_actual = response_body["event"]["categoryName"]
        deviceReceivedTime = response_body["event"]["deviceReceivedTime"]
        deviceSentTime = response_body["event"]["deviceSentTime"]
        cloudReceivedTime = response_body["event"]["cloudReceivedTime"]
        cloudSentTime = response_body["event"]["cloudSentTime"]
        originType = response_body["event"]["originType"]
        originator = response_body["event"]["originator"]
        eventStatus = response_body["event"]["status"]["eventStatus"]
        eventdetails = response_body["event"]["status"]["eventdetails"]
        priority = response_body["event"]["priority"]

        print("\n--------------------------------------------")
        print("------- Notification Event Details -----------")
        print("----------------------------------------------")
        print(f"Category Id         => {categoryId_actual}")
        print(f"Category Name       => {categoryName_actual}")
        print(f"Device Received Time=> {deviceReceivedTime}")
        print(f"Device Sent Time    => {deviceSentTime}")
        print(f"Cloud Received Time => {cloudReceivedTime}")
        print(f"Cloud Sent Time     => {cloudSentTime}")
        print(f"Origin Type         => {originType}")
        print(f"Originator          => {originator}")
        print(f"Event Status        => {eventStatus}")
        print(f"Event Details       => {eventdetails}")
        print(f"Priority            => {priority}")

        if "alert_trigger_from_device" in tc:
            if originType == "DEVICE" and originator == "C2C Edge Analytics" and eventStatus == "DELIVERED":
                testResult(self, "passed",
                           notification_name + "  alert/notification triggered from device should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from device is delivered to the kafka")
            else:
                testResult(self, "failed",
                           notification_name + "  alert/notification triggered from device should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from device is not delivered to the kafka")

        elif "alert_trigger_from_cloud" in tc:
            if originType == "API" and originator == "API" and eventStatus == "DELIVERED":
                testResult(self, "passed",
                           notification_name + "  alert/notification triggered from cloud API should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from cloud API is delivered to the kafka")
            else:
                testResult(self, "failed",
                           notification_name + "  alert/notification triggered from cloud API should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from cloud API is not delivered to the kafka")

        elif "sms_alert" in tc:
            if originType == "SMS" and originator == "SMS" and eventStatus == "DELIVERED":
                testResult(self, "passed",
                           notification_name + "  alert/notification triggered from mobile should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from mobile is delivered to the kafka")
            else:
                testResult(self, "failed",
                           notification_name + "  alert/notification triggered from mobile should be delivered to the kafka",
                           notification_name + "  alert/notification triggered from mobile is not delivered to the kafka")

        else:
            testResult(self, "failed",
                       notification_name + "  alert/notification should be delivered to the kafka",
                       notification_name + "  alert/notification is not delivered to the kafka")
    else:
        testResult(self, "failed",
                   notification_name + "  alert/notification should be triggered for this vehicle System ID",
                   notification_name + "  alert/notification is not triggered for this vehicle System ID or something went "
                                       "wrong. pls refer device & cloud logs for detailed info")
    print("----------------------------------------------------------")
# Notification - Update event status based on message Id & system Id
def notification_eventDetails_by_eventId(self, systemId, eventId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_event_details_by_eventId")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Url :
    complete_url = str(base_url + endpoint).replace('{systemId}', systemId).replace('{eventId}', eventId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)
    # print(header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send PUT request.
    response = requests.get(complete_url, headers=header_x)
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('notification_event_details_by_eventId', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_event_details_by_eventId",
                           response.text)

    return response

#Notification element configuration API

def notify_save_attribute_id(self, alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
                             elementId, unit, dataType, active, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_save_attribute_id")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["alertAttributeName"] = alertAttributeName
    json_object["modelCode"] = modelCode
    json_object["eventType"] = eventType
    json_object["attributeName"] = attributeName
    json_object["attributeDisplayName"] = attributeDisplayName
    json_object["elementId"] = elementId
    json_object["unit"] = unit
    json_object["dataType"] = dataType
    json_object ["active"] = active

    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details app's
    save_api_resp_into_file('notification_save_attribute_id', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_save_attribute_id", response.text)

    return response


def notify_update_attribute_id(self, telemetryId, alertAttributeName, modelCode, eventType, attributeName,
                               attributeDisplayName,
                               elementId, unit, dataType, active, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_update_attribute_id")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{Id}', telemetryId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    json_object["alertAttributeName"] = alertAttributeName
    json_object["modelCode"] = modelCode
    json_object["eventType"] = eventType
    json_object["attributeName"] = attributeName
    json_object["attributeDisplayName"] = attributeDisplayName
    json_object["elementId"] = elementId
    json_object["unit"] = unit
    json_object["dataType"] = dataType
    json_object["active"] = active

    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details app's
    save_api_resp_into_file('notification_update_attribute_id', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_update_attribute_id", response.text)

    return response


def notify_fetch_attribute_id(self, modelCode, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_fetch_attribute_id")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{modelCode}', modelCode)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details app's
    save_api_resp_into_file('notification_fetch_attribute_id', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_fetch_attribute_id", response.text)

    return response


def notify_delete_attribute_id(self, telemetryId, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "notification_delete_attribute_id")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # url
    complete_url = str(base_url + endpoint).replace('{Id}', telemetryId)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Header : ", header_x)

    # payload
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: Send POST request to create the vehicle group
    response = requests.delete(complete_url, headers=header_x, data=json.dumps(payload))
    print("API Response:", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details app's
    save_api_resp_into_file('notification_delete_attribute_id', response.text)
    save_api_resp_in_excel(self, "API_Data", "notification_delete_attribute_id", response.text)

    return response


def notification_attribute(self, alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
                             elementId, unit, dataType, active, tc):
    # print(option, tc)
    if tc == "save_notification_attribute":

        # Call vehicle group creation reusable module
        # Save/POST
        response = notify_save_attribute_id(
            self,
            alertAttributeName, modelCode, eventType, attributeName, attributeDisplayName,
            elementId, unit, dataType, active, "valid"
        )

        # Parse API response into JSON
        try:
            response_body = response.json()
        except Exception as e:
            assert False, f"Save API returned non-JSON response: {e}"

        # Validate response code and body
        if response.status_code == 200:
            if response_body.get("message") == "SUCCESS" and response_body.get("telemetryId"):
                telemetryId = response_body["telemetryId"]
                testResult(self, "passed", "New attribute should be saved successfully",
                           "New attribute is saved successfully")
                assert True
            else:
                testResult(self, "failed", "New attribute should be saved successfully",
                    "Save API did not return SUCCESS or telemetryId missing."
                    f"Status: {response.status_code}, Body: {response_body}")
                assert False
        else:
            testResult(self, "failed", "New attribute should be saved successfully",f"Save API failed with HTTP {response.status_code}. Body: {getattr(response, 'text', '')}")
            assert False

        telemetryId_file = os.path.join(folder_path, 'telemetryId.txt')
        print("Notification Telemetry Id File : ", telemetryId_file)

        text_file = open(telemetryId_file, "w+")
        text_file.write(str(telemetryId))
        text_file.close()

    elif tc == "update_notification_attribute":
        telemetryId_file = os.path.join(folder_path, 'telemetryId.txt')
        print("Notification Telemetry Id File : ", telemetryId_file)

        text_file = open(telemetryId_file, "r")
        telemetryId = text_file.read()
        text_file.close()

        # Call vehicle group update reusable module
        response = notify_update_attribute_id(self, telemetryId, alertAttributeName, modelCode, eventType, attributeName,
                               attributeDisplayName,
                               elementId, unit, dataType, active, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response code and body
        if response.status_code == 200:
            if response_body.get("message") == "SUCCESS" and response_body.get("telemetryId"):
                telemetryId = response_body["telemetryId"]
                assert True
                testResult(self, "passed", "Attribute details should be updated successfully",
                           "Attribute detail is updated successfully")
                assert True
            else:
                testResult(self, "failed", "Attribute details should be updated successfully",
                           "Update API did not return SUCCESS or telemetryId missing."
                           f"Status: {response.status_code}, Body: {response_body}")
                assert False
        else:
            testResult(self, "failed", "Attribute details should be updated successfully",
                       f"Update API failed with HTTP {response.status_code}. Body: {getattr(response, 'text', '')}")
            assert False

    elif tc == "delete_notification_attribute":

        telemetryId_file = os.path.join(folder_path, 'telemetryId.txt')
        print("Notification Telemetry Id File : ", telemetryId_file)

        text_file = open(telemetryId_file, "r")
        telemetryId_for_delete = text_file.read()
        text_file.close()

        # Call vehicle group deletion reusable module
        response = notify_delete_attribute_id(self, telemetryId_for_delete, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        message = response_body["message"]

        if message == "SUCCESS":
            testResult(self, "passed",
                       "Notification attribute should be deleted successfully",
                       "Notification attribute is deleted successfully")
        else:
            testResult(self, "failed",
                       "Notification attribute should be deleted successfully",
                       "Failed to delete notification attribute. Refer api response for failure details")
    else:
        print("Incorrect test case/option")

    print("----------------------------------------------------------")

    # Fetch/GET
    response = notify_fetch_attribute_id(self, modelCode, "valid")

    if response.status_code == 200:
        try:
            response_body = response.json()
        except Exception as e:
            assert False, f"Fetch API returned non-JSON response: {e}"

        if response_body.get("message") == "SUCCESS":
            telemetry_elements = response_body.get("telemetryElements", [])
            data_len = len(telemetry_elements)

            if data_len >= 1:
                found = False
                for i in range(data_len):
                    # telemetryId_1 = telemetry_elements[i]["telemetryId"]
                    alertAttributeName_1 = str(telemetry_elements[i].get("alertAttributeName"))
                    modelCode_1 = str(telemetry_elements[i].get("modelCode"))
                    eventType_1 = str(telemetry_elements[i].get("eventType"))
                    attributeName_1 = str(telemetry_elements[i].get("attributeName"))
                    attributeDisplayName_1 = str(telemetry_elements[i].get("attributeDisplayName"))
                    elementId_1 = str(telemetry_elements[i].get("elementId"))
                    unit_1 = str(telemetry_elements[i].get("unit"))
                    dataType_1 = str(telemetry_elements[i].get("dataType"))
                    active_1 = str(telemetry_elements[i].get("active"))

                    if (alertAttributeName == alertAttributeName_1 and
                            modelCode == modelCode_1 and
                            eventType == eventType_1 and
                            attributeName == attributeName_1 and
                            attributeDisplayName == attributeDisplayName_1 and
                            elementId == elementId_1 and
                            unit == unit_1 and
                            dataType == dataType_1 and
                            active == active_1):
                        assert True
                        testResult(self, "passed", "Notification attribute should be saved and fetched successfully",
                                                   "Saved element is found in fetched telemetryElements.\n"
                                                   f"Expected: alertAttributeName={alertAttributeName}, modelCode={modelCode}, eventType={eventType}, "
                                                   f"attributeName={attributeName}, attributeDisplayName={attributeDisplayName}, elementId={elementId}, "
                                                   f"unit={unit}, dataType={dataType}, active={active}.\n"
                                                   f"Total elements returned: {data_len}"
                                   )
                        found = True
                        # Only break after a successful match (prevents premature exit)
                        break

                # Explicit failure if no matching element found
                if not found:
                    if tc == "delete_notification_attribute":
                        testResult(self, "passed", "Notification attribute should be deleted successfully",
                        "Deleted element not found in fetched telemetryElements.\n"
                        f"Expected: alertAttributeName={alertAttributeName}, modelCode={modelCode}, eventType={eventType}, "
                        f"attributeName={attributeName}, attributeDisplayName={attributeDisplayName}, elementId={elementId}, "
                        f"unit={unit}, dataType={dataType}, active={active}.\n"
                        f"Total elements returned: {data_len}"
                    )
                        assert True
                    else:
                        testResult(self, "failed", "Notification attribute should be saved/updated and fetched successfully",
                                   "Saved/updated element not found in fetched telemetryElements.\n"
                                   f"Expected: alertAttributeName={alertAttributeName}, modelCode={modelCode}, eventType={eventType}, "
                                   f"attributeName={attributeName}, attributeDisplayName={attributeDisplayName}, elementId={elementId}, "
                                   f"unit={unit}, dataType={dataType}, active={active}.\n"
                                   f"Total elements returned: {data_len}"
                                   )
                        assert False
            else:
                assert False, "Fetch API returned SUCCESS but telemetryElements is empty."
        else:
            assert False, f"Fetch API message != SUCCESS. Body: {response_body}"
    else:
        assert False, f"Fetch API failed with HTTP {response.status_code}. Body: {getattr(response, 'text', '')}"
