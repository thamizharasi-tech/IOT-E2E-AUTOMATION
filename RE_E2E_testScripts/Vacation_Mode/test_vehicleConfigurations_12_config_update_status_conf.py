import pytest
import random
import json
import time

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.vehicle_configurations import *
from C2CModules.primary_IVI_device_modules import *
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult
from C2CModules.api_modules import verify_api_response_for_invalid_header


OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
global model, version, RegionalAPNEndpoints

class Test_ConfigurationUpdateTracking_Negative:

    @pytest.mark.Smoke
    def test12a_negative_VehicleConfiguration_configurationUpdateTracking_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read tracking Id from VehicleConfiguration_updateConfiguration api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        trackingId = json_object["trackingId"]
        if trackingId == "" or trackingId == "NA":
            trackingId = "efe83b3e-bdeb-41ce-b2bc-99e5897fea95"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "invalid_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Configuration update status API should throw appropriate error message for invalid apikey.",
                   "Configuration update status API showing/throwing appropriate error message for invalid apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12b_negative_VehicleConfiguration_configurationUpdateTracking_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read tracking Id from VehicleConfiguration_updateConfiguration api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        trackingId = json_object["trackingId"]
        if trackingId == "" or trackingId == "NA":
            trackingId = "efe83b3e-bdeb-41ce-b2bc-99e5897fea95"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "empty_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Configuration update status API should throw appropriate error message for empty apikey.",
                   "Configuration update status API showing/throwing appropriate error message for empty apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12c_negative_VehicleConfiguration_configurationUpdateTracking_no_apikey(self):
        print("----------------------------------------------------------")

        # Read tracking Id from VehicleConfiguration_updateConfiguration api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        trackingId = json_object["trackingId"]
        if trackingId == "" or trackingId == "NA":
            trackingId = "efe83b3e-bdeb-41ce-b2bc-99e5897fea95"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "no_apiKey")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Configuration update status API should throw appropriate error message for no apikey.",
                   "Configuration update status API showing/throwing appropriate error message for no apikey.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12d_negative_VehicleConfiguration_configurationUpdateTracking_empty_xrequestor(self):
        print("----------------------------------------------------------")

        # Read tracking Id from VehicleConfiguration_updateConfiguration api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        trackingId = json_object["trackingId"]
        if trackingId == "" or trackingId == "NA":
            trackingId = "efe83b3e-bdeb-41ce-b2bc-99e5897fea95"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "empty_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Configuration update status API should throw appropriate error message for empty x-requestor.",
                   "Configuration update status API showing/throwing appropriate error message for empty x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12e_negative_VehicleConfiguration_configurationUpdateTracking_no_xrequestor(self):
        print("----------------------------------------------------------")

        # Read tracking Id from VehicleConfiguration_updateConfiguration api resp from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "VehicleConfiguration_updateConfiguration")
        api_resp = str(dict1["Actual API Response"])
        # print(api_resp)
        json_object = json.loads(api_resp)
        trackingId = json_object["trackingId"]
        if trackingId == "" or trackingId == "NA":
            trackingId = "efe83b3e-bdeb-41ce-b2bc-99e5897fea95"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "no_x-requestor")

        # Parse API response into JSON
        response_body = response.json()

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Configuration update status API should throw appropriate error message for no x-requestor.",
                   "Configuration update status API showing/throwing appropriate error message for no x-requestor.")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12f_negative_VehicleConfiguration_configurationUpdateTracking_invalid_trackingId(self):
        print("----------------------------------------------------------")

        trackingId = "xyz"

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code == 400:
            assert True
        else:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "16023" and response_body["errors"][0]["message"] == "Tracking Id does not exists.":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12g_negative_VehicleConfiguration_configurationUpdateTracking_empty_trackingId(self):
        print("----------------------------------------------------------")

        trackingId = ""

        print('Tracking Id : ', trackingId)

        # Verify command & control response
        response = vehicleConfigurations_configurationUpdateTracking(self, trackingId, "valid")

        if response.status_code == 404:
            assert True
        else:
            assert False

        print("----------------------------------------------------------")
