import datetime
import time

import pytest

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.fms_modules import assetManagement_trip_info_by_date, assetManagement_trip_info_by_tripId, \
    assetManagement_trip_waypoints_by_tripid, assetManagement_trip_waypoints_by_systemId, \
    assetManagement_latest_trip_meta, assetManagement_latest_trip_details, get_tridId_from_log, \
    assetManagement_latest_trip_details_new, assetManagement_trip_info_by_date_new, \
    assetManagement_trip_info_by_tripId_new, assetManagement_trip_waypoints_by_tripid_new, \
    assetManagement_trip_waypoints_by_systemId_new, assetManagement_latest_trip_meta_new
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_AssetManagement:

    # Asset Management Trip Info
    @pytest.mark.Smoke
    def test1_positive_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

            # Call asset management reusable module
            assetManagement_trip_info_by_date(self, startDate, endDate)
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

            # Call asset management reusable module
            assetManagement_trip_info_by_date(self, startDate, endDate)

        print("----------------------------------------------------------")

    # AssetManagement_trip-info-by-tripId
    @pytest.mark.Smoke
    def test2_positive_AssetManagement_trip_info_by_tripId(self):

        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            trip_id = str(dict1["tripId"])

            print("Trip Id :", trip_id)

            # Call asset management reusable module
            assetManagement_trip_info_by_tripId(self, trip_id)

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
    def test3_positive_AssetManagement_trip_waypoints_by_tripid(self):

        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-tripid")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            trip_id = str(dict1["tripId"])

            print("Trip Id :", trip_id)

            # Call asset management reusable module
            assetManagement_trip_waypoints_by_tripid(self, trip_id)
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
    def test4_positive_assetManagement_trip_waypoints_by_systemId(self):

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
            assetManagement_trip_waypoints_by_systemId(self, startDate, endDate, systemId)

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
            assetManagement_trip_waypoints_by_systemId(self, startDate, endDate, systemId)

        print("----------------------------------------------------------")

    # AssetManagement_latest-trip-meta
    @pytest.mark.Smoke
    def test5_positive_AssetManagement_latest_trip_meta(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-meta")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            assetManagement_latest_trip_meta(self, vin, systemId, status)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            i = 0
            while i in range(10):
                response_body = assetManagement_latest_trip_meta(self, vin, systemId, status)
                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            # Validation of api response data

            assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")

    # AssetManagement_latest-trip-details
    @pytest.mark.Smoke
    def test6_positive_AssetManagement_latest_trip_details(self):

        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-details")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            assetManagement_latest_trip_details(self, vin, systemId, status)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            i = 0
            while i in range(10):
                response_body = assetManagement_latest_trip_details(self, vin, systemId, status)
                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            # Validation of api response data

            assert (response_body["responseData"]['message'] == "Success")

        print("----------------------------------------------------------")


# ------------------------
# NEW test scripts

class Test_AssetManagement_new:

    # Asset Management Trip Info
    @pytest.mark.Smoke
    def test1_positive_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseData"]["message"] == "Success")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

        print("----------------------------------------------------------")

    # AssetManagement_trip-info-by-tripId
    @pytest.mark.Smoke
    def test2_positive_AssetManagement_trip_info_by_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            # Call asset management reusable module
            response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["responseCode"] == str(1200):
                assert True
            else:
                print("response Code is not 1200. Rather found : " + str(response_body))
                assert False

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = get_tridId_from_log(self)
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Trip Id :", tripId)

            time.sleep(120)

            i = 0
            while i in range(10):
                # Call asset management reusable module
                response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

                # Validate response status code
                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                if response_body["responseCode"] == str(1200):
                    assert True
                else:
                    print("response Code is not 1200. Rather found : " + str(response_body))
                    assert False

                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            assert (response_body["responseData"]['message'] == "Success")

            print("----------------------------------------------------------")

    # AssetManagement_trip-waypoints-by-tripid
    @pytest.mark.Smoke
    def test3_positive_AssetManagement_trip_waypoints_by_tripid(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-tripid")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])

            print("Trip Id :", tripId)

            # Call asset management reusable module
            response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["responseCode"] == str(1200):
                assert True
            else:
                print("response Code is not 1200. Rather found : " + str(response_body))
                assert False

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)

            print("Trip Id :", tripId)

            time.sleep(120)

            i = 0
            while i in range(10):
                response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

                # Validate response status code
                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                if response_body["responseCode"] == str(1200):
                    assert True
                else:
                    print("response Code is not 1200. Rather found : " + str(response_body))
                    assert False

                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            assert (response_body["responseData"]['message'] == "Success")

            print("----------------------------------------------------------")

    # assetManagement_trip_waypoints_by_systemId
    @pytest.mark.Smoke
    def test4_positive_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Start Date : ", startDate)
        print("End Date : ", endDate)
        print("System Id : ", systemId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert True
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

        print("----------------------------------------------------------")

    # AssetManagement_latest-trip-meta
    @pytest.mark.Smoke
    def test5_positive_AssetManagement_latest_trip_meta(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-meta")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_meta_new(self, vin, systemId, status, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["responseCode"] == str(1200):
                assert True
            else:
                print("response Code is not 1200. Rather found : " + str(response_body))
                assert False

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            i = 0
            while i in range(10):
                response = assetManagement_latest_trip_meta_new(self, vin, systemId, status, "valid")

                # Validate response status code
                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                if response_body["responseCode"] == str(1200):
                    assert True
                else:
                    print("response Code is not 1200. Rather found : " + str(response_body))
                    assert False

                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            # Validation of api response data

            assert (response_body["responseData"]['message'] == "Success")

            print("----------------------------------------------------------")

    # AssetManagement_latest-trip-details
    @pytest.mark.Smoke
    def test6_positive_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")
        "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-details")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["responseCode"] == str(1200):
                assert True
            else:
                print("response Code is not 1200. Rather found : " + str(response_body))
                assert False

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            i = 0
            while i in range(10):
                response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

                # Validate response status code
                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                if response_body["responseCode"] == str(1200):
                    assert True
                else:
                    print("response Code is not 1200. Rather found : " + str(response_body))
                    assert False

                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            # Validation of api response data

            assert (response_body["responseData"]['message'] == "Success")

            print("----------------------------------------------------------")

    # negative scenarios:
    @pytest.mark.Smoke
    def test1_neg_invalidendDate_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_invalidendDate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = "13-13-2023"
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_neg_invalidstartDate_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_invalidstartDate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            print("Start Date : ", startDate)
            print("End Date : ", endDate)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = "13-13-2023"
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        print("----------------------------------------------------------")

    # INVALID TRIP ID
    @pytest.mark.Smoke
    def test_fms009_negative_assetManagement_trip_waypoints_by_tripid(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId_invalidId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = "1234"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["responseCode"] == str(1000))

        assert (response_body["responseData"]["message"] == "Trip waypoint details not exist")

        # assert len(response_body["responseData"]["dataList"]) == 0

    #  Validate GET API not able to fetch trip waypoint data in FMS UI API Component when null value is given to trip id
    @pytest.mark.Smoke
    def test_fms010_negative_assetManagement_trip_waypoints_by_tripid(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId_invalidId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])

            print("Trip Id :", tripId)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = "1234"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["responseCode"] == str(1000))

        assert (response_body["responseData"]["message"] == "Trip waypoint details not exist")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details by given tripId/ startDate and endDate and also with invalid
    # limit
    @pytest.mark.Smoke
    def test_smryapi10_negative_assetManagement_trip_info_by_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_by-tripId_invalidpageSize")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = str(dict1["pageNo"])
            pageSize = "%$"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        # response_body = response.json()

        # Validate response body
        # assert (response_body["responseCode"] == str(6003))
        # assert (response_body["responseData"]["message"] == "Page size cannot be negative")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details by given tripId/ startDate and endDate and also with   limit 0
    @pytest.mark.Smoke
    def test_smryapi11_negative_assetManagement_trip_info_by_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_by-tripId_invalidpageSize1")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Trip Id :", tripId)
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["responseCode"] == str(6003))

        assert (response_body["responseData"]["message"] == "Page size must not be less than one")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details by given tripId/ startDate and endDate and also with
    # invalid offset(offset)
    @pytest.mark.Smoke
    def test_smryapi12_negative_assetManagement_trip_info_by_tripId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_by-tripId_invalidpageNo")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = str(dict1["pageNo"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = "$%"
        pageSize = str(dict1["pageSize"])

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        # response_body = response.json()

        # assert (response_body["responseCode"] == str(6002))
        # assert (response_body["responseData"]["message"] == "Page number must not be less than zero")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details with startDate and end Date greater than 30 days

    @pytest.mark.Smoke
    def test_smryapi14_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_by-tripId_endDategreaterthan30days")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            startDate = "06-13-2023"
            endDate = "08-17-2023"
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6004))
        assert (response_body["responseData"][
                    "message"] == "Start date and End date difference should not be greater than 30 days")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details with startDate greater than end Date format

    @pytest.mark.Smoke
    def test_smryapi15_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-info_by-tripId_startDategreaterthanendDate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            startDate = "07-13-2024"
            endDate = "06-13-2024"
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6004))
        assert (response_body["responseData"]["message"] == "End date should be greater than Start date")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details with invalid startDate  end Date format(date format should
    # be MM-DD-YYYYY)

    @pytest.mark.Smoke
    def test_smryapi16_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info_invalidstartDate_endDate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            startDate = "13-13-2023"
            endDate = "14-13-2023"
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6004))
        if (response_body["responseData"][
            "message"] == "Date should be in a valid format : MM-dd-yyyy or in Epoch milliseconds" or
                response_body["responseData"]["message"] == "Date should be in a valid format : MM-dd-yyyy"):
            print("Test case passed")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET API to fetch the trip waypoint details based on startDate and end Date, and invalid systemId
    @pytest.mark.Smoke
    def test_getway02_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints-by-systemId_invalidsystemid")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = "sys123"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(1000))
        if response_body["responseData"]["message"] == "Trip waypoint details not exist":
            print("Test case passed")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET API to fetch the trip waypoint details based on startDate and end Date, and empty systemId
    @pytest.mark.Smoke
    def test_getway03_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints-by-systemId_emptysystemid")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = ""

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6000))
        assert (response_body["responseData"]["message"] == "System Id, Start Date and End Date are mandatory")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET API to fetch the trip waypoint details based on filters with invalid startDate valid end Date,
    # and systemId
    @pytest.mark.Smoke
    def test_getway05_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints-by-systemId_invalidstartdate_enddate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = "13-13-2023"
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = "sys123"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6004))
        if (response_body["responseData"][
            "message"] == "Date should be in a valid format : MM-dd-yyyy or in Epoch milliseconds" or
                response_body["responseData"]["message"] == "Date should be in a valid format : MM-dd-yyyy"):
            print("Test case passed")

    # Validate the GET API to fetch the trip waypoint details based on filters with empty startDate valid end Date,
    # and systemId
    @pytest.mark.Smoke
    def test_getway07_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints-by-systemId_emptystartdate_validenddate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            if startDate == "None":
                startDate = ""
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = ""
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = "sys123"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6000))
        assert (response_body["responseData"]["message"] == "System Id, Start Date and End Date are mandatory")

    # Validate the GET API to fetch the trip waypoint details based on filters with valid startDate invalid end Date,
    # and valid systemId
    @pytest.mark.Smoke
    def test_getway08_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints-by-systemId_invalidendDate")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = "13-13-2023"
            systemId = "sys123"

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6004))

        assert (response_body["responseData"][
                    "message"] == "Start date and End date difference should not be greater than 1 days" or response_body["responseData"]["message"]=="Date should be in a valid format : MM-dd-yyyy")

    # Validate the for the GET API to fetch the waypoint details with invalid offset(negative value)
    @pytest.mark.Smoke
    def test_getway19_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints_by-systemId_invalidpageNo")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Trip Id :", tripId)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Parse API response into JSON
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == str(6002))
        assert (response_body["responseData"]["message"] == "Page number must not be less than zero")

    # Validate the for the GET API to fetch the waypoint details with invalid limit(0 or negative value)
    @pytest.mark.Smoke
    def test_getway20_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_trip-waypoints_by-systemId_invalidpageSize")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)
            pageNo = "0"
            pageSize = "-1"
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Trip Id :", tripId)
        print(pageNo, pageSize)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "valid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6003))

        assert (response_body["responseData"]["message"] == "Page size cannot be negative")

    # headers
    # Validate the GET api to fetch the trip summary details with invalid header api-key
    @pytest.mark.Smoke
    def test1_smryapi_17_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))

        assert (response_body["responseData"]["message"] == "api keys are not matching..please provide valid key")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details with empty header api-key
    @pytest.mark.Smoke
    def test1_smryapi_18_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)
        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

            print("Start Date : ", startDate)
            print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))

        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")

        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details without header api-key
    @pytest.mark.Smoke
    def test1_smryapi_19_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")

    # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details without header x-requestor
    @pytest.mark.Smoke
    def test1_smryapi_20_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize,
                                                         "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "x-requestor header cannot be blank")

    # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the GET api to fetch the trip summary details without header x-requestor

    @pytest.mark.Smoke
    def test1_smryapi_21_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component when null value is given to x-requestor

    @pytest.mark.Smoke
    def test1_fms002_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize,
                                                         "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "x-requestor header cannot be blank")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component when space is given to x-requestor

    @pytest.mark.Smoke
    def test1_fms003_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component without x-requestor

    @pytest.mark.Smoke
    def test1_fms004_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component when an invalid value is given to
    # api-key
    @pytest.mark.Smoke
    def test1_fms005_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component when null value is given to api-key

    @pytest.mark.Smoke
    def test1_fms006_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component when space is given to api-key

    @pytest.mark.Smoke
    def test1_fms007_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate GET API not able to fetch trip waypoint data in FMS UI API Component without api-key
    @pytest.mark.Smoke
    def test1_fms008_negative_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the for the GET API to fetch the waypoint details with invalid header api-key

    @pytest.mark.Smoke
    def test1_getway21_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the for the GET API to fetch the waypoint details with empty header api-key
    @pytest.mark.Smoke
    def test1_getway22_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            systemId = str(dict1["systemId"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # gValidate the for the GET API to fetch the waypoint details with  header api-key missing
    @pytest.mark.Smoke
    def test1_getway23_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the for the GET API to fetch the waypoint details with empty header x-requestor
    @pytest.mark.Smoke
    def test1_getway24_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the for the GET API to fetch the waypoint details with missing header x-requestor
    @pytest.mark.Smoke
    def test1_getway25_negative_assetManagement_trip_waypoints_by_systemId_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = str(dict1["systemId"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_waypoints_by_systemId_new(self, startDate, endDate, pageNo, pageSize, systemId,
                                                                  "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with invalid header api-key
    @pytest.mark.Smoke
    def test1_TC002_negative_assetManagement_latest_trip_details_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with empty header api-key
    @pytest.mark.Smoke
    def test1_TC003_negative_assetManagement_latest_trip_details_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "api keys are not matching..please provide valid key")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with without header api-key
    @pytest.mark.Smoke
    def test1_TC004_negative_assetManagement_latest_trip_details_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with empty header x-requestor
    @pytest.mark.Smoke
    def test1_TC005_negative_assetManagement_latest_trip_details_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "x-requestor header cannot be blank")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send without header x-requestor
    @pytest.mark.Smoke
    def test1_TC006_negative_assetManagement_latest_trip_details_new(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = getVIN(self, OnboardingType, chipsetType)
            status = "Completed"

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["responseCode"] == str(6106))
        assert (response_body["responseData"][
                    "message"] == "Required authentication headers are missing..!!!!")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with invalid field vin
    @pytest.mark.Smoke
    def test6_TC007_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-details_invalidvin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(

                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            assert (response_body["responseCode"] == str(6007))
            assert (response_body["responseData"]["message"] == "No data present for this filter")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with invalid systemId
    @pytest.mark.Smoke
    def test6_TC008_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-details_invalidsystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])

            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

            # Parse API response into JSON

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(

                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            assert (response_body["responseCode"] == str(6007))

            assert (response_body["responseData"]["message"] == "No data present for this filter")

    # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send with invalid field status
    @pytest.mark.Smoke
    def test6_TC013_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_latest-trip-details_invalidstatus")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

            # Validate response status code

            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            assert (response_body["responseCode"] == str(6006))
            assert (response_body["responseData"][
                        "message"] == "Invalid status. Status should be either Completed or InProgress")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send without systemId and vin (system id or vin mandatory)
    @pytest.mark.Smoke
    def test6_TC016_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_latest-trip-details_withoutsystemId_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

            vin = str(dict1["vin"])

            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "without_vin_sys")

            # Validate response status code
            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(

                response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            assert (response_body["responseCode"] == str(6005))
            assert (response_body["responseData"][
                        "message"] == "Vin and SystemId cannot be empty. Please provide atleast one value")
        # assert len(response_body["responseData"]["dataList"]) == 0

    # Validate the Post api for latest trip info send empty systemId and vin (system id or vin mandatory)

    @pytest.mark.Smoke
    def test6_TC017_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement",
                                         "AssetManagement_latest-trip-details_emptysystemId_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ""
            status = str(dict1["status"])

            print("VIN : ", vin)
            print("System Id : ", systemId)
            print("Status : ", status)

            # Call asset management reusable module
            response = assetManagement_latest_trip_details_new(self, vin, systemId, status, "valid")

            # Validate response status code

            assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(

                response.status_code)

            # Parse API response into JSON

            response_body = response.json()

            assert (response_body["responseCode"] == str(6005))
            assert (response_body["responseData"][
                        "message"] == "Vin and SystemId cannot be empty. Please provide atleast one value")
        # assert len(response_body["responseData"]["dataList"]) == 0

    @pytest.mark.Smoke
    def test6_TC018_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = ""
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = get_tridId_from_log(self)
            pageNo = ""
            pageSize = "1"

        print("Trip Id :", tripId)
        print("Page No :", pageNo)
        print("Page Size :", pageSize)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Success":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

    @pytest.mark.Smoke
    def test6_TC019_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = ""
            pageSize = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = get_tridId_from_log(self)
            pageNo = ""
            pageSize = ""

        print("Trip Id :", tripId)
        print("Page No :", pageNo)
        print("Page Size :", pageSize)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Success":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

    @pytest.mark.Smoke
    def test6_TC20_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info-by-tripId")

        if dict1['Flag'] == "Yes":

            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])
            pageNo = str(dict1["pageNo"])
            pageSize = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            tripId = get_tridId_from_log(self)
            pageNo = "0"
            pageSize = ""

        print("Trip Id :", tripId)
        print("Page No :", pageNo)
        print("Page Size :", pageSize)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_tripId_new(self, tripId, pageNo, pageSize, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Success":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

    @pytest.mark.Smoke
    def test6_TC21_negative_AssetManagement_latest_trip_details(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet

        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-waypoints-by-tripid")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            tripId = str(dict1["tripId"])

            print("Trip Id :", tripId)

            # Call asset management reusable module
            response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

            # Parse API response into JSON
            response_body = response.json()

            if response_body["responseCode"] == str(1200):
                assert True
                # self.result.set_result(TestResults.passed)
            else:
                print("response Code is not 1200. Rather found : " + str(response_body))
                # self.result.set_result(TestResults.failed)
                assert False

        else:

            print("Flag is not set to Yes, hence running with generic/actual device data")

            tripId = get_tridId_from_log(self)

            print("Trip Id :", tripId)

            time.sleep(120)

            i = 0
            while i in range(10):
                response = assetManagement_trip_waypoints_by_tripid_new(self, tripId, "valid")

                # Validate response status code
                assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                    response.status_code)

                # Parse API response into JSON
                response_body = response.json()

                if response_body["responseCode"] == str(1200):
                    assert True
                    # self.result.set_result(TestResults.passed)
                else:
                    print("response Code is not 1200. Rather found : " + str(response_body))
                    # self.result.set_result(TestResults.failed)
                    assert False

                if response_body["responseData"]['message'] == "Trip summary details not exist":
                    time.sleep(120)
                else:
                    break

            if response_body["responseData"]['message'] == "Success":
                # self.result.set_result(TestResults.passed)
                assert True
            else:
                # self.result.set_result(TestResults.failed)
                assert False

            print("----------------------------------------------------------")

    # Asset Management Trip Info
    @pytest.mark.Smoke
    def test1_positive_AssetManagement_trip_info_date(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "AssetManagement", "AssetManagement_trip-info")
        if dict1['Flag'] == "No":
            print("Flag is set to Yes, hence running with excel data :")
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            today_date = datetime.date.today()
            new_today_date = today_date.strftime("%m-%d-%Y")
            startDate = new_today_date
            endDate = new_today_date
            pageNo = str(dict1["pageNo"])
            pageSize = str(dict1["pageSize"])

        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call asset management reusable module
        response = assetManagement_trip_info_by_date_new(self, startDate, endDate, pageNo, pageSize, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseData"]["message"] == "Success")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

        print("----------------------------------------------------------")
