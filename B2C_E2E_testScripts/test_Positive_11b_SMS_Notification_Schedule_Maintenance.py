import time
from datetime import datetime, timezone

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, telemetry_odo_attribute, \
    b2c_telemetry_odo_value, telemetry_curr_Odo, telemetry_odo_event_type
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notificationServiceController_details_by_systemId_Category, \
    notificationServiceController_subscribe, notificationServiceController_details_by_systemId, \
    notificationServiceController_unsubscribe
from C2CModules.primary_IVI_device_modules import get_SystemId, run_paho_command_on_primary_IVI, \
    push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, pull_logs_from_IVI_device, getVIN
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from C2CModules.vehicleServices_modules import vehicleServices_createVehicleServiceEntry
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
notification_name = "SCHEDULE MAINTENANCE NOTIFICATION"
categoryName = "SCHEDULE%20MAINTENANCE%20NOTIFICATION"
notification_type = "SMS"


class Test_notification:

    def test_Positive_b2c_notificationServiceController_sms_subscribe_schedule_maintenance(self):
        print("----------------------------------------------------------")
        print("Initiate for sms notification by subscribing mobile number :  ")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_subscribe_maintenance")

        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)

        print("Read endpoint, categoryName & destinationType data from excel sheet")

        endPoint = str(dict1["endPoint"])
        categoryName = str(dict1["categoryName"])
        destinationType = str(dict1["destinationType"])

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        print("----------------------------------------------------------")
        # Call subscribe reusable module
        response = notificationServiceController_subscribe(self, systemId, vin, endPoint, categoryName,
                                                                destinationType, "valid")

        # Parse api response into json
        response_body = response.json()

        print("----------------------------------------------------------")
        # Validate response body
        if response_body["message"] == "Successfully Subscribed" or response_body[
            "message"] == "Data Saved Successfully":
            testResult(self, "passed",
                       "Should be subscribed for sms notification successfully ",
                       "Successfully subscribed or data saved for sms notification. pls refer api response & cloud logs for detailed info")
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be subscribed for sms notification successfully ",
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
                               "Should be subscribed for sms notification successfully ",
                               "Successfully subscribed for sms notification. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Subscriber is not verified or active for sms notification")
                    testResult(self, "failed",
                               "Should be subscribed for sms notification successfully ",
                               "Subscriber deatils are not verified or active for sms notification. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                    assert False

            else:
                print("Subscribers list is empty")
                testResult(self, "failed",
                           "Should be subscribed for sms notification successfully ",
                           "Failed to subscribe. pls refer api response & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
                assert False
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    def test_schedule_maintenance_sms_notification(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)

        print("----------------------------------------------------------")
        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Step:1 -> Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for telemetry setup
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:2 -> Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        status = 2
        deviceMaintenanceFlag = bool('true')
        serviceDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
        serviceDueDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        dateReminder = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        # serviceDate = int(1688169600000)
        # serviceDueDate = int(1689724800000)
        # dateReminder = int(1689638400000)
        serviceOdo = int(9000)
        serviceDueOdo = int(1000)
        odoReminder = int(1000)
        notes = "Save vehicle service details"

        print("VIN : ", vin)
        print("System Id : ", systemId)
        print("Device Maintenance Flag : ", deviceMaintenanceFlag)
        print("Service Date : ", serviceDate)
        print("Service Odo : ", serviceOdo)
        print("Service Due Date: ", serviceDueDate)
        print("Service Due Odo : ", serviceDueOdo)
        print("Date Reminder : ", dateReminder)
        print("Odo Reminder : ", odoReminder)
        print("Notes : ", notes)

        # ===========================================================================================
        # Create vehicle service entry via API
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:3 -> Create vehicle service entry for schedule maintenance alert : ")

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "valid")
        # Validate response status code & success message
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")
        if response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed",
                       "Vehicle service data should be saved successfully",
                       "Vehicle service data is saved successfully")
        else:
            testResult(self, "failed",
                       "Vehicle service data should be saved successfully",
                       "Failed to save Vehicle service data")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry odo stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:3 -> Run telemetry - odo stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_odo")
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

        # telemetry - odo

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odo meter attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
            testResult(self, "passed", "Odo-meter attribute should be present in telemetry data",
                       "Odo-meter attribute is present in telemetry dataand device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odo-meter attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Odo-meter attribute should be present in telemetry data ",
                       "Odo-meter attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify odo meter value in the device logs
        tele_odo = telemetry_odo_attribute + b2c_telemetry_odo_value
        ls = verify_message_in_log(self, b2c_telemetry_odo_value, tele_odo)

        if tele_odo in str(ls[0]):
            print(f"Odo meter value printed in device log : ' {tele_odo} ' ")
            testResult(self, "passed", "Odo-meter value should be published to cloud ",
                       "Odo-meter value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odo-meter value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Odo-meter value should be published to cloud ",
                       "Odo-meter value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odo meter value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response_body = telemetry_Curr(self, telemetry_odo_event_type, systemId)
        print(response_body)
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Odo meter value configured in the telemetry stub : ", b2c_telemetry_odo_value)
            print("Odo meter value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_odo_value):
            testResult(self, "passed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Odo meter value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Odo meter value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

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
                            break

                    print("Latest notification details fetched from API response : ")
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

                    try:
                        your_dt = datetime.fromtimestamp(int(createdTime) / 1000)  # using the local timezone
                        createdTime1 = your_dt.strftime("%Y-%m-%d_%H_%M")
                        createdTime2 = your_dt.strftime("%Y-%m-%d_%H")
                    except:
                        testResult(self, "failed",
                                   "Schedule maintenance alert notification should be sent to subscribed email successfully",
                                   "Schedule maintenance alert notification is not sent to subscribed email or something went "
                                   "wrong. pls refer device & cloud logs for detailed info")

                    print("-------------------------------------------------------------------")
                    if createdTime1 == dt or createdTime2 == dt1:
                        testResult(self, "passed",
                                   "Schedule maintenance alert notification should be sent to subscribed email successfully",
                                   "Schedule maintenance alert notification is sent to subscribed email successfully. pls refer "
                                   "device & cloud logs for detailed info")
                    else:
                        print("Mismatch in created date & time")
                        print("Test Execution - Current Date & Time ", dt, dt1)
                        print("API Response - Created Time ", createdTime, createdTime1)
                        testResult(self, "failed",
                                   "Schedule maintenance alert notification should be sent to subscribed email successfully",
                                   "Schedule maintenance alert notification is not sent to subscribed email or something went "
                                   "wrong. pls refer"
                                   "device & cloud logs for detailed info")
                    print("-------------------------------------------------------------------")
                else:
                    print("dataList is empty in api response")
                    testResult(self, "failed",
                               "Schedule maintenance alert notification should be sent to subscribed email successfully",
                               "Schedule maintenance alert notification is not sent to subscribed email or something went "
                               "wrong. pls refer"
                               "device & cloud logs for detailed info")
                    # self.result.set_result(TestResults.failed)
                    assert False
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            testResult(self, "failed",
                       "Schedule maintenance alert notification should be sent to subscribed email successfully",
                       "Schedule maintenance alert notification is not sent to subscribed email or something went "
                       "wrong. pls refer"
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    def test_Positive_b2c_notificationServiceController_sms_unsubscribe_schedule_maintenance(self):
        print("----------------------------------------------------------")
        print("Initiate for unsubscribing sms notification:  ")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Notification_ServiceController",
                                         "notificationServiceController_unsubscribe_maintenance")

        # Read system id from actual device
        print("Read/Fetch System Id & VIN from actual device")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)

        print("Read endpoint, categoryName & destinationType data from excel sheet")

        endPoint = str(dict1["endPoint"])
        categoryName = str(dict1["categoryName"])
        destinationType = str(dict1["destinationType"])

        print("System Id :", systemId)
        print("VIN :", vin)
        print("EndPoint :", endPoint)
        print("Category Name :", categoryName)
        print("Destination Type :", destinationType)

        print("----------------------------------------------------------")
        # Call subscribe reusable module
        response = notificationServiceController_unsubscribe(self, systemId, vin, endPoint, categoryName,
                                                                  destinationType, "valid")

        # Parse api response into json
        response_body = response.json()

        print("----------------------------------------------------------")
        # Validate response body
        if response_body["message"] == "Successfully Unsubscribed" or response_body[
            "message"] == "Data Deleted Successfully":
            testResult(self, "passed",
                       "Should be unsubscribed for sms notification successfully ",
                       "Successfully unsubscribed or sms subscriber data deleted . pls refer api response & cloud logs for detailed info")
        else:
            print("Response message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed",
                       "Should be unsubscribed for sms notification successfully ",
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
                           "SMS Notification should be unsubscribed successfully ",
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
                                   "SMS Notification should be unsubscribed successfully ",
                                   "Subscriber details still listing ie not deleted successfully. pls refer api response & cloud logs for detailed info")
                        # self.result.set_result(TestResults.failed)
                        assert False
                    else:
                        testResult(self, "passed",
                                   "SMS Notification should be unsubscribed successfully ",
                                   "Subscriber details not listing ie deleted successfully. pls refer api response & cloud logs for detailed info")
                        # self.result.set_result(TestResults.passed)

                else:
                    print("Subscribers list is empty")
                    testResult(self, "passed",
                               "SMS Notification should be unsubscribed successfully ",
                               "Subscriber details not listing ie deleted successfully. pls refer api response & cloud logs for detailed info")
                    # self.result.set_result(TestResults.passed)
            else:
                print("Response message is not as expected OR something went wrong, pls check api response")
                testResult(self, "failed",
                           "SMS Notification should be unsubscribed successfully ",
                           "Response message is not as expected OR something went wrong, pls check api response. pls refer api response & cloud logs for detailed info")
                # self.result.set_result(TestResults.failed)
                assert False
            print("----------------------------------------------------------")

