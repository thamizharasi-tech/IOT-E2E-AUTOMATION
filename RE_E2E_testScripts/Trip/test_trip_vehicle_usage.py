import os,sys,datetime,time,subprocess,inspect,logging
from doctest import TestResults
from pathlib import Path

import pytest

from C2CModules.api_modules import verify_api_response_for_invalid_header
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile

sys.path.insert(1, 'C:\Car2Cloud_E2ETesting')
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
p = Path(parent_dir)
parent_dir = os.path.dirname(p)
sys.path.insert(0, parent_dir)

from C2CModules.e2e_testData import *
from C2CModules.fms_modules import get_tridId_from_log, read_tripId_from_Trip_waypoints, latest_trip_meta, \
    latest_trip_details, calculate_trip_distance, calculate_trip_duration, \
    calculate_average_speed, calculate_battery_consumed, calculate_trip_battery_efficiency, \
    read_latest_trip_details_attribute_value, trip_vehicleUsageDetails
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Trip_vehicleUsage:

    # trip_tripevent
    @pytest.mark.Smoke
    def test1_negative_vehicleUsage_no_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "no_apiKey")
        verify_api_response_for_invalid_header(response, "no_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "VehicleUsage details On Vehicle API should throw appropriate error message for no apikey",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_vehicleUsage_no_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])


        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)
        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "no_x-requestor")
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "VehicleUsage details On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_vehicleUsage_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])


        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "invalid_apiKey")
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_vehicleUsage_null_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "null_apiKey")
        verify_api_response_for_invalid_header(response, "null_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "VehicleUsage Details On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_negative_vehicleUsage_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "empty_apiKey")
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6_negative_vehicleUsage_null_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "Vehicle_get_vehicleUsageDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_vehicleUsageDetails(self, systemId, startDate, endDate, "null_x-requestor")
        verify_api_response_for_invalid_header(response, "null_x-requestor")
        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "VehicleUsage Details On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")