import random
import time

import pytest

from C2CModules.fota_api_modules import FOTA_createPresigneUrl
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


# ---------------------------------------------------------
# FOTA-Create presigned Url test scripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_createPresigneUrl(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # try to upload new package in case of duplicate
        if response_body["responseData"]["message"] == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

            # Call createPresigneUrl api module
            response = FOTA_createPresigneUrl(self, packageName, system, model, "valid")

            # Validate response status code
            if response.status_code == 200:
                assert True
            else:
                print("Status code is not 200. Rather found : " + str(response.status_code))
                assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14000":
            upload_url = response_body["responseData"]["message"]
            print('Upload url : ', upload_url)
            testResult(self, "passed", "Presigned-url should be created for package/file upload",
                       "Presigned-url is created for package/file upload")
        elif response_body["responseCode"] != "14000":
            testResult(self, "failed", "Presigned-url should be created for package/file upload",
                       "Failed to create Presigned-url " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")


class Test_negative:
    # ---------------------------------------------------------------------------------------
    # FOTA-create presigned url : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_create_Presigned_url_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False
        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_fota_create_Presigned_url_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_fota_create_Presigned_url_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_fota_create_Presigned_url_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "x-requestor header cannot be blank" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False
        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_fota_create_Presigned_url_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            assert False
        print("----------------------------------------------------------")

    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid model-contain special char
    @pytest.mark.Smoke
    def test6_negative_fota_create_Presigned_url_invalid_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp%^%"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14108" or response_body["responseData"][
            "message"] == "model-name contains special characters":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned url should not be created for invalid model",
                       "Presigned url is not created for invalid model ")
        elif response_body["responseCode"] != "14108":
            testResult(self, "failed", "Presigned url should not be created for invalid model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid empty model
    @pytest.mark.Smoke
    def test7_negative_fota_create_Presigned_url_empty_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = ""
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = ""
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14107" or response_body["responseData"][
            "message"] == "model-name cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for empty model",
                       "Presigned-url is not created for empty model ")
        elif response_body["responseCode"] != "14107":
            testResult(self, "failed", "Presigned-url should not be created for empty model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # invalid model-contain special char
    @pytest.mark.Smoke
    def test8_negative_fota_create_Presigned_url_no_model(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "no_model")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "140107" or response_body["responseData"][
            "message"] == "model-name cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for without model parameter",
                       "Presigned-url should not be created for without model parameter ")
        elif response_body["responseCode"] != "14107":
            testResult(self, "failed", "Presigned-url should not be created for without model parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # invalid system-contain special char
    @pytest.mark.Smoke
    def test9_negative_fota_create_Presigned_url_invalid_system(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl_invalid_system")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI$%"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14106" or response_body["responseCode"] == "14074" or \
                response_body["responseData"]["message"] == "System name is invalid" or response_body["responseData"][
            "message"] == "System contains special characters":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for invalid system",
                       "Presigned-url is not created invalid system ")
        else:
            testResult(self, "failed", "Presigned-url should not be created for invalid system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])

        print("----------------------------------------------------------")

    # invalid empty system
    @pytest.mark.Smoke
    def test10_negative_fota_create_Presigned_url_empty_system(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = ""
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14073" or response_body["responseData"][
            "message"] == "Presigned-url is not created empty system ":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for empty system",
                       "Presigned-url is not created empty system ")
        elif response_body["responseCode"] != "14073":
            testResult(self, "failed", "Presigned-url should not be created for empty system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # invalid without system parameter
    def test11_negative_fota_create_Presigned_url_no_system(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = ""
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = ""
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "no_system")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14073" or response_body["responseData"][
            "message"] == "Presigned-url is not created empty system ":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for without system parameter",
                       "Presigned-url is not created without system parameter ")
        elif response_body["responseCode"] != "14073":
            testResult(self, "failed", "Presigned-url should not be created for without system parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

        # invalid system-contain special char

    @pytest.mark.Smoke
    def test12_negative_fota_create_Presigned_url_invalid_filename(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl_invalid_filename")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v  ' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14109" or response_body["responseData"][
            "message"] == "filename contains special characters":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for invalid filename",
                       "Presigned-url is not created invalid filename ")
        elif response_body["responseCode"] != "14109":
            testResult(self, "failed", "Presigned-url should not be created for invalid filename",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # invalid empty filename
    @pytest.mark.Smoke
    def test13_negative_fota_create_Presigned_url_empty_filename(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = ""
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = ''

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14078" or response_body["responseData"][
            "message"] == "Filename cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for empty filename",
                       "Presigned-url is not created empty filename ")
        elif response_body["responseCode"] != "14078":
            testResult(self, "failed", "Presigned-url should not be created for empty filename",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # invalid without filename parameter
    def test14_negative_fota_create_Presigned_url_no_filename(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            packageName = 'test_v' + str(random_id) + '.zip'

        # Call createPresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "no_filename")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14078" or response_body["responseData"][
            "message"] == "Filename cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Presigned-url should not be created for without filename parameter",
                       "Presigned-url is not created without filename parameter ")
        elif response_body["responseCode"] != "14078":
            testResult(self, "failed", "Presigned-url should not be created for without filename parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test15_negative_fota_create_Presigned_url_duplicate_package(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-createPresigneUrl")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"

        # Call create PresigneUrl api module
        response = FOTA_createPresigneUrl(self, packageName, system, model, "valid")

        time.sleep(5)

        response1 = FOTA_createPresigneUrl(self, packageName, system, model, "valid")

        # Validate response status code
        if response1.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response1.status_code))
            assert False

        # Parse API response into JSON
        response_body = response1.json()

        # Validate response body
        if response_body["responseCode"] == "14029" or response_body["responseData"][
            "message"] == "duplicated Firmware Version":
            testResult(self, "passed", "Presigned-url should be not created for duplicate package/file",
                       "Presigned-url is not created for duplicate package/file")
        elif response_body["responseCode"] != "14029":
            testResult(self, "failed", "Presigned-url should not be created for duplicate package/file",
                       "Failed to create Presigned-url " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")
