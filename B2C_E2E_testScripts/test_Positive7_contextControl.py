import base64
import time

import pytest

from C2CModules.e2e_testData import *
from C2CModules.contextControl_modules import context_Control, context_Control_for_telemetry_location
from C2CModules.primary_IVI_device_modules import get_SystemId, pull_logs_from_IVI_device, decode_msg_body
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

# Block Id's:
blockId = ['3101', '2001', '2002', '1001', '2005', '5002', '3250']
reason_code = 0
enable = 'true'
frequency = 1


class Test1_contextControl:

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test1_context_control_for_telemetry_location1(self):
        print("\n================Start Test Execution================")
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        for i in range(6):
            block_id = blockId[i]
            print(block_id)
            context_Control(self, block_id, reason_code, enable, frequency, systemId)
            time.sleep(30)

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test1_context_control_for_telemetry_location(self):
        print("\n================Start Test Execution================")
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call context control reusable module
        response_body = context_Control_for_telemetry_location(self, systemId)

        assert (response_body["responseCode"] == "1200")
        try:
            print(response_body["message"])

            # ===========================================================================================
            # Device side validations : Fetch logs & verify context control messages
            # ===========================================================================================

            print("========================================================")
            print("Device Validations : ")
            print("========================================================")

            # Fetch/pull logs from device
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Verify Context Control Messages => ")

            print("Verify Context Control message arrived from cloud: : ")
            print("------------------------------------------------------")
            # Verify context control msgs & type code in fetched device logs
            msg_254 = verify_message_in_log(self, contextControl_msg_254, contextControl_msg_254)

            print("Message Type 254 : ", msg_254)

            testResult(self, "passed", "Context Control message should be arrived from cloud ",
                       "Context Control message is arrived from cloud  and device logs are updated accordingly, pls refer "
                       "device logs for detailed info")
        except:
            testResult(self, "failed", "Context Control message should be arrived from cloud ",
                       "Context Control message is not recevied by Device or logs are not updated accordingly, pls refer "
                       "device & cloud logs for detailed info")

        try:

            print("Verify Context Control acknowledge message sent to cloud : ")
            print("------------------------------------------------------")

            # Verify context control msgs & type code in fetched device logs
            msg_255 = verify_message_in_log(self, telemetry_msg_id_published2Cloud, contextControl_msg_255)

            print("Message Type 255 : ", msg_255)

            testResult(self, "passed", "Device should send acknowledge msg for received Context Control message ",
                       "Device sent acknowledge msg for received Context Control message, pls refer "
                       "device logs for detailed info")
        except:
            testResult(self, "failed", "Device should send acknowledge msg for received Context Control message",
                       "Device has not sent acknowledge msg back to cloud or logs are not updated accordingly, pls refer"
                       "device & cloud logs for detailed info")

        try:

            print("Verify Context Control response message sent to cloud : ")
            print("------------------------------------------------------")

            print("Configuration Data : ")
            print("----------------------")
            # Verify context control msgs & type code in fetched device logs
            ls_data = verify_message_in_log(self, 'configuration data =', 'configuration data =')

            print("Configuration data : ", ls_data)

            print("Mapping for reason code : ")
            print("----------------------")
            # Verify context control msgs & type code in fetched device logs
            ls_data = verify_message_in_log(self, 'mapping found for reason_code', 'found for reason_code')

            print("Mapping : ", ls_data)

            if "No mapping found" in str(ls_data).replace('\n', ''):
                testResult(self, "verificationFailed", "Device should have proper mapping for reason code",
                           "'No mapping found for reason_code' is found in logs or logs are not updated accordingly, pls refer"
                           "device & cloud logs for detailed info")

            print("----------------------")

            # Verify context control msgs & type code in fetched device logs
            ls = verify_message_in_log(self, telemetry_msg_id_published2Cloud, contextControl_msg_256)

            print("Message Type 256 : ", ls)

            testResult(self, "passed", "Device should send context control response to cloud ",
                       "Device sent context control response to cloud, pls refer "
                       "device logs for detailed info")

            # self.result.set_result(TestResults.passed)
            print("-----------------------------")

        except:
            testResult(self, "failed", "Device should send context control response to cloud",
                       "Device has not sent context control response to cloud or logs are not updated accordingly, pls refer"
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        try:
            print("Verify Context Control message body for configured attributes & its value: ")
            print("------------------------------------------------------")
            msg_body_data = decode_msg_body(str(ls[0]))
            ls1 = str(ls[0]).split('{"body_encoding_type":1},"body":')
            data = str(ls1[1])
            print(data)
            lenmax = len(data) - len(data) % 4
            decodedBytes = base64.b64decode(data[0:lenmax]).decode()

            msg_body_data = str(decodedBytes)
            print("Decoded message body :", msg_body_data)
        except:
            print("Unable to decode message body data due to truncated logs")

        try:

            if '"block_id": 10' in msg_body_data:
                testResult(self, "passed",
                           "'block_id' should be present in the msg body and it should have configured value",
                           "'block_id' is present in the msg body and it has configured value")
            else:
                testResult(self, "verificationFailed",
                           "'block_id' should be present in the msg body and it should have configured value",
                           "'block_id' is not present in the msg body or not has the configured value")
            if '"reason_code": 51' in msg_body_data:
                testResult(self, "passed",
                           "'reason_code' should be present in the msg body and it should have configured value",
                           "'reason_code' is present in the msg body and it has configured value")
            else:
                testResult(self, "verificationFailed",
                           "'reason_code' should be present in the msg body and it should have configured value",
                           "'reason_code' is not present in the msg body or not has the configured value")

            if '"enable": true' in msg_body_data:
                testResult(self, "passed",
                           "'enable' should be present in the msg body and it should have configured flag",
                           "'enable' is present in the msg body and it has configured flag")
            else:
                testResult(self, "verificationFailed",
                           "'enable' should be present in the msg body and it should have configured flag",
                           "'enable' is not present in the msg body or not has the configured flag")

            if '"frequency": 1' in msg_body_data:
                testResult(self, "passed",
                           "'frequency' should be present in the msg body and it should have configured value",
                           "'frequency' is present in the msg body and it has configured value")
            else:
                testResult(self, "verificationFailed",
                           "'frequency' should be present in the msg body and it should have configured value",
                           "'frequency' is not present in the msg body or not has the configured value")
        except:
            print(
                "Something went wrong while validating the msg body. pls refer device logs for additional details")
        print("----------------------------------------------------------")
