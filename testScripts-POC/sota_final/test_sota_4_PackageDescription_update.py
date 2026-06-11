import pytest

from C2CModules.sota_api_modules import SOTA_UpdatePackageDescription, get_packageId_from_packageDetails_api
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_smoke:

    # -----------------------------------------------------------------
    # SOTA_PATCH: Package desc update
    # -----------------------------------------------------------------

    @pytest.mark.Smoke
    def test1_positive_sota_packageDescriptionUpdate(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response
        if response_body["responseCode"] == str(15000) or response_body["responseCode"] == 15000:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if message == "Success":
                testResult(self, "passed", "Should update package description successfully",
                           "Successfully updated package description")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Should update package description successfully",
                           "Failed to update package description" + " Reason for failure is : " +
                           response_body["responseData"]["message"])
                # self.result.set_result(TestResults.failed)

        elif response_body["responseCode"] != 15000:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should update package description successfully",
                       "Failed to update package description" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


class Test_negative:
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_packageDescriptionUpdate_invalid_apikey(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_sota_packageDescriptionUpdate_empty_apikey(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"
        
        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            #self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


    # no apikey
    @pytest.mark.Smoke
    def test3_negative_sota_packageDescriptionUpdate_no_apikey(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_sota_packageDescriptionUpdate_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "x-requestor header cannot be blank" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_sota_packageDescriptionUpdate_no_xrequestor(self):
        print("----------------------------------------------------------")
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # invalid packageId
    @pytest.mark.Smoke
    def test6_negative_sota_packageDescriptionUpdate_invalid_packageId(self):
        print("----------------------------------------------------------")
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription_invalid_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = "1856$"
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, temp)

        # Validate response status code
        if response.status_code == 400:
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["error"] == str(15084) and response_body[
            "message"] == "Unable to find mandatory input parameter":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # incorrect packageId
    @pytest.mark.Smoke
    def test6a_negative_sota_packageDescriptionUpdate_incorrect_packageId(self):
        print("----------------------------------------------------------")
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription_incorrect_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = "1856"
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, temp)

        # Validate response status code
        if response.status_code == 400:
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15045) and response_body["responseData"][
            "message"] == "package does not exist":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # invalid description-contain special char

    @pytest.mark.Smoke
    def test7_negative_sota_packageDescriptionUpdate_invalid_description(self):
        print("----------------------------------------------------------")
        temp = "invalid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription_invalid_description")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "firmware description update through patch api ^%&&**"
        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, temp)

        # Validate response status code
        if response.status_code == 200:
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15000) or response_body["responseData"][
            "message"] == "Success":
            assert True
            testResult(self, "passed", "Should not throw error message",
                       "Response message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should not throw error message",
                       "Response message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # empty release-note
    @pytest.mark.Smoke
    def test8_negative_sota_packageDescriptionUpdate_empty_description(self):
        print("----------------------------------------------------------")
        temp = "valid"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = ""

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, temp)

        # Validate response status code
        if response.status_code == 400:
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15043) and response_body["responseData"][
            "message"] == "description cannot be empty":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # without release-note
    @pytest.mark.Smoke
    def test9_negative_sota_packageDescriptionUpdate_without_description(self):
        print("----------------------------------------------------------")

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-UpdatePackageDescription")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageId = get_packageId_from_packageDetails_api(self)
            description = "package description update through patch api"

        # call api reusable module
        response = SOTA_UpdatePackageDescription(self, str(packageId), description, "no_description")

        # Validate response status code
        if response.status_code == 400:
            # print("API response status code is :", response.status_code)
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == str(15043) and response_body["responseData"][
            "message"] == "description cannot be empty":
            assert True
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
