import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.notifications import notificationServiceController_subscribe, \
    notificationServiceController_details_by_systemId_Category, notificationServiceController_details_by_systemId, \
    notificationServiceController_unsubscribe
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_NotificationServiceController:

    # Notification Service Control - Subscribe - Speed
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_speed(self):
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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - Subscribe - Geofence
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_geofence(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_geofence")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - Subscribe - SOS ON
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_sos_on(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_sos_on")

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

            print("System Id :", systemId)
            print("VIN :", vin)
            print("EndPoint :", endPoint)
            print("Category Name :", categoryName)
            print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - Subscribe - SOS OFF
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_sos_off(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_sos_off")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_bms(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_bms")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_curfew(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_curfew")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_unauthorizedMovement(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_unauthorizedMovement")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_maintenance(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_maintenance")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_criticalBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_criticalBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_warningBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_warningBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_subscribe_normalBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_normalBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            assert True
            testResult(self, "passed",
                       "Should be subscribed for notification successfully ",
                       "Successfully subscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_details_by_systemId(self):
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
        response_body = notificationServiceController_details_by_systemId(self, systemId, "valid")

        if response_body["message"] == "Successfully fetched the Subscribers Details" or response_body[
            "message"] == "Data Fetched Successfully":
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_details_by_systemId_Category(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_details_by_systemId_Category")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            categoryName = str(dict1["categoryName"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            categoryName = 'SPEED%20NOTIFICATION'

        # Call subscribe reusable module
        response_body = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName, "valid")
        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            assert (response_body["responseMessage"] == "SUCCESS")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - UnSubscribe - Speed
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_speed(self):
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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # Notification Service Control - UnSubscribe - Geofence
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_geofence(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_geofence")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - UnSubscribe - SOS ON
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_sos_on(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_sos_on")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # Notification Service Control - Subscribe - SOS OFF
    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_sos_off(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_sos_off")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_bms(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_bms")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_curfew(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_curfew")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_unauthorizedMovement(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_unauthorizedMovement")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_maintenance(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_maintenance")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_criticalBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_criticalBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_warningBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_warningBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_notificationServiceController_unsubscribe_normalBatteryTemp(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_normalBatteryTemp")

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

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            assert True
            testResult(self, "passed",
                       "Should be unsubscribed for notification successfully ",
                       "Successfully unsubscribed. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")
