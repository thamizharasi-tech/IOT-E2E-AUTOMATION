import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from C2CModules.vehicleDriverScore import Trip_DriverScoreCard_impactScore_HAHBHC, Trip_DriverScoreCard_impactScore, \
    Trip_DriverScoreCard_impactScoreBySystemIdTripId, Trip_DriverScoreCard_impactScoreBySystemId, \
    Trip_DriverScoreCard_impactScore_negative_validation, \
    Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation, \
    Trip_DriverScoreCard_impactScoreBySystemId_negative_validation
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_DriverScore:

    # ---------------------------------------
    # Scripts for Positive API test scenarios
    # ----------------------------------------

    # driverScore_createDriverScoreExpression
    @pytest.mark.Smoke
    def test1_positive_trip_driverScoreCard_impactScore(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
            response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            HA_parameter = 'HA'
            HA_operation = 'multiplication'
            HA_value = 0.5
            HB_parameter = 'HB'
            HB_operation = 'multiplication'
            HB_value = -2.5
            HC_parameter = 'HC'
            HC_operation = 'multiplication'
            HC_value = 0.5

            print("Set the expression to calculate trip & vehicle score")
            response_body = Trip_DriverScoreCard_impactScore_HAHBHC(self, HA_parameter, HA_operation, HA_value,
                                                                    HB_parameter, HB_operation, HB_value, HC_parameter,
                                                                    HC_operation, HC_value)
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        assert response_body["status"] == "ACTIVE"
        print("Expression : ", response_body["expression"])

        print("----------------------------------------------------------")

    # driverScore_trip_driverScoreCard_impactScoreBySystemId
    @pytest.mark.Smoke
    def test2_positive_trip_driverScoreCard_impactScoreBySystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = str(dict1["trip_id"])

        # Call api reusable module
        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        print("--------------------------------------")
        print("Trip Score Card : ")
        print("--------------------------------------")

        assert response_body["responseCode"] == "1200"
        assert response_body["responseData"]["message"] == "SUCCESS"

        if systemId == response_body["responseData"]["data"]["systemId"]:
            exp_systemId = response_body["responseData"]["data"]["systemId"]
            exp_vin = response_body["responseData"]["data"]["vin"]
            engineType = response_body["responseData"]["data"]["engineType"]
            tripScoreCard_TripDistance = response_body["responseData"]["data"]["tripScoreCard"]["tripDistance"]
            tripScoreCard_TripDuration = response_body["responseData"]["data"]["tripScoreCard"]["tripDuration"]
            tripScoreCard_HA = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-acceleration"]
            tripScoreCard_HB = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-breaking"]
            tripScoreCard_HC = response_body["responseData"]["data"]["tripScoreCard"]["violationDetails"][
                "harsh-cornering"]
            tripScoreCard_ImpactScore = response_body["responseData"]["data"]["tripScoreCard"]["impactScore"]

            print("System Id : ", exp_systemId)
            print("VIN : ", exp_vin)
            print("Engine Type : ", engineType)

            print("Trip Distance : ", tripScoreCard_TripDistance)
            print("Trip Duration : ", tripScoreCard_TripDuration)
            print("Harsh Acceleration (HA) : ", tripScoreCard_HA)
            print("Harsh Breaking (HB) : ", tripScoreCard_HB)
            print("Harsh Cornering (HC) : ", tripScoreCard_HC)
            print("Impact Score: ", tripScoreCard_ImpactScore)

        print("----------------------------------------------------------")

    # driverScore_trip_driverScoreCard_driverScore
    @pytest.mark.Smoke
    def test3_positive_trip_driverScoreCard_driverScore(self):

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

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

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
            vehicleScoreCard_CumulativeViolationCounts = response_body["responseData"]["data"]["vehicleScoreCard"][
                "cummulativeViolationCount"]
            vehicleScoreCard_HA = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-acceleration"]
            vehicleScoreCard_HB = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-breaking"]
            vehicleScoreCard_HC = response_body["responseData"]["data"]["vehicleScoreCard"]["violationDetails"][
                "harsh-cornering"]
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
        print("----------------------------------------------------------")

    # ---------------------------------------
    # Scripts for Negative API test scenarios
    # ----------------------------------------

    # driverScore_expressionWithInvalidParameter
    @pytest.mark.Sanity
    def test1_negative_trip_driverScoreCard_impactScore_invalidParameter(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScore_InvalidParameter")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'Hc'
            operation = 'multiplication'
            value = '2'

        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if parameter != 'HA' or 'HB' or 'HC' and response_body["responseCode"] == "6002":
            testResult(self, "passed", "Drive score expression should not be created",
                       "Driver score expression is not created")
        elif response_body["responseCode"] != "6002":

            testResult(self, "failed", "Drive score expression should not be created",
                       "Drive score expression is created or responseCode and responseMessage is invalid" + "Reason "
                                                                                                            "for "
                                                                                                            "failure "
                                                                                                            "is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # driverScore_expression With Empty Parameter
    @pytest.mark.Sanity
    def test2_negative_trip_driverScoreCard_impactScore_EmptyParameter(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScore_EmptyParameter")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
            if parameter == "None":
                parameter = ''
            # response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = ''
            operation = 'multiplication'
            value = '1'

        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "6002" and response_body["responseData"][
                "message"] == "Not a valid Expression,Parameter is null or empty":
            testResult(self, "passed", "Drive score expression should not be created",
                       "Driver score expression is not created")
        elif response_body["responseCode"] != "6002" and response_body["responseData"][
                "message"] != "Not a valid Expression,Parameter is null or empty":

            testResult(self, "failed", "Drive score expression should not be created",
                       "Drive score expression is created or responseCode and responseMessage is invalid" + "Reason "
                                                                                                            "fo "
                                                                                                            "failure "
                                                                                                            "is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # To create Driver score expression without field parameter
    @pytest.mark.Sanity
    def test3_negative_trip_driverScoreCard_impactScore_missing_parameter(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 0.5

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "no_parameter")
        response_body = response.json()
        assert (
                response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        assert response_body["responseCode"] == "6002"
        assert response_body["responseData"]["message"] == "Not a valid Expression,Parameter is null or empty"

        print("----------------Field Parameter Missing------------------------------------------")

    # driverScore_expression With Invalid Operator
    @pytest.mark.Sanity
    def test4_negative_trip_driverScoreCard_impactScore_invalidOperator(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScore_InvalidOperator")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HB'
            operation = 'multip'
            value = '2'

        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if operation != 'addition' or 'multiplication' or 'subtraction' or 'division' and response_body[
                "responseCode"] == "6003":
            testResult(self, "passed", "Drive score expression should not be created",
                       "Driver score expression is not created")
        elif response_body["responseCode"] != "6003":

            testResult(self, "failed", "Drive score expression should not be created",
                       "Drive score expression is created or responseCode and responseMessage is invalid" + "Reason "
                                                                                                            "for "
                                                                                                            "failure "
                                                                                                            "is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # driverScore_expression With Empty Operator
    @pytest.mark.Sanity
    def test5_negative_trip_driverScoreCard_impactScore_EmptyOperator(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScore_EmptyOperator")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
            if operation == "None":
                operation = ''
            # response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = ''
            value = '1'

        print("Set the expression to calculate trip & vehicle score")
        response_body = Trip_DriverScoreCard_impactScore(self, parameter, operation, value)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "6003" and response_body["responseData"][
                "message"] == "Not a valid Expression,Operation is null or empty":
            testResult(self, "passed", "Drive score expression should not be created",
                       "Driver score expression is not created")
        elif response_body["responseCode"] != "6003" and response_body["responseData"][
                "message"] != "Not a valid Expression,Operation is null or empty":

            testResult(self, "failed", "Drive score expression should not be created",
                       "Drive score expression is created or responseCode and responseMessage is invalid" + "Reason "
                                                                                                            "for "
                                                                                                            "failure "
                                                                                                            "is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # To create Driver score expression without field Operation
    @pytest.mark.Sanity
    def test6_negative_trip_driverScoreCard_impactScore_missing_operator(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 0.5

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "no_operation")
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert (
                response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        assert response_body["responseCode"] == "6003"
        assert response_body["responseData"]["message"] == "Not a valid Expression,Operation is null or empty"

        print("----------------Field Operation Missing------------------------------------------")

    # To create Driver score expression without field Value
    @pytest.mark.Sanity
    def test7_negative_trip_driverScoreCard_impactScore_missing_value(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 0.5

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "no_value")
        response_body = response.json()

        assert (
                response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        assert response_body["responseCode"] == "6001"
        assert response_body["responseData"]["message"] == "Not a valid Expression,Value is null or empty"

        print("----------------Field Value Missing------------------------------------------")

    # impactScore By Invalid SystemId
    @pytest.mark.Sanity
    def test8_negative_trip_driverScoreCard_impactScoreBySystemId_invalidSystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_invalidSystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f7"
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"

        # Call api reusable module
        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        print("--------------------------------------")

        if response_body["responseCode"] == "1100":
            testResult(self, "passed", "Trip impact score should not be displayed for invalid systemId",
                       "Trip impact score not available for the given systemId")
        elif response_body["responseCode"] != "1100":
            testResult(self, "failed", "Trip impact score should not be displayed for invalid systemId",
                       "Trip impact score present for the given systemId and TripId" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # impactScore with SystemId as NULL
    @pytest.mark.Sanity
    def test9_negative_trip_driverScoreCard_impactScoreBySystemId_NULLSystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_NULLSystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "NULL"
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"

        # Call api reusable module
        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "1100":
            testResult(self, "passed", "Trip impact score should not be displayed for NULL systemId",
                       "Trip impact score not available for the given systemId")
        elif response_body["responseCode"] != "1100":
            testResult(self, "failed", "Trip impact score should not be displayed for NULL systemId",
                       "Trip impact score present for the given systemId and TripId" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("-------------SystemId is NULL---------------------")

    # Impact score with empty systemID provided in api path
    @pytest.mark.Sanity
    def test10_negative_trip_driverScoreCard_impactScoreBySystemId_emptySystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_emptySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])
            if systemId == "None":
                systemId = ''

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 404), "Status code is not 404. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["status"] == 404 and response_body["error"] == 'Not Found':
            testResult(self, "passed", "Wrong api path hence Trip Impact score should not be displayed",
                       "Wrong api path")
        elif response_body["status"] != "404" and response_body["error"] != 'Not Found':
            testResult(self, "failed", "Wrong api path hence Trip Impact score should not be displayed",
                       "Trip Impact score is present for empty SystemId " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # impactScore By Invalid TripId
    @pytest.mark.Sanity
    def test11_negative_trip_driverScoreCard_impactScoreBySystemId_invalidTripId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_invalidTripId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311eeaed6"
            tripId = "sys0d2e6f718ab311eeaed6_170193"

        # Call api reusable module
        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "1100":
            testResult(self, "passed", "Trip impact score should not be displayed for invalid TripId",
                       "Trip impact score not available for the given TripId")
        elif response_body["responseCode"] != "1100":
            testResult(self, "failed", "Trip impact score should not be displayed for invalid TripId",
                       "Trip impact score present for the given SystemId and TripId" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # impactScore with TripId as NULL
    @pytest.mark.Sanity
    def test12_negative_trip_driverScoreCard_impactScoreBySystemId_NULLTripId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_NULLTripId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311eeaed6"
            tripId = "NULL"

        # Call api reusable module
        print("Verify Trip Score Card details ")

        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "1100":
            testResult(self, "passed", "Trip impact score should not be displayed for NULL TripId",
                       "Trip impact score not available for the given TripId")
        elif response_body["responseCode"] != "1100":
            testResult(self, "failed", "Trip impact score should not be displayed for NULL TripId",
                       "Trip impact score present for the given SystemId and TripId" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Impact score with empty TripID provided in api path
    @pytest.mark.Sanity
    def test13_negative_trip_driverScoreCard_impactScoreBySystemId_emptyTripId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_impactScoreBySystemId_emptyTripId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])
            if tripId == "None":
                tripId = ''

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311eeaed6"
            tripId = ""
        response_body = Trip_DriverScoreCard_impactScoreBySystemIdTripId(self, systemId, tripId)

        assert (response_body.status_code == 404), "Status code is not 404. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["status"] == 404 and response_body["error"] == 'Not Found':
            testResult(self, "passed", "Wrong api path hence Trip Impact score should not be displayed",
                       "Wrong api path")
        elif response_body["status"] != "404" and response_body["error"] != 'Not Found':
            testResult(self, "failed", "Wrong api path hence Trip Impact score should not be displayed",
                       "Trip Impact score is present for empty SystemId " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # driverScore card with invalid systemId
    @pytest.mark.Sanity
    def test14_negative_trip_driverScoreCard_driverScore_invalidSystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_driverScore_invalidSystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311ee"

        response_body = Trip_DriverScoreCard_impactScoreBySystemId(self, systemId)

        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == "1100":
            testResult(self, "passed", "Driver score should not be displayed for invalid SystemId",
                       "Driver score not available for the given SystemId")
        elif response_body["responseCode"] != "1100":
            testResult(self, "failed", "Driver score should not be displayed for invalid SystemId",
                       "Driver score is present for the given SystemId " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Driver score with empty systemID provided in api path
    @pytest.mark.Sanity
    def test15_negative_trip_driverScoreCard_driverScore_emptySystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard",
                                         "Trip_DriverScoreCard_driverScore_emptySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ''

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""

        response_body = Trip_DriverScoreCard_impactScoreBySystemId(self, systemId)

        assert (response_body.status_code == 404), "Status code is not 404. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["status"] == 404 and response_body["error"] == 'Not Found':
            testResult(self, "passed", "Wrong api path hence Driver score should not be displayed",
                       "Wrong api path")
        elif response_body["status"] != "404" and response_body["error"] != 'Not Found':
            testResult(self, "failed", "Wrong api path hence Driver score should not be displayed",
                       "Driver score is present for empty SystemId " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # ---------------------------------------
    # Scripts for Negative Header scenarios
    # ----------------------------------------

    # To create Driver score expression with invalid apikey
    @pytest.mark.Sanity
    def test16_negative_trip_driverScoreCard_impactScore_invalidapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 0.5

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "invalid_apiKey")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------------Api key mismatch------------------------------------------")

    # Get impact score with invalid apikey
    @pytest.mark.Sanity
    def test17_negative_trip_driverScoreCard_impactScoreBySystemId_invalidapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"
        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "invalid_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("-------Api Key Mismatch-------------------------------")

    # Get impact score with NULL apikey
    @pytest.mark.Sanity
    def test18_negative_trip_driverScoreCard_impactScoreBySystemId_NULLapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"
        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "null_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("---------Api Key is NULL-----------")

    # Driver score with invalid api key
    @pytest.mark.Sanity
    def test19_negative_trip_driverScoreCard_driverScore_invalidapikey(self):

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

        response = Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, "invalid_apiKey")

        # Validate response status code

        assert response["responseCode"] == "10000"
        assert response["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("----------Api-Key Mismatch----------------------------")

    # To create Driver score expression with empty apikey
    @pytest.mark.Sanity
    def test20_negative_trip_driverScoreCard_impactScore_emptyapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 1

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "empty_apiKey")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("------------------Empty api-key-------------------------")

    # Get impact score with header apikey empty
    @pytest.mark.Sanity
    def test21_negative_trip_driverScoreCard_impactScoreBySystemId_emptyapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"

        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "empty_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("--------Api-key empty------------------------------")

    # Driver score with header api key empty
    @pytest.mark.Sanity
    def test22_negative_trip_driverScoreCard_driverScore_emptyapikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_driverScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311eeaed8"

        response = Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, "empty_apiKey")

        assert response["responseCode"] == "10000"
        assert response["responseData"]["message"] == "api keys are not matching. Please provide valid key"

        print("---------Api-key empty-----------------------------")

    # To create Driver score expression without header apikey
    @pytest.mark.Sanity
    def test23_negative_trip_driverScoreCard_impactScore_missing_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 1

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "no_apiKey")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("------------------API-Key missing-------------------------")

    # Get impact score without header apikey
    @pytest.mark.Sanity
    def test24_negative_trip_driverScoreCard_impactScoreBySystemId_missing_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = "sys0d2e6f718ab311eeaed6_1701933163704"

        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "no_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("--------API-Key missing------------------------------")

    # Driver score without header api key
    @pytest.mark.Sanity
    def test25_negative_trip_driverScoreCard_driverScore_missing_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_driverScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys0d2e6f718ab311eeaed8"

        response = Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, "no_apiKey")

        assert response["responseCode"] == "10000"
        assert response["responseData"]["message"] == "Required authentication headers are missing"

        print("---------API-Key missing-----------------------------")

    # To create Driver score expression with empty header x-requestor
    @pytest.mark.Sanity
    def test26_negative_trip_driverScoreCard_impactScore_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 1

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "empty_x-requestor")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "x-requestor header cannot be blank"

        print("------------------x-requestor empty-------------------------")

    # Get impact score with empty header x-requestor
    @pytest.mark.Sanity
    def test27_negative_trip_driverScoreCard_impactScoreBySystemId_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = str(dict1["trip_id"])

        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "empty_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "x-requestor header cannot be blank"

        print("--------x-requestor empty------------------------------")

    # Driver score with empty header x-requestor
    @pytest.mark.Sanity
    def test28_negative_trip_driverScoreCard_driverScore_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_driverScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sys0d2e6f718ab311eeaed8"

        response = Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, "empty_x-requestor")

        assert response["responseCode"] == "10000"
        assert response["responseData"]["message"] == "x-requestor header cannot be blank"

        print("---------x-requestor empty-----------------------------")

    # To create Driver score expression without header x-requestor
    @pytest.mark.Sanity
    def test29_negative_trip_driverScoreCard_impactScore_missing_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            parameter = str(dict1["parameter"])
            operation = str(dict1["operation"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            parameter = 'HA'
            operation = 'multiplication'
            value = 1

        response = Trip_DriverScoreCard_impactScore_negative_validation(self, parameter, operation, value,
                                                                        "no_x-requestor")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("------------------x-requestor Missing-------------------------")

    # Get impact score without header x-requestor
    @pytest.mark.Sanity
    def test30_negative_trip_driverScoreCard_impactScoreBySystemId_missing_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_impactScoreBySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            systemId = str(dict1["systemId"])
            tripId = str(dict1["trip_id"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            tripId = str(dict1["trip_id"])

        # Call api reusable module
        response = Trip_DriverScoreCard_impactScoreBySystemIdTripId_negative_validation(self, systemId, tripId,
                                                                                        "no_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response_body.status_code)
        assert response_body["responseCode"] == "10000"
        assert response_body["responseData"]["message"] == "Required authentication headers are missing"

        print("--------x-requestor missing------------------------------")

    # Driver score without header x-requestor
    @pytest.mark.Sanity
    def test31_negative_trip_driverScoreCard_driverScore_missing_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Trip_DriverScoreCard", "Trip_DriverScoreCard_driverScore")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sys0d2e6f718ab311eeaed8"

        response = Trip_DriverScoreCard_impactScoreBySystemId_negative_validation(self, systemId, "no_x-requestor")

        assert response["responseCode"] == "10000"
        assert response["responseData"]["message"] == "Required authentication headers are missing"

        print("---------x-requestor Missing-----------------------------")
