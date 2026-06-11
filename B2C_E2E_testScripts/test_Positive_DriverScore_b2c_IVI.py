import time

import pytest

from C2CModules.e2e_testData import *
from C2CModules.fms_modules import get_tridId_from_log, calculate_trip_distance, read_tripId_from_Trip_waypoints
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    get_SystemId, getVIN
from C2CModules.testResults import testResult
from C2CModules.vehicleDriverScore import Trip_DriverScoreCard_impactScoreBySystemId, \
    Trip_DriverScoreCard_impactScoreBySystemIdTripId, Trip_DriverScoreCard_impactScore_HAHBHC, calculate_impactScore

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

HA_parameter = 'HA'
HA_operation = 'multiplication'
HA_value = 0.5
HB_parameter = 'HB'
HB_operation = 'multiplication'
HB_value = -2.5
HC_parameter = 'HC'
HC_operation = 'multiplication'
HC_value = 0.5


class Test1_driverScore:

    @pytest.mark.regression
    # Validate Driver Scorecard functionality.
    def test1_trip_DriverScoreCard_impactScore(self):

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run charging notification stub on device
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run trip , accelerometer & gyro stubs on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "trip_summary_stub")

        # run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "trip_summary_log")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        try:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)
        except:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_accelerometer_data")
        # time.sleep(1)
        # run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_gyro_data")
        # time.sleep(180)

        print("Trip, Accelerometer & Gyro stub run process is completed, verify logs for score card details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Get systemId and hit request for driver & vehicle score
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)
        time.sleep(180)

        # response_body = Trip_DriverScoreCard_impactScore(self, parameter1, operation, value1)

        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore_HAHBHC(self, HA_parameter, HA_operation, HA_value,
                                                                HB_parameter, HB_operation, HB_value, HC_parameter,
                                                                HC_operation, HC_value)
        response_body = response_body.json()

        assert response_body["status"] == "ACTIVE"
        print("Expression : ", response_body["expression"])

        print("--------------------------------------")

        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        print("--------------------------------------")
        print("Trip Score Card : ")
        print("--------------------------------------")

        response_body = response_body.json()

        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

        if systemId == response_body["responseData"]["data"]["systemId"]:
            exp_systemId = response_body["responseData"]["data"]["systemId"]
            exp_vin = response_body["responseData"]["data"]["vin"]
            engineType = response_body["responseData"]["data"]["engineType"]
            tripScoreCrad_TripDistance = response_body["responseData"]["data"]["tripScoreCard"]["tripDistance"]
            tripScoreCrad_TripDuration = response_body["responseData"]["data"]["tripScoreCard"]["tripDuration"]
            tripScoreCrad_HA = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-acceleration"]
            tripScoreCrad_HB = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-breaking"]
            tripScoreCrad_HC = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-cornering"]
            tripScoreCrad_ImpactScore = response_body["responseData"]["data"]["tripScoreCard"]["impactScore"]

            print("System Id : ", exp_systemId)
            print("VIN : ", exp_vin)
            print("Engine Type : ", engineType)

            print("Trip Distance : ", tripScoreCrad_TripDistance)
            print("Trip Duration : ", tripScoreCrad_TripDuration)
            print("Harsh Acceleration (HA) : ", tripScoreCrad_HA)
            print("Harsh Breaking (HB) : ", tripScoreCrad_HB)
            print("Harsh Cornering (HC) : ", tripScoreCrad_HC)
            print("Impact Score: ", tripScoreCrad_ImpactScore)

        if systemId == exp_systemId.replace('\n', ''):
            testResult(self, "verificationPassed", "Newly generated trip should be mapped to device systemId in cloud DB",
                       "Newly generated trip is mapped to device systemId in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip should be mapped to device systemId in cloud DB",
                       "Newly generated trip is not mapped to device systemId in cloud DB. Refer device logs & cloud api response for additional details")

        if vin == exp_vin.replace('\n', ''):
            testResult(self, "verificationPassed", "Newly generated trip should be mapped to device vin in cloud DB",
                       "Newly generated trip is mapped to device vin in cloud DB")
        else:
            testResult(self, "verificationFailed",
                       "Newly generated trip should be mapped to device vin in cloud DB",
                       "Newly generated trip is not mapped to device vin in cloud DB. Refer device logs & cloud api response for additional details")


        # Calculate trip distance for validation :
        trip_distance = calculate_trip_distance(self, trip_start_odometer_value, trip_end_odometer_value) * 1000

        # validate trip_summary_tripDistance_value_ev
        print(f"Trip Score Card - Trip Distance calculated based on stub values : -> ' {trip_distance} ' ")
        print(f"Trip Score Card - Trip Distance value stored in cloud : -> ' {tripScoreCrad_TripDistance} ' ")

        if float(tripScoreCrad_TripDistance) == trip_distance:
            testResult(self, "verificationPassed",
                       "Trip Score Card - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Score Card - Trip Distance is calculated based on trip start & trip end odo meter values, "
                       "pls refer stub & device/cloud for detailed info")
            if float(tripScoreCrad_TripDuration) > 0:
                testResult(self, "verificationPassed",
                           "Trip Score Card - Trip Duration should be calculated based on trip start & trip end "
                           "timestamp",
                           "Trip Score Card - Trip Duration is calculated based on trip start & trip end timestamp "
                           ", pls refer stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Score Card - Trip Duration should be calculated based on trip start & trip end",
                           "Trip Score Card - Trip Duration is '0' or incorrect. pls refer stub & "
                           "device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Trip Distance should be calculated based on trip start & trip end",
                       "Trip Score Card - Trip Distance is '0' or incorrect. pls refer stub & device/cloud "
                       "for detailed info")

        if float(tripScoreCrad_HA) > 0:
            testResult(self, "verificationPassed",
                       "Trip Score Card - Violation Details - Harsh-Acceleration (HA) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-Acceleration (HA) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Violation Details - Harsh-Acceleration (HA) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-Acceleration (HA) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        if float(tripScoreCrad_HB) > 0:
            testResult(self, "verificationPassed",
                       "Trip Score Card - Violation Details - Harsh-Breaking (HB) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-Breaking (HB) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Violation Details - Harsh-Breaking (HB) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-Breaking (HB) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        if float(tripScoreCrad_HC) > 0:
            testResult(self, "verificationPassed",
                       "Trip Score Card - Violation Details - Harsh-Cornering (HC) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-Cornering (HC) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Violation Details - Harsh-Cornering (HC) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Trip Score Card - Violation Details - Harsh-cornering (HC) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        print(tripScoreCrad_ImpactScore,tripScoreCrad_HA,tripScoreCrad_HB,tripScoreCrad_HC)
        if tripScoreCrad_ImpactScore > 0 or tripScoreCrad_ImpactScore < 0 :
            score = calculate_impactScore(self, int(tripScoreCrad_HA), HA_operation, HA_value,
                                          int(tripScoreCrad_HB), HB_operation, HB_value, int(tripScoreCrad_HC),
                                          HC_operation, HC_value)
            print("Actual Impact Score : ", score)
            if tripScoreCrad_ImpactScore == score:
                testResult(self, "verificationPassed",
                           "Trip Score Card - Impact Score should be calculated based on "
                           "expression & violation values ",
                           "Trip Score Card - Impact Score is calculated based on "
                           "expression & violation values, "
                           "pls refer stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Trip Score Card - Impact Score should be calculated based on "
                           "expression & violation values ",
                           "Trip Score Card - Impact Score is '0' or incorrect"
                           "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Impact Score should be calculated based on "
                       "expression & violation values",
                       "Trip Score Card - Impact Score is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        print("--------------------------------------")

        print("Verify Vehicle Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemId(self, systemId)

        print("--------------------------------------")
        print("Vehicle Score Card : ")
        print("--------------------------------------")

        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

        if systemId == response_body["responseData"]["data"]["systemId"]:
            systemId = response_body["responseData"]["data"]["systemId"]
            vin = response_body["responseData"]["data"]["vin"]
            vehicleScoreCard_fuelType = response_body["responseData"]["data"]["fuelType"]
            vehicleScoreCard_TripDistance = response_body["responseData"]["data"]["vehicleScoreCard"]["tripDistance"]
            vehicleScoreCard_TripDuration = response_body["responseData"]["data"]["vehicleScoreCard"]["tripDuration"]
            vehicleScoreCard_NoOfTrips = response_body["responseData"]["data"]["vehicleScoreCard"]["numberOfTrips"]
            vehicleScoreCard_CumulativeViolationCounts = response_body["responseData"]["data"]["vehicleScoreCard"]["cummulativeViolationCount"]
            vehicleScoreCard_HA = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"]["harsh-acceleration"]
            vehicleScoreCard_HB = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"]["harsh-breaking"]
            vehicleScoreCard_HC = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"]["harsh-cornering"]
            vehicleScoreCard_VehicleScore = response_body["responseData"]["data"]["vehicleScoreCard"]["vehicleScore"]

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

        if float(vehicleScoreCard_TripDistance) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Cumulative Trip Distance should be calculated based on all the trips",
                       "Vehicle Score Card - Cumulative Trip Distance is calculated based on all trips"
                       "pls refer stub & device/cloud for detailed info")
            if float(vehicleScoreCard_TripDuration) > 0:
                testResult(self, "verificationPassed",
                           "Vehicle Score Card - Cumulative Trip Duration should be calculated based on all the trips ",
                           "Vehicle Score Card - Cumulative Trip Duration is calculated based on all trips"
                           ", pls refer stub & device/cloud for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Vehicle Score Card - Cumulative Trip Duration should be calculated based on all the trips",
                           "Vehicle Score Card - Cumulative Trip Duration is '0' or incorrect. pls refer stub & "
                           "device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Cumulative Trip Distance should be calculated based on all the trips",
                       "Vehicle Score Card - Cumulative Trip Distance is '0' or incorrect. pls refer stub & device/cloud "
                       "for detailed info")

        if float(vehicleScoreCard_NoOfTrips) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - No of Trips or Cumulative Trips should be displayed ",
                       "Vehicle Score Card - No of Trips or Cumulative Trips is displayed"
                       ", pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "No of Trips or Cumulative Trips should be displayed",
                       "No of Trips or Cumulative Trips is '0' or incorrect . pls refer stub & "
                       "device/cloud for detailed info")

        if float(vehicleScoreCard_CumulativeViolationCounts) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Cumulative Violation Counts (HA+HB_HC) should be displayed ",
                       "Vehicle Score Card - Cumulative Violation Counts is displayed"
                       ", pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Cumulative Violation Counts (HA+HB_HC) should be displayed",
                       "Cumulative Violation Counts is '0' or incorrect . pls refer stub & "
                       "device/cloud for detailed info")

        if float(vehicleScoreCard_HA) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Acceleration (HA) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Acceleration (HA) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Acceleration (HA) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - cumulative Harsh-Acceleration (HA) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        if float(vehicleScoreCard_HB) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Breaking (HB) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Breaking (HB) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Breaking (HB) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Breaking (HB) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        if float(vehicleScoreCard_HC) > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Cornering (HC) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Cornering (HC) is calculated based on "
                       "threshold value & algorithm defined @ device side, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-Cornering (HC) should be calculated based on "
                       "threshold value & algorithm defined @ device side",
                       "Vehicle Score Card - Violation Details - Cumulative Harsh-cornering (HC) is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        if vehicleScoreCard_VehicleScore > 0:
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Vehicle Score should be calculated based on "
                       "expression & violation values ",
                       "Vehicle Score Card - Vehicle Score is calculated based on "
                       "expression & violation values, "
                       "pls refer stub & device/cloud for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Vehicle Score should be calculated based on "
                       "expression & violation values",
                       "Vehicle Score Card - Vehicle Score is '0' or incorrect "
                       ", pls refer stub & device/cloud for detailed info")

        print("--------------------------------------")

    def test_try(self):
        trip_Id = read_tripId_from_Trip_waypoints(self, OnboardingType, chipsetType, 'Trip_waypoints')



