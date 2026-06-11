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
    read_latest_trip_details_attribute_value, trip_event, trip_event
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Trip_Event:

    # trip_tripevent
    @pytest.mark.Smoke
    def test1_negative_trip_event_without_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId =str(dict1["systemId"])
            #systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "without_tripId")

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body
        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6007) or response_body["errors"][0]["message"] == (
                    "Trip summary details not exist"):
            testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_trip_event_invalidtripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event_invalidtripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId =str(dict1["systemId"])
            #systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168ki3454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 404):
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            #self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6007) or response_body["errors"][0]["message"] == (
                    "Trip summary details not exist"):
            testResult(self, "passed", "Should throw proper error message",
                           "Response/Error message is as expected. Refer api response for additional info/details")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                           "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            #self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_trip_event_withouttripId_startDateandendDate(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "without_tripId_startDate_endDate")

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6007) or response_body["errors"][0]["message"] == (
                   "Start Date and End Date is mandatory"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_trip_event_without_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "no_systemId")

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body[""] == ("Required request parameter 'systemId' for method parameter type String is not present"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    def test5_negative_trip_event_invalid_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event_invalidsystemId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 404):
            assert True

        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if  response_body["errors"][0]["code"] == str(6007) or response_body["errors"][0]["message"] == (
                   "Trip summary details not exist"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    def test6_negative_trip_event_empty_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event_emptysystemId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = ""
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if  response_body["errors"][0]["code"] == str(6004) or response_body["errors"][0]["message"] == (
                   "Start Date and End Date is mandatory"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7_negative_trip_event_no_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "no_apiKey")
        verify_api_response_for_invalid_header(response, "no_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8_negative_trip_event_no_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "no_x-requestor")
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test9_negative_trip_event_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:",endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "invalid_apiKey")
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10_negative_trip_event_null_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "null_apiKey")
        verify_api_response_for_invalid_header(response, "null_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test11_negative_trip_event_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "empty_apiKey")
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12_negative_trip_event_null_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate, "null_x-requestor")
        verify_api_response_for_invalid_header(response, "null_x-requestor")
        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test10_negative_trip_event_Enddate_greaterthan_30days(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip_event_EndDate_greaterthan_30Days")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6015) or response_body["errors"][0]["message"] == (
                "Start date and End date difference should not be greater than 30Days"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test11_negative_trip_event_startDate_greaterThan_EndDate(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip_event_startDate_greaterthan_EndDate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6004) or response_body["errors"][0]["message"] == (
                "End date should be greater than Start date"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12_negative_trip_event_Invalid_dateformat(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip_event_Invalid_dateformat")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("startDate :", startDate)
        print("endDate:", endDate)

        # Call asset management reusable module
        response = trip_event(self, systemId, tripId, startDate, endDate)

        # Validate response status code
        if (response.status_code == 400):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(6004) or response_body["errors"][0]["message"] == (
                "Date should be in a valid format : MM-dd-yyyy"):
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

