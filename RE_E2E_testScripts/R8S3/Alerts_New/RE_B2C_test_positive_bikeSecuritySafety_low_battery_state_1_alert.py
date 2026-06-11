import os,sys,datetime,time,subprocess,inspect,logging
from pathlib import Path

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
sys.path.insert(0, parent_dir)

from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.e2e_testData import *
from C2CModules.notifications import *
from C2CModules.primary_IVI_device_modules import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None


class Test:

    def test_execute(self):

        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
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

        # ===========================================================================================
        # Run tub on device for  ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run LOW BATTERY NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "low_battery_state_1_alert")
        time.sleep(15)

        print("LOW BATTERY NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, low_battery_state_1_notification_deviceLog_string,
                                   low_battery_state_1_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV","GCP-QA4"]:
            verify_notification_details_v2(self, systemId, low_battery_state_1_categoryName,
                                           low_battery_state_1_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, low_battery_state_1_categoryName,
                                                 low_battery_state_1_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

