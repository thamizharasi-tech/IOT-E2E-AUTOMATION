import time

import pytest

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.notifications import notification_verify_alert_details
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile
from C2CModules.resuse_modules import verify_message_in_log

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


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






