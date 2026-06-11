import pytest

from C2CModules.sota_api_modules import get_ScheduledId_from_ScheduleDetails_api, SOTA_deleteSchedule
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


# ---------------------------------------------------------
# FOTA-delete firmware negative test scripts
# ---------------------------------------------------------


class Test_positive:

    @pytest.mark.Smoke
    def test1_positive_sota_delete_schedule(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15000):
            if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                "message"] == "Success":
                assert True
                testResult(self, "passed", "Schedule should be deleted/removed successfully",
                           "Schedule is deleted/removed successfully")

        elif response_body["responseCode"] != str(15000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Schedule should be deleted/removed successfully",
                       "Schedule is not deleted/removed successfully" + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
        print("----------------------------------------------------------")


class Test_negative:
    # ---------------------------------------------------------------------------------------
    # FOTA-firmware delete API : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_delete_schedule_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "invalid_apiKey")

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
    def test1_negative_sota_delete_schedule_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "empty_apiKey")

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
    def test1_negative_sota_delete_schedule_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "no_apiKey")

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
    def test1_negative_sota_delete_schedule_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "empty_x-requestor")

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
    def test1_negative_sota_delete_schedule_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "no_x-requestor")

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
    # invalid scheduleId
    @pytest.mark.Smoke
    def test1_negative_sota_deleteFirmware_invalid_scheduleId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule_invalid_scheduleId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
        else:
            scheduleId = "scheduleId123"

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(15041) or response_body["responseData"]["message"] == (
        "schedule not found"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # scheduleId doesnot exists
    @pytest.mark.Smoke
    def test1_negative_sota_deleteFirmware_incorrect_scheduleId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule_invalid_scheduleId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = "876982734"
        else:
            scheduleId = "0976123"

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(15041) or response_body["responseData"]["message"] == (
                "schedule not found"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty scheduleId
    @pytest.mark.Smoke
    def test1_negative_deleteFirmware_empty_scheduleId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-DeleteSchedule")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = ""
        else:
            scheduleId = ""

        print("Schedule Id : => ", scheduleId)

        # Call api reusable model
        response = SOTA_deleteSchedule(self, scheduleId, "invalid")

        # Validate response status code
        if response.status_code == 405:
            assert True
        else:
            print("Status code is not 405. Rather found : " + str(response.status_code))
            assert False


        print("----------------------------------------------------------")
