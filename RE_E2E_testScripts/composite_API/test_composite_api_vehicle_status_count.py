import os, sys, datetime, time, subprocess, inspect, logging

import json
import time
from datetime import timezone, datetime
import random

import pytest

from C2CModules.e2e_testData import *
from C2CModules.vehicleGrouping import *
from C2CModules.testResults import testResult
from datetime import datetime, timedelta
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.composite_api import telemetry_history, telemetry_data, vehicle_alert_count, vehicle_status_count, vehicle_location, vehicle_location_by_systemId

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
deviceSerialNo = b2c_ivi_adbSerialNo


class Test_compositeAPI:

    def test6_vehicle_status_count(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Vehicle Status Count API functionality. (positive scenario)
        :return: return test status
        Validate Vehicle Status Count
        """
        print("\n------------------ VEHICLE STATUS COUNT ------------------\n")

        regionCode = "NA"
        countryCode = "USA"
        engineType = "2"
        model = "Cruiser"
        year = 2022

        # Call vehicle reusable module
        vehicle_status_count(self, regionCode, countryCode, engineType, model, year, "vehicle_status_count")

        print("\n------------------------------END------------------------------\n")


