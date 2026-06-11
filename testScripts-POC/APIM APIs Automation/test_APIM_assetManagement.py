import json

import pytest
import time
import datetime

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.APIM_ReusableModules import assetManagement_trip_info_by_tripId, \
    assetManagement_trip_waypoints_by_tripid, assetManagement_trip_waypoints_by_systemId,get_tridId_from_log,Trip_DriverScoreCard_impactScoreBySystemId
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_smoke:

    # AssetManagement_trip-info-by-tripId
    @pytest.mark.Smoke
    def test1_positive_AssetManagement_trip_info_by_tripId(self):

        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            trip_id = str(dict1["tripId"])

            print("Trip Id :", trip_id)

            # Call asset management reusable module
            response = assetManagement_trip_info_by_tripId(self, trip_id)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)

            print("Trip Id :", tripId)

            time.sleep(120)

            i = 0
            while i in range(10):
                response_body = assetManagement_trip_info_by_tripId(self, tripId)
                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")

    # AssetManagement_trip-waypoints-by-tripid
    @pytest.mark.Smoke
    def test2_positive_AssetManagement_trip_waypoints_by_tripid(self):

        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-tripid")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            trip_id = str(dict1["tripId"])

            print("Trip Id :", trip_id)

            # Call asset management reusable module
            response = assetManagement_trip_waypoints_by_tripid(self, trip_id)
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)

            print("Trip Id :", tripId)

            time.sleep(120)

            i = 0
            while i in range(10):
                response_body = assetManagement_trip_waypoints_by_tripid(self, tripId)
                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")

    # assetManagement_trip_waypoints_by_systemId
    @pytest.mark.Smoke
    def test3_positive_assetManagement_trip_waypoints_by_systemId(self):


        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)
            print("System Id : ", systemId)

            # Call asset management reusable module
            response = assetManagement_trip_waypoints_by_systemId(self, startDate, endDate, systemId)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("Start Date : ", startDate)
            print("End Date : ", endDate)
            print("System Id : ", systemId)

            # Call asset management reusable module
            response = assetManagement_trip_waypoints_by_systemId(self, startDate, endDate, systemId)

        print("----------------------------------------------------------")

    #driver score
    @pytest.mark.Smoke
    def test4_positive_trip_driverScoreCard_driverScore(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_driverScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Verify Vehicle Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemId(self, systemId)

        print("--------------------------------------")
        print("Vehicle Score Card : ")
        print("--------------------------------------")
        if systemId == response_body["responseData"]["systemId"]:
            systemId = response_body["responseData"]["systemId"]
            vin = response_body["responseData"]["vin"]
            vehicleScoreCard_fuelType = response_body["responseData"]["fuelType"]
            vehicleScoreCard_TripDistance = response_body["responseData"]["vehicleScoreCard"]["tripDistance"]
            vehicleScoreCard_TripDuration = response_body["responseData"]["vehicleScoreCard"]["tripDuration"]
            vehicleScoreCard_NoOfTrips = response_body["responseData"]["vehicleScoreCard"]["numberOfTrips"]
            vehicleScoreCard_CumulativeViolationCounts = response_body["responseData"]["vehicleScoreCard"][
                "cummulativeViolationCount"]
            vehicleScoreCard_HA = response_body["responseData"]["vehicleScoreCard"]["violationDetails"][
                "harsh-acceleration"]
            vehicleScoreCard_HB = response_body["responseData"]["vehicleScoreCard"]["violationDetails"][
                "harsh-breaking"]
            vehicleScoreCard_HC = response_body["responseData"]["vehicleScoreCard"]["violationDetails"][
                "harsh-cornering"]
            vehicleScoreCard_VehicleScore = response_body["responseData"]["vehicleScoreCard"]["vehicleScore"]

            print("System Id : ", systemId)
            print("VIN : ", vin)
            print("Fuel Type : ", vehicleScoreCard_fuelType)

            print("Trip Distance : ", vehicleScoreCard_TripDistance)
            print("Trip Duration : ", vehicleScoreCard_TripDuration)
            print("No of Trips : ", vehicleScoreCard_NoOfTrips)
            print("Cumulative Violation Count : ", vehicleScoreCard_CumulativeViolationCounts)
            print("Harsh Acceleration (HA) : ", vehicleScoreCard_HA)
            print("Harsh Breaking (HB) : ", vehicleScoreCard_HB)
            print("Harsh Cornering (HC) : ", vehicleScoreCard_HC)
            print("Impact Score: ", vehicleScoreCard_VehicleScore)
            testResult(self, "passed", "Should fetch the data/values successfully",
                       "Successfully fetched the values/data")
        elif systemId == response_body["responseData"]["systemId"]:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            testResult(self, "failed", "Should fetch the data/values successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

    print("----------------------------------------------------------")