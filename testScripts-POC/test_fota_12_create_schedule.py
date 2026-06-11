from datetime import datetime, timezone

import pytest

from C2CModules.fota_api_modules import FOTA_createSchedule, get_ScriptId_from_ScriptDetails_api
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


# ---------------------------------------------------------
# FOTA-create script negative testscripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_create_schedule(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(14000):
            if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                "message"] == "Success":
                scheduleId = str(response_body["responseData"]["scheduleId"])
                print("Schedule Id :", scheduleId)
                testResult(self, "passed", "Firmware should be scheduled successfully and campaign should started ",
                           "Firmware scheduled successfully OR Campaign is started ")

        elif response_body["responseCode"] != str(14000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Firmware should be scheduled successfully and campaign should started ",
                       "Firmware is not scheduled successfully OR Campaign is not started  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------------------
    # FOTA-create schedule API : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key"

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing"

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid vin-contain special char
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_vin_withSplChar(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_vin_withSpecialChar")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = "VINQCOMIVI000184%"
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14065) or response_body["responseData"]["message"] == ("Vin contains "
                                                                                                       "special "
                                                                                                       "characters"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # invalid vin-lessthan 17 char
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_vin_lessthan17char(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_vin_lessthan17Char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = "VINQCOMIVI000184"
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14002) or response_body["responseData"]["message"] == (
                "vin must be 17 chars long"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # invalid vin-greaterthan 17 char
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_vin_greaterthan17char(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_vin_greaterthan17Char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = "VINQCOMIVI00018481"
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14002) or response_body["responseData"]["message"] == (
                "vin must be 17 chars long"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty vin
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_vin(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = ""
            scriptId = str(dict1["scriptId"])
        else:
            vin = ""
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14065) or response_body["responseData"]["message"] == (
                "Vin contains special characters"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")


    # no vin
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_vin(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = ""
            scriptId = str(dict1["scriptId"])
        else:
            vin = ""
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_vin")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14056) or response_body["responseData"]["message"] == (
                "Vins cannot be null"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # invalid scriptId
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_scriptId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = "3721632745"

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14099) or response_body["responseData"]["message"] == ("Script not found"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

     # empty scriptId
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = ""
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = ""

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14094) or response_body["responseData"]["message"] == (
                "Script Id Cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # no scriptId
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_scriptId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = ""

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_scriptId")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14094) or response_body["responseData"]["message"] == (
                "Script Id Cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")


    # invalid startDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_startDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_startDate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = "3848327483"
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14103) or response_body["responseData"]["message"] == ("Start date must be a current or future date"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # invalid startDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_incorrect_startDateformat(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        startDate = str(startDate) + "rt"
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty startDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_startDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = ""
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14095) or response_body["responseData"]["message"] == (
                "Start date cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # no startDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_startDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin =getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_startDate")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14095) or response_body["responseData"]["message"] == (
                "Start date cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")






    # invalid endDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_invalid_endDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule_invalid_endDate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = "3848327483"

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14100) or response_body["responseData"]["message"] == ("End date must be atleast 12 hour ahead of start date"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # invalid endDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_incorrect_endDateformat(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType, chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
        endDate = str(endDate) + "rt"

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty endDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_empty_endDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin = getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = ""

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14096) or response_body["responseData"]["message"] == (
                "End date cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # no endDate
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_endDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin =getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_endDate")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14096) or response_body["responseData"]["message"] == (
                "End date cannot be empty"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")


   # start & end date smae
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_same_startDate_endDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin =getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14100) or response_body["responseData"]["message"] == (
                "End date must be atleast 12 hour ahead of start date"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")


   # start greater than end date smae
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_same_startDate_endDate(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin =getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14100) or response_body["responseData"]["message"] == (
                "End date must be atleast 12 hour ahead of start date"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")



   # no period
    @pytest.mark.Smoke
    def test1_negative_fota_create_schedule_no_period(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            scriptId = str(dict1["scriptId"])
        else:
            vin =getVIN(self, OnboardingType,chipsetType)
            scriptId = get_ScriptId_from_ScriptDetails_api(self)

        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        print("VIN No. : => ", vin)
        print("Script Id : => ", scriptId)
        print("Start Date : ", startDate)
        print("End Date : ", endDate)

        # Call api reusable model
        response = FOTA_createSchedule(self, vin, scriptId, startDate, endDate, "no_period")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14057) or response_body["responseData"]["message"] == (
                "Period cannot be null"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

