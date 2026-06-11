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
from C2CModules.commandControl_modules import *
from C2CModules.telemetry_modules import *
from C2CModules.notifications import *


onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_vehConf_ERT:

    def test_pos_ert_crash(self):

        # Read testdata from excel sheet
        dict = read_api_data_from_excel(self, "Notification", "sms_alert")

        mobileNo = str(dict["mobileNo"])

        ert_sms_alert(self, onboardingType, chipsetType, crash_categoryId, mobileNo, "crash_sms")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        # ===========================================================================================
        # Run stub on device for crash alert
        # ===========================================================================================

        print("Run stub for CRASH ALERT on device : ")
        print("----------------------------------------------------------")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert")
        # time.sleep(2)

        print("CRASH ALERT - stub run process is completed, verify logs for alert details : ")
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

        # Verify whether the alert is sent from device to cloud when crash event occurs
        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
                                   crash_alert_notification_deviceLog_string)
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
        #systemId = "gzgfyapC4ebGX3Gf8huKV"

        print("System Id : ", systemId)

        print("----------------------------------------------------------")

        # Call verification module to validate alert details
        #******** cloud side validation is yet to add, currently sms is not stored anywhere on the cloud, so not able to add the validation at cloud side***************
        verify_notification_details_v3(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
                                       notification_type, dt,
                                       dt1, "sms_alert")
        #self.result.set_result(TestResults.passed)

    def test_pos_sos_(self):

        ert_sms_alert(self, onboardingType, chipsetType, sos_categoryId, "sos_sms")

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
        # Run stub on device for tamper alert
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run stub for SOS ALERT on device : ")

        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1", "GCP-QA4","GCP-QA5","PRE-PROD","GCP-QA8"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "sos_alert2")
        else:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "sos_alert1")
        time.sleep(5)

        print("SOS ALERT - stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify whether the alert is sent from device to cloud when ignition is on
        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, sos_alert_notification_deviceLog_string,
                                   sos_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # read systemId from c2c_vehicle.json
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)

        print("\n================ END ================")

        # Call verification module to validate alert details
        #******** cloud side validation is yet to add, currently sms is not stored anywhere on the cloud, so not able to add the validation at cloud side***************

        #self.result.set_result(TestResults.passed)

    def test_pos_towaway(self):

        ert_sms_alert(self, onboardingType, chipsetType, towAway_categoryId, "towaway_sms")

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
        # Run tub on device for TOW AWAY ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TOW AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "towAway_alert3")
        # time.sleep(15)

        print("TOW AWAY ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        # towAway_enable_msg = "tamper_alert:1"
        # ls = verify_message_in_log(self, towAway_enable_msg, towAway_enable_msg)
        # print(ls)

        towAway_alert_notification_string = "constr_and_send_proto_msg success for 1"
        ls = verify_message_in_log(self, towAway_alert_notification_string, towAway_alert_notification_string)
        print(ls)

        # towAway_disable_msg = "tamper_alert:0"
        # ls = verify_message_in_log(self, towAway_disable_msg , towAway_disable_msg)
        # print(ls)

        print("----------------------------------------------------------")

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

        # Call verification module to validate alert details

        # Call verification module to validate alert details
        # ******** cloud side validation is yet to add, currently sms is not stored anywhere on the cloud, so not able to add the validation at cloud side***************

        # self.result.set_result(TestResults.passed)