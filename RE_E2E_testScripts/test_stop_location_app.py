import pytest
import time
from datetime import datetime, timezone, timedelta

from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
deviceSerialNo = b2c_ivi_adbSerialNo

class Test_TelemetryPersistHistory:


    def test2_positive_stop_location_service_on_the_device(self):
        print("\n------------------------------START------------------------------\n")


        print("\n------------------STOP DEFAULT LOCATION APP------------------\n")

        # Command to stop location_service
        stop_location_app = "shell am force-stop com.qti.c2cplatformservice"

        run_command_on_primary_IVI_device(self, deviceSerialNo, stop_location_app)