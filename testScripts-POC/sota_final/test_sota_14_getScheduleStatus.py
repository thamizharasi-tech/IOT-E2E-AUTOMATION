import pytest

from C2CModules.sota_api_modules import SOTA_ListScheduleVin, get_ScheduledId_from_ScheduleDetails_api
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_smoke:

    # -----------------------------------------------------------------
    # Fota-Get schedules status
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus(self):

        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
            vin = getVIN(self, OnboardingType, chipsetType)

        response = SOTA_ListScheduleVin(self, scheduleId, vin, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            data_len = len(response_body["responseData"]["dataList"])
            if data_len >= 1:
                for i in range(data_len):
                    print("vin : ", response_body["responseData"]["dataList"][i]["vin"])
                    print("status : ", response_body["responseData"]["dataList"][i]["status"])
                    print("offeredTime : ", response_body["responseData"]["dataList"][i]["offeredTime"])
                    print("acceptedTime : ", response_body["responseData"]["dataList"][i]["acceptedTime"])
                    print("completeTime : ", response_body["responseData"]["dataList"][i]["completeTime"])

                    print("statusTime : ", response_body["responseData"]["dataList"][i]["statusTime"])
                    print("metaInfo : ", response_body["responseData"]["dataList"][i]["metaInfo"])
                    print("system : ", response_body["responseData"]["dataList"][i]["system"])

                testResult(self, "passed", "Should fetch schedule status successfully",
                           "Successfully fetched the data/status for selected schedule ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch schedule status successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
        elif response_body["responseCode"] != str(14000):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch schedule status successfully ",
                       "Failed to fetch the schedule status " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_invalidapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching..please provide valid key"

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_emptyapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching..please provide valid key"

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_noapikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_emptyxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_noxrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!"

        print("----------------------------------------------------------")

    # scheduleId less than 0
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_scheduleId_lessthanzero(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin_scheduleId_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "-1"
            vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, temp)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response_body["responseCode"] == str(15006):
            assert response_body["responseData"]["message"] == "No data available"
        else:
            assert False

        print("----------------------------------------------------------")

    # invalid scheduleId like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_invalidscheduleId(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin_invalid_scheduleId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "-1"
            vin = getVIN(self, OnboardingType, chipsetType)
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15006) and response_body["responseData"][
            "message"] == "No data available":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # vin lessthan zero
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_vin_lessthanzero(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin_vin_lessthanZero")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
            vin = "-1"
        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15006) and response_body["responseData"][
            "message"] == "No data available":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    print("----------------------------------------------------------")

    # invalid vin like 1x,aa,..etc
    @pytest.mark.Smoke
    def test1_negative_sota_getScheduleStatus_invalidvin(self):
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin_invalid_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
            vin = "vin123"

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, temp)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15006) and response_body["responseData"][
            "message"] == "No data available":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    print("----------------------------------------------------------")

    # without queryparams(scheduleId,vin)
    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_without_queryparams(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "removeQueryParams_from_url")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            data_len = len(response_body["responseData"]["dataList"])
            if data_len >= 1:
                for i in range(data_len):
                    print("vin : ", response_body["responseData"]["dataList"][i]["vin"])
                    print("status : ", response_body["responseData"]["dataList"][i]["status"])
                    print("offeredTime : ", response_body["responseData"]["dataList"][i]["offeredTime"])
                    print("acceptedTime : ", response_body["responseData"]["dataList"][i]["acceptedTime"])
                    print("completeTime : ", response_body["responseData"]["dataList"][i]["completeTime"])

                    print("statusTime : ", response_body["responseData"]["dataList"][i]["statusTime"])
                    print("metaInfo : ", response_body["responseData"]["dataList"][i]["metaInfo"])
                    print("system : ", response_body["responseData"]["dataList"][i]["system"])

                testResult(self, "passed", "Should fetch schedule status successfully",
                           "Successfully fetched the data/status for selected schedule ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch schedule status successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch schedule status successfully ",
                       "Failed to fetch the schedule status " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")


    # without queryparams(scheduleId,vin)
    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_invalid_pageNo_lessthanZero(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "invalid_pageNo_lessthanZero")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15047) and response_body["responseData"][
            "message"] == "Page number must not be less than one":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams(scheduleId,vin)
    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_invalid_pageSize_lessthanZero(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "invalid_pageSize_lessthanZero")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15048) and response_body["responseData"][
            "message"] == "Page size must not be less than one":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # without queryparams(scheduleId,vin)

    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_invalid_pageNo(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "invalid_pageNo")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["error"] == str(15084) and response_body[
            "message"] == "Unable to find mandatory input parameter":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams(scheduleId,vin)
    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_invalid_pageSize(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "invalid_pageSize")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["error"] == str(15084) and response_body[
            "message"] == "Unable to find mandatory input parameter":

            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without queryparams(scheduleId,vin)
    @pytest.mark.Smoke
    def test1_Positive_sota_getScheduleStatus_no_vin(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-ListScheduleVin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            scheduleId = str(dict1["scheduleId"])
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            scheduleId = "1"
            vin = "10"

        scheduleId = get_ScheduledId_from_ScheduleDetails_api(self)
        vin = getVIN(self, OnboardingType, chipsetType)

        # call api reusable module
        response = SOTA_ListScheduleVin(self, scheduleId, vin, "no_vin")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            # message = response_body["responseData"]["message"]
            # print('Message : ', message)
            data_len = len(response_body["responseData"]["dataList"])
            if data_len >= 1:
                for i in range(data_len):
                    print("vin : ", response_body["responseData"]["dataList"][i]["vin"])
                    print("status : ", response_body["responseData"]["dataList"][i]["status"])
                    print("offeredTime : ", response_body["responseData"]["dataList"][i]["offeredTime"])
                    print("acceptedTime : ", response_body["responseData"]["dataList"][i]["acceptedTime"])
                    print("completeTime : ", response_body["responseData"]["dataList"][i]["completeTime"])

                    print("statusTime : ", response_body["responseData"]["dataList"][i]["statusTime"])
                    print("metaInfo : ", response_body["responseData"]["dataList"][i]["metaInfo"])
                    print("system : ", response_body["responseData"]["dataList"][i]["system"])

                testResult(self, "passed", "Should fetch schedule status successfully",
                           "Successfully fetched the data/status for selected schedule ")
            else:
                print(" => datalist is empty")
                testResult(self, "verificationFailed", "Should fetch schedule status successfully",
                           "End point is working fine, but there is no data in DB , thus marking test case as fail")
        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch schedule status successfully ",
                       "Failed to fetch the schedule status " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

