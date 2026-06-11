import time
import pytest

from C2CModules.packageController_modules import packageController_packageUpgrade, packageController_packageAllDetails, \
    packageController_packageIdDetails, packageController_packageAssignmentDetails, \
    packageController_packageAssignmentStatusUpdate, read_packageId, read_packageStatus_byPackageId, \
    read_packageStatus_byTrackingId, packageController_categoryDetails
from C2CModules.primary_IVI_device_modules import getVIN, get_SystemId
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_Package:

    # packageController_packageAllDetails
    @pytest.mark.Smoke
    def test1_positive_packageController_packageAllDetails(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            data_len = len(response_body["responseData"]["dataList"])
            if data_len <= 0:
                print("Data list is empty")
            testResult(self, "passed", "Should list all the packages",
                       "All packages are listed ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should list all the packages ",
                       "All packages are not listed  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test2_positive_PackageController_PackageIdDetails(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")
            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")
            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                assert False

            # Parse API response into JSON
            response_body = response.json()

            packageId = read_packageId(self, response_body, "Value")

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "valid")
        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        data_len = len(response_body["responseData"]["dataList"])
        if data_len <= 0:
            print("Data list is empty")
            testResult(self, "failed", "Should fetch and list the package details ",
                       "Package details is not fetched or listed   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            testResult(self, "passed", "Should fetch and list the package details",
                       "Package details is successfully fetched and listed ")

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test3_positive_PackageController_PackageAssignmentDetails(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        data_len = len(response_body["responseData"]["dataList"])
        if data_len <= 0:
            print("Data list is empty")
            testResult(self, "failed", "Should fetch and list the package assignment details of the device ",
                       "Package assignment details of the device is not fetched or listed   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            testResult(self, "passed", "Should fetch and list the package assignment details of the device",
                       "Package assignment details of the device is successfully fetched and listed")

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test4_positive_PackageController_PackageUpgrade(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")
            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                assert False

            # Parse API response into JSON
            response_body = response.json()

            packageId = read_packageId(self, response_body, "Value")

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            if response.status_code == 400:
                response = packageController_packageUpgrade(self, systemId, vin, "103", "valid")
                # Validate response status code
                if response.status_code == 200:
                    print("Response Status Code : " + str(response.status_code))
                else:
                    print("Status code is not 200. Rather found : " + str(response.status_code))
                    assert False

        # Parse API response into JSON
        response = response.json()

        if response['message'] == 'Vehicle Package Mapping already exist':
            print(" => Vehicle is already mapped to package, hence skipping this step")

            print("--------------------------------------------------------------")
            print("Verify package status : ")
            print("--------------------------------------------------------------")
            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Get package id & status'
            status = read_packageStatus_byPackageId(self, response, packageId)

            print("Package Id: ", packageId)
            print("Package status: ", status)

            if status == "SUCCESS":
                testResult(self, "passed",
                           "'Value' package status should be set to 'SUCCESS'",
                           "'Value' package status is set to 'SUCCESS'")
            elif status != "SUCCESS":
                testResult(self, "failed",
                           "Package status should be set to 'SUCCESS'",
                           "Package status is not set to 'SUCCESS'")
        else:
            # Get package tracking id'
            packageTrackingId = response["responseData"]["packageTrackingId"]

            print("Package Tracking ID : ", packageTrackingId)
            testResult(self, "passed",
                       "Initiate package upgrade or Assign desired/selected package to Vehicle via API",
                       "Package Upgrade is initiated successfully ")

            print("--------------------------------------------------------------")
            print("Verify package status : ")
            print("--------------------------------------------------------------")

            for i in range(20):
                # Verify package upgrade status
                response = packageController_packageAssignmentDetails(self, systemId, "valid")

                response = response.json()

                # Get package id & status'

                packageId, status = read_packageStatus_byTrackingId(self, response, packageTrackingId)
                if status != "SUCCESS" or status == "IN_PROGRESS" or status == 'RECEIVED':
                    time.sleep(30)
                else:
                    break

            if status == "SUCCESS":
                print("Upgraded Package Id: ", packageId)
                print("Upgraded Package status: ", status)
                testResult(self, "passed",
                           "Vehicle should be mapped to desired selected package",
                           "Vehicle is mapped to desired selected package successfully")
            elif status != "SUCCESS":
                print("Vehicle is mapped to - Package Id: ", packageId)
                print("Vehicle Package status: ", status)
                testResult(self, "failed",
                           "Vehicle should be mapped to desired selected package",
                           "Vehicle is not mapped to desired selected package successfully")

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test5_positive_PackageController_PackageAssignmentStatusUpdate(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                assert False

            # Parse API response into JSON
            response = response.json()

            # Get package id & status'
            status = read_packageStatus_byPackageId(self, response, packageId)

            # Get package tracking id'
            try:
                packageTrackingId = response["responseData"]["packageTrackingId"]
            except:
                packageTrackingId = response["responseData"]["dataList"][1]["trackingId"]

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        data_len = len(response_body["responseData"]["dataList"])
        if data_len <= 0:
            print("Data list is empty")
            testResult(self, "failed", "Should fetch and list the package assignment status for the device ",
                       "Package assignment details of the device is not fetched or listed   " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            testResult(self, "passed", "Should fetch and list the package assignment status for the device",
                       "Package assignment details of the device is successfully fetched and listed")

        print("----------------------------------------------------------")

    # packageController_categoryDetails
    @pytest.mark.Smoke
    def test6_positive_packageController_categoryDetails(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_CategoryDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_categoryDetails(self, "valid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            data_len = len(response_body["responseData"]["dataList"])
            if data_len <= 0:
                print("Data list is empty")
            testResult(self, "passed", "Should list all the category",
                       "All category are listed ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should list all the category ",
                       "All category are not listed  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")


class Test_Negative:

    # packageController_packageAllDetails_invalid_apiKey
    @pytest.mark.Smoke
    def test1_negative_packageController_packageAllDetails_invalid_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_negative_packageController_packageAllDetails_empty_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_negative_packageController_packageAllDetails_no_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_negative_packageController_packageAllDetails_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_negative_packageController_packageAllDetails_no_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6_negative_packageController_packageAllDetails_invalid_PageNo(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "invalid_pageNo")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["message"] == "Success":
            testResult(self, "passed", "Should throw Success message",
                       "Response message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response code & message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7_negative_packageController_packageAllDetails_empty_PageNo(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "empty_pageNo")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["message"] == "Success":
            testResult(self, "passed", "Should throw proper Success message",
                       "Response message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response code & message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8_negative_packageController_packageAllDetails_no_PageNo(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAllDetails")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No Input Required")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No Input Required")

        # Call api reusable module
        response = packageController_packageAllDetails(self, "no_pageNo")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "1200" or response_body["message"] == "Success":
            testResult(self, "passed", "Should throw Success message",
                       "Response message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response code & message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test9_negative_PackageController_PackageAssignmentDetails_invalid_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test10_negative_PackageController_PackageAssignmentDetails_empty_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test11_negative_PackageController_PackageAssignmentDetails_no_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test12_negative_PackageController_PackageAssignmentDetails_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test13_negative_PackageController_PackageAssignmentDetails_no_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test14_negative_PackageController_PackageAssignmentDetails_invalid_systemIdLessthan23char(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentDetails_invalid_systemIdLessthan23char")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "SystemId should be 23 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test15_negative_PackageController_PackageAssignmentDetails_invalid_systemIdGreaterthan23char(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentDetails_invalid_systemIdGreaterthan23char")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys6dd7b393311911eeaed61"

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "SystemId should be 23 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test16_negative_PackageController_PackageAssignmentDetails_incorrect_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentDetails_incorrect_systemId")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys6dd7b393311911eeaed5"

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given system id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentDetails
    @pytest.mark.Smoke
    def test17_negative_PackageController_PackageAssignmentDetails_empty_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""

        print("System Id :", systemId)

        # Call api reusable module
        response = packageController_packageAssignmentDetails(self, systemId, "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404 and response_body["error"] == "Not Found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test18_positive_PackageController_PackageIdDetails_invalid_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "102"

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test19_positive_PackageController_PackageIdDetails_empty_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "102"

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test20_positive_PackageController_PackageIdDetails_no_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "102"

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test21_positive_PackageController_PackageIdDetails_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "102"

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False
        print("----------------------------------------------------------")

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test22_positive_PackageController_PackageIdDetails_no_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
            print("Package Id :", packageId)

        else:
            print("Flag is not set to Yes, pls update the test data in sheet")

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "102"

            print("Package Id for 'Value' Package : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test23_positive_PackageController_PackageIdDetails_invalid_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageIdDetails_invalid_packageId")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
        else:
            print("Flag is not set to Yes, pls update the test data in sheet")
            packageId = "12$"

        print("Package Id : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "parameter datatype is not correct":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test24_positive_PackageController_PackageIdDetails_incorrect_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageIdDetails_incorrect_packageId")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = str(dict1["packageId"])
        else:
            print("Flag is not set to Yes, pls update the test data in sheet")
            packageId = "12"

        print("Package Id : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given package id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageIdDetails
    @pytest.mark.Smoke
    def test25_positive_PackageController_PackageIdDetails_empty_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageIdDetails")
        message = str(dict["Message"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            packageId = ""
        else:
            print("Flag is not set to Yes, pls update the test data in sheet")
            packageId = ""

        print("Package Id : ", packageId)

        # Call api reusable module
        response = packageController_packageIdDetails(self, packageId, "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404 and response_body["error"] == "Not Found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test26_positive_PackageController_PackageUpgrade_invalid_apiKey(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test27_positive_PackageController_PackageUpgrade_empty_apiKey(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test28_positive_PackageController_PackageUpgrade_no_apiKey(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test29_positive_PackageController_PackageUpgrade_empty_xrequestor(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test30_positive_PackageController_PackageUpgrade_no_xrequestor(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test31_positive_PackageController_PackageUpgrade_invalid_systemIdLessthan23char(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_invalid_systemIdLessthan23char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "SystemId should be 23 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test32_positive_PackageController_PackageUpgrade_invalid_systemIdGreaterthan23char(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_invalid_systemIdGreaterthan23char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys6dd7b393311911eeaed61"
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "SystemId should be 23 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test33_positive_PackageController_PackageUpgrade_incorrect_systemId(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_incorrect_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys6dd7b393311911eeaed5"
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given system id is not found or empty":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test34_positive_PackageController_PackageUpgrade_empty_systemId(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            vin = getVIN(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404 and response_body["error"] == "Not Found":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test35_positive_PackageController_PackageUpgrade_invalid_vinLessthan17char(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_invalid_vinLessthan17char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = "vin123"

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Vin should be 17 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test36_positive_PackageController_PackageUpgrade_invalid_vinGreaterthan17char(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_invalid_vinGreaterthan17char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = "VINQCQAIVI71721591"

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Vin should be 17 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test37_positive_PackageController_PackageUpgrade_incorrect_vin(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_incorrect_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = "VINQCQAIVI1111155"

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Vehicle Package Mapping already exist":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test38_positive_PackageController_PackageUpgrade_empty_vin(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = ""

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Multiple validations failed" and response_body["responseData"][
            "message"] == "Vin is empty, Vin should be 17 characters long":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test39_positive_PackageController_PackageUpgrade_no_vin(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = ""

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response_body = response.json()

                packageId = read_packageId(self, response_body, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "no_vin")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Vin is empty":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")



    def test40_positive_PackageController_PackageUpgrade_invalid_packageId(self):

        global status
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_invalid_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            packageId = "12$"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test41_positive_PackageController_PackageUpgrade_incorrect_packageId(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade_incorrect_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            packageId = "12"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 200:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given package id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test42_positive_PackageController_PackageUpgrade_empty_packageId(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = ""
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            packageId = ""

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Package Id cannot be null or empty":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageUpgrade
    @pytest.mark.Smoke
    def test43_positive_PackageController_PackageUpgrade_no_packageId(self):

        global status
        print("-----------------------------------------]-----------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageUpgrade")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = ""
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            packageId = ""

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("VIN: ", vin)

        # Call api reusable module
        response = packageController_packageUpgrade(self, systemId, vin, packageId, "no_packageId")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Package Id cannot be null or empty":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")


    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test44_positive_PackageController_PackageAssignmentStatusUpdate_invalid_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test45_positive_PackageController_PackageAssignmentStatusUpdate_empty_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "api keys are not matching. Please provide valid key" or "api keys are not matching" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test46_positive_PackageController_PackageAssignmentStatusUpdate_no_apiKey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test47_positive_PackageController_PackageAssignmentStatusUpdate_empty_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "x-requestor header cannot be blank" or "x-requestor header cannot be blank" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test48_positive_PackageController_PackageAssignmentStatusUpdate_no_xrequestor(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body[
            "message"] == "Required authentication headers are missing" or "Required authentication headers are missing" in \
                response_body["message"]:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test49_positive_PackageController_PackageAssignmentStatusUpdate_invalid_systemIdLessthan23char(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentDetails_invalid_systemIdLessthan23char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        systemId = "sys123"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given system id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test50_positive_PackageController_PackageAssignmentStatusUpdate_invalid_systemIdGreaterthan23char(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_invalid_systemIdGreaterthan23char")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        systemId = "sys6dd7b393311911eeaed61"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given system id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test51_positive_PackageController_PackageAssignmentStatusUpdate_incorrect_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_incorrect_systemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        systemId = "sys6dd7b393311911eeaed4"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given system id is not present in the database":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test52_positive_PackageController_PackageAssignmentStatusUpdate_empty_systemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController", "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Get package id for value package'
            response = packageController_packageAllDetails(self, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))
                # Parse API response into JSON
                response = response.json()

                packageId = read_packageId(self, response, "Value")
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageId = "103"

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package id & status'
                status = read_packageStatus_byPackageId(self, response, packageId)

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"

        systemId = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["status"] == 404:
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test53_positive_PackageController_PackageAssignmentStatusUpdate_invalid_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_invalid_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    status = response["responseData"]["status"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    status = response["responseData"]["dataList"][0]["status"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                status = "SUCCESS"

        packageId = "$%"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test54_positive_PackageController_PackageAssignmentStatusUpdate_incorrect_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_incorrect_packageId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    status = response["responseData"]["status"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    status = response["responseData"]["dataList"][0]["status"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                status = "SUCCESS"

        packageId = "12"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test55_positive_PackageController_PackageAssignmentStatusUpdate_empty_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    status = response["responseData"]["status"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    status = response["responseData"]["dataList"][0]["status"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                status = "SUCCESS"

        packageId = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

        # PackageController_PackageAssignmentStatusUpdate

    @pytest.mark.Smoke
    def test56_positive_PackageController_PackageAssignmentStatusUpdate_no_packageId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    status = response["responseData"]["status"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    status = response["responseData"]["dataList"][0]["status"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                status = "SUCCESS"

        packageId = ""
        print("System Id :", systemId)
        #print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "no_packageId")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test57_positive_PackageController_PackageAssignmentStatusUpdate_invalid_status(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_invalid_status")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    packageId = response["responseData"]["packageId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                packageId = "102"

        status = "$%"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given status is not valid":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test58_positive_PackageController_PackageAssignmentStatusUpdate_incorrect_status(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_incorrect_status")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    packageId = response["responseData"]["packageId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                packageId = "102"

        status = "success"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given status is not valid":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test59_positive_PackageController_PackageAssignmentStatusUpdate_empty_status(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    packageId = response["responseData"]["packageId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                packageId = "102"

        status = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given status is not valid":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test60_positive_PackageController_PackageAssignmentStatusUpdate_no_status(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    packageTrackingId = response["responseData"]["packageTrackingId"]
                    packageId = response["responseData"]["packageId"]
                except:
                    packageTrackingId = response["responseData"]["dataList"][0]["trackingId"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                packageTrackingId = "b939c95a-8ebe-4346-acfd-6ef91fcbdecb"
                packageId = "102"

        status = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        #print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "no_status")

        # Validate response status code
        if response.status_code == 404:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 404. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Given status is not valid":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")



    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test61_positive_PackageController_PackageAssignmentStatusUpdate_invalid_trackingId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_invalid_trackingId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    status = response["responseData"]["status"]
                    packageId = response["responseData"]["packageId"]
                except:
                    status = response["responseData"]["dataList"][0]["status"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageId = "102"

        packageTrackingId = "$#%#%$-$%$"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test62_positive_PackageController_PackageAssignmentStatusUpdate_incorrect_trackingId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate_incorrect_trackingId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    status = response["responseData"]["status"]
                    packageId = response["responseData"]["packageId"]
                except:
                    status = response["responseData"]["dataList"][0]["status"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageId = "102"

        packageTrackingId = "b939c951-8ebe-4346-acfd-6ef91fcbdecb"
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test63_positive_PackageController_PackageAssignmentStatusUpdate_empty_trackingId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    status = response["responseData"]["status"]
                    packageId = response["responseData"]["packageId"]
                except:
                    status = response["responseData"]["dataList"][0]["status"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageId = "102"

        packageTrackingId = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "invalid")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

    # PackageController_PackageAssignmentStatusUpdate
    @pytest.mark.Smoke
    def test64_positive_PackageController_PackageAssignmentStatusUpdate_no_trackingId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "PackageController",
                                         "PackageController_PackageAssignmentStatusUpdate")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            packageId = str(dict1["packageId"])
            packageTrackingId = str(dict1["trackingId"])
            status = str(dict1["status"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            # Verify package upgrade status
            response = packageController_packageAssignmentDetails(self, systemId, "valid")

            # Validate response status code
            if response.status_code == 200:
                print("Response Status Code : " + str(response.status_code))

                # Parse API response into JSON
                response = response.json()

                # Get package tracking id'
                try:
                    status = response["responseData"]["status"]
                    packageId = response["responseData"]["packageId"]
                except:
                    status = response["responseData"]["dataList"][0]["status"]
                    packageId = response["responseData"]["dataList"][0]["packageId"]
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                status = "SUCCESS"
                packageId = "102"

        packageTrackingId = ""
        print("System Id :", systemId)
        print("Package Id: ", packageId)
        print("Package status: ", status)
        #print("Package tracking Id: ", packageTrackingId)

        # Call api reusable module
        response = packageController_packageAssignmentStatusUpdate(self, systemId, packageId, status, packageTrackingId,
                                                                   "no_trackingId")

        # Validate response status code
        if response.status_code == 400:
            print("Response Status Code : " + str(response.status_code))
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "PackageId or TrackingId is not found in DB":
            testResult(self, "passed", "Should throw proper error message",
                       "Response/Error message is as expected. Refer api response for additional info/details")
            # self.result.set_result(TestResults.passed)
            assert True

        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            testResult(self, "failed", "Should throw proper error message",
                       "Response/Error message is not as expected OR something went wrong, pls check api response for additional info/details")
            # self.result.set_result(TestResults.failed)
            assert False

        print("----------------------------------------------------------")

