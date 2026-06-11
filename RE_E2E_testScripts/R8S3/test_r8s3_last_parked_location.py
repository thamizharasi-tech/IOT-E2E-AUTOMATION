import time
import pytest
from datetime import datetime, timedelta

from C2CModules.e2e_testData import *
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file
from C2CModules.telemetry_modules import *
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import vehicle_update_metadata
from utils.XLUtils import read_api_data_from_excel

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_R8S3_LastParkedLocation:

    @pytest.mark.regression
    # Validate telemetry-odometer functionality.
    def test1_positive_bikeSecuritySafety_lastParkedLocation(self):
        print("\n================ Start Test Execution ================")

        # -------------------------------------------------------------------------
        # Timestamp
        # -------------------------------------------------------------------------
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("----------------------------------------------------------")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        # -------------------------------------------------------------------------
        # Run telemetry stub on device
        # -------------------------------------------------------------------------
        print("----------------------------------------------------------")
        print("Run Last Parked Location - Telemetry stub on device : ")

        # run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "last_parked_location")

        if cloudEnv in ["GCP-DEMO2", "GCP-QA"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "last_parked_location1")
        elif cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "RE-UAT"]:
            run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "last_parked_location2")

        time.sleep(15)
        print("Last Parked Location - Telemetry stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # -------------------------------------------------------------------------
        # Pull logs for validations
        # -------------------------------------------------------------------------
        print("Pull/Fetch device logs for validation : ")
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        print("Logs are fetched from device to host machine @ desired location for validation")
        print("----------------------------------------------------------")

        # -------------------------------------------------------------------------
        # Device side validations
        # -------------------------------------------------------------------------
        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Ignition On attribute in the device
        if cloudEnv in ["GCP-QA3", "RE-DM1", "RE-DEV", "RE-UAT"]:
            telemetry_ignition_value = "0"
        else:
            telemetry_ignition_value = "3"

        tele_ignition_on = telemetry_ignition_attribute + telemetry_ignition_value
        ls = verify_message_in_log(self, telemetry_ignition_value, tele_ignition_on)

        if telemetry_ignition_attribute in str(ls[0]):
            print(f"Ignition Off attribute name printed in device log : ' {telemetry_ignition_attribute} ' ")
            testResult(
                self,
                "passed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs contains the logs for Ignition Off, pls refer device logs for detailed info"
            )
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print("Ignition Off logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(
                self,
                "verificationFailed",
                "Device logs should contain the logs for Ignition Off",
                "Device logs doesnot contain the logs for Ignition Off or failed to read the device log, pls refer device logs for detailed info"
            )

        print("----------------------------------------------------------")

        # -------------------------------------------------------------------------
        # Cloud side validations - Ignition State
        # -------------------------------------------------------------------------
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_ignition_event_type, systemId, "valid")
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] in [
                    telemetry_Curr_ignition_state,
                    telemetry_attribute_ignition_ev,
                    telemetry_attribute_ignition_ev2
                ]:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Ignition State value configured in the stub : ", telemetry_ignition_value)
        print("Ignition State value stored in Cloud DB : ", value)

        if int(value) == int(telemetry_ignition_value):
            testResult(
                self,
                "passed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )
        else:
            testResult(
                self,
                "failed",
                "Ignition State value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                "Ignition State value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer cloud logs for detailed info"
            )

        print("-------------------------------------------------------------------------")

        # -------------------------------------------------------------------------
        # Cloud side validations - Last Parked Location
        # -------------------------------------------------------------------------
        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        telemetry_lastParkedLocation(self, cloudEnv, systemId)

        print("-------------------------------------------------------------------------")







