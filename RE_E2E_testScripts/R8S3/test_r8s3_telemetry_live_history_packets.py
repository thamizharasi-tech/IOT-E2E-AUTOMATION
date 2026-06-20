import pytest
import time
from datetime import datetime, timezone, timedelta

from C2CModules.telemetry_persistance import telemetry_persist_history, telemetry_persist_history_v2
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *
from C2CModules.fms_modules import get_tridId_from_log, read_tripId_from_Trip_waypoints
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import vehicle_update_metadata

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
deviceSerialNo = b2c_ivi_adbSerialNo

class Test_R8S3_TelemetryPersistHistory:

    def test1_positive_telemetryPersistHistory_trip_inactive_live_packet(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inactive live packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for LIVE Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - LIVE PACKET------------------\n")

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        #systemId = "7238"
        # start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        #start_time = 1742533682881

        #end_time = 1742534102880

        tc = "trip_inactive_live_packet"
        # Call telemetry update reusable module
        telemetry_persist_history(self, systemId, telemetry_lat_event_type, start_time, end_time, tc)
        # telemetryUpdate(env, systemId, telemetry_speed_event_type, telemetry_attribute_speed1)

        print("\n------------------------------END------------------------------\n")

    def test2_positive_telemetryPersistHistory_trip_inactive_history_packet(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inactive history packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for HISTORY Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - HISTORY PACKET------------------\n")

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        # Run the command
        #result = os.system(disable_network)

        # Check the result
        #if result == 0:
            #print("Wi-Fi disabled successfully!")
        #else:
         #   print("Failed to disable Wi-Fi. Please check your device or setup.")

        time.sleep(30)

        # Run the command
        #result = os.system(enable_network)

        # Check the result
        #if result == 0:
         #   print("Wi-Fi enabled successfully!")
        #else:
         #   print("Failed to enable Wi-Fi. Please check your device or setup.")
        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(30)
        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        #systemId = "7238"
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 -100000
        #start_time = 1742664600000

        #end_time = 1742666400000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000

        tc = "trip_inactive_history_packet"

        # Call telemetry update reusable module
        telemetry_persist_history(self, systemId, telemetry_lat_event_type, start_time, end_time, tc)

        print("\n------------------------------END------------------------------\n")

    def test3_positive_telemetryPersistHistory_trip_active_live_packet(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inactive live packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for LIVE Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - LIVE PACKET------------------\n")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Run trip stub on device : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stub')
        #time.sleep(30)

        print("Trip stub start/run process is completed, verify logs for trip & telemetry details : ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Pull/Fetch device logs for trip Id & validate : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify trip messages in log file
        # ===========================================================================================

        # Get trip Id

        # ===========================================================================================
        # Pull logs for Trip Id
        # ===========================================================================================
        # print("Pull/Fetch device logs for Trip Id & validate : ")

        i = 0
        while i <= 2:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)
            if tripId != '':
                break
            else:
                ("Trip Id not found in c2c logs, thus fetching 'Trip_Waypoints' folder to host machine for trip file")
                tripId = read_tripId_from_Trip_waypoints(self, OnboardingType, chipsetType, 'Trip_waypoints')
                if tripId != '':
                    break
                else:
                    time.sleep(10)
            i = i + 1

        if tripId == "":
            testResult(self, "failed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start = "event_type": 4005

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validate Trip Start Event/Reason code : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        ls = verify_message_in_log(self, trip_start_reason_code, trip_start_reason_code)

        if trip_start_reason_code in str(ls[0]):
            print(f"Trip is started with ' {trip_start_reason_code} ' ")
            testResult(self, "passed", "Trip should start on device ",
                       "Trip is started and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        #systemId = "7222"
        #start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        #start_time = 1742533682881

        #end_time = 1742534102880

        tc = "trip_active_live_packet"
        # Call telemetry update reusable module
        telemetry_persist_history(self, systemId, telemetry_lat_event_type, start_time, end_time, tc)
        # telemetryUpdate(env, systemId, telemetry_speed_event_type, telemetry_attribute_speed1)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Run trip stop stub on device : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stop')
        #time.sleep(15)

        print("Trip stop process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validate Trip Stop Event/Reason code : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])
        if str(ls[0]) == "Error":
            print(
                "Either trip is not stopped or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        #  time.sleep(60)
        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")

    def test4_positive_telemetryPersistHistory_trip_active_history_packet(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inative history packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for HISTORY Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - HISTORY PACKET------------------\n")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Run trip stub on device : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stub')
        #time.sleep(15)

        print("Trip stub start/run process is completed, verify logs for trip & telemetry details : ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Pull/Fetch device logs for trip Id & validate : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify trip messages in log file
        # ===========================================================================================

        # Get trip Id

        # ===========================================================================================
        # Pull logs for Trip Id
        # ===========================================================================================
        # print("Pull/Fetch device logs for Trip Id & validate : ")

        i = 0
        while i <= 2:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)
            if tripId != '':
                break
            else:
                ("Trip Id not found in c2c logs, thus fetching 'Trip_Waypoints' folder to host machine for trip file")
                tripId = read_tripId_from_Trip_waypoints(self, OnboardingType, chipsetType, 'Trip_waypoints')
                if tripId != '':
                    break
                else:
                    time.sleep(10)
            i = i + 1

        if tripId == "":
            testResult(self, "failed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # telemetry - trip start = "event_type": 4005

        print("# # # # # # # # # # # # # # # # # # # # # # # # ")
        print("Device Side Validations : ")
        print("# # # # # # # # # # # # # # # # # # # # # # # # ")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validate Trip Start Event/Reason code : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        ls = verify_message_in_log(self, trip_start_reason_code, trip_start_reason_code)

        if trip_start_reason_code in str(ls[0]):
            print(f"Trip is started with ' {trip_start_reason_code} ' ")
            testResult(self, "passed", "Trip should start on device ",
                       "Trip is started and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Either trip is not started or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should start on device ",
                       "Either trip is not started or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(30)

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(20)

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        #systemId = "7233"
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        #start_time = 1742664600000

        #end_time = 1742666400000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000

        tc = "trip_active_history_packet"

        # Call telemetry update reusable module
        telemetry_persist_history(self, systemId, telemetry_lat_event_type, start_time, end_time, tc)

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Run trip stop stub on device : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'trip_stop')
        #time.sleep(15)

        print("Trip stop process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")

        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("Validate Trip Stop Event/Reason code : ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

        ls = verify_message_in_log(self, trip_stop_reason_code, trip_stop_reason_code)

        if trip_stop_reason_code in str(ls[0]):
            print(f"Trip is stopped with ' {trip_stop_reason_code} ' ")
            testResult(self, "passed", "Trip should stop on device ",
                       "Trip is stopped and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])
        if str(ls[0]) == "Error":
            print(
                "Either trip is not stopped or device logs are not updated or have been rotated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Trip should stop on device ",
                       "Either trip is not stopped or device logs are not updated. pls refer device logs in detail ")

        #  time.sleep(60)
        print("----------------------------------------------------------")

        print("\n------------------------------END------------------------------\n")

    def test5_positive_telemetryPersistHistory_trip_inactive_live_packet_v2(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inactive live packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for LIVE Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - LIVE PACKET------------------\n")

        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        offset = "0"
        limit = "20"
        eventType = "1001"
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        #systemId = "7238"
        # start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000
        #start_time = 1742533682881

        #end_time = 1742534102880

        tc = "trip_inactive_live_packet"
        # Call telemetry update reusable module
        telemetry_persist_history_v2(self, systemId, eventType, start_time, end_time, offset, limit, tc)

        print("\n------------------------------END------------------------------\n")

    def test6_positive_telemetryPersistHistory_trip_inactive_history_packet_v2(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the telemetry Update - trip inactive history packet functionality. (positive scenario)
        :return: return test status
        Validate telemetry update/value for HISTORY Packet
        """
        print("\n------------------TELEMETRY UPDATE - TRIP INACTIVE - HISTORY PACKET------------------\n")

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(60)

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(20)
        # Read systemId from vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        #systemId = "7238"
        eventType = "1001"
        offset = "0"
        limit = "20"
        start_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 - 100000

        end_time = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000

        tc = "trip_inactive_history_packet"

        # Call telemetry update reusable module
        telemetry_persist_history_v2(self, systemId, eventType, start_time, end_time, offset, limit, tc)

        print("\n------------------------------END------------------------------\n")
