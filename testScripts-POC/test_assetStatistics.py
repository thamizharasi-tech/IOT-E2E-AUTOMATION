import datetime
import os
import pytest

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN, get_SystemId
from C2CModules.statistics_modules import Statistics_Monthly_trip_summaries_vin, \
    Statistics_Monthly_trip_summaries_fleet, Statistics_daily_trip_summaries_vin, Statistics_daily_trip_summaries_fleet, \
    Statistics_DailyTripSummariesFleet_byFleetId, Statistics_MonthlyTripSummariesVin_byVin, \
    Statistics_MonthlyTripSummariesFleet_byFleetId, Statistics_DailyTripSummariesVin_byVin
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

CurrentPath = os.path.realpath(__file__)
BaseName = os.path.basename(__file__)
Test_Case_No = BaseName.replace('.py', '')
print(Test_Case_No)

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_Statistics:

    # ---------------------------------------------
    # Positive Test scenarios
    # ---------------------------------------------

    # Statistics-MonthlyTripSummariesVin
    @pytest.mark.Smoke
    def test1_positive_Statistics_Monthly_trip_summaries_vin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response_body = Statistics_Monthly_trip_summaries_vin(self, fromMonth, toMonth)

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len <= 0:
                        print("Data list is empty")
                    testResult(self, "passed", "Should list all the trips of the selected month",
                               "All trips of the selected month are listed")
            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month ",
                           "All trips of the selected month are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed")

    # Statistics-MonthlyTripSummariesFleet
    @pytest.mark.Smoke
    def test2_positive_Statistics_MonthlyTripSummariesFleet(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response_body = Statistics_Monthly_trip_summaries_fleet(self, fromMonth, toMonth)

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len <= 0:
                        print("Data list is empty")
                    testResult(self, "passed", "Should list all the trips of the selected month",
                               "All trips of the selected month are listed")
            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month ",
                           "All trips of the selected month are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed")

    # Statistics_daily_trip_summaries_vin
    @pytest.mark.Smoke
    def test3_positive_Statistics_daily_trip_summaries_vin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response_body = Statistics_daily_trip_summaries_vin(self, fromDate, toDate)

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len <= 0:
                        print("Data list is empty")
                    testResult(self, "passed", "Should list all the trips of the selected date",
                               "All trips of the selected date are listed")
            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date ",
                           "All trips of the selected date are not listed  " + " Reason for failure is : " +
                           response)

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed")

    # Statistics-DailyTripSummariesFleet
    @pytest.mark.Smoke
    def test4_positive_Statistics_daily_trip_summaries_fleet(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response_body = Statistics_daily_trip_summaries_fleet(self, fromDate, toDate)

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len <= 0:
                        print("Data list is empty")
                    testResult(self, "passed", "Should list all the trips of the selected date",
                               "All trips of the selected date are listed")
            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date ",
                           "All trips of the selected date are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed ")

    # ---------------------------------------------
    # Positive Test scenarios - New
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId
    @pytest.mark.Smoke
    def test1_positive_Statistics_DailyTripSummariesFleet_byFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)

                        assert (fleetId == fleet_Id)

                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed ")

    # Statistics_MonthlyTripSummariesFleet_byFleetId
    @pytest.mark.Smoke
    def test2_positive_Statistics_MonthlyTripSummariesFleet_byFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)

                        assert (fleetId == fleet_Id)

                        testResult(self, "passed", "Should list all the trips of the selected month & fleetId",
                                   "All trips of the selected month & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & fleetId",
                                   "Statistics - month trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month & fleetId ",
                           "All trips of the selected month & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed  ")

    # Statistics_DailyTripSummariesVin_byVin
    @pytest.mark.Smoke
    def test3_positive_Statistics_DailyTripSummariesVin_byVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)

                        assert (fleetId == fleet_Id)

                        testResult(self, "passed", "Should list all the trips of the selected date & vin",
                                   "All trips of the selected date & vin are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & vin",
                                   "Statistics - daily trip summaries by vin dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected vin & fleetId ",
                           "All trips of the selected vin & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin
    @pytest.mark.Smoke
    def test4_positive_Statistics_MonthlyTripSummariesVin_byVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)

                        assert (fleetId == fleet_Id)

                        testResult(self, "passed", "Should list all the trips of the selected month & vin",
                                   "All trips of the selected month & vin are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & vin",
                                   "Statistics - month trip summaries by vin dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month & vin ",
                           "All trips of the selected month & vin are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios o invalid api key
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_invalid_apiKey
    @pytest.mark.Smoke
    def test1_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalid_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "invalid_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for invalid api key",
                               "Showing proper error for invalid api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid api key",
                               "Not showing proper error for invalid api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for invalid api key",
                           "Not showing proper response code & error for invalid api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid api key ",
                       "Not showing proper response code & error for invalid api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_apiKey
    @pytest.mark.Smoke
    def test2_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "invalid_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for invalid api key",
                               "Showing proper error for invalid api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid api key",
                               "Not showing proper error for invalid api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for invalid api key",
                           "Not showing proper response code & error for invalid api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid api key ",
                       "Not showing proper response code & error for invalid api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_DailyTripSummariesVin_byVin_invalid_apiKey
    @pytest.mark.Smoke
    def test3_positive_Statistics_DailyTripSummariesVin_byVin_invalid_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "invalid_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for invalid api key",
                               "Showing proper error for invalid api key")

                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid api key",
                               "Not showing proper error for invalid api key")
            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for invalid api key",
                           "Not showing proper response code & error for invalid api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid api key ",
                       "Not showing proper response code & error for invalid api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_invalid_apiKey
    @pytest.mark.Smoke
    def test4_positive_Statistics_MonthlyTripSummariesVin_byVin_invalid_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "invalid_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for invalid api key",
                               "Showing proper error for invalid api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid api key",
                               "Not showing proper error for invalid api key")
            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for invalid api key",
                           "Not showing proper response code & error for invalid api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid api key ",
                       "Not showing proper response code & error for invalid api key.  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios o empty api key
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_empty_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_empty_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "empty_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for empty api key",
                               "Showing proper error for empty api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for empty api key",
                               "Not showing proper error for empty api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty api key",
                           "Not showing proper response code & error for empty api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty api key ",
                       "Not showing proper response code & error for empty api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_MonthlyTripSummariesFleet_byFleetId_empty_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_empty_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId, "empty_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for empty api key",
                               "Showing proper error for empty api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for empty api key",
                               "Not showing proper error for empty api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty api key",
                           "Not showing proper response code & error for empty api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty api key ",
                       "Not showing proper response code & error for empty api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_DailyTripSummariesVin_byVin_empty_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_empty_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "empty_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for empty api key",
                               "Showing proper error for empty api key")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for empty api key",
                               "Not showing proper error for empty api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty api key",
                           "Not showing proper response code & error for empty api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty api key ",
                       "Not showing proper response code & error for empty api key.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_empty_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_empty_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "empty_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "api keys are not matching. Please provide valid key":
                    testResult(self, "passed", "Should throw proper error for empty api key",
                               "Showing proper error for empty api key")

                else:
                    testResult(self, "verificationFailed", "Should throw proper error for empty api key",
                               "Not showing proper error for empty api key")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty api key",
                           "Not showing proper response code & error for empty api key")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty api key ",
                       "Not showing proper response code & error for empty api key.  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios without api key parameter
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_no_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_no_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "no_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for no api key parameter",
                               "Showing proper error for no api key parameter")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for no api key parameter",
                               "Not showing proper error for no api key parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for no api key parameter",
                           "Not showing proper response code & error for no api key parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for no api key parameter",
                       "Not showing proper response code & error for no api key parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_MonthlyTripSummariesFleet_byFleetId_no_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_no_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId, "no_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for no api key parameter",
                               "Showing proper error for no api key parameter")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for no api key parameter",
                               "Not showing proper error for no api key parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for no api key parameter",
                           "Not showing proper response code & error for no api key parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for no api key parameter",
                       "Not showing proper response code & error for no api key parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_DailyTripSummariesVin_byVin_no_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_no_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "no_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for no api key parameter",
                               "Showing proper error for no api key parameter")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for no api key parameter",
                               "Not showing proper error for no api key parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for no api key parameter",
                           "Not showing proper response code & error for no api key parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for no api key parameter",
                       "Not showing proper response code & error for no api key parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_no_apiKey
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_no_apiKey(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "no_apiKey")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for no api key parameter",
                               "Showing proper error for no api key parameter")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for no api key parameter",
                               "Not showing proper error for no api key parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for no api key parameter",
                           "Not showing proper response code & error for no api key parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for no api key parameter",
                       "Not showing proper response code & error for no api key parameter.  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios without header x-requestor
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_no_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_no_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "no_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for without x-requestor parameter",
                               "Showing proper error for without x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for without x-requestor parameter parameter",
                               "Not showing proper error for without x-requestor parameter parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                           "Not showing proper response code & error for without x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                       "Not showing proper response code & error for without x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_MonthlyTripSummariesFleet_byFleetId_no_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_no_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "no_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for without x-requestor parameter",
                               "Showing proper error for without x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for without x-requestor parameter",
                               "Not showing proper error for without x-requestor parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                           "Not showing proper response code & error for without x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                       "Not showing proper response code & error for without x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_DailyTripSummariesVin_byVin_no_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_no_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "no_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for without x-requestor parameter",
                               "Showing proper error for without x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for without x-requestor parameter",
                               "Not showing proper error for without x-requestor parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                           "Not showing proper response code & error for without x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                       "Not showing proper response code & error for without x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_no_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_no_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "no_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "Required authentication headers are missing":
                    testResult(self, "passed", "Should throw proper error for without x-requestor parameter",
                               "Showing proper error for without x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for without x-requestor parameter",
                               "Not showing proper error for without x-requestor parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                           "Not showing proper response code & error for without x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for without x-requestor parameter",
                       "Not showing proper response code & error for without x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios for empty header x-requestor
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_empty_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_empty_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "empty_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "x-requestor header cannot be blank":
                    testResult(self, "passed", "Should throw proper error for empty x-requestor parameter",
                               "Showing proper error for empty x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for empty x-requestor parameter parameter",
                               "Not showing proper error for empty x-requestor parameter parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                           "Not showing proper response code & error for empty x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                       "Not showing proper response code & error for empty x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_MonthlyTripSummariesFleet_byFleetId_empty_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_empty_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "empty_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "x-requestor header cannot be blank":
                    testResult(self, "passed", "Should throw proper error for empty x-requestor parameter",
                               "Showing proper error for empty x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for empty x-requestor parameter parameter",
                               "Not showing proper error for empty x-requestor parameter parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                           "Not showing proper response code & error for empty x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                       "Not showing proper response code & error for empty x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics_DailyTripSummariesVin_byVin_empty_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_empty_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "empty_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "x-requestor header cannot be blank":
                    testResult(self, "passed", "Should throw proper error for empty x-requestor parameter",
                               "Showing proper error for empty x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for empty x-requestor parameter parameter",
                               "Not showing proper error for empty x-requestor parameter parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                           "Not showing proper response code & error for empty x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                       "Not showing proper response code & error for empty x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_empty_x-requestor
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_empty_xrequestor(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "empty_x-requestor")

            # Validate response status code
            assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(6106):
                if response_body["responseData"]["message"] == "x-requestor header cannot be blank":
                    testResult(self, "passed", "Should throw proper error for empty x-requestor parameter",
                               "Showing proper error for empty x-requestor parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper error for empty x-requestor parameter parameter",
                               "Not showing proper error for empty x-requestor parameter parameter")

            elif response_body["responseCode"] != str(6106):
                testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                           "Not showing proper response code & error for empty x-requestor parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for empty x-requestor parameter",
                       "Not showing proper response code & error for empty x-requestor parameter.  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios for invalid data - Statistics-DailyTripSummariesFleet_byFleetId
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_invalidFromDate
    @pytest.mark.Smoke
    def test1_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalidFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_invalidFromDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = "04/32/2021"
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid from date",
                               "Showing proper response code & error message for invalid from date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid from date",
                               "Not showing proper error message for invalid from date")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed", "Should throw proper response code & error message for invalid from date",
                           "Not showing proper response code for invalid from date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_emptyFromDate
    @pytest.mark.Smoke
    def test2_positive_Statistics_DailyTripSummariesFleet_byFleetId_emptyFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_emptyFromDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                if fromDate == "None":
                    fromDate = ""
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = ""
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty from date",
                               "Showing proper response code & error message for empty from date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty from date",
                               "Not showing proper error message for empty from date")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty from date",
                           "Not showing proper response code for empty from date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_withoutFromDate
    @pytest.mark.Smoke
    def test3_positive_Statistics_DailyTripSummariesFleet_byFleetId_noFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                if fromDate == "None":
                    fromDate = ""
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "no_fromDate")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without from date parameter",
                               "Showing proper response code & error message for without from date parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without from date parameter",
                               "Not showing proper error message for without from date parameter")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without from date parameter",
                           "Not showing proper response code for without from date parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_invalidToDate
    @pytest.mark.Smoke
    def test4_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalidToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_invalidToDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = datetime.datetime.today().strftime("%m/%d/%Y")
                toDate = "04/32/2021"
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid to date",
                               "Showing proper response code & error message for invalid to date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid to date",
                               "Not showing proper error message for invalid to date")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid to date",
                           "Not showing proper response code for invalid to date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_emptyToDate
    @pytest.mark.Smoke
    def test5_positive_Statistics_DailyTripSummariesFleet_byFleetId_emptyToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_emptyToDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                if toDate == "None":
                    toDate = ""
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = datetime.datetime.today().strftime("%m/%d/%Y")
                toDate = ""
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty to date",
                               "Showing proper response code & error message for empty to date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty to date",
                               "Not showing proper error message for empty to date")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty to date",
                           "Not showing proper response code for empty to date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_withoutToDate
    @pytest.mark.Smoke
    def test6_positive_Statistics_DailyTripSummariesFleet_byFleetId_noToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                if fromDate == "None":
                    fromDate = ""
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "no_toDate")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without to date parameter",
                               "Showing proper response code & error message for without to date parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without to date parameter",
                               "Not showing proper error message for without to date parameter")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without to date parameter",
                           "Not showing proper response code for without to date parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_invalidFleetId
    @pytest.mark.Smoke
    def test7_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalidFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_invalidFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = datetime.datetime.today().strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "fllet177*12"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_emptyFleetId
    @pytest.mark.Smoke
    def test8_positive_Statistics_DailyTripSummariesFleet_byFleetId_emptyFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId_emptyFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
                if fleetId == "None":
                    fleetId = ""
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = datetime.datetime.today().strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = ""

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesFleet_byFleetId_withoutFleetId
    @pytest.mark.Smoke
    def test9_positive_Statistics_DailyTripSummariesFleet_byFleetId_noFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId,
                                                                    "no_fleetId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # -----------------------------------------------------------------------------------------------------

    # ---------------------------------------------
    # Negative Test scenarios for invalid data - Statistics-MonthlyTripSummariesFleet_byFleetId
    # ---------------------------------------------

    # Statistics-MonthlyTripSummariesFleet_byFleetId_invalidFromMonth
    @pytest.mark.Smoke
    def test1_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalidFromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_invalidFromMonth")
            if dict['Flag'] == "Yes":
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = "13/2023"
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid from month",
                               "Showing proper response code & error message for invalid from month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid from month",
                               "Not showing proper error message for invalid from month")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid from month",
                           "Not showing proper response code for invalid from month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_emptyFromMonth
    @pytest.mark.Smoke
    def test2_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_emptyFromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_emptyFromMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                if fromMonth == 'None':
                    fromMonth = ""
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = ""
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty from month",
                               "Showing proper response code & error message for empty from month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty from month",
                               "Not showing proper error message for empty from month")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty from month",
                           "Not showing proper response code for empty from month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_withoutFromMonth
    @pytest.mark.Smoke
    def test3_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_noFromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "no_fromMonth")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without from month parameter",
                               "Showing proper response code & error message for without from month parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without from month parameter",
                               "Not showing proper error message for without from month parameter")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without from month parameter",
                           "Not showing proper response code for without from month parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_invalidToMonth
    @pytest.mark.Smoke
    def test4_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalidToMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_invalidToMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = "04/32/2021"
                fleetId = "flet123"

            print("From Date : ", fromMonth)
            print("To Date : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid to month",
                               "Showing proper response code & error message for invalid to month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid to month",
                               "Not showing proper error message for invalid to month")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid to month",
                           "Not showing proper response code for invalid to month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_emptyToMonth
    @pytest.mark.Smoke
    def test5_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_emptyToMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_emptyToMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                if toMonth == "None":
                    toMonth = ""
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = ""
                fleetId = "flet123"

            print("From Date : ", fromMonth)
            print("To Date : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty to month",
                               "Showing proper response code & error message for empty to month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty to month",
                               "Not showing proper error message for empty to month")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty to month",
                           "Not showing proper response code for empty to month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_withoutToMonth
    @pytest.mark.Smoke
    def test6_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_noToMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                if fromMonth == "None":
                    fromMonth = ""
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            # print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "no_toMonth")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without to month parameter",
                               "Showing proper response code & error message for without to month parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without to month parameter",
                               "Not showing proper error message for without to month parameter")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without to month parameter",
                           "Not showing proper response code for without to month parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_invalidFleetId
    @pytest.mark.Smoke
    def test7_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalidFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_invalidFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "fllet177*12"

            print("From Date : ", fromMonth)
            print("To Date : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_emptyFleetId
    @pytest.mark.Smoke
    def test8_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_emptyFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId_emptyFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
                if fleetId == "None":
                    fleetId = ""
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = ""

            print("From Date : ", fromMonth)
            print("To Date : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected month & fleetId",
                                   "All trips of the selected month & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & fleetId",
                                   "Statistics - Monthly trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month & fleetId ",
                           "All trips of the selected month & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesFleet_byFleetId_withoutFleetId
    @pytest.mark.Smoke
    def test9_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_noFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Date : ", fromMonth)
            print("To Date : ", toMonth)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "no_fleetId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected month & fleetId",
                                   "All trips of the selected month & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & fleetId",
                                   "Statistics - Monthly trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month & fleetId ",
                           "All trips of the selected month & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios for invalid data - Statistics-DailyTripSummariesVin_byVin
    # ---------------------------------------------

    # Statistics-DailyTripSummariesVin_byVin_invalidFromDate
    @pytest.mark.Smoke
    def test1_positive_Statistics_DailyTripSummariesVin_byVin_invalidFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidFromDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = "04/32/2021"
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid from date",
                               "Showing proper response code & error message for invalid from date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid from date",
                               "Not showing proper error message for invalid from date")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid from date",
                           "Not showing proper response code for invalid from date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptyFromDate
    @pytest.mark.Smoke
    def test2_positive_Statistics_DailyTripSummariesVin_byVin_emptyFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptyFromDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                if fromDate == "None":
                    fromDate = ""
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = ""
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty from date",
                               "Showing proper response code & error message for empty from date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty from date",
                               "Not showing proper error message for empty from date")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty from date",
                           "Not showing proper response code for empty from date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutFromDate
    @pytest.mark.Smoke
    def test3_positive_Statistics_DailyTripSummariesVin_byVin_noFromDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            # print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_fromDate")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without from date parameter",
                               "Showing proper response code & error message for without from date parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without from date parameter",
                               "Not showing proper error message for without from date parameter")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without from date parameter",
                           "Not showing proper response code for without from date parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_invalidToDate
    @pytest.mark.Smoke
    def test4_positive_Statistics_DailyTripSummariesVin_byVin_invalidToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidToDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = "04/32/2021"
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid to date",
                               "Showing proper response code & error message for invalid to date")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid to date",
                               "Not showing proper error message for invalid to date")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid to date",
                           "Not showing proper response code for invalid to date")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptyToDate
    @pytest.mark.Smoke
    def test5_positive_Statistics_DailyTripSummariesVin_byVin_emptyToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptyToDate")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                if toDate == "None":
                    todate = ""
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = ""
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

                print("From Date : ", fromDate)
                print("To Date : ", toDate)
                print("Fleet Id : ", fleetId)

                # Call api reusable model
                response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                                  fuelType,
                                                                  "valid")

                # Validate response status code
                assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                # Validate response body
                if response_body["responseCode"] == str(17104):
                    if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                        testResult(self, "passed",
                                   "Should throw proper response code & error message for empty to date",
                                   "Showing proper response code & error message for empty to date")
                    else:
                        testResult(self, "verificationFailed",
                                   "Should throw proper response code & error message for empty to date",
                                   "Not showing proper error message for empty to date")

                elif response_body["responseCode"] != str(17104):
                    testResult(self, "failed",
                               "Should throw proper response code & error message for empty to date",
                               "Not showing proper response code for empty to date")

                print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutToDate
    @pytest.mark.Smoke
    def test6_positive_Statistics_DailyTripSummariesVin_byVin_noToDate(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            # print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_toDate")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without to date parameter",
                               "Showing proper response code & error message for without to date parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without to date parameter",
                               "Not showing proper error message for without to date parameter")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without to date parameter",
                           "Not showing proper response code for without to date parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_invalidFleetId
    @pytest.mark.Smoke
    def test7_positive_Statistics_DailyTripSummariesVin_byVin_invalidFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet177*12"
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptyFleetId
    @pytest.mark.Smoke
    def test8_positive_Statistics_DailyTripSummariesVin_byVin_emptyFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptyFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                if fleetId == "None":
                    fleetId = ""
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = ""
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutFleetId
    @pytest.mark.Smoke
    def test9_positive_Statistics_DailyTripSummariesVin_byVin_noFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_fleetId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_invalidVin
    @pytest.mark.Smoke
    def test10_positive_Statistics_DailyTripSummariesVin_byVin_invalidVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = "vin123"
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("VIN : ", vin)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid vin",
                               "Showing proper response code & error message for invalid vin")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid vin",
                               "Not showing proper error message for invalid vin")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid vin",
                           "Not showing proper response code for invalid vin")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptyVin
    @pytest.mark.Smoke
    def test11_positive_Statistics_DailyTripSummariesVin_byVin_emptyVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptyVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                if vin == "None":
                    vin = ""
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = ""
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since vin is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutVin
    @pytest.mark.Smoke
    def test12_positive_Statistics_DailyTripSummariesVin_byVin_noVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_vin")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since vin is a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_invalidSystemId
    @pytest.mark.Smoke
    def test13_positive_Statistics_DailyTripSummariesVin_byVin_invalidSystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidSystemId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = "sys123"
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("System Id : ", systemId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid vin",
                               "Showing proper response code & error message for invalid vin")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid vin",
                               "Not showing proper error message for invalid vin")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid vin",
                           "Not showing proper response code for invalid vin")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptySystemId
    @pytest.mark.Smoke
    def test14_positive_Statistics_DailyTripSummariesVin_byVin_emptySystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptySystemId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                if systemId == "None":
                    systemId = ""
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = ""
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since system Id is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutSystemId
    @pytest.mark.Smoke
    def test15_positive_Statistics_DailyTripSummariesVin_byVin_noSystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_systemId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since system Id is a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_invalidFuelType
    @pytest.mark.Smoke
    def test16_positive_Statistics_DailyTripSummariesVin_byVin_invalidFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_invalidFuelType")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "g"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("System Id : ", systemId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since fuel type is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_emptyFuelType
    @pytest.mark.Smoke
    def test17_positive_Statistics_DailyTripSummariesVin_byVin_emptyFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin_emptyFuelType")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                if systemId == "None":
                    systemId = ""
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = ""

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since fuel type is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-DailyTripSummariesVin_byVin_withoutFuelType
    @pytest.mark.Smoke
    def test18_positive_Statistics_DailyTripSummariesVin_byVin_noFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId, fuelType,
                                                              "no_fuelType")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fuel type is a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # ---------------------------------------------
    # Negative Test scenarios for invalid data - Statistics-MonthlyTripSummariesVin_byVin
    # ---------------------------------------------

    # Statistics-MonthlyTripSummariesVin_byVin_invalidFromMonth
    @pytest.mark.Smoke
    def test1_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidFromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidFromMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = "32/2021"
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid from month",
                               "Showing proper response code & error message for invalid from month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid from month",
                               "Not showing proper error message for invalid from month")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid from month",
                           "Not showing proper response code for invalid from month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptyFromMonth
    @pytest.mark.Smoke
    def test2_positive_Statistics_MonthlyTripSummariesVin_byVin_emptyFromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptyFromMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                if fromMonth == "None":
                    fromMonth = ""
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = ""
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for empty From Month",
                               "Showing proper response code & error message for empty From Month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for empty From Month",
                               "Not showing proper error message for empty From Month")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for empty From Month",
                           "Not showing proper response code for empty From Month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_withoutfromMonth
    @pytest.mark.Smoke
    def test3_positive_Statistics_MonthlyTripSummariesVin_byVin_nofromMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            # print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_fromMonth")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17103):
                if response_body["responseData"]["message"] == "Invalid start date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without From Month parameter",
                               "Showing proper response code & error message for without From Month parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without From Month parameter",
                               "Not showing proper error message for without From Month parameter")

            elif response_body["responseCode"] != str(17103):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without From Month parameter",
                           "Not showing proper response code for without From Month parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_invalidToMonth
    @pytest.mark.Smoke
    def test4_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidToMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidToMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = "04/32/2021"
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17106):
                if response_body["responseData"]["message"] == "Invalid date format!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid to month",
                               "Showing proper response code & error message for invalid to month")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid to month",
                               "Not showing proper error message for invalid to month")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid to month",
                           "Not showing proper response code for invalid to month")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptyToMonth
    @pytest.mark.Smoke
    def test5_positive_Statistics_MonthlyTripSummariesVin_byVin_emptyToMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptyToMonth")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                if toMonth == "None":
                    toMonth = ""
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = ""
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

                print("From Month : ", fromMonth)
                print("To Month : ", toMonth)
                print("Fleet Id : ", fleetId)

                # Call api reusable model
                response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                    fuelType,
                                                                    "valid")

                # Validate response status code
                assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                # Validate response body
                if response_body["responseCode"] == str(17104):
                    if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                        testResult(self, "passed",
                                   "Should throw proper response code & error message for empty To Month",
                                   "Showing proper response code & error message for empty To Month")
                    else:
                        testResult(self, "verificationFailed",
                                   "Should throw proper response code & error message for empty To Month",
                                   "Not showing proper error message for empty To Month")

                elif response_body["responseCode"] != str(17104):
                    testResult(self, "failed",
                               "Should throw proper response code & error message for empty To Month",
                               "Not showing proper response code for empty To Month")

                print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_withouttoMonth
    @pytest.mark.Smoke
    def test6_positive_Statistics_MonthlyTripSummariesVin_byVin_notoMonth(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            # print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_toMonth")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17104):
                if response_body["responseData"]["message"] == "Invalid end date!!! Please input a valid date":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for without To Month parameter",
                               "Showing proper response code & error message for without To Month parameter")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for without To Month parameter",
                               "Not showing proper error message for without To Month parameter")

            elif response_body["responseCode"] != str(17104):
                testResult(self, "failed",
                           "Should throw proper response code & error message for without To Month parameter",
                           "Not showing proper response code for without To Month parameter")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_invalidFleetId
    @pytest.mark.Smoke
    def test7_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet177*12"
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptyFleetId
    @pytest.mark.Smoke
    def test8_positive_Statistics_MonthlyTripSummariesVin_byVin_emptyFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptyFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                if fleetId == "None":
                    fleetId = ""
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = ""
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_withoutFleetId
    @pytest.mark.Smoke
    def test9_positive_Statistics_MonthlyTripSummariesVin_byVin_noFleetId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_fleetId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fleet_id os a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_invalidVin
    @pytest.mark.Smoke
    def test10_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = "vin123"
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("VIN : ", vin)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body

            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptyVin
    @pytest.mark.Smoke
    def test11_positive_Statistics_MonthlyTripSummariesVin_byVin_emptyVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptyVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                if vin == "None":
                    vin = ""
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = ""
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since vin is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_withoutVin
    @pytest.mark.Smoke
    def test12_positive_Statistics_MonthlyTripSummariesVin_byVin_noVin(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_vin")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since vin is a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_invalidSystemId
    @pytest.mark.Smoke
    def test13_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidSystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidSystemId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = "sys123"
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("System Id : ", systemId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body

            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Showing proper response code & error message for invalid fleetId")
                else:
                    testResult(self, "verificationFailed",
                               "Should throw proper response code & error message for invalid fleetId",
                               "Not showing proper error message for invalid fleetId")

            elif response_body["responseCode"] != str(17106):
                testResult(self, "failed",
                           "Should throw proper response code & error message for invalid fleetId",
                           "Not showing proper response code for invalid fleetId")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper response code & error message",
                       "Not showing proper response code & error message.  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptySystemId
    @pytest.mark.Smoke
    def test14_positive_Statistics_MonthlyTripSummariesVin_byVin_emptySystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptySystemId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                if systemId == "None":
                    systemId = ""
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = ""
                fleetId = "fllet123"
                fuelType = "gas"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since system Id is a optional field, when its empty it fetches the record based on from_date and to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_withoutSystemId
    @pytest.mark.Smoke
    def test15_positive_Statistics_MonthlyTripSummariesVin_byVin_noSystemId(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_systemId")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since system Id is a optional field, when its empty it fetches the record based on from_date and "
                  "to_date which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected date & fleetId",
                                   "All trips of the selected date & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected date & fleetId",
                                   "Statistics - daily trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected date & fleetId ",
                           "All trips of the selected date & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected date ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_invalidFuelType
    @pytest.mark.Smoke
    def test16_positive_Statistics_MonthlyTripSummariesVin_byVin_invalidFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_invalidFuelType")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = "g"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("System Id : ", systemId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since fuel type is a optional field, when its empty it fetches the record based on from_month and to_month which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected month & fleetId",
                                   "All trips of the selected month & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & fleetId",
                                   "Statistics - monthly trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month",
                           "All trips of the selected month is not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected date are not listed  " + " Reason for failure is : " +
                       response.text)

    # Statistics-MonthlyTripSummariesVin_byVin_emptyFuelType
    @pytest.mark.Smoke
    def test17_positive_Statistics_MonthlyTripSummariesVin_byVin_emptyFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin_emptyFuelType")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                if systemId == "None":
                    systemId = ""
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = "fllet123"
                fuelType = ""

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print(
                "Since fuel type is a optional field, when its empty it fetches the record based on from_month and to_month which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected month & fleetId",
                                   "All trips of the selected month & fleet Id are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month & fleetId",
                                   "Statistics - monthly trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month & fleetId ",
                           "All trips of the selected month & fleet Id are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed")

    # Statistics-MonthlyTripSummariesVin_byVin_withoutFuelType
    @pytest.mark.Smoke
    def test18_positive_Statistics_MonthlyTripSummariesVin_byVin_noFuelType(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics",
                                            "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")

                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)
            # print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType,
                                                                "no_fuelType")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            print("Since fuel type is a optional field, when its empty it fetches the record based on from_month and "
                  "to_month which is a mandatory field")
            if response_body["responseCode"] == str(1200):
                if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                    "message"] == "Success":
                    data_len = len(response_body["responseData"]["data"])
                    if data_len >= 1:
                        data_len = int(data_len - 1)
                        fleet_Id = response_body["responseData"]["data"][data_len]["fleetId"]
                        engine_Type = response_body["responseData"]["data"][data_len]["tripSummary"]["engineType"]
                        print("fleet Id : ", fleet_Id)
                        print("Engine Type :", engine_Type)
                        testResult(self, "passed", "Should list all the trips of the selected month",
                                   "All trips of the selected month are listed")
                    else:
                        print("Data list is empty")
                        testResult(self, "verificationFailed",
                                   "Should list all the trips of the selected month",
                                   "Statistics - monthly trip summaries by fleet Id dalatlist is empty, but end point is working fine, thus marking test case pass")


            elif response_body["responseCode"] != str(1200):
                testResult(self, "failed", "Should list all the trips of the selected month ",
                           "All trips of the selected month are not listed  " + " Reason for failure is : " +
                           response_body["responseData"]["message"])

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should list all the trips of the selected month ",
                       "All trips of the selected month are not listed")

    # ---------------------------------------------
    # Negative Test scenarios - Page parameter validations
    # ---------------------------------------------

    # Statistics-DailyTripSummariesFleet_byFleetId_pageSize_0
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalid_pageSize_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "pageSize_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics-DailyTripSummariesFleet_byFleetId_pageSize_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalid_pageSize_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "pageSize_1001")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics-DailyTripSummariesFleet_byFleetId_pageNo_0
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalid_pageNo_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "pageNo_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17109):
                if response_body["responseData"]["message"] == "Page number must not be less than one":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17109):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics-DailyTripSummariesFleet_byFleetId_pageNo_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesFleet_byFleetId_invalid_pageNo_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                fleetId = "flet123"

            print("From Date : ", fromDate)
            print("To Date : ", toDate)
            print("Fleet Id : ", fleetId)

            # Call api reusable model
            response = Statistics_DailyTripSummariesFleet_byFleetId(self, fromDate, toDate, fleetId, "pageNo_1001")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17105):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageSize_0
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageSize_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "pageSize_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageSize_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageSize_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "pageSize_1001")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageNo_0
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageNo_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "pageNo_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17109):
                if response_body["responseData"]["message"] == "Page number must not be less than one":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17109):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageNo_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesFleet_byFleetId_invalid_pageNo_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesFleet_byFleetId")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                fleetId = str(dict["fleetId"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                fleetId = "flet123"

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesFleet_byFleetId(self, fromMonth, toMonth, fleetId,
                                                                      "pageNo_1001")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17105):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics_DailyTripSummariesVin_byVin_invalid_pageSize_0
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_invalid_pageSize_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "pageSize_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics_DailyTripSummariesVin_byVin_invalid_pageSize_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_invalid_pageSize_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "pageSize_1001")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics_DailyTripSummariesVin_byVin_invalid_pageNo_0
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_invalid_pageNo_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "pageNo_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17109):
                if response_body["responseData"]["message"] == "Page number must not be less than one":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17109):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics_DailyTripSummariesVin_byVin_invalid_pageNo_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_DailyTripSummariesVin_byVin_invalid_pageNo_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-DailyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromDate = str(dict["fromDate"])
                toDate = str(dict["toDate"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromDate = datetime.datetime.today().replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ) - datetime.timedelta(days=1)
                fromDate = fromDate.strftime("%m/%d/%Y")
                toDate = datetime.datetime.today().strftime("%m/%d/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Date : ", fromDate)
            print("To Date : ", toDate)

            # Call api reusable model
            response = Statistics_DailyTripSummariesVin_byVin(self, fromDate, toDate, systemId, vin, fleetId,
                                                              fuelType,
                                                              "pageNo_1001")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17105):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics-MonthlyTripSummariesVin_invalid_pageSize_0
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_invalid_pageSize_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "pageSize_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics-MonthlyTripSummariesVin_invalid_pageSize_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_invalid_pageSize_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "pageSize_1001")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17110):
                if response_body["responseData"][
                    "message"] == "Page size must not be less than one or greater than 1000":
                    testResult(self, "passed", "Should throw proper error for invalid page size",
                               "Showing proper error for invalid page size")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid paze size",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17110):
                testResult(self, "failed", "Should throw proper error for invalid page size",
                           "Not showing proper response code & error for invalid page size")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page size ",
                       "Not showing proper response code & error for invalid page size")

    # Statistics-MonthlyTripSummariesVin_invalid_pageNo_0
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_invalid_pageNo_0(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "pageNo_0")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17109):
                if response_body["responseData"]["message"] == "Page number must not be less than one":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17109):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")

    # Statistics-MonthlyTripSummariesVin_invalid_pageNo_1001
    @pytest.mark.Smoke
    def test_positive_Statistics_MonthlyTripSummariesVin_byVin_invalid_pageNo_1001(self):
        response = ''
        try:
            print("----------------------------------------------------------")
            dict = read_api_data_from_excel(self, "Statistics", "Statistics-MonthlyTripSummariesVin_byVin")
            if dict['Flag'] == "Yes":
                print("Flag is set to Yes, hence running with excel data :")
                fromMonth = str(dict["fromMonth"])
                toMonth = str(dict["toMonth"])
                systemId = str(dict["systemId"])
                vin = str(dict["vin"])
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])
            else:
                print("Flag is not set to Yes, hence running with generic/actual device data")
                fromMonth = datetime.datetime.today().strftime("%m/%Y")
                toMonth = datetime.datetime.today().strftime("%m/%Y")
                vin = getVIN(self, OnboardingType, chipsetType)
                systemId = get_SystemId(self, OnboardingType, chipsetType)
                fleetId = str(dict["fleetId"])
                fuelType = str(dict["fuelType"])

            print("From Month : ", fromMonth)
            print("To Month : ", toMonth)

            # Call api reusable model
            response = Statistics_MonthlyTripSummariesVin_byVin(self, fromMonth, toMonth, systemId, vin, fleetId,
                                                                fuelType, "pageNo_1001")

            # Validate response status code
            assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["responseCode"] == str(17105):
                if response_body["responseData"]["message"] == "No data present in db for this filter":
                    testResult(self, "passed", "Should throw proper error for invalid page No",
                               "Showing proper error for invalid page No")
                else:
                    testResult(self, "verificationFailed", "Should throw proper error for invalid page No",
                               "Not showing proper error for invalid page size")

            elif response_body["responseCode"] != str(17105):
                testResult(self, "failed", "Should throw proper error for invalid page No",
                           "Not showing proper response code & error for invalid page No")

            print("----------------------------------------------------------")

        except:
            print("something went wrong, pls refer api response & logs")
            testResult(self, "failed", "Should throw proper error for invalid page No ",
                       "Not showing proper response code & error for invalid page No")
