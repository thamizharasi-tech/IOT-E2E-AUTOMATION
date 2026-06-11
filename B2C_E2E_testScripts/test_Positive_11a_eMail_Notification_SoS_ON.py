import time
from datetime import datetime

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, telemetry_speed_event_type, \
    b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_state_ON, b2c_telemetry_sidestand_attribute, b2c_telemetry_SOS
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notificationServiceController_details_by_systemId_Category, \
    notificationServiceController_subscribe, notificationServiceController_details_by_systemId, \
    notificationServiceController_unsubscribe
from C2CModules.primary_IVI_device_modules import get_SystemId, run_paho_command_on_primary_IVI, \
    push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, pull_logs_from_IVI_device, getVIN
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
notification_name = "SOS_ON NOTIFICATION"
categoryName = "SOS_ON%20NOTIFICATION"
notification_type = "EMAIL"


class Test_notification:

    def test_Positive_b2c_notificationServiceController_email_subscribe_sos_on(self):
        print("----------------------------------------------------------")
        print("Initiate for email notification by subscribing email :  ")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_sos_on")

        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)

        print("Read endpoint, categoryName & destinationType data from excel sheet")

        endPoint = str(dict1["endPoint1"])
        categoryName = str(dict1["categoryName"])
        destinationType = str(dict1["destinationType1"])

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        print("----------------------------------------------------------")
        # Call subscribe reusable module
        response_body = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")
        print("----------------------------------------------------------")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            testResult(self, "passed",
                       "Should be subscribed for email notification successfully ",
                       "Successfully subscribed or data saved for email notification. pls refer api response & cloud logs for detailed info")
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for email notification successfully ",
                       "Failed to subscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("Fetch & verify Subscribers details : ")
        # Call subscribe reusable module
        response_body = notificationServiceController_details_by_systemId(self, systemId, "valid")

        print("----------------------------------------------------------")
        if response_body["message"] == "Successfully fetched the Subscribers Details" or response_body[
            "message"] == "Data Fetched Successfully":
            verified = active = systemId_actual = destinationType_actual = categoryName_actual = subscriberId = endpoint_actual = ""
            data_len = len(response_body["responseData"]["subscribers"])
            if data_len >= 1:
                for i in range(data_len):
                    categoryName_actual = response_body["responseData"]["subscribers"][i]["categoryName"]
                    destinationType_actual = response_body["responseData"]["subscribers"][i]["destinationType"]
                    systemId_actual = response_body["responseData"]["subscribers"][i]["systemId"]
                    endpoint_actual = response_body["responseData"]["subscribers"][i]["endpoint"]
                    if categoryName_actual == categoryName and destinationType_actual == destinationType and systemId_actual == systemId and endpoint_actual == endPoint:
                        subscriberId = response_body["responseData"]["subscribers"][i]["subscriberId"]
                        vin = response_body["responseData"]["subscribers"][i]["vin"]
                        verified = response_body["responseData"]["subscribers"][i]["verified"]
                        active = response_body["responseData"]["subscribers"][i]["active"]
                        print("System Id : ", systemId_actual)
                        print("Destination Type  : ", destinationType_actual)
                        print("Category Name : ", categoryName_actual)
                        print("Subscriber Id : ", subscriberId)
                        print("Endpoint : ", endpoint_actual)
                        print("VIN : ", vin)
                        print("Verified : ", verified)
                        print("Active : ", active)
                        break

                if str(verified) == "True" and str(active) == "True":
                    testResult(self, "passed",
                               "Should be subscribed for email notification successfully ",
                               "Successfully subscribed for email notification. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Subscriber is not verified or active for email notification")
                    testResult(self, "failed",
                               "Should be subscribed for email notification successfully ",
                               "Subscriber deatils are not verified or active for email notification. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                    assert False

            else:
                print("Subscribers list is empty")
                testResult(self, "failed",
                           "Should be subscribed for email notification successfully ",
                           "Failed to subscribe. pls refer api response & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    def test_SoS_ON__email_notification_can(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Step:1 -> Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:2 -> Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:3 -> Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_SOS_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Step:4 -> Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Step:5 -> Device Side Validations : ")
        print("-----------------------------")

        # verify SoS attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_SOS_attribute, b2c_telemetry_SOS_attribute)

        if b2c_telemetry_SOS_attribute in str(ls[0]):
            print(f"SoS attribute name printed in device log : ' {b2c_telemetry_SOS_attribute} ' ")
            testResult(self, "verificationPassed", "SOS attribute should be present in telemetry data",
                       "SOS attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS attribute should be present in telemetry data ",
                       "SOS attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify value in the device logs
        tele_SOS = b2c_telemetry_SOS_attribute + b2c_telemetry_SOS_state_ON
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_attribute, tele_SOS)

        if tele_SOS in str(ls[0]):
            print(f"SOS flag value printed in device log : ' {tele_SOS} ' ")
            testResult(self, "verificationPassed", "SOS value should be published to cloud ",
                       "SOS flag value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "SOS value should be published to cloud ",
                       "SOS value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Step:6 -> Cloud Side Validations : ")
        print("-----------------------------")

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)
        value = ""

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_SOS:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("SoS flag configured in the telemetry stub : ", tele_SOS)
            print("SoS flag stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_SOS_state_ON):
            testResult(self, "verificationPassed",
                       "SOS flag should be set to '1' in the Cloud DB. ",
                       "SOS flag is set to '1' in the Cloud DB. pls refer "
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "SOS flag should be set to '1' in the Cloud DB. ",
                       "SOS flag is not set to '1' in the Cloud DB. pls refer "
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")

        # Call subscribe reusable module
        response_body = notificationServiceController_details_by_systemId_Category(self, systemId, categoryName,
                                                                                   "valid")

        if response_body["responseCode"] == str(1200) or response_body["responseCode"] == 1200:
            if response_body["responseMessage"] == "SUCCESS":
                data_len = len(response_body["responseData"])
                createdBy = createdTime = updatedBy = updatedTime = id = paramaters = status = subscriber_id = notificationType_actual = categoryName_actual = ""
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
                            paramaters = response_body["responseData"][i]["paramaters"]
                            status = response_body["responseData"][i]["status"]
                            subscriber_id = response_body["responseData"][i]["subscriber"]["subscriber_id"]
                            # print("Latest notification details fetched from API response : ")
                            print("Created By : ", createdBy)
                            print("Created Time : ", createdTime)
                            print("Updated By : ", updatedBy)
                            print("Updated Time : ", updatedTime)
                            print("Id : ", id)
                            print("Parameters : ", paramaters)
                            print("Status : ", status)
                            print("Category : ", categoryName_actual)
                            print("Notification Type : ", notificationType_actual)
                            print("Subscriber Id : ", subscriber_id)
                            break

                    your_dt = datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
                    createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
                    createdTime2 = your_dt.strftime("%Y-%m-%d_%H")

                    print("-------------------------------------------------------------------")
                    if createdTime1 == dt or createdTime2 == dt1:
                        testResult(self, "passed",
                                   "SOS ON alert notification should be sent to subscribed email successfully",
                                   "SOS ON alert notification is sent to subscribed email successfully. pls refer "
                                   "device & cloud logs for detailed info")
                        # self.result.set_result(TestResults.passed)
                    else:
                        print("Mismatch in created date & time")
                        print("Test Execution - Current Date & Time ", dt, dt1)
                        print("API Response - Created Time ", createdTime, createdTime1)
                        testResult(self, "failed",
                                   "SOS ON alert notification should be sent to subscribed email successfully",
                                   "SOS ON alert notification is not sent to subscribed email or something went "
                                   "wrong. pls refer"
                                   "device & cloud logs for detailed info")
                        # self.result.set_result(TestResults.failed)
                        assert False
                    print("-------------------------------------------------------------------")
                else:
                    print("dataList is empty in api response")
                    testResult(self, "failed",
                               "SOS ON alert notification should be sent to subscribed email successfully",
                               "SOS ON alert notification is not sent to subscribed email or something went "
                               "wrong. pls refer"
                               "device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                    assert False
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            testResult(self, "failed",
                       "SOS ON alert notification should be sent to subscribed email successfully",
                       "SOS ON alert notification is not sent to subscribed email or something went "
                       "wrong. pls refer"
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    def test_Positive_b2c_notificationServiceController_email_unsubscribe_sos_on(self):
        print("----------------------------------------------------------")
        print("Initiate for unsubscribing email notification:  ")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_sos_on")

        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)

        print("Read endpoint, categoryName & destinationType data from excel sheet")

        endPoint = str(dict1["endPoint1"])
        categoryName = str(dict1["categoryName"])
        destinationType = str(dict1["destinationType1"])

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        print("----------------------------------------------------------")
        # Call subscribe reusable module
        response_body = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")
        print("----------------------------------------------------------")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            testResult(self, "passed",
                       "Should be unsubscribed for email notification successfully ",
                       "Successfully unsubscribed or email subscriber data deleted . pls refer api response & cloud logs for detailed info")
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for email notification successfully ",
                       "Failed to unsubscribe. pls refer api response & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        print("Fetch & verify Subscribers details : ")
        # Call subscribe reusable module
        response_body = notificationServiceController_details_by_systemId(self, systemId, "valid")

        try:
            if response_body.status_code == 204:
                print("API response is empty")
                testResult(self, "passed",
                           "EMAIL Notification should be unsubscribed successfully ",
                           "Subscriber details not listing ie deleted successfully, thus api response is empty. pls refer api response & cloud logs for detailed info")
                # self.result.set_result(TestResults.passed)
        except:
            print("----------------------------------------------------------")
            if response_body["message"] == "Successfully fetched the Subscribers Details" or response_body[
                "message"] == "Data Fetched Successfully":
                verified = active = systemId_actual = destinationType_actual = categoryName_actual = subscriberId = endpoint_actual = ""
                data_len = len(response_body["responseData"]["subscribers"])
                if data_len >= 1:
                    for i in range(data_len):
                        categoryName_actual = response_body["responseData"]["subscribers"][i]["categoryName"]
                        destinationType_actual = response_body["responseData"]["subscribers"][i]["destinationType"]
                        systemId_actual = response_body["responseData"]["subscribers"][i]["systemId"]
                        endpoint_actual = response_body["responseData"]["subscribers"][i]["endpoint"]
                        if categoryName_actual == categoryName and destinationType_actual == destinationType and systemId_actual == systemId and endpoint_actual == endPoint:
                            subscriberId = response_body["responseData"]["subscribers"][i]["subscriberId"]
                            endpoint = response_body["responseData"]["subscribers"][i]["endpoint"]
                            vin = response_body["responseData"]["subscribers"][i]["vin"]
                            verified = response_body["responseData"]["subscribers"][i]["verified"]
                            active = response_body["responseData"]["subscribers"][i]["active"]
                            print("System Id : ", systemId_actual)
                            print("Destination Type  : ", destinationType_actual)
                            print("Category Name : ", categoryName_actual)
                            print("Subscriber Id : ", subscriberId)
                            print("Endpoint : ", endpoint)
                            print("VIN : ", vin)
                            print("Verified : ", verified)
                            print("Active : ", active)
                            print("Endpoint : ", endpoint)
                            break

                    if categoryName_actual == categoryName and destinationType_actual == destinationType and systemId_actual == systemId and endpoint_actual == endPoint:
                        testResult(self, "failed",
                                   "Email Notification should be unsubscribed successfully ",
                                   "Subscriber details still listing ie not deleted successfully. pls refer api response & cloud logs for detailed info")
                        # self.result.set_result(TestResults.failed)
                        assert False
                    else:
                        testResult(self, "passed",
                                   "Email Notification should be unsubscribed successfully ",
                                   "Subscriber details not listing ie deleted successfully. pls refer api response & cloud logs for detailed info")
                        # self.result.set_result(TestResults.passed)

                else:
                    print("Subscribers list is empty")
                    testResult(self, "passed",
                               "Email Notification should be unsubscribed successfully ",
                               "Subscriber details not listing ie deleted successfully. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
            else:
                print("Response message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed",
                           "Email Notification should be unsubscribed successfully ",
                           "Response message is not as expected OR something went wrong, pls check api response. pls refer api response & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
                assert False
            print("----------------------------------------------------------")
