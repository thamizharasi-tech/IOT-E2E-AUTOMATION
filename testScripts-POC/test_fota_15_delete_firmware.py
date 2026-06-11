from datetime import datetime, timezone

import pytest

from C2CModules.fota_api_modules import FOTA_createSchedule, get_ScriptId_from_ScriptDetails_api, \
    FOTA_deleteFirmware, get_firmId_from_firmwareDetails_api
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


# ---------------------------------------------------------
# FOTA-delete firmware negative test scripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_delete_firmware(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(14000):
            if response_body["responseData"]["message"] == "success" or response_body["responseData"][
                "message"] == "Success":
                assert True
                testResult(self, "passed", "Firmware should be deleted/removed successfully",
                           "Firmware is deleted/removed successfully")

        elif response_body["responseCode"] != str(14000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Firmware should be deleted/removed successfully",
                       "Firmware is not deleted/removed successfully" + " Reason for failure is : " +
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
    def test1_negative_fota_delete_firmware_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "invalid_apiKey")

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
    def test1_negative_fota_delete_firmware_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "empty_apiKey")

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
    def test1_negative_fota_delete_firmware_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "no_apiKey")

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
    def test1_negative_fota_delete_firmware_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "empty_x-requestor")

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
    def test1_negative_fota_delete_firmware_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = get_firmId_from_firmwareDetails_api(self)

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "no_x-requestor")

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
    # invalid firmId
    @pytest.mark.Smoke
    def test1_negative_fota_deleteFirmware_invalid_firmId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware_invalid_firmId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = str(dict1["packageId"])
        else:
            firmId = "firmId123"

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["Response Code"] == str(14122) or response_body["Response Message"] == (
        "Input parameter is invalid"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # firmId doesnot exists
    @pytest.mark.Smoke
    def test1_negative_fota_deleteFirmware_incorrect_firmId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware_invalid_firmId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = "876982734"
        else:
            firmId = "0976123"

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Verify response body
        if response_body["responseCode"] == str(14024) or response_body["responseData"]["message"] == (
                "No firmware package available"):
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    # empty firmId
    @pytest.mark.Smoke
    def test1_negative_deleteFirmware_empty_firmId(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-DeleteFirmware")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            firmId = ""
        else:
            firmId = ""

        print("Firmware Id. : => ", firmId)

        # Call api reusable model
        response = FOTA_deleteFirmware(self, firmId, "invalid")

        # Validate response status code
        if response.status_code == 405:
            assert True
        else:
            print("Status code is not 405. Rather found : " + str(response.status_code))
            assert False
        print("----------------------------------------------------------")
