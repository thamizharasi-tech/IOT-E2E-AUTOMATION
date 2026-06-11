import time
import pytest
from datetime import datetime, timedelta

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import *
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_crashAlert_R8S3:
    @pytest.mark.regression
    # Validate crash alert functionality.
    # Validate that the alert is sent from device to cloud when a crash event occurs
    # Validate whether the user is able to update the notification event
    def test1_positive_bikeSecuritySafety_crash_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crashAlert_simulation")
        time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

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

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        verify_notification_details_v3(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
                                          notification_type, dt, dt1, "alert_trigger_from_device")


class Test_ignitionAlert_R8S3:

    @pytest.mark.regression
    # Validate Battery IGNITION ON alert functionality.
    # Verify whether the alert is sent from device to cloud when IGNITION is ON
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_ignitionON_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for IGNITION ON ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOn_simulation")
            time.sleep(5)

            print("IGNITION ON ALERT - stub run process is completed, verify logs for alert details : ")
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
            ls = verify_message_in_log(self, ignition_on_alert_notification_deviceLog_string,
                                       ignition_on_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, ignition_on_categoryName, ignition_on_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

    def test2_positive_bikeSecuritySafety_ignitionOFF_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for IGNITION ON ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignitionOff_simulation")
            time.sleep(5)

            print("IGNITION ON ALERT - stub run process is completed, verify logs for alert details : ")
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
            ls = verify_message_in_log(self, ignition_off_alert_notification_deviceLog_string,
                                       ignition_off_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, ignition_off_categoryName, ignition_off_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

class Test_HeatColdAlert_R8S3:

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_batteryHeat_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "batteryHeatAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, battery_heat_alert_notification_deviceLog_string,
                                       battery_heat_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, battery_heat_categoryName, battery_heat_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test2_positive_bikeSecuritySafety_batteryCold_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "batteryColdAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, battery_cold_alert_notification_deviceLog_string,
                                       battery_cold_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, battery_cold_categoryName, battery_cold_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

class Test_ToAwayAlert_R8S3:

    @pytest.mark.regression
    # Validate tow away alert functionality.
    # Verify whether the alert is sent from device when tow away event occurs
    # Validate that the tow way alert is not sent from device when IMU value is 0 and location is triggered
    def test1_positive_bikeSecuritySafety_towAway_alert1(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # Run tub on device for TOW AWAY ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TOW AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "towAwayAlert_simulation")
        time.sleep(15)

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
        towAway_alert_notification_string = "constr_and_send_proto_msg success for 1 : 0"
        ls = verify_message_in_log(self, towAway_alert_notification_string, towAway_alert_notification_string)
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

        # Call verification module to validate alert details
        verify_notification_details_v2(self, systemId, towAway_categoryName_v2, towAway_notification_name_v2,
                                          notification_type, dt, dt1)

class Test_RemoteLockUnlockAlert_R8S3:

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_remote_lock_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remoteLockAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, remote_lock_alert_notification_deviceLog_string,
                                       remote_lock_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, remote_lock_categoryName, remote_lock_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test2_positive_bikeSecuritySafety_remote_unlock_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "remoteUnlockAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, remote_unlock_alert_notification_deviceLog_string,
                                       remote_unlock_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, remote_unlock_categoryName, remote_unlock_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

class Test_PlugInOutAlert_R8S3:

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_plug_in_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "plugInAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, plug_in_alert_notification_deviceLog_string,
                                       plug_in_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, plug_in_categoryName, plug_in_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test2_positive_bikeSecuritySafety_plug_out_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for BATTERY HEAT COLD ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "plugOutAlert_simulation")
            time.sleep(5)

            print("BATTERY HEAT COLD ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when battery heat cold event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, plug_out_alert_notification_deviceLog_string,
                                       plug_out_alert_notification_deviceLog_string)
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

            # systemId = "313"
            print("System Id : ", systemId)

            # Call verification module to validate alert details
            #time.sleep(60)
            verify_notification_details_v2(self, systemId, plug_out_categoryName, plug_out_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

class Test_sosAlert_R8S3:

    @pytest.mark.regression
    # Validate tow away alert functionality.
    # Verify whether the alert is sent from device when tow away event occurs
    # Validate that the tow way alert is not sent from device when IMU value is 0 and location is triggered
    def test1_positive_bikeSecuritySafety_sos_alert(self):
        print("\n================Start Test Execution================")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

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
        # Run tub on device for TOW AWAY ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TOW AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "sosAlert_simulation")
        time.sleep(15)

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
        ls = verify_message_in_log(self, sos_alert_notification_deviceLog_string, sos_alert_notification_deviceLog_string)
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

        # Call verification module to validate alert details
        verify_notification_details_v2(self, systemId, sos_categoryName, sos_notification_name,
                                          notification_type, dt, dt1)


class Test_Alert_R8S4:

    @pytest.mark.regression
    # Validate tow away alert functionality.
    # Verify whether the alert is sent from device when tow away event occurs
    # Validate that the tow way alert is not sent from device when IMU value is 0 and location is triggered
    def test1_positive_bikeSecuritySafety_transaction_control_indicator_alert(self):
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
        # Run tub on device for TOW AWAY ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run TOW AWAY ALERT  stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "transaction_control_indicator_alert")
        time.sleep(15)

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
        ls = verify_message_in_log(self, traction_control_indicator_alert_deviceLog_string, traction_control_indicator_alert_deviceLog_string)
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

        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV"]:
            verify_notification_details_v2(self, systemId, traction_control_indicator_categoryName,
                                           traction_control_indicator_alert_notification_name,
                                           notification_type, dt, dt1)
        else:
            notification_verify_alert_details_v3(self, systemId, traction_control_indicator_categoryName,
                                                 traction_control_indicator_alert_notification_name,
                                                 notification_type, dt, dt1)
        #self.result.set_result(TestResults.passed)
