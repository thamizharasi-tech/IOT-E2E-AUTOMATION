import json
import time
from datetime import timezone, datetime
import random
import re
import requests
import zstandard as zstd
import os
import hashlib


from C2CModules.e2e_testData import *

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId
from C2CModules.notifications import notification_verify_alert_details_v2
from C2CModules.deviceRegistration_modules import *
from datetime import datetime, timedelta
from C2CModules.ddl import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

logger = logging.getLogger(__name__)
adb_path = r'C:\ADB\adb.exe'
logcat_pid = None

class Test_ddl_v3:

    def test1_positive_deep_logging_download_file_user_role_masked_v3(self):
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

        #print("Setup network connectivity if network is unreachable on device : ")
        #set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run tub on device for CRASH ALERT
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run CRASH ALERT  stub on device : ")

       # run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "crash_alert_ddl")
        #time.sleep(15)

        print("CRASH ALERT stub run process is completed, verify logs for alert details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        #print("Pull/Fetch device logs for validation : ")

        #pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        #print("Logs are fetched from device to host machine @ desired location ")
        #print("----------------------------------------------------------")

        # Verify notification msgs & type code in fetched device logs
        #ls = verify_message_in_log(self, crash_alert_notification_deviceLog_string,
         #                          crash_alert_notification_deviceLog_string)
        #print(ls)

        cloudEnv = read_cloud_env(self)

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        #systemId = '_Zuty6zrAVcMAk5ICtoZ9'

        print("System Id : ", systemId)
        print("----------------------------------------------------------------------------")

        # Call verification module to validate alert details
        # notification_verify_alert_details_v2(self, systemId, crash_categoryName_v2, crash_notification_name_v2,
        #                                 notification_type, dt, dt1)

        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)
        #time.sleep(60)

        successful_filenames = get_and_download_ddl_file_v2(self, systemId,"TELEMETRY_FILE", "TELEMETRY_FILE")
        #decompress_downloaded_files_from_folder_v2(self, "ROLE_MASKED", successful_filenames)
        #decompress_downloaded_files_from_folder_v2(self, "ROLE_MASKED", successful_filenames, onboardingType, chipsetType)
        validate_telemetry_data_from_decompressed_file_v3(self, cloudEnv, "TELEMETRY_FILE", "ROLE_MASKED")

