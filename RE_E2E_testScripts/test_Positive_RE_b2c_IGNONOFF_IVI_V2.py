import time

import pytest

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notification_verify_alert_details, \
    notificationServiceController_details_by_systemId_Category
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


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
        #time.sleep(5)

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

    @pytest.mark.regression
    # Validate Battery IGNITION ON alert functionality.
    # Verify whether the alert is sent from device to cloud when IGNITION is OFF
    # Validate whether the user can get notification message details
    def test1_positive_bikeSecuritySafety_ignitionOFF_alert(self):
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
        #time.sleep(5)

        try:

            # ===========================================================================================
            # Run stub on device for tamper alert
            # ===========================================================================================
            print("----------------------------------------------------------")
            print("Run stub for IGNITION ON ALERT on device : ")

            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "ignition_off_alert")
            #time.sleep(2)

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


















    @pytest.mark.regression
    # Validate that the ignition on alert message is stored in t_notification_events table
    def test2_positive_bikeSecuritySafety_ignition_on_alert_event_details(self):
        print("----------------------------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")

        print("System Id : ", systemId)
        event_status =""

        # Call subscribe reusable module
        response = notificationServiceController_details_by_systemId_Category(self, systemId, ignition_notification_name, "valid")

        #event_id = read_notification_details(self, response, ignition_notification_name, notification_type, "event_id")

        #response = notification_getEvent_details(self, systemId, str(event_id), "valid")

        #event_status = read_notification_event_details(self, response, "eventStatus")

        if event_status == "DELIVERED":
            testResult(self, "passed",
                       "The event status should be updated as DELIVERED in the cloud DB table",
                       "The event status is updated as DELIVERED in the cloud DB table. pls refer device & cloud logs for detailed info")
        else:
            testResult(self, "failed",
                       "The event status should be updated as DELIVERED in the cloud DB table",
                       "The event status is not updated as DELIVERED in the cloud DB table. pls refer device & cloud logs for detailed info")







