import random

import pytest

from C2CModules.COTA_modules import COTA_liveCommandTracking_getCurrentFrequency, \
    COTA_telemetry_getCotaDetails_by_requestId, COTA_command_request, COTA_telemetry_request, \
    COTA_telemetry_getCurrentState, COTA_command_getCurrentState, COTA_command_getCotaDetails_by_requestId
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


# COTA - COTA_liveCommandTracking_getCurrentFrequency
class Test_COTA_getCurrentFrequency:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_COTA_liveCommandTracking_getCurrentFrequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Data fetched successfully'):

            print("Live Tracking", response_body["responseData"]["liveTracking"])
            print("Current Frequency", response_body["responseData"]["currentFrequency"])

            testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                       "Successfully fetched the current values/data for desired System Id ")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != str('Data fetched successfully'):

            testResult(self, "failed", "Should fetch the current data/values for System id successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_COTA_liveCommandTracking_getCurrentFrequency_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key":
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty api key
    @pytest.mark.Smoke
    def test2_negative_COTA_liveCommandTracking_getCurrentFrequency_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key":
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no api key
    @pytest.mark.Smoke
    def test3_negative_COTA_liveCommandTracking_getCurrentFrequency_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_COTA_liveCommandTracking_getCurrentFrequency_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no x-requestor
    @pytest.mark.Smoke
    def test5_negative_COTA_liveCommandTracking_getCurrentFrequency_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with invalid system id
    @pytest.mark.Smoke
    def test6_negative_COTA_liveCommandTracking_getCurrentFrequency_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        # Call COTA reusable module
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "invalid")

        # Validate response status code
        assert (
                response.status_code == 400 or response.status_code == 403 or response.status_code == 404), "Status code is not 400/403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response.status_code == 400:
            if response_body["errors"][0]["errorCode"] == str(14508):
                if response_body["errors"][0]["message"] == str('System Id should be 23 characters long'):
                    testResult(self, "passed", "Should throw proper error for invalid System Id",
                               "Showing proper error code & message for invalid System Id")
                    # self.result.set_result(TestResults.passed)

            elif response_body["message"] == str('Data fetched successfully'):

                testResult(self, "failed", "Should throw proper error for invalid System Id",
                           "Not showing proper error code & message for invalid System Id")
                # self.result.set_result(TestResults.failed)
                assert False

        elif response.status_code == 403 or response.status_code == 404:
            testResult(self, "passed", "Should throw proper error for invalid System Id",
                       "Showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.passed)

        else:
            testResult(self, "failed", "Should throw proper error for invalid System Id",
                       "Not showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty system id
    @pytest.mark.Smoke
    def test7_negative_COTA_liveCommandTracking_getCurrentFrequency_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_liveCommandTracking_getCurrentFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""

        # Call COTA reusable module
        response_body = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "invalid")

        # Validate response status code

        assert (response_body.status_code == 404), "Status code is not 404. Rather found : " + str(
            response_body.status_code)


# COTA - COTA_command_request
class Test_cotaRequest_command_post:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_cota_command_request(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response_body = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                             postcondition, condition_handler,
                                             command_handler, timeout, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Success'):

            print("Request Id : ", response_body["responseData"]["requestId"])

            testResult(self, "passed", " Should send command context control data message to device successfully",
                       "Command context control data message is sent to device successfully")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] == str('Data fetched successfully'):

            testResult(self, "failed", "Should send command context control data message to device successfully",
                       "Failed to send command context control data message to device " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_cota_command_request_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty api key
    @pytest.mark.Smoke
    def test2_negative_cota_command_request_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no api key
    @pytest.mark.Smoke
    def test3_negative_command_request_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_command_request_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no x-requestor
    @pytest.mark.Smoke
    def test5_negative_command_request_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with invalid system id
    @pytest.mark.Smoke
    def test6_negative_command_request_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid")

        print(response.status_code)
        # Validate response status code
        assert (
                response.status_code == 400 or response.status_code == 403 or response.status_code == 404), "Status code is not 400/403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response.status_code == 400:
            if response_body["errorCode"] == str(14552):
                if response_body["message"] == str('The length of system id must be 23 characters'):
                    testResult(self, "passed", "Should throw proper error for invalid System Id",
                               "Showing proper error code & message for invalid System Id")
                    # self.result.set_result(TestResults.passed)

            elif response_body["errorCode"] != str(14552):

                testResult(self, "failed", "Should throw proper error for invalid System Id",
                           "Not showing proper error code & message for invalid System Id")
                # self.result.set_result(TestResults.failed)
                assert False

        elif response.status_code == 403 or response.status_code == 404:
            testResult(self, "passed", "Should throw proper error for invalid System Id",
                       "Showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error for invalid System Id",
                       "Not showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty system id
    @pytest.mark.Smoke
    def test7_negative_command_request_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid")

        # Validate response status code

        # print(response_body.status_code)
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        response_body = response.json()

        if response_body["status"] == 404:
            if response_body["error"] == str('Not Found'):
                testResult(self, "passed", "Should throw proper error for empty System Id",
                           "Showing proper error code & message for empty System Id")
                # self.result.set_result(TestResults.passed)

        elif response_body["status"] != 404:

            testResult(self, "failed", "Should throw proper error for empty System Id",
                       "Not showing proper error code & message for empty System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # Not valid Test cases

    # COTA_live command tracking with invalid command name
    @pytest.mark.skip
    def test8_negative_command_request_invalid_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "^%&"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid")

        # print(response.status_code)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14500) and response_body["message"] == str('Invalid Name'):
            testResult(self, "passed", "Should throw proper error for invalid name",
                       "Showing proper error code & message for invalid command name")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14500):

            testResult(self, "failed", "Should throw proper error for invalid name",
                       "Not showing proper error code & message for invalid name")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for invalid name",
                       "Not showing proper error code & message for invalid name")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty command name
    @pytest.mark.skip
    def test9_negative_command_request_empty_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = ""
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = ""
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid")

        # print(response.status_code)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14501) and response_body["message"] == str('commandName can not be empty'):
            testResult(self, "passed", "Should throw proper error for empty command name",
                       "Showing proper error code & message for empty command name")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14501):

            testResult(self, "failed", "Should throw proper error for empty command name",
                       "Not showing proper error code & message for empty command name")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for empty command name",
                       "Not showing proper error code & message for empty command name")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking without command name
    @pytest.mark.skip
    def test10_negative_command_request_no_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "no_name")

        # print(response.status_code)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14501) and response_body["message"] == str('commandName can not be empty'):
            testResult(self, "passed", "Should throw proper error for without command name parameter",
                       "Showing proper error code & message for without command name parameter")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14501):

            testResult(self, "failed", "Should throw proper error for without command name parameter",
                       "Not showing proper error code & message for without command name parameter")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for without command name parameter",
                       "Not showing proper error code & message for without command name parameter")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid frequency
    @pytest.mark.skip
    def test11_negative_command_request_enable_false(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = "false"
            operation = str(dict1["operation"])
            ccid = str(dict1["ccid"])
            name = str(dict1["name"])
            precondition = str(dict1["precondition"])
            postcondition = str(dict1["postcondition"])
            condition_handler = str(dict1["condition_handler"])
            command_handler = str(dict1["command_handler"])
            timeout = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "false"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"

        # Call COTA reusable module
        response = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                        postcondition, condition_handler,
                                        command_handler, timeout, "invalid")

        print(response.status_code)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Validate response status code

        if response.status_code == 400:
            testResult(self, "passed", "Should throw proper error for invalid frequency",
                       "Showing proper error code & message for invalid frequency")
            # self.result.set_result(TestResults.passed)

        elif response.status_code != 400:

            testResult(self, "failed", "Should throw proper error for invalid frequency",
                       "Not showing proper error code & message for invalid frequency")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for invalid frequency",
                       "Not showing proper error code & message for invalid frequency")
            # self.result.set_result(TestResults.failed)
            assert False


class Test_command_getCotaDetails_by_requestId:

    # COTA_command_getCotaDetails_by_requestId(
    @pytest.mark.Smoke
    def test1_positive_COTA_command_getCotaDetails_by_requestId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            print("Flag is set to No, hence running with device data:")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            ccid = "2501"
            name = "IGNITION"
            precondition = "0"
            postcondition = "0"
            condition_handler = "0"
            command_handler = "0"
            timeout = "0"
            requestId = ""

            # Call COTA reusable module
            response_body = COTA_command_request(self, systemId, enable, operation, ccid, name, precondition,
                                                 postcondition, condition_handler,
                                                 command_handler, timeout, "valid")

            # Validate response status code

            assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
                response_body.status_code)

            # Parse API response into JSON
            response_body = response_body.json()

            if response_body["message"] == str('Success'):
                requestId = response_body["responseData"]["requestId"]

        # Call COTA reusable module
        response_body = COTA_command_getCotaDetails_by_requestId(self, requestId, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        # Verify cota details
        if response_body["message"] == "SUCCESS":
            data_len = len(response_body["responseData"])
            if data_len >= 1:
                createdBy = response_body["responseData"][0]["createdBy"]
                createdTime = response_body["responseData"][0]["createdTime"]
                updatedBy = response_body["responseData"][0]["updatedBy"]
                updatedTime = response_body["responseData"][0]["updatedTime"]
                transId = response_body["responseData"][0]["transId"]
                requestId = response_body["responseData"][0]["requestId"]
                systemId = response_body["responseData"][0]["systemId"]
                thresholdId = response_body["responseData"][0]["thresholdId"]

                print(" Created By : ", createdBy)
                print(" Created Time : ", createdTime)
                print(" Updated By : ", updatedBy)
                print(" Updated time : ", updatedTime)
                print(" Trans Id : ", transId)
                print(" Request Id : ", requestId)
                print(" System Id : ", systemId)
                print(" Threshold Id : ", thresholdId)

            testResult(self, "passed",
                       "Command should be initiated and fetch the cotaDetails by requestId successfully",
                       "Command is initiated and also fetched the cotaDetails by requestId successfully")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Command should be initiated and fetch the cotaDetails by requestId successfully",
                       "Command is not initiated or COTA details not fetched successfully")

            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_negative_COTA_command_getCotaDetails_by_invalid_requestId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId_invalid_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "fgtd-64747"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "invalid")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into json
        response_body = response.json()

        # Verify cota details
        if response_body["message"] == "Given requestId is not a UUID":

            testResult(self, "passed",
                       "Should throw proper error code and message for invalid request id",
                       "Showing proper error code and message for invalid request id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Should throw proper error code and message for invalid request id",
                       "Not showing proper error code and message for invalid request id")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_negative_COTA_command_getCotaDetails_with_empty_requestId(self):

        # API Operation to get command cota Details by requestId
        response = COTA_command_getCotaDetails_by_requestId(self, "", "invalid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        # Parse API response into json
        response_body = response.json()

        # Verify cota details
        if response_body["error"] == "Not Found":
            testResult(self, "passed",
                       "Should throw proper error code and message for empty request id",
                       "Showing proper error code and message for empty request id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Should throw proper error code and message for empty request id",
                       "Not showing proper error code and message for empty request id")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_negative_COTA_command_getCotaDetails_by_requestId_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key":
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_COTA_command_getCotaDetails_by_requestId_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key":
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_COTA_command_getCotaDetails_by_requestId_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_COTA_command_getCotaDetails_by_requestId_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_negative_COTA_command_getCotaDetails_by_requestId_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_command_getCotaDetails_by_requestId(self, requestId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


# COTA - command_getCurrentState
class Test_COTA_command_getCurrentState:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_cota_command_getCurrentState(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response_body = COTA_command_getCurrentState(self, systemId, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Success'):

            data_len = len(response_body["responseData"])
            if data_len >= 1:
                datalen = len(response_body["responseData"][0]["currentsState"]["config"])
                if datalen >= 1:
                    print("ccid : ", response_body["responseData"][0]["currentsState"]["config"][0]["ccid"])
                    print("Name : ", response_body["responseData"][0]["currentsState"]["config"][0]["name"])
                    print("Enable : ", response_body["responseData"][0]["currentsState"]["config"][0]["enable"])
                    print("Status : ", response_body["responseData"][0]["currentsState"]["config"][0]["status"])

                    testResult(self, "passed", " Should get current value details successfully",
                               "Current value details are fetched successfully")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Current State list/array is empty")
            else:
                print("COTA Configuration list/array is empty")

        elif response_body["message"] != str('Success'):

            testResult(self, "failed", "Should get current value details successfully",
                       "Failed to fetch current value details " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_cota_command_getCurrentState_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty api key
    @pytest.mark.Smoke
    def test2_negative_cota_command_getCurrentState_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no api key
    @pytest.mark.Smoke
    def test3_negative_command_getCurrentState_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_command_getCurrentState_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no x-requestor
    @pytest.mark.Smoke
    def test5_negative_command_getCurrentState_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with invalid system id
    @pytest.mark.Smoke
    def test6_negative_command_getCurrentState_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_command_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "invalid")

        print(response.status_code)
        # Validate response status code
        assert (
                response.status_code == 400 or response.status_code == 403 or response.status_code == 404), "Status code is not 400/403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response.status_code == 400:
            if response_body["errorCode"] == str(14552):
                if response_body["message"] == str('The length of system id must be 23 characters'):
                    testResult(self, "passed", "Should throw proper error for invalid System Id",
                               "Showing proper error code & message for invalid System Id")
                    # self.result.set_result(TestResults.passed)

            elif response_body["errorCode"] != str(14552):

                testResult(self, "failed", "Should throw proper error for invalid System Id",
                           "Not showing proper error code & message for invalid System Id")
                # self.result.set_result(TestResults.failed)
                assert False

        elif response.status_code == 403 or response.status_code == 404:
            testResult(self, "passed", "Should throw proper error for invalid System Id",
                       "Showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error for invalid System Id",
                       "Not showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty system id
    @pytest.mark.Smoke
    def test7_negative_command_getCurrentState_empty_systemId(self):
        systemId = ""

        # Call COTA reusable module
        response = COTA_command_getCurrentState(self, systemId, "invalid")

        # Validate response status code

        # print(response_body.status_code)
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        response_body = response.json()

        if response_body["status"] == 404:
            if response_body["error"] == str('Not Found'):
                testResult(self, "passed", "Should throw proper error for empty System Id",
                           "Showing proper error code & message for empty System Id")
                # self.result.set_result(TestResults.passed)

        elif response_body["status"] != 404:

            testResult(self, "failed", "Should throw proper error for empty System Id",
                       "Not showing proper error code & message for empty System Id")
            # self.result.set_result(TestResults.failed)
            assert False


# COTA - COTA_telemetry_request
class Test_cotaRequest_telemetry_post:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_cota_telemetry_request(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response_body = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                               enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                               timeout1, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Success'):

            print("Request Id : ", response_body["responseData"]["requestId"])

            testResult(self, "passed", " Should send context control the sensor data message to device successfully",
                       "Context control the sensor data message is sent to device successfully")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] == str('Data fetched successfully'):

            testResult(self, "failed", "Should send context control the sensor data message to device successfully",
                       "Failed to send context control the sensor data message to device " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_cota_telemetry_request_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty api key
    @pytest.mark.Smoke
    def test2_negative_cota_telemetry_request_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no api key
    @pytest.mark.Smoke
    def test3_negative_command_telemetry_request_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_telemetry_request_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no x-requestor
    @pytest.mark.Smoke
    def test5_negative_telemetry_request_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with invalid system id
    @pytest.mark.Smoke
    def test6_negative_telemetry_request_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "invalid")

        print(response.status_code)
        # Validate response status code
        assert (
                response.status_code == 400 or response.status_code == 403 or response.status_code == 404), "Status code is not 400/403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response.status_code == 400:
            if response_body["errorCode"] == str(14552):
                if response_body["message"] == str('The length of system id must be 23 characters'):
                    testResult(self, "passed", "Should throw proper error for invalid System Id",
                               "Showing proper error code & message for invalid System Id")
                    # self.result.set_result(TestResults.passed)

            elif response_body["errorCode"] != str(14552):

                testResult(self, "failed", "Should throw proper error for invalid System Id",
                           "Not showing proper error code & message for invalid System Id")
                # self.result.set_result(TestResults.failed)
                assert False

        elif response.status_code == 403 or response.status_code == 404:
            testResult(self, "passed", "Should throw proper error for invalid System Id",
                       "Showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error for invalid System Id",
                       "Not showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty system id
    @pytest.mark.Smoke
    def test7_negative_telemetry_request_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_request")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
            enable = str(dict1["enable"])
            operation = str(dict1["operation"])
            buffer = str(dict1["buffer"])
            count = str(dict1["count"])
            block_id = str(dict1["block_id"])
            reason_code = str(dict1["reason_code"])
            frequency = str(dict1["frequency"])
            data_items = str(dict1["data_items"])
            filter_plugins = str(dict1["filter_plugins"])
            msg_type = str(dict1["msg_type"])
            buffer1 = str(dict1["buffer"])
            count1 = str(dict1["count"])
            timeout = str(dict1["timeout"])
            timeout1 = str(dict1["timeout"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

        # Call COTA reusable module
        response = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                          enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                          timeout1, "invalid")

        # Validate response status code

        # print(response_body.status_code)
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        response_body = response.json()

        if response_body["status"] == 404:
            if response_body["error"] == str('Not Found'):
                testResult(self, "passed", "Should throw proper error for empty System Id",
                           "Showing proper error code & message for empty System Id")
                # self.result.set_result(TestResults.passed)

        elif response_body["status"] != 404:

            testResult(self, "failed", "Should throw proper error for empty System Id",
                       "Not showing proper error code & message for empty System Id")
            # self.result.set_result(TestResults.failed)
            assert False


class Test_telemetry_getCotaDetails_by_requestId:

    # COTA_telemetry_getCotaDetails_by_requestId(
    @pytest.mark.Smoke
    def test1_positive_COTA_telemetry_getCotaDetails_by_requestId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = ""
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            enable = "true"
            operation = "0"
            buffer = buffer1 = "0"
            count = count1 = "0"
            block_id = "0"
            reason_code = "0"
            frequency = "0"
            data_items = "0"
            timeout = timeout1 = "0"
            filter_plugins = "0"
            msg_type = "0"

            # Call COTA reusable module
            response_body = COTA_telemetry_getCurrentState(self, systemId, "valid")

            # Validate response status code

            assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
                response_body.status_code)

            # Parse API response into JSON
            response_body = response_body.json()

            if response_body["message"] == str('Success'):

                data_len = len(response_body["responseData"])
                if data_len >= 1:
                    datalen = len(response_body["responseData"][0]["currentsState"]["config"])
                    if datalen >= 1:
                        block_id = response_body["responseData"][0]["currentsState"]["config"][0]["block_id"]
                        reason_code = response_body["responseData"][0]["currentsState"]["config"][0]["reason_code"]

            # Call COTA reusable module
            response_body = COTA_telemetry_request(self, systemId, buffer, count, timeout, operation, block_id, reason_code,
                                               enable, frequency, data_items, filter_plugins, msg_type, buffer1, count1,
                                               timeout1, "valid")

            # Validate response status code

            assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
                response_body.status_code)

            # Parse API response into JSON
            response_body = response_body.json()

            if response_body["message"] == str('Success'):
                requestId = response_body["responseData"]["requestId"]

            print("Request Id : ", requestId)

        # Call COTA reusable module
        response_body = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        # Verify cota details
        if response_body["message"] == "SUCCESS":
            data_len = len(response_body["response"]["responseData"])
            if data_len >= 1:
                createdBy = response_body["response"]["responseData"][0]["createdBy"]
                createdTime = response_body["response"]["responseData"][0]["createdTime"]
                updatedBy = response_body["response"]["responseData"][0]["updatedBy"]
                updatedTime = response_body["response"]["responseData"][0]["updatedTime"]
                transId = response_body["response"]["responseData"][0]["transId"]
                requestId = response_body["response"]["responseData"][0]["requestId"]
                systemId = response_body["response"]["responseData"][0]["systemId"]
                thresholdId = response_body["response"]["responseData"][0]["thresholdId"]

                print(" Created By : ", createdBy)
                print(" Created Time : ", createdTime)
                print(" Updated By : ", updatedBy)
                print(" Updated time : ", updatedTime)
                print(" Trans Id : ", transId)
                print(" Request Id : ", requestId)
                print(" System Id : ", systemId)
                print(" Threshold Id : ", thresholdId)

            testResult(self, "passed",
                       "Command should be initiated and fetch the cotaDetails by requestId successfully",
                       "Command is initiated and also fetched the cotaDetails by requestId successfully")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Command should be initiated and fetch the cotaDetails by requestId successfully",
                       "Command is not initiated or COTA details not fetched successfully")

            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_negative_COTA_telemetry_getCotaDetails_by_invalid_requestId(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId_invalid_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "fgtd-64747"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into json
        response_body = response.json()

        # Verify cota details
        if response_body["errors"][0]["errorCode"] == "14511" and response_body["errors"][0]["message"] == "Given requestId is not a UUID":

            testResult(self, "passed",
                       "Should throw proper error code and message for invalid request id",
                       "Showing proper error code and message for invalid request id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Should throw proper error code and message for invalid request id",
                       "Not showing proper error code and message for invalid request id")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_negative_COTA_telemetry_getCotaDetails_with_empty_requestId(self):

        # API Operation to get command cota Details by requestId
        response = COTA_telemetry_getCotaDetails_by_requestId(self, "", "invalid")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into json
        response_body = response.json()

        # Verify cota details
        if response_body["message"] == "Missing Authentication Token":
            testResult(self, "passed",
                       "Should throw proper error code and message for empty request id",
                       "Showing proper error code and message for empty request id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Should throw proper error code and message for empty request id",
                       "Not showing proper error code and message for empty request id")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_negative_COTA_telemetry_getCotaDetails_by_requestId_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key":
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_COTA_telemetry_getCotaDetails_by_requestId_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "api keys are not matching..please provide valid key" or response_body["message"] == response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_COTA_telemetry_getCotaDetails_by_requestId_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_COTA_telemetry_getCotaDetails_by_requestId_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank" or response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_negative_COTA_telemetry_getCotaDetails_by_requestId_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCotaDetails_by_requestId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            requestId = str(dict1["requestId"])
        else:
            requestId = "51e704ec-98d2-4f6e-9547-1f8781b00387"

        # Call COTA reusable module
        response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Required authentication headers are missing..!!!!":
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


# COTA - telemetry_getCurrentState
class Test_COTA_telemetry_getCurrentState:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_cota_telemetry_getCurrentState(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response_body = COTA_telemetry_getCurrentState(self, systemId, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Success'):

            data_len = len(response_body["responseData"])
            if data_len >= 1:
                datalen = len(response_body["responseData"][0]["currentsState"]["config"])
                if datalen >= 1:
                    print("Block Id : ", response_body["responseData"][0]["currentsState"]["config"][0]["block_id"])
                    print("Reason Code : ",
                          response_body["responseData"][0]["currentsState"]["config"][0]["reason_code"])
                    print("Enable : ", response_body["responseData"][0]["currentsState"]["config"][0]["enable"])
                    print("Frequency : ", response_body["responseData"][0]["currentsState"]["config"][0]["frequency"])

                    testResult(self, "passed", " Should get current value details successfully",
                               "Current value details are fetched successfully")
                    # self.result.set_result(TestResults.passed)
                else:
                    print("Current State list/array is empty")
            else:
                print("COTA Configuration list/array is empty")

        elif response_body["message"] != str('Success'):

            testResult(self, "failed", "Should get current value details successfully",
                       "Failed to fetch current value details " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_cota_telemetry_getCurrentState_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for invalid api key",
                       "Showing proper error for invalid api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for invalid api key",
                       "Not showing proper response code & error for invalid api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty api key
    @pytest.mark.Smoke
    def test2_negative_cota_telemetry_getCurrentState_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for empty api key",
                       "Showing proper error for empty api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty api key",
                       "Not showing proper response code & error for empty api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no api key
    @pytest.mark.Smoke
    def test3_negative_telemetry_getCurrentState_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no api key",
                       "Showing proper error for no api key")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no api key",
                       "Not showing proper response code & error for no api key")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_telemetry_getCurrentState_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "x-requestor header cannot be blank":
            testResult(self, "passed", "Should throw proper error for empty x-requestor",
                       "Showing proper error for empty x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for empty x-requestor",
                       "Not showing proper response code & error for empty x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with no x-requestor
    @pytest.mark.Smoke
    def test5_negative_telemetry_getCurrentState_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error for no x-requestor",
                       "Showing proper error for no x-requestor")
            # self.result.set_result(TestResults.passed)
        else:

            testResult(self, "failed", "Should throw proper error for no x-requestor",
                       "Not showing proper response code & error for no x-requestor")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # COTA_live command tracking with invalid system id
    @pytest.mark.Smoke
    def test6_negative_telemetry_getCurrentState_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "COTA_telemetry_getCurrentState")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "invalid")

        print(response.status_code)
        # Validate response status code
        assert (
                response.status_code == 400 or response.status_code == 403 or response.status_code == 404), "Status code is not 400/403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response.status_code == 400:
            if response_body["errorCode"] == str(14552):
                if response_body["message"] == str('The length of system id must be 23 characters'):
                    testResult(self, "passed", "Should throw proper error for invalid System Id",
                               "Showing proper error code & message for invalid System Id")
                    # self.result.set_result(TestResults.passed)

            elif response_body["errorCode"] != str(14552):

                testResult(self, "failed", "Should throw proper error for invalid System Id",
                           "Not showing proper error code & message for invalid System Id")
                # self.result.set_result(TestResults.failed)
                assert False

        elif response.status_code == 403 or response.status_code == 404:
            testResult(self, "passed", "Should throw proper error for invalid System Id",
                       "Showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error for invalid System Id",
                       "Not showing proper error code & message for invalid System Id")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty system id
    @pytest.mark.Smoke
    def test7_negative_telemetry_getCurrentState_empty_systemId(self):
        systemId = ""

        # Call COTA reusable module
        response = COTA_telemetry_getCurrentState(self, systemId, "invalid")

        # Validate response status code

        # print(response_body.status_code)
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(
            response.status_code)

        response_body = response.json()

        if response_body["status"] == 404:
            if response_body["error"] == str('Not Found'):
                testResult(self, "passed", "Should throw proper error for empty System Id",
                           "Showing proper error code & message for empty System Id")
                # self.result.set_result(TestResults.passed)

        elif response_body["status"] != 404:

            testResult(self, "failed", "Should throw proper error for empty System Id",
                       "Not showing proper error code & message for empty System Id")
            # self.result.set_result(TestResults.failed)
            assert False
