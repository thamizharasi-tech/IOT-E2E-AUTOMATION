import time
import pytest
from datetime import datetime, timedelta

from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notification_verify_update_status, notification_verify_notify_status, \
    notification_verify_event_details, notification_verify_alert_details, \
    notificationServiceController_details_by_systemId_Category
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_RE_SP2_TamperingAlert:

    @pytest.mark.regression
    # Validate tamper alert functionality.
    # Verify whether the alert is sent from device to cloud when tampering event occurs
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_tampering_alert(self):
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
            print("Run stub for TAMPER ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "tampering_alert")
            # time.sleep(2)

            print("TAMPER ALERT - stub run process is completed, verify logs for alert details : ")
            print("----------------------------------------------------------")

            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, onboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            # Verify whether the alert is sent from device to cloud when tampering event occurs
            # Verify notification msgs & type code in fetched device logs
            ls = verify_message_in_log(self, tamper_alert_notification_deviceLog_string,
                                       tamper_alert_notification_deviceLog_string)
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
            notification_verify_alert_details(self, systemId, tamper_categoryName_v2, tamper_notification_name_v2,
                                              notification_type, dt, dt1)
        except:
            assert False


class Test_RE_SP2_ToAwayAlert:

    @pytest.mark.regression
    # Validate tow away alert functionality.
    # Verify whether the alert is sent from device when tow away event occurs
    # Validate that the tow way alert is not sent from device when IMU value is 0 and location is triggered
    def test1_positive_bikeSecuritySafety_towAway_alert(self):
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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "towAway_alert")
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
        notification_verify_alert_details(self, systemId, towAway_categoryName_v2, towAway_notification_name_v2,
                                          notification_type, dt, dt1)


class Test_RE_SP2_crashAlert:
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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert")
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
        notification_verify_alert_details(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
                                          notification_type, dt, dt1)


class Test_RE_SP3_ignitionAlert:

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

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignition_on_alert")
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
            ls = verify_message_in_log(self, ignition_alert_notification_deviceLog_string,
                                       ignition_alert_notification_deviceLog_string)
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
            time.sleep(60)
            notification_verify_alert_details(self, systemId, ignition_categoryName, ignition_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False

class Test_RE_SP3_HeatColdAlert:

    @pytest.mark.regression
    # Validate Battery Heat Cold alert functionality.
    # Verify whether the alert is sent from device to cloud when Battery Heat Cold event occurs
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_batteryHeatCold_alert(self):
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

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "batteryHeatCold_alert")
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
            ls = verify_message_in_log(self, battery_heatCold_alert_notification_deviceLog_string,
                                       battery_heatCold_alert_notification_deviceLog_string)
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
            time.sleep(60)
            notification_verify_alert_details(self, systemId, battery_heatCold_categoryName, battery_heatCold_notification_name,
                                              notification_type, dt, dt1)
        except:
            assert False


class Test_RE_SP2_ToAwayAlert:

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

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "towAway_alert1")
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
        notification_verify_alert_details(self, systemId, towAway_categoryName_v2, towAway_notification_name_v2,
                                          notification_type, dt, dt1)