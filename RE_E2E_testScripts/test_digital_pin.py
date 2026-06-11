import pytest
import random
import time, datetime
import uuid

from C2CModules.digital_pin import *
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile,  run_paho_command_on_primary_IVI, pull_logs_from_IVI_device
from C2CModules.e2e_testData import *
from C2CModules.testResults import testResult
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.notifications import notification_verify_alert_details_v2
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test:

    def test1_positive_generate_digital_pin(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_generate")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_generate_msg_type_code, digitalPin_generate_msg_type_code)

        if digitalPin_generate_msg_type_code in str(ls[0]):
            print(f"Digital Pin generated message printed in device log : ' {digitalPin_generate_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for pin generation",
                       "Device logs contains the logs for pin generation, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Pin generation logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for pin generation",
                       "Device logs does not contain the logs for pin generation or failed to read the device log, pls refer device logs for detailed info")

        #pin_1 - Admin
        #PIN
        #pin_2 - Primary
        #PIN
        #pin_3, pin_4, pin_5, pin_6, pin_7 - Secondary
        #PIN.

    def test2_positive_digital_pin_reset_primary_pin(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN RESET===================================")

        id = "pin_2"
        user_id = str(uuid.uuid4())
        value = random.randint(100000, 999999)
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "reset"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("Value: ", value)
        print("System Id: ", systemId)
        print("Action: ", action)

        #call api reusable module

        response = DigitalPin_reset_PIN(self, systemId, action, id, user_id, value,  "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin reset is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: " ,response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Primary Pin - {id} reset request should send to device",f"Primary Pin - {id} reset request is sent to to device")
                    assert True
        elif response_body["message"] != "Pin reset is in progress":
            testResult(self, "failed", f"Primary Pin - {id} reset request should send to device",f"Failed to send Primary Pin - {id} reset request to cloud")
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Primary Pin reset request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Primary Pin reset request message should send to device from cloud",

                       "Primary Pin reset request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary Pin reset request is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Primary Pin reset request message should send to device from cloud",

                       "Primary Pin reset request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Primary Pin reset response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Primary Pin reset response message should send to cloud from device",

                       "Primary Pin reset response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary Pin reset response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Primary Pin reset response message should send to device from cloud",

                       "Primary Pin reset response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        #call tracking api reusable module

        response = DigitalPin_statusTracking(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"Primary Pin - {id} reset should be success",
                               f"Primary Pin - {id} reset is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Primary Pin - {id} reset should be success",
                                   f"Primary Pin - {id} reset is failed" + " Reason for failure is Pin status " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Primary Pin - {id} reset should be success",
                       f"Failed to reset the primary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong. Please check the api response for more info " + response_body)
            assert False

    def test3_positive_digital_pin_revoke_admin_pin(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================REVOKE ADMIN PIN===================================")

        id = "pin_1"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "revoke"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)
        print("Action: ", action)

        # call api reusable module

        response = DigitalPin_revoke_PIN(self, systemId, action, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin revoke is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Admin Pin - {id} revoke request should send to device",
                               f"Admin Pin - {id} revoke is sent to to device")
                    assert True
        elif response_body["message"] != "Pin revoke is in progress":
            testResult(self, "failed", f"Admin Pin - {id} revoke request should send to device",
                       f"Failed to send the Admin pin -{id} revoke request to device")
            assert False
        else:
            print("Something went wrong. Please check ap[i response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Admin Pin revoke request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Admin Pin revoke request message should send to device from cloud","Admin Pin revoke request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin Pin revoke is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Admin Pin revoke request message should send to device from cloud","Admin Pin revoke request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Admin Pin revoke response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed",
                       "Admin Pin revoke response message should send to cloud from device",

                       "Admin Pin revoke response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin Pin revoke response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Admin Pin revoke response message should send to device from cloud",

                       "Admin Pin revoke response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # call tracking api reusable module

        response = DigitalPin_statusTracking(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"Admin Pin - {id} should revoked successfully",
                               f"Admin Pin - {id} revoke is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Admin Pin - {id} should revoked successfully",
                               f"Admin Pin - {id} revoke is success" + "Reason for failure is " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Admin Pin - {id} should revoked successfully",
                       f"Admin to revoke the Secondary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test4_positive_digital_pin_revoke_secondary_pin(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN REVOKE===================================")

        id = "pin_3"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "revoke"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)
        print("Action: ", action)

        # call api reusable module

        response = DigitalPin_revoke_PIN(self, systemId, action, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin revoke is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Secondary Pin - {id} revoke request should send to device",
                               f"Secondary Pin - {id} revoke is sent to to device")
                    assert True
        elif response_body["message"] != "Pin revoke is in progress":
            testResult(self, "failed", f"Secondary Pin - {id} revoke request should send to device",
                       f"Failed to send the Secondary pin -{id} revoke request to device")
            assert False
        else:
            print("Something went wrong. Please check ap[i response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Secondary Pin revoke request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Secondary Pin revoke request message should send to device from cloud","Secondary Pin revoke request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Secondary Pin revoke is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Secondary Pin revoke request message should send to device from cloud","Secondary Pin revoke request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Secondary Pin revoke response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed",
                       "Secondary Pin revoke response message should send to cloud from device",

                       "Secondary Pin revoke response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "secondary Pin revoke response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Secondary Pin revoke response message should send to device from cloud",

                       "Secondary Pin revoke response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # call tracking api reusable module

        response = DigitalPin_statusTracking(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"secondary Pin - {id} should revoked successfully",
                               f"Secondary Pin - {id} revoke is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Secondary Pin - {id} should revoked successfully",
                               f"Secondary Pin - {id} revoke is success" + "Reason for failure is " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Secondary Pin - {id} should revoked successfully",
                       f"Failed to revoke the Secondary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test5_positive_digital_pin_share_admin_pin(self):

        print("================================PIN SHARING===================================")

        id = "pin_1"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)

        # call api reusable module

        response = DigitalPin_share_PIN(self, systemId, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SHARED":
                    value = response_body["pin"]["value"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Pin Value: ", value)
                    testResult(self, "passed", f"Admin Pin - {id} should be shared successfully to user {user_id}",
                               f"Admin Pin - {id} shared successfully to user {user_id}")
                    assert True
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Admin Pin - {id} should be shared successfully to user {user_id}",
                               f"Admin Pin - {id} failed to share user {user_id}" + "Reason for failure is " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test6_positive_digital_pin_share_primary_pin(self):

        print("================================PIN SHARING===================================")

        id = "pin_2"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)

        # call api reusable module

        response = DigitalPin_share_PIN(self, systemId, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SHARED":
                    value = response_body["pin"]["value"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Pin Value: ", value)
                    testResult(self, "passed", f"Primary Pin - {id} should be shared successfully to user {user_id}",
                               f"Primary Pin - {id} shared successfully to user {user_id}")
                    assert True
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Primary Pin - {id} should be shared successfully to user {user_id}",
                               f"Primary Pin - {id} failed to share user {user_id}" + "Reason for failure is " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test7_positive_digital_pin_share_secondary_pin(self):

        print("================================PIN SHARING===================================")

        id = "pin_4"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)

        # call api reusable module

        response = DigitalPin_share_PIN(self, systemId, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SHARED":
                    value = response_body["pin"]["value"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Pin Value: ", value)
                    testResult(self, "passed", f"Secondary Pin - {id} should be shared successfully to user {user_id}",
                               f"Secondary Pin - {id} shared successfully to user {user_id}")
                    assert True
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Secondary Pin - {id} should be shared successfully to user {user_id}",
                               f"Secondary Pin - {id} failed to share user {user_id}" + "Reason for failure is " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test8_positive_digital_pin_reset_more_than_6_digits(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN RESET===================================")

        id = "pin_2"
        user_id = str(uuid.uuid4())
        value = random.randint(1000000, 9999990)
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "reset"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("Value: ", value)
        print("System Id: ", systemId)
        print("Action: ", action)

        #call api reusable module

        response = DigitalPin_reset_PIN(self, systemId, action, id, user_id, value,  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["errorCode"] == "18031" and response_body["errors"][0]["message"] == "value should contains 6 digits":
            testResult(self, "passed", "Pin should contain 6 digit numbers to reset successfully","Pin contains more/less than 6 digit")
            assert True
        else:
            print("Something went wrong. Please check api response for more info ", response_body)
            assert False

    def test9_positive_digital_pin_unlock_admin(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_vehicle_unlock_admin")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_vehicle_unlock_msg_type_code, digitalPin_vehicle_unlock_msg_type_code)

        if digitalPin_vehicle_unlock_msg_type_code in str(ls[0]):
            print(f"Admin user vehicle unlock message printed in device log : ' {digitalPin_vehicle_unlock_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for admin user vehicle unlock",
                       "Device logs contains the logs for admin user vehicle unlock, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin user vehicle unlock logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for admin user vehicle unlock",
                       "Device logs does not contain the logs for vehicle unlock or failed to read the device log, pls refer device logs for detailed info")

        #pin_1 - Admin
        #PIN
        #pin_2 - Primary
        #PIN
        #pin_3, pin_4, pin_5, pin_6, pin_7 - Secondary
        #PIN.

    def test10_positive_digital_pin_unlock_primary(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_vehicle_unlock_primary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_vehicle_unlock_msg_type_code, digitalPin_vehicle_unlock_msg_type_code)

        if digitalPin_vehicle_unlock_msg_type_code in str(ls[0]):
            print(f"Primary user vehicle unlock message printed in device log : ' {digitalPin_vehicle_unlock_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for primary user vehicle unlock",
                       "Device logs contains the logs for primary user vehicle unlock, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary user vehicle unlock logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for primary user vehicle unlock",
                       "Device logs does not contain the logs for vehicle unlock or failed to read the device log, pls refer device logs for detailed info")

        #pin_1 - Admin
        #PIN
        #pin_2 - Primary
        #PIN
        #pin_3, pin_4, pin_5, pin_6, pin_7 - Secondary
        #PIN.

    def test11_positive_digital_pin_unlock_secondary(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_vehicle_unlock_secondary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_vehicle_unlock_msg_type_code, digitalPin_vehicle_unlock_msg_type_code)

        if digitalPin_vehicle_unlock_msg_type_code in str(ls[0]):
            print(f"Secondary user vehicle unlock message printed in device log : ' {digitalPin_vehicle_unlock_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for secondary user vehicle unlock",
                       "Device logs contains the logs for secondary user vehicle unlock, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Secondary user vehicle unlock logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for secondary user vehicle unlock",
                       "Device logs does not contain the logs for vehicle unlock or failed to read the device log, pls refer device logs for detailed info")

        #pin_1 - Admin
        #PIN
        #pin_2 - Primary
        #PIN
        #pin_3, pin_4, pin_5, pin_6, pin_7 - Secondary
        #PIN.

    def test12_positive_digital_pin_expiry_admin(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_admin")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Admin user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for admin user pin expiry",
                       "Device logs contains the logs for admin userpin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for admin user pin expiry",
                       "Device logs does not contain the logs for admin pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test13_positive_digital_pin_expiry_primary(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        # print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_primary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Primary user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for primary user pin expiry",
                       "Device logs contains the logs for primary user pin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for primary user pin expiry",
                       "Device logs does not contain the logs for primary pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                             notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test14_positive_digital_pin_expiry_secondary(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        # print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_secondary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Secondary user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for secondary user pin expiry",
                       "Device logs contains the logs for secondary user pin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Secondary user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for secondary user pin expiry",
                       "Device logs does not contain the logs for secondary pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                             notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

class Test_Digital_Pin:

    def test1_positive_generate_digital_pin_global(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_generate")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_generate_msg_type_code, digitalPin_generate_msg_type_code)

        if digitalPin_generate_msg_type_code in str(ls[0]):
            print(f"Digital Pin generated message printed in device log : ' {digitalPin_generate_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for pin generation",
                       "Device logs contains the logs for pin generation, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Pin generation logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for pin generation",
                       "Device logs does not contain the logs for pin generation or failed to read the device log, pls refer device logs for detailed info")

        #pin_1 - Admin
        #PIN
        #pin_2 - Primary
        #PIN
        #pin_3, pin_4, pin_5, pin_6, pin_7 - Secondary
        #PIN.

    def test2_positive_digital_pin_reset_primary_pin_global(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN RESET===================================")

        id = "pin_2"
        user_id = str(uuid.uuid4())
        value = random.randint(100000, 999999)
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "reset"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("Value: ", value)
        print("System Id: ", systemId)
        print("Action: ", action)

        #call api reusable module

        response = DigitalPin_reset_PIN_global(self, systemId, action, id, user_id, value,  "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin reset is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: " ,response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Primary Pin - {id} reset request should send to device",f"Primary Pin - {id} reset request is sent to to device")
                    assert True
        elif response_body["message"] != "Pin reset is in progress":
            testResult(self, "failed", f"Primary Pin - {id} reset request should send to device",f"Failed to send Primary Pin - {id} reset request to cloud")
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Primary Pin reset request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Primary Pin reset request message should send to device from cloud",

                       "Primary Pin reset request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary Pin reset request is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Primary Pin reset request message should send to device from cloud",

                       "Primary Pin reset request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Primary Pin reset response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Primary Pin reset response message should send to cloud from device",

                       "Primary Pin reset response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary Pin reset response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Primary Pin reset response message should send to device from cloud",

                       "Primary Pin reset response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        #call tracking api reusable module

        response = DigitalPin_statusTracking_global(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"Primary Pin - {id} reset should be success",
                               f"Primary Pin - {id} reset is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Primary Pin - {id} reset should be success",
                                   f"Primary Pin - {id} reset is failed" + " Reason for failure is Pin status " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Primary Pin - {id} reset should be success",
                       f"Failed to reset the primary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong. Please check the api response for more info " + response_body)
            assert False

    def test3_positive_digital_pin_revoke_admin_pin_global(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================REVOKE ADMIN PIN===================================")

        id = "pin_1"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "revoke"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)
        print("Action: ", action)

        # call api reusable module

        response = DigitalPin_revoke_PIN(self, systemId, action, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin revoke is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Admin Pin - {id} revoke request should send to device",
                               f"Admin Pin - {id} revoke is sent to to device")
                    assert True
        elif response_body["message"] != "Pin revoke is in progress":
            testResult(self, "failed", f"Admin Pin - {id} revoke request should send to device",
                       f"Failed to send the Admin pin -{id} revoke request to device")
            assert False
        else:
            print("Something went wrong. Please check ap[i response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Admin Pin revoke request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Admin Pin revoke request message should send to device from cloud","Admin Pin revoke request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin Pin revoke is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Admin Pin revoke request message should send to device from cloud","Admin Pin revoke request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Admin Pin revoke response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed",
                       "Admin Pin revoke response message should send to cloud from device",

                       "Admin Pin revoke response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin Pin revoke response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Admin Pin revoke response message should send to device from cloud",

                       "Admin Pin revoke response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # call tracking api reusable module

        response = DigitalPin_statusTracking(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"Admin Pin - {id} should revoked successfully",
                               f"Admin Pin - {id} revoke is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Admin Pin - {id} should revoked successfully",
                               f"Admin Pin - {id} revoke is success" + "Reason for failure is " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Admin Pin - {id} should revoked successfully",
                       f"Admin to revoke the Secondary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test4_positive_digital_pin_revoke_secondary_pin_global(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN REVOKE===================================")

        id = "pin_3"
        user_id = str(uuid.uuid4())
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "revoke"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("System Id: ", systemId)
        print("Action: ", action)

        # call api reusable module

        response = DigitalPin_revoke_PIN(self, systemId, action, id, user_id, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Pin revoke is in progress":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "INPROGRESS":
                    trackingId = response_body["pin"]["trackingId"]
                    print("Response Message: ", response_body["message"])
                    print("Pin Id: ", response_body["pin"]["id"])
                    print("Pin Status: ", response_body["pin"]["status"])
                    print("Tracking Id: ", trackingId)
                    testResult(self, "passed", f"Secondary Pin - {id} revoke request should send to device",
                               f"Secondary Pin - {id} revoke is sent to to device")
                    assert True
        elif response_body["message"] != "Pin revoke is in progress":
            testResult(self, "failed", f"Secondary Pin - {id} revoke request should send to device",
                       f"Failed to send the Secondary pin -{id} revoke request to device")
            assert False
        else:
            print("Something went wrong. Please check ap[i response for more info " + response_body)
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

        # Verify whether the Digital Pin req is sent from cloud to device post triggering API
        # Verify Pin reset msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_req_msg_type_code,
                                   digitalPin_reset_req_msg_type_code)
        print(ls)

        if digitalPin_reset_req_msg_type_code in str(ls[0]):
            print(f"Secondary Pin revoke request sent from cloud' {digitalPin_reset_req_msg_type_code} ' ")
            testResult(self, "verificationPassed", "Secondary Pin revoke request message should send to device from cloud","Secondary Pin revoke request has been received successfully from the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Secondary Pin revoke is not received or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Secondary Pin revoke request message should send to device from cloud","Secondary Pin revoke request is not received from the cloud")

        print("----------------------------------------------------------")
        time.sleep(90)

        # Verify whether the DTC Clear res is sent from device to cloud
        # Verify DTC Clear msgs & type code in fetched device logs
        ls = verify_message_in_log(self, digitalPin_reset_res_msg_type_code,
                                   digitalPin_reset_res_msg_type_code)
        print(ls)

        if digitalPin_reset_res_msg_type_code in str(ls[0]):
            print(f"Secondary Pin revoke response sent to cloud' {digitalPin_reset_res_msg_type_code} ' ")
            testResult(self, "verificationPassed",
                       "Secondary Pin revoke response message should send to cloud from device",

                       "Secondary Pin revoke response has been sent successfully to the cloud")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "secondary Pin revoke response is not sent or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Secondary Pin revoke response message should send to device from cloud",

                       "Secondary Pin revoke response is not received from the cloud")

        print("----------------------------------------------------------")

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # call tracking api reusable module

        response = DigitalPin_statusTracking(self, trackingId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            if response_body["pin"]["id"] == id:
                if response_body["pin"]["status"] == "SUCCESS":
                    testResult(self, "passed", f"secondary Pin - {id} should revoked successfully",
                               f"Secondary Pin - {id} revoke is success")
                    assert True
                elif response_body["pin"]["status"] != "SUCCESS":
                    testResult(self, "failed", f"Secondary Pin - {id} should revoked successfully",
                               f"Secondary Pin - {id} revoke is success" + "Reason for failure is " + response_body["pin"]["status"])
                    assert False
        elif response_body["message"] != "Success":
            testResult(self, "failed", f"Secondary Pin - {id} should revoked successfully",
                       f"Failed to revoke the Secondary pin - {id}" + " Reason for failure is : " + response_body["message"])
            assert False
        else:
            print("Something went wrong.Please check api response for more info " + response_body)
            assert False

    def test8_positive_digital_pin_reset_more_than_6_digits_global(self):

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
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        print("================================PIN RESET===================================")

        id = "pin_2"
        user_id = str(uuid.uuid4())
        value = random.randint(1000000, 9999990)
        systemId = read_vehicleJsonFile(self, "system_id")
        action = "reset"

        print("Pin Id: ", id)
        print("User Id: ", user_id)
        print("Value: ", value)
        print("System Id: ", systemId)
        print("Action: ", action)

        #call api reusable module

        response = DigitalPin_reset_PIN(self, systemId, action, id, user_id, value,  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        if response.status_code != 400:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errors"][0]["errorCode"] == "18031" and response_body["errors"][0]["message"] == "value should contains 6 digits":
            testResult(self, "passed", "Pin should contain 6 digit numbers to reset successfully","Pin contains more/less than 6 digit")
            assert True
        else:
            print("Something went wrong. Please check api response for more info ", response_body)
            assert False

    def test12_positive_digital_pin_expiry_admin_global(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        #print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_admin")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Admin user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for admin user pin expiry",
                       "Device logs contains the logs for admin userpin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Admin user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for admin user pin expiry",
                       "Device logs does not contain the logs for admin pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test13_positive_digital_pin_expiry_primary_global(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        # print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_primary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Primary user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for primary user pin expiry",
                       "Device logs contains the logs for primary user pin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Primary user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for primary user pin expiry",
                       "Device logs does not contain the logs for primary pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                             notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    def test14_positive_digital_pin_expiry_secondary_global(self):

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

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        # print("Run stub for vehicle health report on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "digital_pin_expiry_secondary")
        time.sleep(5)

        print("Digital Pin generation stub run process is completed, verify logs for more info: ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify digital pin generated messages in log file
        # ===========================================================================================

        # Digital Pin - Generate

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify digital pin generate in the device logs
        ls = verify_message_in_log(self, digitalPin_expiry_msg_type_code, digitalPin_expiry_msg_type_code)

        if digitalPin_expiry_msg_type_code in str(ls[0]):
            print(f"Secondary user Pin expiry message printed in device log : ' {digitalPin_expiry_msg_type_code} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for secondary user pin expiry",
                       "Device logs contains the logs for secondary user pin expiry, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Secondary user Pin expiry logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for secondary user pin expiry",
                       "Device logs does not contain the logs for secondary pin expiry or failed to read the device log, pls refer device logs for detailed info")

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
        notification_verify_alert_details_v2(self, systemId, pin_expiry_categoryName, pin_expiry_notification_name,
                                             notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")