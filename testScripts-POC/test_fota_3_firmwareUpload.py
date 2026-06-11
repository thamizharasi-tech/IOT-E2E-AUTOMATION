import os
import random
import shutil
import time

import pytest

from C2CModules.fota_api_modules import FOTA_firmwareUpload, FOTA_uploadFile, save_firmwareId_in_excel
from C2CModules.OTA_reuse_modules import presignedUrl
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


# ---------------------------------------------------------
# FOTA-firmware upload negative test scripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_firmware_upload(self):
        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14000" and response_body["responseData"]["message"] == "success":
            firmwareId = response_body["responseData"]["firmwareId"]
            print('Firmware Id : ', firmwareId)
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should be uploaded successfully",
                       "Firmware package is uploaded successfully ")
        elif response_body["message"] != "success":
            testResult(self, "failed", "Firmware package should be uploaded successfully",
                       "Failed to upload firmware pacakge " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

class Test_negative:
    # ---------------------------------------------------------------------------------------
    # FOTA-firmware upload API : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_firmware_upload_invalid_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid_apiKey")

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
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_fota_firware_upload_empty_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "empty_apiKey")

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
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_fota_fimware_upload_no_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_apiKey")

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
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_fota_firmware_upload_empty_xrequestor(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "empty_x-requestor")

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
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_fota_firmware_upload_no_xrequestor(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_x-requestor")

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
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid model-contain special char
    @pytest.mark.Smoke
    def test6_negative_fota_firmware_upload_invalid_model(self):
        global dest_filepath
        # valid model name for file upload
        valid_model_name = "adp"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp^%"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14049" or response_body["responseData"]["message"] == "Model contains specials characters":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid model",
                       "Firmware package is not uploaded for invalid model ")
        elif response_body["responseCode"] != "14049":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

# invalid empty model
    @pytest.mark.Smoke
    def test7_negative_fota_firmware_upload_empty_model(self):
        global dest_filepath
        # valid model name for file upload
        valid_model_name = "adp"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = " "
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = ""
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14001" or response_body["responseData"]["message"] == "model is not allowed to be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty model",
                       "Firmware package is not uploaded for empty model ")
        elif response_body["responseCode"] != "14001":
            testResult(self, "failed", "Firmware package should not be uploaded for empty model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid model-contain special char
    @pytest.mark.Smoke
    def test8_negative_fota_firmware_upload_no_model(self):
        global dest_filepath
        # valid model name for file upload
        valid_model_name = "adp"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp^%"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, valid_model_name, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_model")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14001" or response_body["responseData"]["message"] == "model is not allowed to be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without model parameter",
                       "Firmware package is not uploaded for without model parameter ")
        elif response_body["responseCode"] != "14001":
            testResult(self, "failed", "Firmware package should not be uploaded for without model parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    # invalid system-contain special char
    @pytest.mark.Smoke
    def test9_negative_fota_firmware_upload_invalid_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_system")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            invalid_system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            invalid_system = "IVI1%$"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, invalid_system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14074" or response_body["responseData"]["message"] == "System contains special characters":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid system",
                       "Firmware package is not uploaded for invalid system ")
        elif response_body["responseCode"] != "14074":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid empty system
    @pytest.mark.Smoke
    def test10_negative_fota_firmware_upload_empty_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = ""
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = ""
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14073" or response_body["responseData"]["message"] == "System cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty system",
                       "Firmware package is not uploaded for empty system ")
        elif response_body["responseCode"] != "14073":
            testResult(self, "failed", "Firmware package should not be uploaded for empty system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid without system parameter
    def test11_negative_fota_firmware_upload_no_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_system")


        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14073" or response_body["responseData"]["message"] == "System cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without system parameter",
                       "Firmware package is not uploaded for without system parameter ")
        elif response_body["responseCode"] != "14073":
            testResult(self, "failed", "Firmware package should not be uploaded for without system parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    # invalid IsDiffImage
    @pytest.mark.Smoke
    def test12_negative_fota_firmware_upload_invalid_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_isDiffImage")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true1"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid isDiffImage",
                       "Firmware package is not uploaded for invalid isDiffImage ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid isDiffImage",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid IsDiffImage
    @pytest.mark.Smoke
    def test13_negative_fota_firmware_upload_empty_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = ""
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = ""
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14079" or response_body["responseData"][
            "message"] == "isDiffImage cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty isDiffImage",
                       "Firmware package is not uploaded for empty isDiffImage ")
        elif response_body["responseCode"] != "14079":
            testResult(self, "failed", "Firmware package should not be uploaded for empty isDiffImage",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # no IsDiffImage
    @pytest.mark.Smoke
    def test14_negative_fota_firmware_upload_no_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_isDiffImage")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14079" or response_body["responseData"][
            "message"] == "isDiffImage cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for wothout isDiffImage parameter",
                       "Firmware package is not uploaded for without isDiffImage parameter ")
        elif response_body["responseCode"] != "14079":
            testResult(self, "failed", "Firmware package should not be uploaded for without isDiffImage parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")



    # invalid IsBase
    @pytest.mark.Smoke
    def test15_negative_fota_firmware_upload_invalid_IsBase(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_isBase")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false1"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid isBase",
                       "Firmware package is not uploaded for invalid isBase ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid isBase",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid IsBase
    @pytest.mark.Smoke
    def test16_negative_fota_firmware_upload_empty_IsBase(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = ""
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = ""
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14080" or response_body["responseData"][
            "message"] == "isBase cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty isBase",
                       "Firmware package is not uploaded for empty isBase ")
        elif response_body["responseCode"] != "14080":
            testResult(self, "failed", "Firmware package should not be uploaded for empty isBase",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # no IsBase
    @pytest.mark.Smoke
    def test17_negative_fota_firmware_upload_no_IsBase(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_isBase")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14080" or response_body["responseData"][
            "message"] == "isBase cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without isBase parameter",
                       "Firmware package is not uploaded for without isBase parameter ")
        elif response_body["responseCode"] != "14080":
            testResult(self, "failed", "Firmware package should not be uploaded for without isBase parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test18_negative_fota_firmware_upload_invalid_IsFull(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_isFull")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false1"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid isFull",
                       "Firmware package is not uploaded for invalid isFull ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid isFull",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # invalid IsBase
    @pytest.mark.Smoke
    def test19_negative_fota_firmware_upload_empty_IsFull(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = ""
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = ""
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14111" or response_body["responseData"][
            "message"] == "isFull cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty isFull",
                       "Firmware package is not uploaded for empty isFull ")
        elif response_body["responseCode"] != "14111":
            testResult(self, "failed", "Firmware package should not be uploaded for empty isFull",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    # no IsBase
    @pytest.mark.Smoke
    def test20_negative_fota_firmware_upload_no_IsFull(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_isFull")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14111" or response_body["responseData"][
            "message"] == "isFull cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without isFull parameter",
                       "Firmware package is not uploaded for without isFull parameter ")
        elif response_body["responseCode"] != "14111":
            testResult(self, "failed", "Firmware package should not be uploaded for without isFull parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test21_negative_fota_firmware_upload_invalid_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_downloadConsent")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false1"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid downloadConsent",
                       "Firmware package is not uploaded for invalid downloadConsent ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid downloadConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test22_negative_fota_firmware_upload_empty_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = ""
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = ""
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14082" or response_body["responseData"][
            "message"] == "downloadConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty downloadConsent",
                       "Firmware package is not uploaded for empty downloadConsent ")
        elif response_body["responseCode"] != "14082":
            testResult(self, "failed", "Firmware package should not be uploaded for empty downloadConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test23_negative_fota_firmware_upload_no_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_downloadConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14082" or response_body["responseData"][
            "message"] == "downloadConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without downloadConsent parameter",
                       "Firmware package is not uploaded for without downloadConsent parameter ")
        elif response_body["responseCode"] != "14082":
            testResult(self, "failed", "Firmware package should not be uploaded for without downloadConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test24_negative_fota_firmware_upload_invalid_installConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_installConsent")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false1"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid installConsent",
                       "Firmware package is not uploaded for invalid installConsent ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid installConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test25_negative_fota_firmware_upload_empty_installConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = ""
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = ""
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14081" or response_body["responseData"][
            "message"] == "installConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty installConsent",
                       "Firmware package is not uploaded for empty installConsent ")
        elif response_body["responseCode"] != "14081":
            testResult(self, "failed", "Firmware package should not be uploaded for empty installConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test26_negative_fota_firmware_upload_no_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_installConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14081" or response_body["responseData"][
            "message"] == "installConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without installConsent parameter",
                       "Firmware package is not uploaded for without installConsent parameter ")
        elif response_body["responseCode"] != "14081":
            testResult(self, "failed", "Firmware package should not be uploaded for without installConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test27_negative_fota_firmware_upload_invalid_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload_invalid_rebootConsent")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false1"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 202:
            assert True
        else:
            print("Status code is not 202. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for invalid rebootConsent",
                       "Firmware package is not uploaded for invalid rebootConsent ")
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "Firmware package should not be uploaded for invalid rebootConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test28_negative_fota_firmware_upload_empty_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = ""
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = ""
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14083" or response_body["responseData"][
            "message"] == "rebootConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for empty rebootConsent",
                       "Firmware package is not uploaded for empty installConsent ")
        elif response_body["responseCode"] != "14083":
            testResult(self, "failed", "Firmware package should not be uploaded for empty rebootConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test29_negative_fota_firmware_upload_no_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_rebootConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14083" or response_body["responseData"][
            "message"] == "rebootConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without rebootConsent parameter",
                       "Firmware package is not uploaded for without rebootConsent parameter ")
        elif response_body["responseCode"] != "14083":
            testResult(self, "failed", "Firmware package should not be uploaded for without rebootConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test30_negative_fota_firmware_upload_no_description(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = ""

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "no_description")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14075" or response_body["responseData"][
            "message"] == "Description cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for without Description parameter",
                       "Firmware package is not uploaded for without Description parameter ")
        elif response_body["responseCode"] != "14075":
            testResult(self, "failed", "Firmware package should not be uploaded for without Description parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test31_negative_fota_firmware_upload_empty_description(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = ""
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = ""

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file
        response = FOTA_firmwareUpload(self, model, system, "", isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14075" or response_body["responseData"][
            "message"] == "Description cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "Firmware package should not be uploaded for Description",
                       "Firmware package is not uploaded for empty Description ")
        elif response_body["responseCode"] != "14075":
            testResult(self, "failed", "Firmware package should not be uploaded for Description",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test32_negative_fota_firmware_upload_duplicate_package(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            isDiffImage = str(dict1["isDiffImage"])
            isBase = str(dict1["isBase"])
            isFull = str(dict1["isFull"])
            downloadConsent = str(dict1["downloadConsent"])
            rebootConsent = str(dict1["rebootConsent"])
            installConsent = str(dict1["installConsent"])
            packageName = str(dict1["packageName"])
            packageVersion = str(dict1["packageVersion"])
            packagePath = str(dict1["packagePath"])
            description = str(dict1["description"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            isDiffImage = "true"
            isBase = "false"
            isFull = "false"
            downloadConsent = "false"
            rebootConsent = "false"
            installConsent = "false"
            packageName = "test_v111.zip"
            packageVersion = "111"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test firmware upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "fota", system)

        # try to upload new package in case of duplicate
        if upload_url == "duplicated Firmware Version":
            random_id = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])
            dest_filename = 'test_v' + str(random_id) + '.zip'
            print(dest_filename)
            dest_filepath = packagePath + '\\' + dest_filename
            print(dest_filepath)
            shutil.copy2(filepath, dest_filepath)
            filepath = dest_filepath
            packageName = dest_filename
            packageVersion = random_id

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload firmware pacakge file

        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")
        time.sleep(10)
        response = FOTA_firmwareUpload(self, model, system, description, isDiffImage, isBase,
                                       isFull,
                                       downloadConsent, installConsent, rebootConsent, packageName,
                                       packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "14029" or response_body["responseData"][
            "message"] == "duplicated Firmware Version":
            # print('Message : ', message)
            testResult(self, "passed", "Duplicate firmware package should not be uploaded",
                       "Duplicate firmware package is not uploaded ")
        elif response_body["responseCode"] != "14029":
            testResult(self, "failed", "Duplicate firmware package should not be uploaded",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        os.remove(dest_filepath)
        print("----------------------------------------------------------")
