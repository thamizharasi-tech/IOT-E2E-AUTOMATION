import pytest

from C2CModules.COTA_modules import COTA_liveCommandTracking_getCurrentFrequency, \
    COTA_telemetry_getCotaDetails_by_requestId
from C2CModules.commandControl_modules import CommandControl_liveTracking
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_CommandControl_post:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_CommandControl_liveTracking_updateFrequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response_body = CommandControl_liveTracking(self, name, systemId, frequency, value, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Live Tracking Command Published Successfully'):

            print("Tracking Id : ", response_body["responseData"]["trackingId"])

            testResult(self, "passed", "Live Tracking Command should be published successfully",
                       "Live Tracking Command Published Successfully")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] == str('Data fetched successfully'):

            testResult(self, "failed", "Live Tracking Command should be published successfully ",
                       "Failed to publish Live Tracking Command " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid api key
    @pytest.mark.Smoke
    def test1_negative_CommandControl_liveTracking_updateFrequency_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid_apiKey")

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
    def test2_negative_CommandControl_liveTracking_updateFrequency_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "empty_apiKey")

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
    def test3_negative_CommandControl_liveTracking_updateFrequency_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "no_apiKey")

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
    def test4_negative_CommandControl_liveTracking_updateFrequency_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "empty_x-requestor")

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
    def test5_negative_CommandControl_liveTracking_updateFrequency_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "no_x-requestor")

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
    def test6_negative_CommandControl_liveTracking_updateFrequency_invalid_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency_invalid_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid")

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
    def test7_negative_CommandControl_liveTracking_updateFrequency_empty_systemId(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            name = "LiveTracking"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response_body = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid")

        # Validate response status code

        # print(response_body.status_code)
        assert (response_body.status_code == 404), "Status code is not 404. Rather found : " + str(
            response_body.status_code)

        response_body = response_body.json()

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

    # COTA_live command tracking with invalid command name
    @pytest.mark.Smoke
    def test8_negative_CommandControl_liveTracking_updateFrequency_invalid_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking1"
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid")

        # print(response.status_code)
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14500) and response_body["message"] == str('Invalid Command Name'):
            testResult(self, "passed", "Should throw proper error for invalid command name",
                       "Showing proper error code & message for invalid command name")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14500):

            testResult(self, "failed", "Should throw proper error for invalid command name",
                       "Not showing proper error code & message for invalid command name")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for invalid command name",
                       "Not showing proper error code & message for invalid command name")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty command name
    @pytest.mark.Smoke
    def test9_negative_CommandControl_liveTracking_updateFrequency_empty_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = ""
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = ""
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid")

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
    @pytest.mark.Smoke
    def test10_negative_CommandControl_liveTracking_updateFrequency_no_name(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = ""
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = ""
            frequency = 2
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "no_commandName")

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
    @pytest.mark.Smoke
    def test11_negative_CommandControl_liveTracking_updateFrequency_invalid_frequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency_invalid_freq")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = "a"
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid_frequency")

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

    # COTA_live command tracking with empty frequency
    @pytest.mark.Smoke
    def test12_negative_CommandControl_liveTracking_updateFrequency_empty_frequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = ""
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking1"
            frequency = ""
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid_frequency")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14534) and response_body["message"] == str(
                'Frequency is mandatory cannot be null or empty'):
            testResult(self, "passed", "Should throw proper error for empty frequency",
                       "Showing proper error code & message for empty frequency")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14534):

            testResult(self, "failed", "Should throw proper error for empty frequency",
                       "Not showing proper error code & message for empty frequency")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for empty frequency",
                       "Not showing proper error code & message for empty frequency")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking without frequency parameter
    @pytest.mark.Smoke
    def test13_negative_CommandControl_liveTracking_updateFrequency_no_frequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = ""
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking1"
            frequency = ""
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "no_frequency")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14534) and response_body["message"] == str(
                'Frequency is mandatory cannot be null or empty'):
            testResult(self, "passed", "Should throw proper error for without frequency parameter",
                       "Showing proper error code & message for without frequency parameter") \
                # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14534):

            testResult(self, "failed", "Should throw proper error for without frequency parameter",
                       "Not showing proper error code & message for without frequency parameter")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for without frequency parameter",
                       "Not showing proper error code & message for without frequency parameter")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with specified frequency
    @pytest.mark.Smoke
    def test14_negative_CommandControl_liveTracking_updateFrequency_specified_frequency(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA",
                                         "CommandControl_liveTracking_updateFrequency_invalid_specifiedFreq")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 100
            value = 1

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14546) and response_body["message"] == str('Provide a better frequency'):
            testResult(self, "passed", "Should throw proper error for specified frequency",
                       "Showing proper error code & message for specified frequency")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14546):

            testResult(self, "failed", "Should throw proper error for specified frequency",
                       "Not showing proper error code & message for specified frequency")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for specified frequency",
                       "Not showing proper error code & message for specified frequency")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with invalid value
    @pytest.mark.Smoke
    def test15_negative_CommandControl_liveTracking_updateFrequency_invalid_value(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = str(dict1["value"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 100
            value = "a"

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid_value")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["message"] == str('Live Tracking turned off Successfully'):
            testResult(self, "passed", "Live Tracking should be turned off Successfully",
                       "Live Tracking turned off Successfully")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != str('Live Tracking turned off Successfully'):
            testResult(self, "failed", "Live Tracking should be turned off Successfully",
                       "Live Tracking is not turned off Successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Live Tracking should be turned off Successfully",
                       "Live Tracking is not turned off Successfully")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking with empty value
    @pytest.mark.Smoke
    def test16_negative_CommandControl_liveTracking_updateFrequency_empty_value(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 100
            value = ""

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "invalid_value")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["message"] == str('Live Tracking turned off Successfully'):
            testResult(self, "passed", "Live Tracking should be turned off Successfully",
                       "Live Tracking turned off Successfully")
            # self.result.set_result(TestResults.passed)

        elif response_body["message"] != str('Live Tracking turned off Successfully'):
            testResult(self, "failed", "Live Tracking should be turned off Successfully",
                       "Live Tracking is not turned off Successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Live Tracking should be turned off Successfully",
                       "Live Tracking is not turned off Successfully")
            # self.result.set_result(TestResults.failed)
            assert False

    # COTA_live command tracking without value parameter
    @pytest.mark.Smoke
    def test17_negative_CommandControl_liveTracking_updateFrequency_no_value(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "COTA", "CommandControl_liveTracking_updateFrequency")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            name = str(dict1["name"])
            frequency = str(dict1["frequency"])
            value = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            name = "LiveTracking"
            frequency = 100
            value = ""

        # Call COTA reusable module
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "no_value")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        if response_body["errorCode"] == str(14544) and response_body["message"] == str(
                'Default template id is invalid'):
            testResult(self, "passed", "Should throw proper error for without value parameter",
                       "Showing proper error code & message for without value parameter")
            # self.result.set_result(TestResults.passed)

        elif response_body["errorCode"] != str(14544):
            testResult(self, "failed", "Should throw proper error for without value parameter",
                       "Not showing proper error code & message for without value parameter")
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            testResult(self, "failed", "Should throw proper error for without value parameter",
                       "Not showing proper error code & message for without value parameter")
            # self.result.set_result(TestResults.failed)
            assert False

