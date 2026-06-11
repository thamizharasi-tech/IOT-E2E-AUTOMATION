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

    def test1_positive_telemetry_history_single_event(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - telemetry history packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for HISTORY Packet
        """
        print("\n------------------TELEMETRY UPDATE - TELEMETRY HISTORY PACKET------------------\n")

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        print("\n------------------TURNING OFF WIFI------------------\n")
        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)
        time.sleep(30)

        print("\n------------------TURNING ON WIFI------------------\n")
        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)
        time.sleep(30)

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        eventType = "3101"
        offset = "0"
        limit = "10"

        # Call telemetry update reusable module
        telemetry_history(self, systemId, eventType, start_time, end_time, offset, limit, "valid")

        print("\n------------------------------END------------------------------\n")

    def test2_positive_telemetry_history_multiple_event(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip history packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for HISTORY Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP HISTORY PACKET------------------\n")

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        print("\n------------------TURNING OFF WIFI------------------\n")
        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)
        time.sleep(30)

        print("\n------------------TURNING ON WIFI------------------\n")
        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)
        time.sleep(30)

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000
        eventType = "3101,1008"
        offset = "0"
        limit = "10"

        # Call telemetry update reusable module
        telemetry_history(self, systemId, eventType, start_time, end_time, offset, limit, "valid")

        print("\n------------------------------END------------------------------\n")


