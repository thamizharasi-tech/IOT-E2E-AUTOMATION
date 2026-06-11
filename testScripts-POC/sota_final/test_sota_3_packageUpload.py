import os
import random
import shutil
import time

import pytest

from C2CModules.sota_api_modules import SOTA_uploadFile, SOTA_uploadPackage
from C2CModules.OTA_reuse_modules import presignedUrl
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel


# ---------------------------------------------------------
# SOTA-package upload negative test scripts
# ---------------------------------------------------------
class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_sota_package_upload(self):
        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                           isFull,
                                           downloadConsent, installConsent, rebootConsent, packageName,
                                           packageVersion, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15000" and response_body["responseData"]["message"] == "Success":
            packageId = response_body["responseData"]["packageId"]
            print('Package Id : ', packageId)
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should be uploaded successfully",
                       "SOTA package is uploaded successfully ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "success":
            testResult(self, "failed", "SOTA package should be uploaded successfully",
                       "Failed to upload SOTA pacakge " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
            
        except:
            print()
        print("----------------------------------------------------------")


class Test_negative:
    # ---------------------------------------------------------------------------------------
    # SOTA-package upload API : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_sota_package_upload_invalid_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_sota_firware_upload_empty_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "empty_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "api keys are not matching" in response_body["message"] or response_body[
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_sota_fimware_upload_no_apikey(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_apiKey")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_sota_package_upload_empty_xrequestor(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "empty_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "x-requestor header cannot be blank" in response_body["message"] or response_body[
            "message"] == "x-requestor header cannot be blank":
            # self.result.set_result(TestResults.passed)
            assert True
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_sota_package_upload_no_xrequestor(self):

        global dest_filepath
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_x-requestor")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        if "Required authentication headers are missing" in response_body["message"] or response_body[
            "message"] == "Required authentication headers are missing..!!!!":
            assert True
            # self.result.set_result(TestResults.passed)
        else:
            print("Response/Error message is not as expected OR something went wrong, pls check api response")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # -----------h---------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid model-contain special char
    @pytest.mark.Smoke
    def test6_negative_sota_package_upload_invalid_model(self):
        dest_filepath = ""
        # valid model name for file upload
        valid_model_name = "adp"
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_model")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15014" and response_body["responseData"][
            "message"] == "model contains special characters":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid model",
                       "SOTA package is not uploaded for invalid model ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15014":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # invalid empty model
    @pytest.mark.Smoke
    def test7_negative_sota_package_upload_empty_model(self):
        global dest_filepath
        # valid model name for file upload
        valid_model_name = "adp"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15009" and response_body["responseData"][
            "message"] == "model cannot be null or empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty model",
                       "SOTA package is not uploaded for empty model ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15009":
            testResult(self, "failed", "SOTA package should not be uploaded for empty model",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # invalid model-contain special char
    @pytest.mark.Smoke
    def test8_negative_sota_package_upload_no_model(self):
        global dest_filepath
        # valid model name for file upload
        valid_model_name = "adp"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, valid_model_name, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_model")

        # Validate response status code
        if response.status_code == 400:
            print("API response status code is :", str(response.status_code))
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15009" and response_body["responseData"][
            "message"] == "model cannot be null or empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without model parameter",
                       "SOTA package is not uploaded for without model parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "14001":
            testResult(self, "failed", "SOTA package should not be uploaded for without model parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # invalid system-contain special char
    @pytest.mark.Smoke
    def test9_negative_sota_package_upload_invalid_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_system")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, invalid_system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15007" and response_body["responseData"][
            "message"] == "System name is invalid":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid system",
                       "SOTA package is not uploaded for invalid system ")
            # self.result.set_result(TestResults.passed)

        elif response_body["responseCode"] != "15007":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False

        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # invalid empty system
    @pytest.mark.Smoke
    def test10_negative_sota_package_upload_empty_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15029" and response_body["responseData"][
            "message"] == "system cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty system",
                       "SOTA package is not uploaded for empty system ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15029":
            testResult(self, "failed", "SOTA package should not be uploaded for empty system",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)
        except:
            print()
        print("----------------------------------------------------------")

    # invalid without system parameter
    def test11_negative_sota_package_upload_no_system(self):
        global dest_filepath
        # valid system for file upload
        valid_system = "IVI"
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", valid_system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_system")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15029" and response_body["responseData"][
            "message"] == "system cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without system parameter",
                       "SOTA package is not uploaded for without system parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15029":
            testResult(self, "failed", "SOTA package should not be uploaded for without system parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # invalid IsDiffImage
    @pytest.mark.Smoke
    def test12_negative_sota_package_upload_invalid_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_isDiffImage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid isDiffImage",
                       "SOTA package is not uploaded for invalid isDiffImage ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid isDiffImage",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # invalid IsDiffImage
    @pytest.mark.Smoke
    def test13_negative_sota_package_upload_empty_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15056" and response_body["responseData"][
            "message"] == "isDiffImage cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty isDiffImage",
                       "SOTA package is not uploaded for empty isDiffImage ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15056":
            testResult(self, "failed", "SOTA package should not be uploaded for empty isDiffImage",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    # no IsDiffImage
    @pytest.mark.Smoke
    def test14_negative_sota_package_upload_no_IsDiffImage(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_isDiffImage")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15056" and response_body["responseData"][
            "message"] == "isDiffImage cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for wothout isDiffImage parameter",
                       "SOTA package is not uploaded for without isDiffImage parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15056":
            testResult(self, "failed", "SOTA package should not be uploaded for without isDiffImage parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test21_negative_sota_package_upload_invalid_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_downloadConsent")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid downloadConsent",
                       "SOTA package is not uploaded for invalid downloadConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid downloadConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test22_negative_sota_package_upload_empty_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15058" and response_body["responseData"][
            "message"] == "downloadConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty downloadConsent",
                       "SOTA package is not uploaded for empty downloadConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15058":
            testResult(self, "failed", "SOTA package should not be uploaded for empty downloadConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test23_negative_sota_package_upload_no_downloadConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_downloadConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15058" and response_body["responseData"][
            "message"] == "downloadConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without downloadConsent parameter",
                       "SOTA package is not uploaded for without downloadConsent parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15058":
            testResult(self, "failed", "SOTA package should not be uploaded for without downloadConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test24_negative_sota_package_upload_invalid_installConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_installConsent")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid installConsent",
                       "SOTA package is not uploaded for invalid installConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid installConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test25_negative_sota_package_upload_empty_installConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15059" and response_body["responseData"][
            "message"] == "installConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty installConsent",
                       "SOTA package is not uploaded for empty installConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15059":
            testResult(self, "failed", "SOTA package should not be uploaded for empty installConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test26_negative_sota_package_upload_no_installConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_installConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15059" and response_body["responseData"][
            "message"] == "installConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without installConsent parameter",
                       "SOTA package is not uploaded for without installConsent parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15059":
            testResult(self, "failed", "SOTA package should not be uploaded for without installConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test27_negative_sota_package_upload_invalid_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage_invalid_rebootConsent")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for invalid rebootConsent",
                       "SOTA package is not uploaded for invalid rebootConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Json Parse Error":
            testResult(self, "failed", "SOTA package should not be uploaded for invalid rebootConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test28_negative_sota_package_upload_empty_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15057" and response_body["responseData"][
            "message"] == "rebootConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for empty rebootConsent",
                       "SOTA package is not uploaded for empty installConsent ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15057":
            testResult(self, "failed", "SOTA package should not be uploaded for empty rebootConsent",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test29_negative_sota_package_upload_no_rebootConsent(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_rebootConsent")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15057" and response_body["responseData"][
            "message"] == "rebootConsent cannot be null":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without rebootConsent parameter",
                       "SOTA package is not uploaded for without rebootConsent parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15057":
            testResult(self, "failed", "SOTA package should not be uploaded for without rebootConsent parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test30_negative_sota_package_upload_no_description(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = ""

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "no_description")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15043" and response_body["responseData"][
            "message"] == "description cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for without Description parameter",
                       "SOTA package is not uploaded for without Description parameter ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15043":
            testResult(self, "failed", "SOTA package should not be uploaded for without Description parameter",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test31_negative_sota_package_upload_empty_description(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = ""

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file
        response = SOTA_uploadPackage(self, model, system, "", isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15043" and response_body["responseData"][
            "message"] == "description cannot be empty":
            # print('Message : ', message)
            testResult(self, "passed", "SOTA package should not be uploaded for Description",
                       "SOTA package is not uploaded for empty Description ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15043":
            testResult(self, "failed", "SOTA package should not be uploaded for Description",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)

        except:
            print()
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test32_negative_sota_package_upload_duplicate_package(self):
        global dest_filepath
        # valid system for file upload
        dest_filename = ""
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "SOTA", "SOTA-uploadPackage")
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
            packageName = "apkpure_v1.zip"
            packageVersion = "1"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'
            description = " test sota package upload "

        # print(packagePath, packageName)
        filepath = packagePath + '\\' + packageName

        # Call upload package url
        upload_url = presignedUrl(self, model, packageName, "sota", system)

        # try to upload new package in case of duplicate
        if upload_url == "File already exists":
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
            upload_url = presignedUrl(self, model, packageName, "sota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = SOTA_uploadFile(self, upload_url, filepath, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Call module to upload sota pacakge file

        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")
        time.sleep(10)
        response = SOTA_uploadPackage(self, model, system, description, isDiffImage, isBase,
                                      isFull,
                                      downloadConsent, installConsent, rebootConsent, packageName,
                                      packageVersion, "invalid")

        # Validate response status code
        if response.status_code == 400:
            assert True
        else:
            print("Status code is not 400. Rather found : " + str(response.status_code))
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15040" and response_body["responseData"][
            "message"] == "File already exists":
            # print('Message : ', message)
            testResult(self, "passed", "Duplicate sota package should not be uploaded",
                       "Duplicate sota package is not uploaded ")
            # self.result.set_result(TestResults.passed)
        elif response_body["responseCode"] != "15040":
            testResult(self, "failed", "Duplicate sota package should not be uploaded",
                       " Reason for failure is : " +
                       response_body["responseData"]["message"])
            # self.result.set_result(TestResults.failed)
            assert False
        else:
            print("Something went wrong")
            # self.result.set_result(TestResults.failed)
            assert False

        # Clean up/Delete package file
        try:
            if dest_filepath != "":
                os.remove(dest_filepath)            
        except:
            print()
        print("----------------------------------------------------------")
