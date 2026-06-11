import inspect
import logging
import os
import sys
import time
from pathlib import Path

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
sys.path.insert(0, parent_dir)

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.testResults import testResult
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr_eventType

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

try:
    from axiom.ttypes import *
except:
    from Axiom.ttypes import *
from axiom_framework.tests.base import Test as Base
from axiom_framework.results.base import TestResults


class Test(Base):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self):
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

    def execute(self):

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "critical_battery")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - odo

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify battery soc attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_block_msg, b2c_telemetry_battery_block_msg)

        if b2c_telemetry_battery_block_msg in str(ls[0]):
            print(f"Battery SOC attribute name printed in device log : ' {b2c_telemetry_battery_block_msg} ' ")
            testResult(self, "passed", "Battery message should be published to cloud",
                       "Battery message is published to cloud, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            testResult(self, "verificationFailed", "Battery message should be published to cloud ",
                       "Battery message is not published to cloud or device logs are not updated. pls refer device logs in detail ")

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

        # Hit telemetry curr api with data
        response = telemetry_Curr_eventType(self, "", systemId, "invalid")

        # Parse API response into JSON
        response_body = response.json()

        print("-------------------------------------------------------------------------")

        # Validate response body
        if response_body["responseCode"] == "1200":
            self.result.set_result(TestResults.passed)
            try:
                dataList_len = len(response_body["responseData"]["dataList"])
                # print(dataList_len)
                for j in range(dataList_len):
                    print("Id : ", response_body["responseData"]["dataList"][j]["id"])
                    print("Name : ", response_body["responseData"]["dataList"][j]["name"])
                    print("Unit : ", response_body["responseData"]["dataList"][j]["unit"])
                    print("Value : ", response_body["responseData"]["dataList"][j]["value"])
                    print("Update Time : ", response_body["responseData"]["dataList"][j]["updatedTime"])
                    print("Response Code : ", response_body["responseData"]["dataList"][j]["reasonCode"])
                    print("Area : ", response_body["responseData"]["dataList"][j]["area"])
                    print("Area name : ", response_body["responseData"]["dataList"][j]["areaName"])
                    print("-------------------------------------------------------------------------")
            except:
                print("dataList is empty in api response")
                self.result.set_result(TestResults.failed)
        else:
            self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

    def cleanup(self):
        pass


if __name__ == '__main__':
    test = Test()
    test.run()
