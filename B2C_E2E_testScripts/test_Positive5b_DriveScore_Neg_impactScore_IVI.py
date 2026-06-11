import pytest

from C2CModules.fms_modules import get_tridId_from_log, calculate_trip_distance, read_tripId_from_Trip_waypoints
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.vehicleDriverScore import Trip_DriverScoreCard_impactScore_HAHBHC, \
    Trip_DriverScoreCard_impactScoreBySystemIdTripId, calculate_impactScore, Trip_DriverScoreCard_impactScoreBySystemId

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

HA_parameter = 'HA'
HA_operation = 'multiplication'
HA_value = 0.5
HB_parameter = 'HB'
HB_operation = 'multiplication'
HB_value = -4.5
HC_parameter = 'HC'
HC_operation = 'multiplication'
HC_value = -0.5
value = ""


class Test1_FMS_trip:

    @pytest.mark.regression
    # Validate telemetry functionality.
    def test1_driverScore_negative_impactScore(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Set the expression for Driver Score calculation
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore_HAHBHC(self, HA_parameter, HA_operation, HA_value,
                                                                HB_parameter, HB_operation, HB_value, HC_parameter,
                                                                HC_operation, HC_value)
        assert response_body["status"] == "ACTIVE"
        print("Expression : ", response_body["expression"])
        time.sleep(5)

        print("----------------------------------------------------------")
        # ===========================================================================================
        # Run trip , accelerometer & gyro stubs on device :
        # ===========================================================================================
        print("Run trip , accelerometer & gyro stubs on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "trip_summary_stub")

        print("Trip, Accelerometer & Gyro stub run process is completed, verify logs for score card details : ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # ===========================================================================================
        # Pull logs for Trip Id
        # ===========================================================================================
        print("Pull/Fetch device logs for Trip Id : ")

        i = 0
        while i <= 2:
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
            tripId = get_tridId_from_log(self)
            if tripId != '':
                break
            else:
                time.sleep(10)
                i = i + 1

        time.sleep(30)

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "trip_summary_log")

        if tripId == '':
            print("Trip Id not found in c2c logs, thus fetching 'Trip_Waypoints' folder to host machine for trip file")
            tripId = read_tripId_from_Trip_waypoints(self, OnboardingType, chipsetType, 'Trip_waypoints')

        # Verify Trip Id
        if tripId != '':
            testResult(self, "verificationPassed",
                       "Trip Id should be generated on device and in 'systemId_timestamp' format ",
                       "Trip Id is generated in 'systemId_timestamp' format")
        else:
            testResult(self, "failed", "Trip Id should be generated on device and in 'systemId_timestamp' format ",
                       "Trip Id is not generated or not in 'systemId_timestamp' format")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # Get systemId & VIN and hit request for driver & vehicle score
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        vin = getVIN(self, OnboardingType, chipsetType)
        time.sleep(180)
        value = ""

        # response_body = Trip_DriverScoreCard_impactScore(self, parameter1, operation, value1)

        print("--------------------------------------")

        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        print("--------------------------------------")
        print("Trip Score Card : ")
        print("--------------------------------------")

        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

        if systemId == response_body["responseData"]["data"]["systemId"]:
            actual_systemId = response_body["responseData"]["data"]["systemId"]
            actual_vin = response_body["responseData"]["data"]["vin"]
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

            print("System Id : ", actual_systemId)
            print("VIN : ", actual_vin)
            print("Engine Type : ", engineType)

            print("Trip Distance : ", tripScoreCrad_TripDistance)
            print("Trip Duration : ", tripScoreCrad_TripDuration)
            print("Harsh Acceleration (HA) : ", tripScoreCrad_HA)
            print("Harsh Breaking (HB) : ", tripScoreCrad_HB)
            print("Harsh Cornering (HC) : ", tripScoreCrad_HC)
            print("Impact Score: ", tripScoreCrad_ImpactScore)

        if systemId == actual_systemId.replace('\n', ''):
            testResult(self, "verificationPassed",
                       "Trip Score Card - Newly generated trip should be mapped to device systemId for Trip Score",
                       "Trip Score Card - Newly generated trip is mapped to device systemId for Trip Score")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Newly generated trip should be mapped to device systemId for Trip Score",
                       "Trip Score Card - Newly generated trip is not mapped to device systemId for Trip Score. Refer device logs & cloud api response for additional details")

        if vin == actual_vin.replace('\n', ''):
            testResult(self, "verificationPassed",
                       "Trip Score Card - Newly generated trip should be mapped to device vin for Trip Score",
                       "Trip Score Card - Newly generated trip is mapped to device vin for Trip Score")
        else:
            testResult(self, "verificationFailed",
                       "Trip Score Card - Newly generated trip should be mapped to device vin for Trip Score",
                       "Trip Score Card - Newly generated trip is not mapped to device vin for Trip Score. Refer device logs & cloud api response for additional details")

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
            value = "FAIL"

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
            value = "FAIL"

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
            value = "FAIL"

        # print(tripScoreCrad_ImpactScore,tripScoreCrad_HA,tripScoreCrad_HB,tripScoreCrad_HC)
        if tripScoreCrad_ImpactScore > 0 or tripScoreCrad_ImpactScore < 0:
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
                value = "FAIL"
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
            actual_systemId = response_body["responseData"]["data"]["systemId"]
            actual_vin = response_body["responseData"]["data"]["vin"]
            vehicleScoreCard_fuelType = response_body["responseData"]["data"]["fuelType"]
            vehicleScoreCard_TripDistance = response_body["responseData"]["data"]["vehicleScoreCard"]["tripDistance"]
            vehicleScoreCard_TripDuration = response_body["responseData"]["data"]["vehicleScoreCard"]["tripDuration"]
            vehicleScoreCard_NoOfTrips = response_body["responseData"]["data"]["vehicleScoreCard"]["numberOfTrips"]
            vehicleScoreCard_CumulativeViolationCounts = response_body["responseData"]["data"]["vehicleScoreCard"][
                "cummulativeViolationCount"]
            vehicleScoreCard_HA = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-acceleration"]
            vehicleScoreCard_HB = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-breaking"]
            vehicleScoreCard_HC = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-cornering"]
            vehicleScoreCard_VehicleScore = response_body["responseData"]["data"]["vehicleScoreCard"]["vehicleScore"]

            print("System Id : ", actual_systemId)
            print("VIN : ", actual_vin)
            print("Fuel Type : ", vehicleScoreCard_fuelType)

            print("Trip Distance : ", vehicleScoreCard_TripDistance)
            print("Trip Duration : ", vehicleScoreCard_TripDuration)
            print("No of Trips : ", vehicleScoreCard_NoOfTrips)
            print("Cumulative Violation Count : ", vehicleScoreCard_CumulativeViolationCounts)
            print("Harsh Acceleration (HA) : ", vehicleScoreCard_HA)
            print("Harsh Breaking (HB) : ", vehicleScoreCard_HB)
            print("Harsh Cornering (HC) : ", vehicleScoreCard_HC)
            print("Impact Score: ", vehicleScoreCard_VehicleScore)

        if systemId == actual_systemId.replace('\n', ''):
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Newly generated trip should be mapped to device systemId for vehicle score",
                       "Vehicle Score Card - Newly generated trip is mapped to device systemId for vehicle score")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Newly generated trip should be mapped to device systemId for vehicle score",
                       "Vehicle Score Card - Newly generated trip is not mapped to device systemId for vehicle score. Refer device logs & cloud api response for additional details")

        if vin == actual_vin.replace('\n', ''):
            testResult(self, "verificationPassed",
                       "Vehicle Score Card - Newly generated trip should be mapped to device vin for vehicle score",
                       "Vehicle Score Card - Newly generated trip is mapped to device vin for vehicle score")
        else:
            testResult(self, "verificationFailed",
                       "Vehicle Score Card - Newly generated trip should be mapped to device vin for vehicle score ",
                       "Vehicle Score Card - Newly generated trip is not mapped to device vin for vehicle score. Refer device logs & cloud api response for additional details")

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
            value = "FAIL"

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
            value = "FAIL"

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
            value = "FAIL"

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

        if value == "FAIL":
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            assert True
            # self.result.set_result(TestResults.passed)

        print("-------------------------------------------------------------------------")


