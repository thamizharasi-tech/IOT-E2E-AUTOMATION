import json
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
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = c2c_ivi_chipset


class Test_LogManager:

    # API operation to fetch all user details
    @pytest.mark.Smoke
    def test1_positive_LogManager_FetchAllUserDetails(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchAllUserDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "username"

        # Call api reusable model
        response = logManager_fetchAllUserDetails(self, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            user_len = len(response_body["responseData"]["users"])
            if user_len >= 1:
                for i in range(user_len):
                    userId = response_body["responseData"]["users"][i]["userId"]
                    name = response_body["responseData"]["users"][i]["name"]
                    status = response_body["responseData"]["users"][i]["status"]
                    vehiclesCount = response_body["responseData"]["users"][i]["vehiclesCount"]
                    if vehiclesCount >= 1:
                        vin = response_body["responseData"]["users"][i]["vehiclesAssigned"][0]
                        break
                print("User Id : ", userId)
                print("Name : ", name)
                print("Status : ", status)
                print("vehiclesCount : ", vehiclesCount)
                print("VIN : ", vin)

                testResult(self, "passed", "Should fetch all user details successfully",
                           "Successfully fetched all users details")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all user details successfully",
                           "User list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all user details successfully",
                       "Failed to fetch all user details. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to save vehicle details to the user
    @pytest.mark.Smoke
    def test2_positive_LogManager_SaveVehicleDetailsToUser(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_SaveVehicleDetailsToUser")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            userName = str(dict1["userName"])
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            # vin = getVIN(self, OnboardingType, chipsetType)
            userName = "jackadmin"

        # Call api reusable model
        response = logManager_saveVehicleDetailsToUser(self, userName, systemId, "valid")

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
        if response_body['message'] == "Success":
            userId = response_body["responseData"]["userId"]
            vehicle_len = len(response_body["responseData"]["vehicles"])
            if vehicle_len >= 1:
                for i in range(vehicle_len):
                    systemId_actual = response_body["responseData"]["vehicles"][i]["systemId"]
                    vin = response_body["responseData"]["vehicles"][i]["vin"]
                    if systemId_actual == systemId:
                        break

                vehiclesCount = response_body["responseData"]["vehiclesCount"]
                print("User Id : ", userId)
                print("System Id : ", systemId)
                print("VIN : ", vin)
                print("vehiclesCount : ", vehiclesCount)

                testResult(self, "passed", "Should save vehicle to the user successfully",
                           "Successfully saved the vehicle to the user ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should save vehicle to the user successfully",
                           "vehicle list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should save vehicle to the user successfully",
                       "Failed to save vehicle to the user . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch all vehicles details on the basis of username
    @pytest.mark.Smoke
    def test3_positive_LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            userName = str(dict1["userName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            userName = "jackadmin"

        # Call api reusable model
        response = logManager_fetchAllVehiclesDetails_onTheBasisOfUsername(self, userName, "valid")

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
        if response_body['message'] == "Success":
            vehicle_len = len(response_body["responseData"]["vehicles"])
            if vehicle_len >= 1:
                deviceId = response_body["responseData"]["vehicles"][0]["deviceId"]
                systemId_actual = response_body["responseData"]["vehicles"][0]["systemId"]
                vin = response_body["responseData"]["vehicles"][0]["vin"]
                isAssigned = response_body["responseData"]["vehicles"][0]["isAssigned"]

                print("Device Id : ", deviceId)
                print("System Id : ", systemId_actual)
                print("VIN : ", vin)
                print("isAssigned : ", isAssigned)

                testResult(self, "passed", "Should fetch all vehicles details on the basis of username successfully",
                           "Successfully fetched all vehicles details on the basis of username ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all vehicles details on the basis of username successfully",
                           "vehicle list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all vehicles details on the basis of username successfully",
                       "Failed to fetch all vehicles details on the basis of username . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to save vehicle details to the user
    @pytest.mark.Smoke
    def test4_positive_LogManager_SaveAllUser_RegisteredWithVehicleId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_SaveAllUser_RegisteredWithVehicleId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            userName = str(dict1["userName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            userName = "jackadmin"

        # Call api reusable model
        response = logManager_saveAllUser_registeredWithVehicleId(self, systemId, userName, "valid")

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
        if response_body['message'] == "Success":
            systemId_actual = response_body["responseData"]["systemId"]
            vin = response_body["responseData"]["vin"]
            print("System Id : ", systemId_actual)
            print("VIN : ", vin)
            activeUsers_len = len(response_body["responseData"]["activeUsers"])
            if activeUsers_len >= 1:
                activeUsers = response_body["responseData"]["activeUsers"][0]
                print("Active User : ", activeUsers)
                testResult(self, "passed", "Should save all user registered with vehicleId successfully",
                           "Successfully save all user registered with vehicleId ")
                # self.result.set_result(TestResults.passed)
            invalidUsers_len = len(response_body["responseData"]["invalidUsers"])
            if invalidUsers_len >= 1:
                invalidUsers = response_body["responseData"]["invalidUsers"][0]
                print("Invalid User : ", invalidUsers)
                testResult(self, "failed", "Should save all user registered with vehicleId successfully",
                           "Failed to save all user registered with vehicleId")
                # self.result.set_result(TestResults.failed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should save all user registered with vehicleId successfully",
                       "Failed to save all user registered with vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch all user details on the basis of vehicleId
    @pytest.mark.Smoke
    def test5_positive_LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call api reusable model
        response = logManager_fetchAllUserDetails_onTheBasisOfVehicleId(self, systemId, "valid")

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
        if response_body['message'] == "Success":
            users_len = len(response_body["responseData"]["users"])
            if users_len >= 1:
                userId = response_body["responseData"]["users"][0]["userId"]
                name = response_body["responseData"]["users"][0]["name"]
                status = response_body["responseData"]["users"][0]["status"]
                isAssigned = response_body["responseData"]["users"][0]["isAssigned"]
                role = response_body["responseData"]["users"][0]["role"]

                print("User Id : ", userId)
                print("Name : ", name)
                print("Status : ", status)
                print("IsAssigned : ", isAssigned)
                print("Role : ", role)

                testResult(self, "passed", "Should fetch all user details on the basis of vehicleId successfully",
                           "Successfully fetched all user details on the basis of vehicleId ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all user details on the basis of vehicleId successfully",
                           "user list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all user details on the basis of vehicleId successfully",
                       "Failed to fetch all user details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to create incident
    @pytest.mark.Smoke
    def test6_positive_LogManager_CreateIncident(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_CreateIncident")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            userName = str(dict1["userName"])
            notes = str(dict1["notes"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            userName = "jackadmin"
            notes = "create new incident"

        # Call api reusable model
        response = logManager_createIncident(self, systemId, notes, userName, "valid")

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
        if response_body['message'] == "Success":
            incidentId = response_body["responseData"]["id"]
            systemId = response_body["responseData"]["systemId"]
            userName = response_body["responseData"]["userName"]
            notes = response_body["responseData"]["notes"]
            uploadTime = response_body["responseData"]["uploadTime"]

            print("Incident Id : ", incidentId)
            print("System Id : ", systemId)
            print("User Name : ", userName)
            print("Notes : ", notes)
            print("uploadTime : ", uploadTime)

            testResult(self, "passed", "Should create new incident for vehicleId & user successfully",
                       "Successfully created new incident")
            # self.result.set_result(TestResults.passed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should create new incident for vehicleId & user successfully",
                       "Failed to create new incident. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to update incident
    @pytest.mark.Smoke
    def test7_positive_LogManager_UpdateIncident(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_UpdateIncident")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            userName = str(dict1["userName"])
            notes = str(dict1["notes"])
            incidentId = str(dict1["incidentId"])
            if incidentId == "NA":
                # Read incident Id from create incident api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "LogManager_CreateIncident")
                api_resp = str(dict1["Actual API Response"])
                print(api_resp)
                json_object = json.loads(api_resp)
                incidentId = json_object["responseData"]["id"]

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            userName = "jackadmin"
            notes = "create new incident"

            # Call api reusable model
            response = logManager_createIncident(self, systemId, notes, userName, "valid")

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
            if response_body['message'] == "Success":
                incidentId = response_body["responseData"]["users"][0]["id"]
            else:
                incidentId = "1"

        print('Incident Id for update : ', incidentId)

        # Call api reusable model
        response = logManager_updateIncident(self, systemId, incidentId, notes, userName, "valid")

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
        if response_body['message'] == "Success":
            incidentId = response_body["responseData"]["id"]
            systemId = response_body["responseData"]["systemId"]
            userName = response_body["responseData"]["userName"]
            notes = response_body["responseData"]["notes"]
            uploadTime = response_body["responseData"]["uploadTime"]

            print("Incident Id : ", incidentId)
            print("System Id : ", systemId)
            print("User Name : ", userName)
            print("Notes : ", notes)
            print("uploadTime : ", uploadTime)

            testResult(self, "passed", "Should update existing incident for vehicleId & user successfully",
                       "Successfully updated existing incident")
            # self.result.set_result(TestResults.passed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should update existing incident for vehicleId & user successfully",
                       "Failed to update incident. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch all incident details
    @pytest.mark.Smoke
    def test8_positive_LogManager_FetchIncidentDetails(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchIncidentDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"

        # Call api reusable model
        response = logManager_fetchIncidentDetails(self, systemId, offset, limit, "valid")

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
        if response_body['message'] == "Success":
            incidents_len = len(response_body["responseData"]["incidents"])
            if incidents_len >= 1:
                incidentId = response_body["responseData"]["incidents"][0]["incidentId"]
                notes = response_body["responseData"]["incidents"][0]["notes"]
                systemId = response_body["responseData"]["incidents"][0]["systemId"]
                uploadTime = response_body["responseData"]["incidents"][0]["uploadTime"]

                print("Incident Id : ", incidentId)
                print("notes : ", notes)
                print("systemId : ", systemId)
                print("uploadTime : ", uploadTime)

                testResult(self, "passed", "Should fetch all incident details on the basis of vehicleId successfully",
                           "Successfully fetched all incident details on the basis of vehicleId ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all incident details on the basis of vehicleId successfully",
                           "Incident list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all incident details on the basis of vehicleId successfully",
                       "Failed to fetch all incident details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch vehicle details
    @pytest.mark.Smoke
    def test9_positive_LogManager_FetchVehicleDetails(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchVehicleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchVehicleDetails(self, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            incidents_len = len(response_body["responseData"]["vehicles"])
            if incidents_len >= 1:
                systemId = response_body["responseData"]["vehicles"][0]["systemId"]
                vin = response_body["responseData"]["vehicles"][0]["vin"]
                deviceId = response_body["responseData"]["vehicles"][0]["deviceId"]
                uploadInterval = response_body["responseData"]["vehicles"][0]["uploadInterval"]
                lastUploadedTime = response_body["responseData"]["vehicles"][0]["lastUploadedTime"]
                users = response_body["responseData"]["vehicles"][0]["users"]

                print("System Id : ", systemId)
                print("Vin : ", vin)
                print("Device Id : ", deviceId)
                print("uploadInterval : ", uploadInterval)
                print("lastUploadedTime : ", lastUploadedTime)
                print("users : ", users)

                testResult(self, "passed", "Should fetch vehicle details successfully",
                           "Successfully fetched vehicle details ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch vehicle details successfully",
                           "Vehicle list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch vehicle details successfully",
                       "Failed to fetch vehicle details . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle
    @pytest.mark.Smoke
    def test10_positive_LogManager_FetchLogFiles(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle based of log search criteria
    @pytest.mark.Smoke
    def test11_positive_LogManager_FetchLogFiles_basedOnLogSearchCriteria(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                incidentId = "NA"
                notes = "NA"
                fromDate = "NA"
                toDate = "NA"
                incidentIdReport = "NA"

                # Call api reusable module
                logManager_fetchLogFiles_basedOnLogSearchCriteria(self, systemId, offset, limit, sortDirection, sortBy,
                                                                  logName, logType, logUploadType, incidentId,
                                                                  notes, fromDate, toDate, fileCreatedTime,
                                                                  incidentIdReport, "valid")

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
                if response_body['message'] == "Success":
                    logs_len = len(response_body["responseData"]["logs"])
                    if logs_len >= 1:
                        id = response_body["responseData"]["logs"][0]["id"]
                        logName = response_body["responseData"]["logs"][0]["logName"]
                        logType = response_body["responseData"]["logs"][0]["logType"]
                        logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                        systemId = response_body["responseData"]["logs"][0]["systemId"]
                        vin = response_body["responseData"]["logs"][0]["vin"]
                        buildId = response_body["responseData"]["logs"][0]["buildId"]
                        filePath = response_body["responseData"]["logs"][0]["filePath"]
                        fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                        fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                        createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                        createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                        updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                        updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                        downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                        fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                        print("Id : ", id)
                        print("logName : ", logName)
                        print("logType : ", logType)
                        print("logUploadType : ", logUploadType)
                        print("systemId : ", systemId)
                        print("vin : ", vin)
                        print("buildId : ", buildId)
                        print("filePath : ", filePath)
                        print("fileCreatedTime : ", fileCreatedTime)
                        print("fileUploadTime : ", fileUploadTime)
                        print("createdTime : ", createdTime)
                        print("createdBy : ", createdBy)
                        print("updatedTime : ", updatedTime)
                        print("updatedBy : ", updatedBy)
                        print("downloadUrl : ", downloadUrl)
                        print("fileSize : ", fileSize)

                        testResult(self, "passed",
                                   "Should fetch all log details on the basis of vehicleId successfully",
                                   "Successfully fetched all log details on the basis of vehicleId")
                        # self.result.set_result(TestResults.passed)
                    else:
                        testResult(self, "failed",
                                   "Should fetch all log details on the basis of vehicleId successfully",
                                   "Log list is empty")

                elif response_body['message'] != "Success":
                    testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                               "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                               response_body["message"])
                    # self.result.set_result(TestResults.failed)
                else:
                    print("Something went wrong")
                    # self.result.set_result(TestResults.failed)
                print("----------------------------------------------------------")

    # API operation to view log file content
    @pytest.mark.Smoke
    def test12_positive_LogManager_viewLogFileContent(self):
        print("----------------------------------------------------------")
        logId = "1"
        action = "view"

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                for i in range(logs_len):
                    logId = response_body["responseData"]["logs"][i]["id"]
                    fileSize = response_body["responseData"]["logs"][i]["fileSize"]
                    if fileSize <= 40000:
                        action = "view"
                        break

        # Call api reusable model
        response = logManager_downloadAndViewLogFileContent(self, systemId, logId, action, "valid")

        time.sleep(5)
        # Validate response status code
        if response.status_code == 200:
            print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # API operation to download log file
    @pytest.mark.Smoke
    def test13_positive_LogManager_downloadLogFile(self):
        print("----------------------------------------------------------")
        logId = "1"
        action = "download"

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                for i in range(logs_len):
                    logId = response_body["responseData"]["logs"][i]["id"]
                    fileSize = response_body["responseData"]["logs"][i]["fileSize"]
                    if fileSize >= 40000:
                        action = "download"
                        break

        # Call api reusable model
        response = logManager_downloadAndViewLogFileContent(self, systemId, logId, action, "valid")

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
        downloadLink = response_body['downloadLink']
        fileName = response_body['fileName']
        expirationDate = response_body['expirationDate']

        print("Download Link : ", downloadLink)
        print("FileName : ", fileName)
        print("Expiration Date : ", expirationDate)

        print("----------------------------------------------------------")

    # API operation to fetch log config
    @pytest.mark.Smoke
    def test14_positive_LogManager_FetchLogConfig(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogConfig")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call api reusable model
        response = logManager_fetchLogConfig(self, systemId, "valid")

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
        if response_body['message'] == "Success":
            uploadInterval = response_body["responseData"]["uploadInterval"]
            print("uploadInterval : ", uploadInterval)

            testResult(self, "passed", "Should fetch log file configuration successfully",
                       "Successfully fetched log file configuration")
            # self.result.set_result(TestResults.passed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch log file configuration successfully",
                       "Failed to fetch log file configuration . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to update log config
    @pytest.mark.Smoke
    def test15_positive_LogManager_UpdateLogConfig(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_UpdateLogConfig")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            uploadInterval = str(dict1["uploadInterval"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            uploadInterval = "15"

        # Call api reusable model
        response = logManager_updateLogConfig(self, systemId, uploadInterval, "valid")

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
        if response_body['message'] == "Message Send to device successfully":
            # Call api reusable model
            response = logManager_fetchLogConfig(self, systemId, "valid")

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
            if response_body['message'] == "Success":
                uploadInterval_actual = response_body["responseData"]["uploadInterval"]
                print("uploadInterval : ", uploadInterval_actual)

            testResult(self, "passed", "Should update log file configuration successfully",
                       "Successfully updated log file configuration")
            # self.result.set_result(TestResults.passed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should update log file configuration successfully",
                       "Failed to update log file configuration . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to add description to log file
    @pytest.mark.Smoke
    def test16_positive_LogManager_AddDescriptionToLogFile(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                for i in range(logs_len):
                    logId = response_body["responseData"]["logs"][i]["id"]
                    break

        description = "add description"
        # Call api reusable model
        response = logManager_addDescriptionToLogFile(self, systemId, logId, description, "valid")

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
        # response_body = response.json()

        # Validate response body
        # print("Validation: ")

        print("----------------------------------------------------------")

    # API operation to delete log file
    @pytest.mark.Smoke
    def test17_positive_LogManager_DeleteLogFile(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                for i in range(logs_len):
                    logId = response_body["responseData"]["logs"][i]["id"]
                    break

        description = "add description"
        # Call api reusable model
        response = logManager_deleteLogFile(self, systemId, logId, "valid")

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
        # response_body = response.json()

        # Validate response body
        # print("Validation: ")

        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle (sortDirection: ASC)
    @pytest.mark.Smoke
    def test18_positive_LogManager_FetchLogFiles_sortDirection_ASC(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "ASC"
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "ASC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle (sortBy=logName)
    @pytest.mark.Smoke
    def test19_positive_LogManager_FetchLogFiles_sortBy_logName(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "ASC"
            sortBy = "logName"
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "ASC"
            sortBy = "logName"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle (sortBy=logUploadType)
    @pytest.mark.Smoke
    def test20_positive_LogManager_FetchLogFiles_sortBy_logUploadType(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "DESC"
            sortBy = "logUploadType"
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "logUploadType"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle (sortBy=incidentId)
    @pytest.mark.Smoke
    def test21_positive_LogManager_FetchLogFiles_sortBy_incidentId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "DESC"
            sortBy = "incidentId"
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "incidentId"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch/retrieve log files of a vehicle (sortBy=logType)
    @pytest.mark.Smoke
    def test22_positive_LogManager_FetchLogFiles_sortBy_logType(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "DESC"
            sortBy = "logType"
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "logType"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 1:
                id = response_body["responseData"]["logs"][0]["id"]
                logName = response_body["responseData"]["logs"][0]["logName"]
                logType = response_body["responseData"]["logs"][0]["logType"]
                logUploadType = response_body["responseData"]["logs"][0]["logUploadType"]
                systemId = response_body["responseData"]["logs"][0]["systemId"]
                vin = response_body["responseData"]["logs"][0]["vin"]
                buildId = response_body["responseData"]["logs"][0]["buildId"]
                filePath = response_body["responseData"]["logs"][0]["filePath"]
                fileCreatedTime = response_body["responseData"]["logs"][0]["fileCreatedTime"]
                fileUploadTime = response_body["responseData"]["logs"][0]["fileUploadTime"]
                createdTime = response_body["responseData"]["logs"][0]["createdTime"]
                createdBy = response_body["responseData"]["logs"][0]["createdBy"]
                updatedTime = response_body["responseData"]["logs"][0]["updatedTime"]
                updatedBy = response_body["responseData"]["logs"][0]["updatedBy"]
                downloadUrl = response_body["responseData"]["logs"][0]["downloadUrl"]
                fileSize = response_body["responseData"]["logs"][0]["fileSize"]

                print("Id : ", id)
                print("logName : ", logName)
                print("logType : ", logType)
                print("logUploadType : ", logUploadType)
                print("systemId : ", systemId)
                print("vin : ", vin)
                print("buildId : ", buildId)
                print("filePath : ", filePath)
                print("fileCreatedTime : ", fileCreatedTime)
                print("fileUploadTime : ", fileUploadTime)
                print("createdTime : ", createdTime)
                print("createdBy : ", createdBy)
                print("updatedTime : ", updatedTime)
                print("updatedBy : ", updatedBy)
                print("downloadUrl : ", downloadUrl)
                print("fileSize : ", fileSize)

                testResult(self, "passed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Successfully fetched all log details on the basis of vehicleId")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                           "Log list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all log details on the basis of vehicleId successfully",
                       "Failed to fetch log details on the basis of vehicleId . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch all user details (sortDirection: ASC)
    @pytest.mark.Smoke
    def test23_positive_LogManager_FetchAllUserDetails_sortDirection_ASC(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchAllUserDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "ASC"
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            offset = "1"
            limit = "10"
            sortDirection = "ASC"
            sortBy = "username"

        # Call api reusable model
        response = logManager_fetchAllUserDetails(self, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            user_len = len(response_body["responseData"]["users"])
            if user_len >= 1:
                for i in range(user_len):
                    userId = response_body["responseData"]["users"][i]["userId"]
                    name = response_body["responseData"]["users"][i]["name"]
                    status = response_body["responseData"]["users"][i]["status"]
                    vehiclesCount = response_body["responseData"]["users"][i]["vehiclesCount"]
                    if vehiclesCount >= 1:
                        vin = response_body["responseData"]["users"][i]["vehiclesAssigned"][0]
                        break
                print("User Id : ", userId)
                print("Name : ", name)
                print("Status : ", status)
                print("vehiclesCount : ", vehiclesCount)
                print("VIN : ", vin)

                testResult(self, "passed", "Should fetch all user details successfully",
                           "Successfully fetched all users details")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all user details successfully",
                           "User list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all user details successfully",
                       "Failed to fetch all user details. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to fetch vehicle details (sortDirection: ASC)
    @pytest.mark.Smoke
    def test24_positive_LogManager_FetchVehicleDetails_sortDirection_ASC(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchVehicleDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "ASC"
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            offset = "1"
            limit = "10"
            sortDirection = "ASC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchVehicleDetails(self, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            incidents_len = len(response_body["responseData"]["vehicles"])
            if incidents_len >= 1:
                systemId = response_body["responseData"]["vehicles"][0]["systemId"]
                vin = response_body["responseData"]["vehicles"][0]["vin"]
                deviceId = response_body["responseData"]["vehicles"][0]["deviceId"]
                uploadInterval = response_body["responseData"]["vehicles"][0]["uploadInterval"]
                lastUploadedTime = response_body["responseData"]["vehicles"][0]["lastUploadedTime"]
                users = response_body["responseData"]["vehicles"][0]["users"]

                print("System Id : ", systemId)
                print("Vin : ", vin)
                print("Device Id : ", deviceId)
                print("uploadInterval : ", uploadInterval)
                print("lastUploadedTime : ", lastUploadedTime)
                print("users : ", users)

                testResult(self, "passed", "Should fetch vehicle details successfully",
                           "Successfully fetched vehicle details ")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch vehicle details successfully",
                           "Vehicle list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch vehicle details successfully",
                       "Failed to fetch vehicle details . " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # API operation to download multiple log files
    @pytest.mark.Smoke
    def test25_positive_LogManager_download_multiple_logFiles(self):
        print("----------------------------------------------------------")
        logId = "1"
        logId1 = "2"
        action = "download"

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchLogFiles")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = str(dict1["sortDirection"])
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "lastUploadedTime"

        # Call api reusable model
        response = logManager_fetchLogFiles(self, systemId, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            logs_len = len(response_body["responseData"]["logs"])
            if logs_len >= 2:
                for i in range(logs_len):
                    logId = response_body["responseData"]["logs"][i]["id"]
                    logId1 = response_body["responseData"]["logs"][i + 1]["id"]
                    fileSize = response_body["responseData"]["logs"][i]["fileSize"]
                    if fileSize >= 40000:
                        action = "download"
                        break

        mul_logId = str(logId) + ',' + str(logId1)
        print("Multiple log ids :", mul_logId)
        # Call api reusable model
        response = logManager_downloadAndViewLogFileContent(self, systemId, mul_logId, action, "valid")

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
        downloadLink = response_body['downloadLink']
        fileName = response_body['fileName']
        expirationDate = response_body['expirationDate']

        print("Download Link : ", downloadLink)
        print("FileName : ", fileName)
        print("Expiration Date : ", expirationDate)

        if ".zip" in fileName:
            testResult(self, "passed", "Should download multiple log files in zip format successfully",
                       "Downloaded multiple log files in zip format successfully")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should download multiple log files in zip format successfully",
                       "Failed to download multiple log files in zip format . " + " Reason for failure is : " +
                       response_body["message"])

        print("----------------------------------------------------------")

    # API operation to fetch all user details (SearchBy: <username>)
    @pytest.mark.Smoke
    def test26_positive_LogManager_FetchAllUserDetails_searchBy_username(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_FetchAllUserDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            offset = str(dict1["offset"])
            limit = str(dict1["limit"])
            sortDirection = "DESC"
            sortBy = str(dict1["sortBy"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            offset = "1"
            limit = "10"
            sortDirection = "DESC"
            sortBy = "username"

        sortDirection = sortDirection + "&searchBy=jackadmin"

        # Call api reusable model
        response = logManager_fetchAllUserDetails(self, offset, limit, sortDirection, sortBy, "valid")

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
        if response_body['message'] == "Success":
            user_len = len(response_body["responseData"]["users"])
            if user_len >= 1:
                for i in range(user_len):
                    userId = response_body["responseData"]["users"][i]["userId"]
                    name = response_body["responseData"]["users"][i]["name"]
                    status = response_body["responseData"]["users"][i]["status"]
                    vehiclesCount = response_body["responseData"]["users"][i]["vehiclesCount"]
                    if vehiclesCount >= 1:
                        vin = response_body["responseData"]["users"][i]["vehiclesAssigned"][0]
                        break
                print("User Id : ", userId)
                print("Name : ", name)
                print("Status : ", status)
                print("vehiclesCount : ", vehiclesCount)
                print("VIN : ", vin)

                testResult(self, "passed", "Should fetch all user details successfully",
                           "Successfully fetched all users details")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should fetch all user details successfully",
                           "User list is empty")

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch all user details successfully",
                       "Failed to fetch all user details. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")

    # Log Config APIs - API operation to get status post update log config
    @pytest.mark.Smoke
    def test27_positive_LogManager_updateLogConfig_status(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_UpdateLogConfig_status")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call api reusable model
        response = logManager_updateLogConfig_status(self, systemId, "valid")

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
        if response_body['message'] == "Success":
            status = response_body['responseData']["status"]
            remainingTime = response_body['responseData']["remainingTime"]

            print("Status : ", status)
            print("Remaining Time : ", remainingTime)

            testResult(self, "passed", "Should fetch status post update config file update",
                       "Fetched status post update config file update")
            # self.result.set_result(TestResults.passed)

        elif response_body['message'] != "Success":
            testResult(self, "failed", "Should fetch status post update config file update",
                       "Failed to fetch status. " + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
        print("----------------------------------------------------------")
