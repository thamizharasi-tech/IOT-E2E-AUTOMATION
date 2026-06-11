import json

import pytest
import time
import datetime

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.APIM_ReusableModules import notificationServiceController_subscribe, notificationServiceController_details_by_systemId, \
    notificationServiceController_unsubscribe,notificationServiceController_getNotifications
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_smoke:

    # Notification Service Control - Subscribe
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_speed")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            endPoint = str(dict1["endPoint"])
            categoryName = str(dict1["categoryName"])
            destinationType = str(dict1["destinationType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            endPoint = int(dict1["endPoint"])
            categoryName = str(dict1["categoryName"])
            destinationType = str(dict1["destinationType"])

            # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType)
        assert (response_body["message"] == "Data Saved Successfully")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_positive_notificationServiceController_details_by_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_details_by_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Call subscribe reusable module
        response_body = notificationServiceController_details_by_systemId(self, systemId)
        assert (response_body["message"] == "Data Fetched Successfully")
        print("----------------------------------------------------------")

    # Notification Service Control - UnSubscribe
    @pytest.mark.Smoke
    def test3_positive_notificationServiceController_unsubscribe(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                     "notificationServiceController_unsubscribe_speed")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            endPoint = str(dict1["endPoint"])
            categoryName = str(dict1["categoryName"])
            destinationType = str(dict1["destinationType"])
        else:
             print("Flag is not set to Yes, hence running with generic/actual device data")
             systemId = get_SystemId(self, OnboardingType, chipsetType)
             vin = getVIN(self, OnboardingType, chipsetType)
             endPoint = int(dict1["endPoint"])
             categoryName = str(dict1["categoryName"])
             destinationType = str(dict1["destinationType"])

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                              destinationType)
        assert (response_body["message"] == "Data Deleted Successfully")
        print("----------------------------------------------------------")

    # get notifications by type
    @pytest.mark.Smoke
    def test4_positive_notificationServiceController_getNotificationsBy_type(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                     "notificationServiceController_get_notification_by_type")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            type = str(dict1["type"])
            subscriber=str(dict1["subscriber"])
        else:
             print("Flag is not set to Yes, hence running with generic/actual device data")
             type="EMAIL"
             subscriber=""
        # Call subscribe reusable module
        response_body = notificationServiceController_getNotifications(self,type,subscriber,"getNotificationsByType")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            if response_body["responseMessage"] == "success" or response_body["responseMessage"] == "SUCCESS":
                if len(response_body["responseData"]) != 0:
                    print("Created By: ",response_body["responseData"][0]["createdBy"])
                    print("Created Time: ", response_body["responseData"][0]["createdTime"])
                    print("Updated By: ", response_body["responseData"][0]["updatedBy"])
                    print("Updated Time: ", response_body["responseData"][0]["updatedTime"])
                    print("Id: ", response_body["responseData"][0]["id"])
                    print("Parameters: ", response_body["responseData"][0]["paramaters"])
                    print("Status: ", response_body["responseData"][0]["status"])
                    print("Category: ", response_body["responseData"][0]["category"])
                    print("Notification Type: ", response_body["responseData"][0]["notificationType"])
                    print("Category: ", response_body["responseData"][0]["subscriber"]["subscriber_id"])
                    testResult(self, "passed", "Should fetch notification details successfully",
                               "Notifications details fetched successfully")
                else:
                    print(" => datalist is empty")
                    testResult(self, "verificationFailed", "Should fetch notification details successfully",
                               "End point is working fine, but there is no data in DB for this type, thus marking test case as pass")
        elif response_body["responseCode"] != 1200:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch notification details successfully",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

   # get notifications by subscriber
    @pytest.mark.Smoke
    def test5_positive_notificationServiceController_getNotificationsBy_subscriber(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                     "notificationServiceController_get_notification_by_subscriber")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            type = str(dict1["type"])
            subscriber=str(dict1["subscriber"])
        else:
             print("Flag is not set to Yes, hence running with generic/actual device data")
             type=""
             subscriber="a169b007-a25e-4f0e-a12e-0f78ce17a9ce"
        # Call subscribe reusable module
        response_body = notificationServiceController_getNotifications(self,type,subscriber,"getNotificationsBySubscriber")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            if response_body["responseMessage"] == "success" or response_body["responseMessage"] == "SUCCESS":
                if len(response_body["responseData"]) != 0:
                    print("Created By: ",response_body["responseData"][0]["createdBy"])
                    print("Created Time: ", response_body["responseData"][0]["createdTime"])
                    print("Updated By: ", response_body["responseData"][0]["updatedBy"])
                    print("Updated Time: ", response_body["responseData"][0]["updatedTime"])
                    print("Id: ", response_body["responseData"][0]["id"])
                    print("Parameters: ", response_body["responseData"][0]["paramaters"])
                    print("Status: ", response_body["responseData"][0]["status"])
                    print("Category: ", response_body["responseData"][0]["category"])
                    print("Notification Type: ", response_body["responseData"][0]["notificationType"])
                    print("Category: ", response_body["responseData"][0]["subscriber"]["subscriber_id"])
                    testResult(self, "passed", "Should fetch notification details successfully",
                               "Notifications details fetched successfully")
                else:
                    print(" => datalist is empty")
                    testResult(self, "verificationFailed", "Should fetch notification details successfully",
                               "End point is working fine, but there is no data in DB for this type, thus marking test case as pass")
        elif response_body["responseCode"] != 1200:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch notification details successfully",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")