import ast
import time
import requests
import json

from C2CModules.api_modules import header_update
from C2CModules.resuse_modules import save_api_resp_into_file
from utils.XLUtils import read_api_data_from_excel, save_api_resp_in_excel, save_api_header_in_excel


def read_API_common_data(self):
    dictionary = {}
    dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
    Env = str(dict["Value"])
    dict = read_api_data_from_excel(self, "API_Common_Data", "API_Type")
    apiType = str(dict["Value"])
    dict = read_api_data_from_excel(self, "API_Common_Data", "User Name")
    userName = str(dict["Value"])
    dict = read_api_data_from_excel(self, "API_Common_Data", "Password")
    password = str(dict["Value"])
    dict = read_api_data_from_excel(self, "API_Common_Data", "userPoolId")
    userPoolId = str(dict["Value"])
    # print(Env,apiType,userName,password)
    dictionary = {"Env": Env, "apiType": apiType, "userName": userName, "password": password, "userPoolId": userPoolId}
    # print(dictionary)
    return dictionary


def token_gen_reus_mod(self, sheetname, testCasename):
    # Read api configuration/common data
    api_common_data = read_API_common_data(self)

    if api_common_data["apiType"] == "API_Gateway":

        # Read api test data from excel sheet
        dict = read_api_data_from_excel(self, sheetname, testCasename)
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        payload = str(dict["Payload"]).replace('\n', '')

        # Arrange: Test data (url,header and payload) for POST request

        # Url :
        complete_url = base_url + endpoint
        print("Complete Url : ", complete_url)
        # Header :
        x = ast.literal_eval(headers)
        x['x-requestor'] = api_common_data["userName"]
        # Payload :
        json_object = json.loads(payload)
        json_object['username'] = api_common_data["userName"]
        json_object['password'] = api_common_data["password"]
        json_object['userPoolId'] = api_common_data["userPoolId"]

        # Act: Call POST request function
        response = requests.post(complete_url, headers=x, data=json.dumps(json_object))
        print("API response : ", response.text)

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_resp_into_file(testCasename, response.text)
        save_api_resp_in_excel(self, sheetname, testCasename, response.text)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        print("API response  : ", response_body)

        # Validate api response body contents
        assert (response_body["responseCode"] == "1200")
        assert (response_body["responseMessage"] == "SUCCESS")
        idToken = response_body["responseData"]["idToken"]
        expiresIn = response_body["responseData"]["expiresIn"]

    else:
        print("Skipping token generation, as API type is not selected as 'API_Gateway' option")


def update_apiheader_with_token_inExcel(self, sheetname, testCasename, tokenTestCasename):
    # Read api configuration/common data
    api_common_data = read_API_common_data(self)

    if api_common_data["apiType"] == "API_Gateway":
        # Read api test data from excel sheet
        dict = read_api_data_from_excel(self, sheetname, testCasename)
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        payload = str(dict["Payload"]).replace('\n', '')

        # Arrange: Test data (url,header and payload) for POST request

        # Read API token from Registration_DeviceReg api resp from excel sheet
        dict1 = read_api_data_from_excel(self, sheetname, tokenTestCasename)
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        idToken = json_object["responseData"]["idToken"]
        # print(idToken)

        # Header update :
        header_x = ast.literal_eval(headers)
        if api_common_data["apiType"] == "API_Gateway":
            header_x['authorization-token'] = idToken
            header_x['x-requestor'] = api_common_data["userName"]
        header = str(header_x)
        # print(header)

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_header_in_excel(self, sheetname, testCasename, header)
        time.sleep(5)
    else:
        print("API_Gateway option is not selected")


# -------------------------------------
# Mahindra APIs
# -------------------------------------
def mahindra_token_gen_reus_mod(self, sheetname, testCasename):
    # Read api configuration/common data
    api_common_data = read_API_common_data(self)

    if api_common_data["apiType"] == "API_Gateway":

        # Read api test data from excel sheet
        dict = read_api_data_from_excel(self, sheetname, testCasename)
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        payload = str(dict["Payload"]).replace('\n', '')

        # Arrange: Test data (url,header and payload) for POST request

        # Url :
        complete_url = base_url + endpoint
        print("Complete Url : ", complete_url)
        # Header :
        x = ast.literal_eval(headers)
        x['x-requestor'] = api_common_data["userName"]
        # Payload :
        json_object = json.loads(payload)
        json_object['username'] = api_common_data["userName"]
        json_object['password'] = api_common_data["password"]

        # Act: Call POST request function
        response = requests.post(complete_url, headers=x, data=json.dumps(json_object))
        print("API response : ", response.text)

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_resp_into_file(testCasename, response.text)
        save_api_resp_in_excel(self, sheetname, testCasename, response.text)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        print("API response  : ", response_body)

        # Validate api response body contents
        assert (response_body["message"] == "success")

    else:
        print("Skipping token generation, as API type is not selected as 'API_Gateway' option")


def mahindra_update_apiheader_with_token_inExcel(self, sheetname, testCasename, tokenTestCasename):
    # Read api configuration/common data
    api_common_data = read_API_common_data(self)

    if api_common_data["apiType"] == "API_Gateway":
        # Read api test data from excel sheet
        dict = read_api_data_from_excel(self, sheetname, testCasename)
        base_url = str(dict["Base Url"])
        endpoint = str(dict["Endpoint"])
        headers = str(dict["Headers"]).replace('\n', '')
        payload = str(dict["Payload"]).replace('\n', '')

        # Arrange: Test data (url,header and payload) for POST request

        # Read API token from Registration_DeviceReg api resp from excel sheet
        dict1 = read_api_data_from_excel(self, sheetname, tokenTestCasename)
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        accessToken = json_object["responseData"]["accessToken"]
        # print(idToken)

        # Header update :
        header_x = ast.literal_eval(headers)
        if api_common_data["apiType"] == "API_Gateway":
            header_x['Authorization'] = f'Bearer {accessToken}'
        header = str(header_x)
        # print(header)

        # Save test result in Excel sheet @ desired cell for get count or device details api's
        save_api_header_in_excel(self, sheetname, testCasename, header)
        time.sleep(5)
    else:
        print("API_Gateway option is not selected")


# ------------------------------------
# Update header for c2c features
# ------------------------------------


def setup_Registration_testdata(self):
    # Registration :
    update_apiheader_with_token_inExcel(self, "API_Data", "Registration-DeviceReg", "Registration-RequestToken")


def setup_Registration_status_testdata(self):
    # Registration Status :
    update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getCount",
                                        "Registration-RequestToken_GETmethod")
    update_apiheader_with_token_inExcel(self, "API_Data", "Registration_getDetails",
                                        "Registration-RequestToken_GETmethod")


def setup_Telemtery_testdata(self):
    # Telemetry :
    update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_clearSoS", "Telemetry_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_sensorElements", "Telemetry_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Telemetry_Curr", "Telemetry_AuthToken")


def setup_commandControl_testdata(self):
    # Command Control :
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Request", "CommandControl_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Tracking", "CommandControl_AuthToken")


def setup_asset_testdata(self):
    # Asset Management :
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-info", "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-info-by-tripId",
                                        "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-waypoints-by-tripid",
                                        "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-waypoints",
                                        "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_trip-waypoints-by-systemId",
                                        "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-meta",
                                        "AssetManagement_trip_AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "AssetManagement_latest-trip-details",
                                        "AssetManagement_trip_AuthToken")


def setup_notify_testdata(self):
    # Notification :
    update_apiheader_with_token_inExcel(self, "API_Data", "Notification_message", "Notification-AuthToken")


def setup_vehicle_testdata(self):
    # Vehicle :
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_update-vehicle-meta-data",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get-vehicle-meta-data",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle_get-device-meta-data",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsbyModelNew",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinCountByAllModels",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel",
                                        "Vehicle-AuthToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Vehicle-GetVinsByModel_v3",
                                        "Vehicle-AuthToken")


def setup_SOTA_testdata(self):
    # SOTA :
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadPackage", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreatePresignUrl", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-uploadFile", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateScript", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels1", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-GetPreconditions", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListApps", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-CreateSchedule", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListModels", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListPackages", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScripts", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListSchedules", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-ListScheduleVin", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-UpdatePackageDescription", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-EditScriptNotes", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeletePackage", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteScript", "SOTA-getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-DeleteScript_scheduleId", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-devAppDeviceStatus", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-devApps", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-devDeviceState", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-devSchedule", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-trigger", "SOTA-getToken")
    # update_apiheader_with_token_inExcel(self, "API_Data", "SOTA-vehicleOnboard", "SOTA-getToken")


def setup_FOTA_testdata(self):
    # FOTA :
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-firmwareUpload", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetListOfModels&Count", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createPresigneUrl", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-uploadFile", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createScript", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetPrecondition", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetFirmwareMmodels", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-getVersionDetails", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-createSchedule", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetScriptmodel", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllScriptDetails", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllScheduleDetails", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetAllFirmware", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-GetScheduleStatus", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-PATCH-firmwareDescription", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-PATCH-scriptReleaseNoteUpdate", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteFirmware", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteScript", "FOTA-GetToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "FOTA-DeleteSchedule", "FOTA-GetToken")


def setup_license_testdata(self):
    # License :
    update_apiheader_with_token_inExcel(self, "API_Data", "LicenseCleanup", "NA")


def setup_SMP_testdata(self):
    # SMP :
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GetVINdetails", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GetSKUupdateList", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GetFeatureUpdateList", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_VinGetuPvChipsetSpIdlist")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_VinGetSKUIdlist", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_VinUpdateSKU", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_CreateGroup", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GrpGetuPvChipsetSpIdlist", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GrpGetSKUIdlist", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GrpUpdateSKU", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GetFilterValuesbyGroup", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_GetFeaturesforselectedFilters", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "SMP_SendUpdateFeatureRequest", "NA")


def setup_commandWrapper_testdata(self):
    # Command & Control Wrapper :
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_BuzzBike", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_IgnitionON", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_IgnitionOFF", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Mobilize", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_Immobilize", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_HandleUnlock", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "CommandControl_HandleLock", "NA")


def setup_telPublisher_testdata(self):
    # Telemetry publisher :
    update_apiheader_with_token_inExcel(self, "API_Data", "TelemetryPublisher", "TelemetryPublisher_getToken")


def setup_contextControl_testdata(self):
    # Context Control :
    update_apiheader_with_token_inExcel(self, "API_Data", "ContextControl", "ContextControl_getToken")


def setup_statistics_testdata(self):
    # Statistics :
    update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesFleet", "Statistics_getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-DailyTripSummariesVin", "Statistics_getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesFleet", "Statistics_getToken")
    update_apiheader_with_token_inExcel(self, "API_Data", "Statistics-MonthlyTripSummariesVin", "Statistics_getToken")


def setup_packageController_testdata(self):
    # Package Controller :
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageUpgrade", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAssignmentDetails", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAssignmentStatusUpdate", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageIdDetails", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageAllDetails", "NA")
    update_apiheader_with_token_inExcel(self, "API_Data", "PackageController_PackageFailureDetails", "NA")


def setup_logManager_testdata(self):
    # Package Controller :
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchAllUserDetails",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_SaveVehicleDetailsToUser",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                   "LogManager_FetchAllVehiclesDetails_OnTheBasisOfUsername",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_SaveAllUser_RegisteredWithVehicleId",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                   "LogManager_FetchAllUserDetails_OnTheBasisOfVehicleId",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_CreateIncident", "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateIncident", "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchIncidentDetails",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchVehicleDetails",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchLogFiles", "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_DownloadAndViewLogFileContent",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_AddDescriptionToLogFile",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_DeleteLogFile", "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_FetchLogConfig", "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateLogConfig",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "LogManager_UpdateLogConfig_status",
                                                   "LogManager_getToken")


def setup_userManagementService_testdata(self):
    # Package Controller :
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_Signup",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_VerifyCode",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_VerifyCode",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_VerifyCodeAfterSignUp",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_AssignAdminRole",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ChangeUserRoleToAdmin",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_Login",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_UserLogin",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_UpdateUserStatus",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_FetchApprovedUsers",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_FetchEnabledUsers",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_FetchDisabledUsers",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ResetPassword",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_ForgotPassword",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_InitiateForgotPassword",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data",
                                                   "UserManagementService_ConfirmPasswordAfterInitiatingForgotPassword",
                                                   "LogManager_getToken")
    logManager_update_apiheader_with_token_inExcel(self, "API_Data", "UserManagementService_Logout",
                                                   "LogManager_getToken")


def logManager_token_generation(self):
    # Read api test data from excel sheet
    dict1 = read_api_data_from_excel(self, "LogManager", "LogManager_getToken")
    username = str(dict1["userName"])
    password = str(dict1["password"])

    # Read api test data from excel sheet
    dict = read_api_data_from_excel(self, "API_Data", "LogManager_getToken")
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Arrange: Test data (url,header and payload) for POST request

    # Url :
    complete_url = str(base_url + endpoint).replace('{username}', username)
    print("Complete URL : ", complete_url)

    # Header :
    header_x = ast.literal_eval(headers)

    # Payload :
    json_object = json.loads(payload)
    json_object["password"] = password
    payload = json_object
    print("Payload : ", payload)

    # Act: convert dict to json by json.dumps() for body data and send POST request.
    response = requests.post(complete_url, headers=header_x, data=json.dumps(payload))
    print("API response : ", response.text)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_resp_into_file('LogManager_getToken', response.text)
    save_api_resp_in_excel(self, "API_Data", "LogManager_getToken", response.text)

    return response


def logManager_update_apiheader_with_token_inExcel(self, sheetname, testCasename, tokenTestCasename):
    dict = read_api_data_from_excel(self, sheetname, testCasename)
    base_url = str(dict["Base Url"])
    endpoint = str(dict["Endpoint"])
    headers = str(dict["Headers"]).replace('\n', '')
    payload = str(dict["Payload"]).replace('\n', '')

    # Read API token from Registration_DeviceReg api resp from excel sheet
    dict1 = read_api_data_from_excel(self, sheetname, tokenTestCasename)
    api_resp = str(dict1["Actual API Response"])
    # print(api_resp)
    json_object = json.loads(api_resp)
    accessToken = json_object["responseData"]["accessToken"]
    # print(idToken)

    # Header update :
    header_x = ast.literal_eval(headers)
    header_x['Authorization'] = f'Bearer {accessToken}'
    header = str(header_x)
    print(header)

    # Save test result in Excel sheet @ desired cell for get count or device details api's
    save_api_header_in_excel(self, sheetname, testCasename, header)
    time.sleep(10)
