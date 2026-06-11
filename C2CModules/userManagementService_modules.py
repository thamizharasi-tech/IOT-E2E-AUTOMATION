import ast
import json
import time
import requests

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.token_generation import logManager_token_generation, logManager_update_apiheader_with_token_inExcel
from utils.XLUtils import save_api_resp_in_excel, read_api_data_from_excel


# ---------------------------
# User Management Service APIs
# ---------------------------
def UserManagementService_Signup(self, firstName, lastName, email, username, password, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_Signup")
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
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object[0]["firstName"] = firstName
    json_object[0]["lastName"] = lastName
    json_object[0]["email"] = email
    json_object[0]["username"] = username
    json_object[0]["password"] = password
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_Signup",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_Signup', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_Signup", response.text)

    return response


def UserManagementService_VerifyCodeAfterSignUp(self, username, code, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_VerifyCodeAfterSignUp")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["code"] = code
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_VerifyCodeAfterSignUp",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_VerifyCodeAfterSignUp', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_VerifyCodeAfterSignUp", response.text)

    return response


def UserManagementService_ChangeUserRoleToAdmin(self, username, role, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_ChangeUserRoleToAdmin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["role"] = role
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ChangeUserRoleToAdmin",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_ChangeUserRoleToAdmin', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_ChangeUserRoleToAdmin", response.text)

    return response


def UserManagementService_UserLogin(self, username, password, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_UserLogin")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["password"] = password
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_UserLogin",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_UserLogin', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_UserLogin", response.text)

    return response


def UserManagementService_UpdateUserStatus(self, username, status, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_UpdateUserStatus")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["status"] = status
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_UpdateUserStatus",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_UpdateUserStatus', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_UpdateUserStatus", response.text)

    return response


def UserManagementService_ResetPassword(self, username, currPassword, newPassword, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_ResetPassword")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    json_object["currPassword"] = currPassword
    json_object["newPassword"] = newPassword
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ResetPassword",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_ResetPassword', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_ResetPassword", response.text)

    return response


def UserManagementService_ForgotPassword(self, email, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_ForgotPassword")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{email}", email)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ForgotPassword",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.get(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_ForgotPassword', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_ForgotPassword", response.text)

    return response


def UserManagementService_Logout(self, username, tc):
    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "UserManagementService_Logout")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for PUT request

    # Url :
    complete_url = str(base_url + endpoint).replace("{username}", username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)
    header_x = header_update(header_x, tc)
    print("Headers:\n", header_x)

    # Payload :
    json_object = json.loads(payload)
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send GET request.
    response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    if response.status_code == 401 or response.status_code == "401":
        print("Generate token : ")
        # Generate token
        logManager_token_generation(self)
        logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_Logout",
                                                       "LogManager_getToken")

        time.sleep(60)
        response = requests.put(complete_url, headers=header_x, data=json.dumps(payload))
        print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('UserManagementService_Logout', response.text)
    save_api_resp_in_excel(self, "API_Data", "UserManagementService_Logout", response.text)

    return response

