import os,sys,datetime,time,subprocess,inspect,logging
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
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.testResults import testResult

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

    def execute(self):

        print("----------------------------------------------------------")    
        print("Validate that the critical battery message send from device are getting stored to database and the user is able to fetch the data via API ")
        print("----------------------------------------------------------")

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

        # verify battery soc attribute in the device logs
        ls = verify_message_in_log(self, b2c_telemetry_battery_soc_attribute, b2c_telemetry_battery_soc_attribute)

        if b2c_telemetry_battery_soc_attribute in str(ls[0]):
            print(f"Battery SOC attribute name printed in device log : ' {b2c_telemetry_battery_soc_attribute} ' ")
            testResult(self, "passed", "Battery SOC attribute should be present in telemetry data",
                       "Battery SOC attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery SOC attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Battery SOC attribute should be present in telemetry data ",
                       "Battery SOC attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify soc value in the device logs
        tele_battery = b2c_telemetry_battery_soc_attribute + b2c_telemetry_battery_soc_value
        ls = verify_message_in_log(self, b2c_telemetry_battery_soc_value, tele_battery)

        if tele_battery in str(ls[0]):
            print(f"Battery SOC value printed in device log : ' {tele_battery} ' ")
            testResult(self, "passed", "Battery SOC value should be published to cloud ",
                       "Battery SOC value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Battery SOC value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Battery SOC value should be published to cloud ",
                       "Battery SOC value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

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
        status = ""

        response = telemetry_Curr_eventType(self, telemetry_battery_eventType, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            # print(dataList_len)
            for j in range(dataList_len):
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_soc:
                    soc_value = response_body["responseData"]["dataList"][j]["value"]
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_level:
                    level_value = response_body["responseData"]["dataList"][j]["value"]
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_voltage:
                    voltage_value = response_body["responseData"]["dataList"][j]["value"]
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_current:
                    current_value = response_body["responseData"]["dataList"][j]["value"]
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_temp:
                    temp_value = response_body["responseData"]["dataList"][j]["value"]
                if response_body["responseData"]["dataList"][j]["name"] == telemetry_attribute_ev_battery_soh:
                    soh_value = response_body["responseData"]["dataList"][j]["value"]
        except:
            print("dataList is empty in api response")

        print("----------------------------------------------------------")

        print("Battery SOC value configured in the telemetry stub : ", b2c_telemetry_battery_soc_value)
        print("Battery SOC value stored in Cloud DB : ", soc_value)

        if float(soc_value) == float(b2c_telemetry_battery_soc_value):            
            testResult(self, "passed",
                       "Battery SOC value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery SOC value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "verificationFailed",
                       "Battery SOC value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery SOC value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            status = "FAIL"
        print("----------------------------------------------------------")

        print("Battery Level value configured in the telemetry stub : ", b2c_telemetry_battery_level_value)
        print("Battery Level value stored in Cloud DB : ", level_value)

        if float(level_value) == float(b2c_telemetry_battery_level_value):
            testResult(self, "passed",
                       "Battery Level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Level value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "VerificationFailed",
                       "Battery Level value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Level value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            status = "FAIL"
        print("----------------------------------------------------------")

        print("Battery Voltage value configured in the telemetry stub : ", b2c_telemetry_battery_voltage_value)
        print("Battery Voltage value stored in Cloud DB : ", voltage_value)

        if float(voltage_value) == float(b2c_telemetry_battery_voltage_value):
            testResult(self, "passed",
                       "Battery Voltage value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Voltage value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "VerificationFailed",
                       "Battery Voltage value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Voltage value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            status = "FAIL"
        print("----------------------------------------------------------")

        print("Battery Current value configured in the telemetry stub : ", b2c_telemetry_battery_current_value)
        print("Battery Current value stored in Cloud DB : ", current_value)

        if float(current_value) == float(b2c_telemetry_battery_current_value):
            testResult(self, "passed",
                       "Battery Current value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Current value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "VerificationFailed",
                       "Battery Current value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Current value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            status = "FAIL"
        print("----------------------------------------------------------")

        print("Battery Temperature value configured in the telemetry stub : ", b2c_telemetry_battery_temperature_value)
        print("Battery Temperature value stored in Cloud DB : ", temp_value)

        if float(temp_value) == float(b2c_telemetry_battery_temperature_value):
            testResult(self, "passed",
                       "Battery Temperature value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Temperature value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "VerificationFailed",
                       "Battery Temperature value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery Temperature value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            # status = "FAIL"
        print("----------------------------------------------------------")

        print("Battery SOH value configured in the telemetry stub : ", b2c_telemetry_battery_soh_value)
        print("Battery SOH value stored in Cloud DB : ", soh_value)

        if float(soh_value) == float(b2c_telemetry_battery_soh_value):
            testResult(self, "passed",
                       "Battery SOH value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery SOH value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")            
        else:
            testResult(self, "VerificationFailed",
                       "Battery SOH value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Battery SOH value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            # status = "FAIL"
        print("----------------------------------------------------------")

        if status == "FAIL":
            self.result.set_result(TestResults.failed)
            print("Battery value is incorrect. hence marking this test cases as Fail ")
            print("----------------------------------------------------------")
            assert False
        else:
            self.result.set_result(TestResults.passed)
            print("-------------------------------------------------------------------------")            

        
    def cleanup(self):
        pass
        


if __name__ == '__main__':
    test = Test()
    test.run()

