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


class Test_R8S3_VehicleLiveLocation:

    @pytest.mark.regression
    # Validate telemetry-live location functionality.
    def test1_positive_bikeSecuritySafety_vehicleLiveLocation(self):
        print("\n================Start Test Execution================")

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
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry - live location stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "live_location2")
        time.sleep(15)

        print("Telemetry - Live Location stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        # get_SystemId(self, onboardingType, chipsetType)
        print("System Id : ", systemId)

        telemetry_liveLocation(self, systemId, telemetry_lat_event_type, "vehicleLocation")

    def test2_positive_bikeSecuritySafety_single_systemId_multiple_eventIds(self):
        print("----------------------------------------------------------")
        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry - live location stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "live_location2")
        time.sleep(5)

        print("Telemetry - Live Location stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id :", systemId)
        telemetry_lat_event_type = 3101

        # Call telemetry update reusable module [option : vehicleLocation, realTimeTracking]
        response = vehicle_live_location(self, systemId, telemetry_lat_event_type,
                                         "vehicleLocation_single_systemId_multiple_eventIds")

        # Validate status code
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        dataList_len = len(response_body["responseData"]["data"])

        for i in range(dataList_len):
            dataList_len = len(response_body["responseData"]["data"][i]["signals"])

            # print(dataList_len)
            for j in range(dataList_len):
                # print(response_body["responseData"]["dataList"][j]["name"])
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed1:
                    gps_speed_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_latitude:
                    latitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_longitude:
                    longitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_altitude:
                    altitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction1:
                    direction_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_ignition:
                    ignition_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
            print("------------------------------------------------")
            print("System Id : ", response_body["responseData"]["data"][i]["systemId"])
            print("------------------------------------------------")
            print("gps_speed_value :", gps_speed_value)
            print("latitude_value :", latitude_value)
            print("longitude_value :", longitude_value)
            print("altitude_value :", altitude_value)
            print("direction_value :", direction_value)
            print("ignition_value :", ignition_value)
            print("------------------------------------------------")

        #self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry-live location functionality.
    def test3_positive_bikeSecuritySafety_vehicleLiveLocation_multiple_systemIds(self):
        print("\n================Start Test Execution================")

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
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry - live location stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "live_location2")
        time.sleep(15)

        print("Telemetry - Live Location stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        # get_SystemId(self, onboardingType, chipsetType)
        print("System Id : ", systemId)

        # Call telemetry update reusable module [option : vehicleLocation, realTimeTracking]
        response = vehicle_live_location(self, systemId, telemetry_lat_event_type,
                                         "vehicleLocation_multiple_systemIds")

        # Validate status code
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        dataList_len = len(response_body["responseData"]["data"])

        for i in range(dataList_len):
            dataList_len = len(response_body["responseData"]["data"][i]["signals"])

            # print(dataList_len)
            for j in range(dataList_len):
                # print(response_body["responseData"]["dataList"][j]["name"])
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed1:
                    gps_speed_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_latitude:
                    latitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_longitude:
                    longitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_altitude:
                    altitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction1:
                    direction_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
            print("------------------------------------------------")
            print("System Id : ", response_body["responseData"]["data"][i]["systemId"])
            print("------------------------------------------------")
            print("gps_speed_value :", gps_speed_value)
            print("latitude_value :", latitude_value)
            print("longitude_value :", longitude_value)
            print("altitude_value :", altitude_value)
            print("direction_value :", direction_value)
            print("------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry-live location functionality.
    def test4_positive_bikeSecuritySafety_vehicleLiveLocation_multiple_systemIds_eventIds(self):
        print("\n================Start Test Execution================")

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
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry - live location stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "live_location2")
        time.sleep(15)

        print("Telemetry - Live Location stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify live location status & response for single systemId & eventId
        systemId = read_vehicleJsonFile(self, "system_id")
        # get_SystemId(self, onboardingType, chipsetType)
        print("System Id : ", systemId)

        # Call telemetry update reusable module [option : vehicleLocation, realTimeTracking]
        response = vehicle_live_location(self, systemId, telemetry_lat_event_type,
                                         "vehicleLocation_multiple_systemIds_eventIds")

        # Validate status code
        assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        dataList_len = len(response_body["responseData"]["data"])

        for i in range(dataList_len):
            dataList_len = len(response_body["responseData"]["data"][i]["signals"])

            # print(dataList_len)
            for j in range(dataList_len):
                # print(response_body["responseData"]["dataList"][j]["name"])
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_gps_speed1:
                    gps_speed_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_latitude:
                    latitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_longitude:
                    longitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_altitude:
                    altitude_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction or response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_direction1:
                    direction_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
                if response_body["responseData"]["data"][i]["signals"][j][
                    "name"] == telemetry_attribute_ignition:
                    ignition_value = response_body["responseData"]["data"][i]["signals"][j]["value"]
            print("------------------------------------------------")
            print("System Id : ", response_body["responseData"]["data"][i]["systemId"])
            print("------------------------------------------------")
            print("gps_speed_value :", gps_speed_value)
            print("latitude_value :", latitude_value)
            print("longitude_value :", longitude_value)
            print("altitude_value :", altitude_value)
            print("direction_value :", direction_value)
            print("ignition_value :", ignition_value)
            print("------------------------------------------------")

