import json
import random
import time

import pytest

from C2CModules.e2e_testData import deviceType_IVI, c2c_ivi_chipset
from C2CModules.logManager_modules import logManager_fetchAllUserDetails, logManager_saveVehicleDetailsToUser, \
    logManager_fetchAllVehiclesDetails_onTheBasisOfUsername, logManager_saveAllUser_registeredWithVehicleId, \
    logManager_fetchAllUserDetails_onTheBasisOfVehicleId, logManager_createIncident, logManager_updateIncident, \
    logManager_fetchIncidentDetails, logManager_fetchVehicleDetails, logManager_fetchLogFiles, \
    logManager_fetchLogFiles_basedOnLogSearchCriteria, logManager_downloadAndViewLogFileContent, \
    logManager_addDescriptionToLogFile, logManager_fetchLogConfig, logManager_updateLogConfig, logManager_deleteLogFile, \
    logManager_updateLogConfig_status
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from C2CModules.userManagementService_modules import UserManagementService_Signup, \
    UserManagementService_VerifyCodeAfterSignUp, UserManagementService_ChangeUserRoleToAdmin, \
    UserManagementService_UserLogin, UserManagementService_UpdateUserStatus, \
    UserManagementService_ResetPassword, UserManagementService_ForgotPassword, UserManagementService_Logout
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = c2c_ivi_chipset


class Test_userManagementService:

    # API operation to signup a user
    @pytest.mark.Smoke
    def test1_positive_UserManagementService_signup(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_Signup")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            firstName = str(dict1["firstName"])
            lastName = str(dict1["lastName"])
            email = str(dict1["email"])
            username = str(dict1["username"])
            password = str(dict1["password"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            random_id = ' '.join([str(random.randint(10, 999)).zfill(3) for _ in range(1)])
            firstName = "MTest" + str(random_id)
            lastName = "LN"
            email = "MTest" + str(random_id) + "@gmail.com"
            username = "MTest" + str(random_id)
            password = "Test@" + str(random_id)

        # Call api reusable model
        response = UserManagementService_Signup(self, firstName, lastName, email, username, password, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body[
            'message'] == "Success. Verifcation code has been sent to mail":
            username = response_body["responseData"]["username"]
            name = response_body["responseData"]["name"]
            userType = response_body["responseData"]["userType"]
            status = response_body["responseData"]["status"]
            print("User Name : ", username)
            print("Name : ", name)
            print("User Type : ", userType)
            print("Status : ", status)
            print("Message : ", response_body['message'])

            testResult(self, "passed",
                       "Should allow to signup new user and verification code should be sent to registered email",
                       "Able to sign up new suer and verification code has been sent to registered email successfully")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed",
                       "Should allow to signup new user and verification code should be sent to registered email",
                       "Failed to sign up new user. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to verifiy code after signup
    @pytest.mark.Smoke
    def test2_positive_UserManagementService_verifyCodeAfterSignUp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_VerifyCodeAfterSignUp")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            code = str(dict1["code"])
            username = str(dict1["username"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            code = "775644"
            username = "Test566"

        # Call api reusable model
        response = UserManagementService_VerifyCodeAfterSignUp(self, username, code, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success":
            testResult(self, "passed", "Code should be verified post signup",
                       "Code is verified post signup")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "Code should be verified post signup",
                       "Failed to verify code post signup. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to change the role of user to admin
    @pytest.mark.Smoke
    def test3_positive_UserManagementService_ChangeUserRoleToAdmin(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_ChangeUserRoleToAdmin")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            role = str(dict1["role"])
            username = str(dict1["username"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            role = "admin"
            username = "Kavya"

        # Call api reusable model
        response = UserManagementService_ChangeUserRoleToAdmin(self, username, role, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success":
            testResult(self, "passed", "Should change User Role to Admin",
                       "Changed User Role to Admin")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "Should change User Role to Admin",
                       "Failed to change User Role to Admin. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation for user login
    @pytest.mark.Smoke
    def test4_positive_UserManagementService_UserLogin(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_UserLogin")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            password = str(dict1["password"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "jackadmin"
            password = "Test@123"

        # Call api reusable model
        response = UserManagementService_UserLogin(self, username, password, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "success" in response_body['message'] or response_body['message'] == "success":
            testResult(self, "passed", "User should login successfully",
                       "User logged in successfully")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should login successfully",
                       "Failed to login. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to enable a user
    @pytest.mark.Smoke
    def test5_positive_UserManagementService_UpdateUserStatus_enable(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_UpdateUserStatus")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            status = str(dict1["status"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "Kavya"
            status = "enable"

        # Call api reusable model
        response = UserManagementService_UpdateUserStatus(self, username, status, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is active now":
            testResult(self, "passed", "User should be Active/Enabled",
                       "User is Active/Enabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Active/Enabled",
                       "Failed to set User Active. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to approve user
    @pytest.mark.Smoke
    def test6_positive_UserManagementService_UpdateUserStatus_approve(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_UpdateUserStatus")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            status = str(dict1["status"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "Kavya"
            status = "approve"

        # Call api reusable model
        response = UserManagementService_UpdateUserStatus(self, username, status, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is active now":
            testResult(self, "passed", "User should be Active/Enabled",
                       "User is Active/Enabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Active/Enabled",
                       "Failed to set User Active. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to disable user
    @pytest.mark.Smoke
    def test7_positive_UserManagementService_UpdateUserStatus_disable(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_UpdateUserStatus")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            status = str(dict1["status"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "Kavya"
            status = "disable"

        # Call api reusable model
        response = UserManagementService_UpdateUserStatus(self, username, status, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is disabled":
            testResult(self, "passed", "User should be Disabled",
                       "User is Disabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Disabled",
                       "Failed to set User Disabled. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to disable user
    @pytest.mark.Smoke
    def test8_positive_UserManagementService_UpdateUserStatus_disable(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_UpdateUserStatus")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            status = str(dict1["status"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "Kavya"
            status = "disable"

        # Call api reusable model
        response = UserManagementService_UpdateUserStatus(self, username, status, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is disabled":
            testResult(self, "passed", "User should be Disabled",
                       "User is Disabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Disabled",
                       "Failed to set User Disabled. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to disable user
    @pytest.mark.Smoke
    def test9_positive_UserManagementService_ResetPassword(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_ResetPassword")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])
            currPassword = str(dict1["currPassword"])
            newPassword = str(dict1["newPassword"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "Kavya"
            currPassword = "Kavya@456"
            newPassword = "Kavya@123"

        # Call api reusable model
        response = UserManagementService_ResetPassword(self, username, currPassword, newPassword, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is disabled":
            testResult(self, "passed", "User should be Disabled",
                       "User is Disabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Disabled",
                       "Failed to set User Disabled. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to disable user
    @pytest.mark.Smoke
    def test10_positive_UserManagementService_ForgotPassword(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_ForgotPassword")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            email = str(dict1["email"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            email = "Kavya@gmail.com"

        # Call api reusable model
        response = UserManagementService_ForgotPassword(self, email, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "Success. user is disabled":
            testResult(self, "passed", "User should be Disabled",
                       "User is Disabled")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should be Disabled",
                       "Failed to set User Disabled. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to sign out a user
    @pytest.mark.Smoke
    def test10_positive_UserManagementService_logout(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "UserManagementService", "UserManagementService_Logout")
        if dict1['Flag'] == "Yes1":
            print("Flag is set to Yes, hence running with excel data :")
            username = str(dict1["username"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            username = "jackadmin"

        # Call api reusable model
        response = UserManagementService_Logout(self, username, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        print("Validation: ")
        if "Success" in response_body['message'] or response_body['message'] == "successfully signed out":
            testResult(self, "passed", "User should sign-out successfully",
                       "User signed out successfully")
            # self.result.set_result(TestResults.passed)

        elif "Success" not in response_body['message']:
            testResult(self, "failed", "User should sign-out successfully",
                       "User is failed to sign-out. " + " Reason for failure is : " +
                       response_body)
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")
