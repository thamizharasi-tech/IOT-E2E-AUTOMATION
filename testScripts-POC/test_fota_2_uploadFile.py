import random
import shutil
import pytest

from C2CModules.fota_api_modules import FOTA_uploadFile
from C2CModules.OTA_reuse_modules import presignedUrl
from utils.XLUtils import read_api_data_from_excel

# ---------------------------------------------------------
# FOTA-file upload test scripts
# ---------------------------------------------------------


class Test_smoke:

    @pytest.mark.Smoke
    def test1_positive_fota_upload_file(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False
        print("----------------------------------------------------------")

class Test_negative:
    # --------------------------------------------------------------------------
    # Negative=Testdata scripts
    # --------------------------------------------------------------------------
    # invalid presigned url
    @pytest.mark.Smoke
    def test1_negative_fota_upload_file_invalid_presignedUrl(self):
        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        upload_url = upload_url + "ghgdftl"

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "invalid")

        # Validate response status code
        if response.status_code == 403:
            assert True
        else:
            print("Status code is not 403. Rather found : " + str(response.status_code))
            assert False

        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------------------
    # FOTA-file upload : Negative Testcases
    # ---------------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_fota_upload_file_invalid_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "invalid_apiKey")

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
    def test2_negative_fota_upload_file_empty_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "empty_apiKey")

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
    def test3_negative_fota_upload_file_no_apikey(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "no_apiKey")

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
    def test4_negative_fota_upload_file_empty_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "empty_x-requestor")

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
    def test5_negative_fota_upload_file_no_xrequestor(self):

        # read api data from excel sheet
        dict1 = read_api_data_from_excel(self, "FOTA", "FOTA-firmwareUpload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
            system = str(dict1["system"])
            packageName = str(dict1["packageName"])
            packagePath = str(dict1["packagePath"])
        else:
            print("Flag is not set to Yes, hence running with hardcoded/actual data :")
            model = "adp"
            system = "IVI"
            packageName = "test_v111.zip"
            packagePath = r'C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages'

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

            # Call upload package url
            upload_url = presignedUrl(self, model, packageName, "fota", system)

        print(" => Uploaded File : ", filepath)

        # Call module to upload pacakge file
        response = FOTA_uploadFile(self, upload_url, filepath, "no_x-requestor")

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
