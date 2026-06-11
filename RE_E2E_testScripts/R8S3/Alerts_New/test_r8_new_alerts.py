
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


class Test_R8_Alerts:

    def test1_RE_B2C_positive_bikeSecuritySafety_bike_charge_state_alert(self):

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
        print("Run BIKE CHARGE STATE ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "bike_charge_state_alert")
        time.sleep(15)

        print("BIKE CHARGE STATE ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, bike_charge_state_alert_notification_deviceLog_string,
                                   bike_charge_state_alert_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, bike_charge_state_categoryName,
                                           bike_charge_state_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, bike_charge_state_categoryName,
                                                 bike_charge_state_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test2_RE_B2C_positive_bikeSecuritySafety_harsh_acceleration_notification(self):

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
        print("Run HARSH ACCELERATION NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "harsh_acceleration_notification")
        time.sleep(15)

        print("HARSH ACCELERATION NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, harsh_acceleration_notification_deviceLog_string,
                                   harsh_acceleration_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, harsh_acceleration_categoryName,
                                           harsh_acceleration_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, harsh_acceleration_categoryName,
                                                 harsh_acceleration_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test3_RE_B2C_positive_bikeSecuritySafety_harsh_barking_notification(self):

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
        print("Run HARSH BRAKING NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "harsh_barking_notification")
        time.sleep(15)

        print("HARSH BRAKING NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, harsh_barking_notification_deviceLog_string,
                                   harsh_barking_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, harsh_barking_categoryName,
                                           harsh_barking_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, harsh_barking_categoryName,
                                                 harsh_barking_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test4_RE_B2C_positive_bikeSecuritySafety_hill_hold_state_alert(self):

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
        print("Run HILL HOLD STATE NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "hill_hold_state_alert")
        time.sleep(15)

        print("HILL HOLD STATE NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, hill_hold_state_alert_notification_deviceLog_string,
                                   hill_hold_state_alert_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, hill_hold_state_categoryName,
                                           hill_hold_state_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, hill_hold_state_categoryName,
                                                 hill_hold_state_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test5_RE_B2C_positive_bikeSecuritySafety_limp_mode_alert(self):

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
        print("Run LIMP MODE NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "limp_mode_alert")
        time.sleep(15)

        print("LIMP MODE NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, limp_mode_alert_notification_deviceLog_string,
                                   limp_mode_alert_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, limp_mode_categoryName,
                                           limp_mode_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, limp_mode_categoryName,
                                                 limp_mode_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test6_RE_B2C_positive_bikeSecuritySafety_low_battery_state_1_alert(self):

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

    def test7_RE_B2C_positive_bikeSecuritySafety_low_battery_state_2_alert(self):

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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "low_battery_state_2_alert")
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
        ls = verify_message_in_log(self, low_battery_state_2_notification_deviceLog_string,
                                   low_battery_state_2_notification_deviceLog_string)
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
            verify_notification_details_v2(self, systemId, low_battery_state_2_categoryName,
                                           low_battery_state_2_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, low_battery_state_2_categoryName,
                                                 low_battery_state_2_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test8_RE_B2C_positive_bikeSecuritySafety_motor_temp_warn_alert(self):

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
        print("Run MOTOR TEMPERATURE WARNING NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "motor_temp_warn_alert")
        time.sleep(15)

        print("MOTOR TEMPERATURE WARNING NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, motor_temp_warn_alert_notification_deviceLog_string,
                                   motor_temp_warn_alert_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, motor_temp_warn_categoryName,
                                           motor_temp_warn_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, motor_temp_warn_categoryName,
                                                 motor_temp_warn_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)

    def test9_RE_B2C_positive_bikeSecuritySafety_transaction_control_indicator_alert(self):

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
        # Run tub on device for TRACTION CONTROL INDICATOR ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TRACTION CONTROL INDICATOR ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "transaction_control_indicator_alert")
        time.sleep(15)

        print("TRACTION CONTROL INDICATOR ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, transaction_control_indicator_alert_deviceLog_string,
                                   transaction_control_indicator_alert_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, traction_control_indicator_categoryName,
                                           traction_control_indicator_alert_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, traction_control_indicator_categoryName,
                                                 traction_control_indicator_alert_notification_name,
                                                 notification_type, dt, dt1)

        # self.result.set_result(TestResults.passed)

    def test10_RE_B2C_positive_bikeSecuritySafety_cruise_control_state_alert(self):

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
        print("Run CRUISE CONTROL STATE NOTIFICATION stub on device: ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "cruise_control_state_alert")
        time.sleep(15)

        print("CRUISE CONTROL STATE ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, cruise_control_state_alert_deviceLog_string,
                                   cruise_control_state_alert_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, cruise_control_state_categoryName,
                                           cruise_control_state_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, cruise_control_state_categoryName,
                                                 cruise_control_state_notification_name,
                                                 notification_type, dt, dt1)
            # self.result.set_result(TestResults.passed)


class Test_R8_Alerts_only_device:

    def test1_RE_B2C_positive_bikeSecuritySafety_low_pressure_for_front_alert(self):

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
        print("Run Low PRESSURE FOR FRONT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "low_pressure_for_front_alert")
        time.sleep(15)

        print("Low PRESSURE FOR FRONT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, low_pressure_for_front_alert_notification_deviceLog_string,
                                   low_pressure_for_front_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test2_RE_B2C_positive_bikeSecuritySafety_flat_tire_error_for_front_alert(self):
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
        print("Run FLAT TIRE ERROR FOR FRONT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "flat_tire_error_for_front_alert")
        time.sleep(15)

        print("FLAT TIRE ERROR FOR FRONT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, flat_tire_error_for_front_alert_notification_deviceLog_string,
                                   flat_tire_error_for_front_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test3_RE_B2C_positive_bikeSecuritySafety_flat_tire_error_for_rear_alert(self):
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
        print("Run FLAT TIRE ERROR FOR REAR  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "flat_tire_error_for_rear_alert")
        time.sleep(15)

        print("FLAT TIRE ERROR FOR REAR stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, flat_tire_error_for_rear_alert_notification_deviceLog_string,
                                   flat_tire_error_for_rear_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test4_RE_B2C_positive_bikeSecuritySafety_low_pressure_for_rear_alert(self):

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
        print("Run Low PRESSURE FOR REAR  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "low_pressure_for_rear_alert")
        time.sleep(15)

        print("Low PRESSURE FOR REAR stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, low_pressure_for_rear_alert_notification_deviceLog_string,
                                   low_pressure_for_rear_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test5_RE_B2C_positive_bikeSecuritySafety_high_pressure_for_rear_alert(self):

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
        print("Run High PRESSURE FOR REAR ALERT stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "high_pressure_for_rear_alert")
        time.sleep(15)

        print("High PRESSURE FOR REAR ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, high_pressure_for_rear_alert_notification_deviceLog_string,
                                   high_pressure_for_rear_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test6_RE_B2C_positive_bikeSecuritySafety_high_pressure_for_front_alert(self):

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
        print("Run High PRESSURE FOR FRONT stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "high_pressure_for_front_alert")
        time.sleep(15)

        print("High PRESSURE FOR FRONT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, high_pressure_for_front_alert_notification_deviceLog_string,
                                   high_pressure_for_front_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test7_RE_B2C_positive_bikeSecuritySafety_pin_error_alert(self):

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
        print("Run PIN ERROR ALERT stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "pin_error_alert")
        time.sleep(15)

        print("PIN ERROR ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, pin_error_alert_notification_deviceLog_string,
                                   pin_error_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test8_RE_B2C_positive_bikeSecuritySafety_battery_health_alert(self):

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
        print("Run BATTERY HEALTH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "battery_health_alert")
        time.sleep(15)

        print("BATTERY HEALTH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, battery_health_alert_notification_deviceLog_string,
                                   battery_health_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test9_RE_B2C_positive_bikeSecuritySafety_battery_high_temp_alert(self):

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
        print("Run BATTERY High TEMP ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "battery_high_temp_alert")
        time.sleep(15)

        print("BATTERY HIGH TEMP ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, battery_high_temp_alert_notification_deviceLog_string,
                                   battery_high_temp_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test10_RE_B2C_positive_bikeSecuritySafety_bms_communication_fail_alert(self):

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
        print("Run BMS Communication Fail Alert  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "bms_communication_fail_alert")
        time.sleep(15)

        print("BMS Communication Fail Alert stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, bms_communication_fail_alert_notification_deviceLog_string,
                                   bms_communication_fail_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test11_RE_B2C_positive_bikeSecuritySafety_brake_control_fail_alert(self):

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
        print("Run BRAKE CONTROL FAIL ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "brake_control_fail_alert")
        time.sleep(15)

        print("BRAKE CONTROL FAIL ALERTT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, brake_control_fail_alert_notification_deviceLog_string,
                                   brake_control_fail_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test12_RE_B2C_positive_bikeSecuritySafety_handlebar_controls_fail_alert(self):

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
        print("Run HANDLEBAR CONTROLS FAIL ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "handlebar_controls_fail_alert")
        time.sleep(15)

        print("HANDLEBAR CONTROLS FAIL ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, handlebar_controls_fail_alert_notification_deviceLog_string,
                                   handlebar_controls_fail_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test13_RE_B2C_positive_bikeSecuritySafety_mcu_high_temp_alert(self):

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
        print("Run MCU HIGH TEMP ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "mcu_high_temp_alert")
        time.sleep(15)

        print("MCU HIGH TEMP ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, mcu_high_temp_alert_notification_deviceLog_string,
                                   mcu_high_temp_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test14_RE_B2C_positive_bikeSecuritySafety_motor_health_alert(self):

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
        print("Run MOTOR HEALTH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "motor_health_alert")
        time.sleep(15)

        print("MOTOR HEALTH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, motor_health_alert_notification_deviceLog_string,
                                   motor_health_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test15_RE_B2C_positive_bikeSecuritySafety_obc_communication_fail_alert(self):

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
        print("Run OBC Communication Fail Alert  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "obc_communication_fail_alert")
        time.sleep(15)

        print("OBC Communication Fail Alert stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, obc_communication_fail_alert_notification_deviceLog_string,
                                   obc_communication_fail_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test16_RE_B2C_positive_bikeSecuritySafety_thermal_run_away_alert(self):

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
        print("Run THERMAL RUN AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "thermal_run_away_alert")
        time.sleep(15)

        print("THERMAL RUN AWAY ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, thermal_run_away_alert_notification_deviceLog_string,
                                   thermal_run_away_alert_notification_deviceLog_string)
        print(ls)

        print("----------------------------------------------------------")

    def test17_RE_B2C_positive_bikeSecuritySafety_vehicle_fully_charged_alert(self):

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
        print("Run VEHICLE FULLY CHARGED NOTIFICATION  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "vehicle_fully_charged_alert")
        time.sleep(15)

        print("VEHICLE FULLY CHARGED NOTIFICATION stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        ls = verify_message_in_log(self, vehicle_fully_charged_alert_notification_deviceLog_string,
                                   vehicle_fully_charged_alert_notification_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "GCP-QA4"]:
            verify_notification_details_v2(self, systemId, vehicle_fully_charged_categoryName,
                                           vehicle_fully_charged_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, vehicle_fully_charged_categoryName,
                                                 vehicle_fully_charged_notification_name,
                                                 notification_type, dt, dt1)
        # self.result.set_result(TestResults.passed)