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
    read_latest_trip_details_attribute_value, trip_event, trip_info, trip_info_new
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Trip_info:

    # trip_tripevent

    @pytest.mark.Smoke
    def test1_negative_tripinfo_pageSize_lessthan1(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_pageSize_lessthan1")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId,"valid")

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
        if response_body["responseCode"] == str(6003) or response_body["responseData"][0]["message"] == (
                "Page size must not be less than one"):
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
    def test2_negative_tripinfo_pageNumber_lessthan0(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_pageNumber_lessthan1")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId,"valid")

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
        if response_body["responseCode"] == str(6002) or response_body["responseData"][0]["message"] == (
                "Page number must not be less than zero"):
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
    def test3_negative_tripinfo_pageNumber_greaterthan200(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_pageNumber_greaterThan200")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)


        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId,"valid")


        # Validate response status code
        if (response.status_code == 404):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(1000) or response_body["errors"][0]["message"] == (
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

    @pytest.mark.Smoke
    def test4_negative_tripinfo_invalid_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_invalid_systemId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "valid")

        # Validate response status code
        if (response.status_code == 404):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["errors"][0]["code"] == str(1000) or response_body["errors"][0]["message"] == (
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

    @pytest.mark.Smoke
    def test5_negative_tripinfo_empty_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_no_systemId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = ""
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "valid")

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
        if response_body["errors"][0]["code"] == str(6013) or response_body["errors"][0]["message"] == (
                "Systemid is mandatory"):
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
    def test6_negative_tripinfo_without_systemId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "without_systemId")

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
        if response_body["errors"][0]["code"] == str(6013) or response_body["errors"][0]["message"] == (
                "Systemid is mandatory"):
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
    def test7_negative_tripinfo_without_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId,  "without_tripId")

        # Validate response status code
        if (response.status_code == 200):
            assert True

        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        # Verify response body

        response_body = response.json()
        if response_body["message"] == ("Success"):
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
    def test8_negative_tripinfo_invalid_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_invalid_tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId)

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
        if response_body["errors"][0]["code"] == str(1000) or response_body["errors"][0]["message"] == (
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

    @pytest.mark.Smoke
    def test9_negative_tripinfo_empty_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_new_no_tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = ""
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = "sysa55706ec09a211eebe7e_168663454"
            systemId = "sys234"
            pageNo = "0"
            pageSize = "10"

        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize:", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId)

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
        if response_body["errors"][0]["code"] == str(1000) or response_body["errors"][0]["message"] == (
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

    @pytest.mark.Smoke
    def test10_negative_tripinfo_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize",pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "invalid_apiKey")
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test11_negative_tripinfo_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "empty_apiKey")
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    def test12_negative_tripinfo_no_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "no_apiKey")
        verify_api_response_for_invalid_header(response, "no_apiKey")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    def test13_negative_tripinfo_empty_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "empty_x-requestor")
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    def test14_negative_tripinfo_no_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_new")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            systemId = str(dict1["systemId"])
            # systemId = read_vehicleJsonFile(self, "system_id")
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        print("Trip Id :", tripId)
        print("systemId :", systemId)
        print("pageNo :", pageNo)
        print("pageSize", pageSize)

        # Call asset management reusable module
        response = trip_info_new(self, pageNo, pageSize, systemId, tripId, "no_x-requestor")
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        # Parse API response into JSON
        # Verify response body

        testResult(self, "passed", "trip Event On Vehicle API should throw appropriate error message for no apikey",
                   "Response/Error message is as expected. Refer api response for additional info/details")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")
