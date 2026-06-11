import pytest
import time
from datetime import datetime, timedelta, timezone

from C2CModules.vehicle_diagnostic import DTC_fetchDTCCodes, DTC_clearDTC,DTC_clearDTC_status, DTC_get_dtc_details, DTC_dtcOccurence, dtc_occurrence
from C2CModules.e2e_testData import *
from C2CModules.notifications import notification_verify_alert_details_v2
from C2CModules.testResults import testResult
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test:

    @pytest.mark.smoke
    def test1_DTC_alert(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Start c2c services
        # ===========================================================================================
        print("----------------------------------------------------------")
        # run_c2cServices_on_primary_IVI(self, onboardingType, chipsetType)
        time.sleep(5)

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the alert is sent from device to cloud when tampering event occurs
        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, dtc_alert_notification_deviceLog_string,
                                   dtc_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        print("----------------------------------------------------------")

        # Call verification module to validate alert details
        notification_verify_alert_details_v2(self, systemId, dtc_categoryName, dtc_notification_name,
                                             notification_type, dt, dt1)

        #self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test_fetch_dtc_details(self):

        print("----------------------------------------------------------")

        startDate = datetime.now() - timedelta(days=1)
        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        offset = "0"
        limit = "10"
        details = "true"
        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("startDate: ", startDate)
        print("endDate: ", endDate)
        print("offset: ", offset)
        print("limit: ", limit)
        print("details: ", details)
        print("systemId: ", systemId)

        # Call DTC reusable module

        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        issuedTime = ""

        if response_body["message"] == "Data Saved Successfully":

            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:

                for i in range(dtc_len):

                    status = response_body["responseData"]["DTCs"][i]["status"]

                    if status == 'Unresolved':
                        deviceId = response_body["responseData"]["DTCs"][i]["deviceId"]

                        dtcCode = response_body["responseData"]["DTCs"][i]["dtcCode"]

                        dtcSensorValue = response_body["responseData"]["DTCs"][i]["dtcSensorValue"]

                        dtcDescription = response_body["responseData"]["DTCs"][i]["dtcDescription"]

                        status = response_body["responseData"]["DTCs"][i]["status"]

                        issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]

                        receiveTime = response_body["responseData"]["DTCs"][i]["receiveTime"]

                        tripId = response_body["responseData"]["DTCs"][i]["tripId"]

                        sequenceNo = response_body["responseData"]["DTCs"][i]["sequenceNo"]

                        packetStatus = response_body["responseData"]["DTCs"][i]["packetStatus"]

                        createdTime = response_body["responseData"]["DTCs"][i]["createdTime"]

                        createdBy = response_body["responseData"]["DTCs"][i]["createdBy"]

                        updatedTime = response_body["responseData"]["DTCs"][i]["updatedTime"]

                        updatedBy = response_body["responseData"]["DTCs"][i]["updatedBy"]

                        break

            else:

                print("No DTC record exists in cloud DB")

                assert False

            # message = response_body["responseData"]["message"]

            print("----------------------------------------------------------")

            print('Device Id : ', deviceId)

            print('DTC Code : ', dtcCode)

            print('DTC Sensor Value : ', dtcSensorValue)

            print('DTC Description : ', dtcDescription)

            print('Status : ', status)

            print('Issued Time : ', issuedTime)

            print('Receive Time : ', receiveTime)

            print('Trip Id : ', tripId)

            print('Sequence No : ', sequenceNo)

            print('Packet Status : ', packetStatus)

            print('Created Time : ', createdTime)

            print('Created By : ', createdBy)

            print('Updated Time : ', updatedTime)

            print('Updated By : ', updatedBy)

            print("----------------------------------------------------------")

            # print('Message : ', message)

            testResult(self,"passed", "DTC Alert details should be saved & fetched successfully",

                   "DTC Alert details are saved & fetched successfully ")

            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":

            # print(response_body["responseData"]["message"])

            testResult(self, "failed", "DTC Alert details should be saved & fetched successfully",

                   "Failed to save/fetch the dtc details " + " Reason for failure is : " +

                   response_body)

            assert False  # self.result.set_result(TestResults.failed)

        else:

            print("Something went wrong")

            # self.result.set_result(TestResults.failed)

            assert False

        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")

    def test1_DTC_clear(self):

        print("\n------------------------------START------------------------------\n")

        """

        This test is validating the Notification - DTC Clear via API e2e functionality. (positive scenario)

        :return: return test status

        Validate DTC Clear via API

        """

        print("\n------------------NOTIFICATION - DTC CLEAR VIA API------------------\n")

        print("----------------------------------------------------------")

        utc_time = datetime.now()

        dt = utc_time.strftime("%Y-%m-%d_%H_%M")

        dt1 = utc_time.strftime("%Y-%m-%d_%H")

        print("Current date & time :", dt)

        # Read systemId
        systemId = read_vehicleJsonFile(self, "system_id")

        startDate = datetime.now() - timedelta(days=1)

        endDate = datetime.now() + timedelta(days=1)

        startDate = startDate.strftime("%Y-%m-%dT%H:%M:%SZ")

        endDate = endDate.strftime("%Y-%m-%dT%H:%M:%SZ")
        offset = "0"
        limit = "10"
        details = "true"

        print("Start Date : ", startDate)

        print("End Date : ", endDate)

        print("----------------------------------------------------------")

        # Call DTC reusable module

        response = DTC_fetchDTCCodes(self, systemId, startDate, endDate, offset, limit, details, "valid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        issuedTime = "1737670726705"

        if response_body["message"] == "Data Saved Successfully":

            dtc_len = len(response_body["responseData"]["DTCs"])

            if dtc_len >= 1:

                for i in range(dtc_len):

                    status = response_body["responseData"]["DTCs"][i]["status"]

                    if status == 'Unresolved':
                        issuedTime = response_body["responseData"]["DTCs"][i]["issuedTime"]

                        break

            print("----------------------------------------------------------")

            print('DTC Issued Time : ', issuedTime)

            print("----------------------------------------------------------")

            # print('Message : ', message)

            testResult(self, "passed", "DTC Alert details should be saved & fetched successfully",

                   "DTC Alert details are saved & fetched successfully ")

            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "Data Saved Successfully":

            # print(response_body["responseData"]["message"])

            testResult(self, "failed", "DTC Alert details should be saved & fetched successfully",

                   "Failed to save/fetch the dtc details " + " Reason for failure is : " +

                   response_body)

            assert False  # self.result.set_result(TestResults.failed)

        else:

            print("Something went wrong")

            # self.result.set_result(TestResults.failed)

            assert False

        print("----------------------------------------------------------")

        action = "CLEAR"

        # Call DTC clear reusable module

        response = DTC_clearDTC(self, systemId, action, issuedTime, "valid")

        # Validate response status code

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        if response_body["message"] == "DTC clear message sent successfully":

            tracking_id = response_body["responseData"]["tracking_id"]

            # message = response_body["responseData"]["message"]

            print("----------------------------------------------------------")

            print('DTC Clear - Tracking Id : ', tracking_id)

            print("----------------------------------------------------------")

            # print('Message : ', message)

            testResult(self, "passed", "DTC Clear message should be sent with tracking Id successfully ",

                   "DTC Clear message is sent with tracking Id successfully  ")

            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != "DTC clear message sent successfully":

            # print(response_body["responseData"]["message"])

            testResult(self, "failed", "DTC Clear message should be sent with tracking Id successfully ",

                   "Failed to send DTC clear msg " + " Reason for failure is : " +

                   response_body)

            assert False  # self.result.set_result(TestResults.failed)

        else:

            print("Something went wrong")

            # self.result.set_result(TestResults.failed)

            assert False
            
        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the DTC Clear req is sent from cloud to device post triggering DTC Clear API
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, dtcClr_req_msg_type_code,
                                   dtcClr_req_msg_type_code)
        print(ls)

        if dtcClr_req_msg_type_code in str(ls[0]):
            print(f"DTC Clear request sent from cloud' {dtcClr_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "DTC Clear request message should send to device from cloud",

                       "DTC Clear request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "DTC Clear request is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "DTC Clear request message should send to device from cloud",

                       "DTC Clear request is not received from the cloud")

        print("----------------------------------------------------------")

                       
        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, dtcClr_res_msg_type_code,
                                   dtcClr_res_msg_type_code)
        print(ls)

        if dtcClr_res_msg_type_code in str(ls[0]):
            print(f"DTC Clear response sent to cloud' {dtcClr_res_msg_type_code} ' ")
            testResult(self, "verificationPassed", "DTC Clear response message should send to cloud from device",

                       "DTC Clear response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "DTC Clear response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "DTC Clear response message should send to device from cloud",

                       "DTC Clear response is not received from the cloud")

        print("----------------------------------------------------------")

        print("----------------------------------------------------------")

        for i in range(5):

            # Call DTC clear reusable module

            response = DTC_clearDTC_status(self, tracking_id, systemId, "valid")

            # Validate response status code

            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)

                assert False

            # Parse API response into JSON

            response_body = response.json()

            # Validate response body

            if response_body["message"] == "Data Fetched Successfully":

                status = response_body["responseData"]["status"]

                if status == "RESOLVED":

                    break

                else:

                    time.sleep(15)

        if response_body["message"] == "Data Fetched Successfully":

            status = response_body["responseData"]["status"]

            # message = response_body["responseData"]["message"]

            print("----------------------------------------------------------")

            print('DTC Clear - Status : ', status)

            print("----------------------------------------------------------")

            # print('Message : ', message)

            if status == "RESOLVED":

                testResult(self, "passed", "DTC Clear status should be set to 'RESOLVED' successfully ",

                       "DTC Clear status is set to 'RESOLVED' successfully  ")

                # self.result.set_result(TestResults.passed)

            else:

                # print(response_body["responseData"]["message"])

                testResult(self, "failed", "DTC Clear status should be set to 'RESOLVED' successfully ",

                       "DTC Clear status is not set to 'RESOLVED' " + " Reason for failure is : " +

                       response_body)

                assert False  # self.result.set_result(TestResults.failed)

        else:

            print("Something went wrong")

            # self.result.set_result(TestResults.failed)

            assert False

        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")

class Test_dtcOccurence:

    def test_pos_dtc_occurrence_status_All(self):

        print("\n------------------------------START------------------------------\n")
        status = "All"
        startTime = int((datetime.now(tz=timezone.utc) - timedelta(days=1)).timestamp()) * 1000
        endTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        offset = "0"
        limit = "10"

        print(f"Start Time: {startTime}")
        print(f"End Time: {endTime}")
        print(f"Offset: {offset}")
        print(f"Limit: {limit}")
        print(f"Status: {status}")

        # Call DTC occurrence reusable module
        response = dtc_occurrence(self, offset, limit, startTime, endTime, status, "valid")
        
        print("\n------------------------------END------------------------------\n")

    def test_pos_dtc_occurrence_status_resolved(self):

        print("\n------------------------------START------------------------------\n")
        status = "RESOLVED"
        startTime = int((datetime.now(tz=timezone.utc) - timedelta(days=1)).timestamp()) * 1000
        endTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        offset = "0"
        limit = "10"

        print(f"Start Time: {startTime}")
        print(f"End Time: {endTime}")
        print(f"Offset: {offset}")
        print(f"Limit: {limit}")
        print(f"Status: {status}")

        # Call DTC occurrence reusable module
        response = dtc_occurrence(self, offset, limit, startTime, endTime, status, "valid")
        
        print("\n------------------------------END------------------------------\n")

    def test_pos_dtc_occurrence_status_unresolved(self):

        print("\n------------------------------START------------------------------\n")
        status = "Unresolved"
        startTime = int((datetime.now(tz=timezone.utc) - timedelta(days=1)).timestamp()) * 1000
        endTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        offset = "0"
        limit = "10"

        print(f"Start Time: {startTime}")
        print(f"End Time: {endTime}")
        print(f"Offset: {offset}")
        print(f"Limit: {limit}")
        print(f"Status: {status}")

        # Call DTC occurrence reusable module
        response = dtc_occurrence(self, offset, limit, startTime, endTime, status, "valid")
        
        print("\n------------------------------END------------------------------\n")

    def test_pos_dtc_occurrence_status_invalid_offset(self):

        startTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        endTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        offset = "-1"
        limit = "10"
        status = "All"

        print("startTime: ", startTime)
        print("endTime: ", endTime)
        print("offset: ", offset)
        print("limit: ", limit)
        print("Status: ", status)

        # Call DTC reusable module

        response = DTC_dtcOccurence(self, offset, limit, startTime, endTime, status, "valid")

        # Validate response status code

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        if response_body["errors"][0]["errorCode"] == "19005" and response_body["errors"][0]["message"] == "Offset value must not be less than zero":

            testResult(self, "passed", "DTC Occurence details API should throw proper error message for invalid offset",

                       "DTC Occurence details API throwing proper error message for invalid offset")

            assert True

        else:

            testResult(self, "passed", "DTC Occurence details API should throw proper error message for invalid offset",

                       "DTC Occurence details API is not throwing proper error message for invalid offset")

            assert False

        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")

    def test_pos_dtc_occurrence_status_invalid_limit(self):

        startTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        endTime = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        offset = "0"
        limit = "0"
        status = "All"

        print("startTime: ", startTime)
        print("endTime: ", endTime)
        print("offset: ", offset)
        print("limit: ", limit)
        print("Status: ", status)

        # Call DTC reusable module

        response = DTC_dtcOccurence(self, offset, limit, startTime, endTime, status, "valid")

        # Validate response status code

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)

            assert False

        # Parse API response into JSON

        response_body = response.json()

        # Validate response body

        if response_body["errors"][0]["errorCode"] == "19006" and response_body["errors"][0][
            "message"] == "Limit value must not be less than one ":

            testResult(self, "passed", "DTC Occurence details API should throw proper error message for invalid limit",

                       "DTC Occurence details API throwing proper error message for invalid limit")

            assert True

        else:

            testResult(self, "passed", "DTC Occurence details API should throw proper error message for invalid limit",

                       "DTC Occurence details API is not throwing proper error message for invalid limit")

            assert False

        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")


