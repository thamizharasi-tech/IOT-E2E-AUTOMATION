import json
import time
from datetime import timezone
import random

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.vehicle_state import *
from C2CModules.telemetry_modules import *


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_vehConf_normalMode:

    def test_over_speed_alert_normal(self):

        #systemId = read_vehicleJsonFile(self, "system_id")
        getset_config_v2(self, onboardingType, chipsetType, "alert_conf", "path2")
        #vehicle_conf_factory_reset(self, systemId)
        time.sleep(20)

        vehicle_conf_alert_conf_update(self, onboardingType, chipsetType, "normal_mode")

        systemId = read_vehicleJsonFile(self, "system_id")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for over speed on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_overspeed")
        time.sleep(5)

        print("Over speed stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - Over Speed

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Over Speed attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_over_speed_attribute, b2c_telemetry_over_speed_attribute)

        if b2c_telemetry_over_speed_attribute in str(ls[0]):
            print(f"Over Speed attribute name printed in device log : ' {b2c_telemetry_over_speed_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs contains the logs for Over Speed (constr_and_send_proto_msg success for 4445), pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Over Speed logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Over Speed (constr_and_send_proto_msg success for 4445)",
                       "Device logs doesnot contain the logs for Over Speed (constr_and_send_proto_msg success for 4445) or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_speed_event_type1, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == "SPEED" or \
                        response_body["responseData"]["signals"][j][
                            "name"] == "Display_info__Display_Vehicle_Speed_RX_V":
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Speed value configured in the telemetry stub : ", telemetry_over_speed_value)
        print("Speed value stored in Cloud DB : ", value)

        if float(value) == float(
                telemetry_over_speed_value):  # and int(reasonCode) == int(telemetry_over_speed_reason_code):
            testResult(self, "passed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Over Speed value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Over Speed value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            #self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")
