from datetime import datetime, timezone
from urllib import response

import pytest

from C2CModules.OTA_modules_re_IVI import *

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import *
from utils.XLUtils import read_api_data_from_excel
from C2CModules.vehicle_metadata import fetch_vehicle_model_by_systemId

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset

# Test Data


class Test_OTA_APIS:

    @pytest.mark.Smoke
    def test1_positive_ota_get_vehicle_ecus(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_vehicle_ecus")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = read_vehicleJsonFile(self, "system_id")
            ota_get_vehicle_ecus(self,systemId,"valid")


        print("systemId: ", systemId)

        # Verify command & control response
        response = ota_get_vehicle_ecus(self,systemId,"valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Master configuration should be updated successfully",
                           "ota get vehicle ecus is updated successfully")
            assert True
        else:
            testResult(self, "failed", "Master configuration should be created successfully",
                       "ota get vehicle ecus is updated is not updated successfully")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test2_positive_ota_generate_presigned_url(self):
        print("----------------------------------------------------------")
        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_generate_presigned_url")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["systemId"])
            packageName = str(dict1["systemId"])
            fileName = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = read_vehicleJsonFile(self, "system_id")
            model = read_ecu_details_of_vehicle(self, systemId, "model")
            fileName = "fotapackage" + ''.join([str(random.randint(1, 9)).zfill(1) for _ in range(1)]) + ".zip"
            packageName = fileName
            #fileName = "fotapackage81.zip?"

        print("model: ", model)
        print("packageName: ", packageName)
        print("fileName: ", fileName)
        #print("action: ", action)

        # generate pre-signed url for package upload
        response = ota_generate_presigned_url(self, model, packageName, fileName, "UPLOAD", "source_fileName")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Read pre-signed url from api response body
        message = response_body["message"]
        if message == "Success":
            presignedUrl = response_body["presignedUrlInfo"]["presignedUrl"]
        else:
            print("Incorrect message")
            presignedUrl = ''
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_positive_ota_upload_package(self):

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_package_upload")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            file = str(dict1["file"])
            presignedUrl = str(dict1["presignedUrl"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            file = r"C:\Car2Cloud_E2ETesting\C2CtestData\usr\local\OTApackages"
            dict1 = read_api_data_from_excel(self, "API_Data", "ota_generate_presigned_url")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            qcToken = json_object["token"]
            presignedUrl = json_object["presignedUrlInfo"]["presignedUrl"]

        # upload package
        print("File : ", file)
        response = ota_package_upload(self, presignedUrl, file, "valid")

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

    @pytest.mark.Smoke
    def test3_positive_ota_create_package(self):
        print("----------------------------------------------------------")

        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_create_package")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            packageName = str(dict1["packageName"])
            ecuName = str(dict1["ecuName"])
            packageType = str(dict1["packageType"])
            sourceVersion = str(dict1["sourceVersion"])
            targetVersion = str(dict1["targetVersion"])
            fileName = str(dict1["fileName"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            packageName = "fotapackage81.zip"  # Replace with actual package name
            model = "adp"  # Replace with actual model value
            ecuName = "hu"  # Replace with actual ECU name
            packageType = "pp"  # Replace with actual package type
            sourceVersion = "s3"  # Replace with actual source version
            targetVersion = "s81"  # Replace with actual target version
            fileName = "fotapackage81.zip?"  # Replace with actual file name
            ota_create_package(self, model, packageName, fileName, ecuName, packageType, sourceVersion, targetVersion,
                               "valid")

        print("model: ", model)
        print("packageName: ", packageName)
        print("ecuName: ", ecuName)
        print("packageType: ", packageType)
        print("sourceVersion: ", sourceVersion)
        print("targetVersion: ", targetVersion)
        print("fileName: ", fileName)

        # Verify command & control response
        response = ota_create_package(self, model, packageName, fileName, ecuName, packageType, sourceVersion,
                                      targetVersion, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "OTA Trigger Campaign should be updated successfully",
                       "ota create package is updated successfully")
            assert True
        else:
            testResult(self, "failed", "OTA Trigger Campaign should be created successfully",
                       "ota create package is not updated successfully")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test12_positive_get_all_campaign_info(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Ota_api_get_all_campaign_info")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            campaign_id = str(dict1["campaignId"])  # Get campaignId from Excel
            system_id = str(dict1.get("systemId", "default_system_id"))  # Get system_id from Excel or use default
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            campaign_id = "default_campaign_id"  # Default value for campaignId
            system_id = "default_system_id"  # Default value for system_id

        print("Campaign ID: ", campaign_id)
        print("System ID: ", system_id)

        # Call the function to get campaign info
        response = ota_get_campaign_info(self, campaign_id, "Test Case 1")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        assert response.status_code == 200, f"Response status is not as expected. Found: {response.status_code}"

        # Validate response body
        if response_body.get("message") == "Success":
            testResult(self, "passed", "Fetching campaign info should be successful",
                       "Fetching campaign info is successful")
            assert True
        else:
            testResult(self, "failed", "Fetching campaign info should be successful",
                       "Fetching campaign info is not successful")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test13_positive_Ota_API_create_package(self):
        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Ota_api_creating_package")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            package_name = str(dict1["packageName"])
            ecu_name = str(dict1["ecuName"])
            package_type = str(dict1["packageType"])
            target_version = str(dict1["targetVersion"])
            source_version = str(dict1["sourceVersion"])
            system_id = str(dict1.get("systemId", "default_system_id"))  # Get system_id from Excel or use default
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Adp"
            package_name = "fotapackage81.zip"
            ecu_name = "hu"
            package_type = "pp"
            target_version = "s81"
            source_version = "s3"
            system_id = "default_system_id"  # Default value for system_id

        print("Model: ", model)
        print("Package Name: ", package_name)
        print("ECU Name: ", ecu_name)
        print("Package Type: ", package_type)
        print("Target Version: ", target_version)
        print("Source Version: ", source_version)
        print("System ID: ", system_id)

        # Call the function to create the package
        response = ota_create_package(self, model, package_name, ecu_name, package_type, target_version,
                                         source_version, system_id, "Test Case 1")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        assert response.status_code == 200, f"Response status is not as expected. Found: {response.status_code}"

        # Validate response body
        if response_body.get("message") == "Success":
            testResult(self, "passed", "Creation of package should be successful",
                       "Creation of package is successful")
            assert True
        else:
            testResult(self, "failed", "Creation of package should be successful",
                       "Creation of package is not successful")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test14_positive_Ota_API_update_campaign_status(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Ota_api_updating_campaign_status")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            campaign_id = str(dict1["campaignId"])  # Get campaignId from Excel
            system_id = str(dict1.get("systemId", "default_system_id"))  # Get system_id from Excel or use default
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            campaign_id = "default_campaign_id"  # Default value for campaignId
            system_id = "default_system_id"  # Default value for system_id

        print("Campaign ID: ", campaign_id)
        print("System ID: ", system_id)

        # Call the function to update the campaign status
        response = ota_updating_campaign_status(self, campaign_id, "Test Case 1")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        assert response.status_code == 200, f"Response status is not as expected. Found: {response.status_code}"

        # Validate response body
        if response_body.get("message") == "Success":
            testResult(self, "passed", "Updating campaign status should be successful",
                       "Updating campaign status is successful")
            assert True
        else:
            testResult(self, "failed", "Updating campaign status should be successful",
                       "Updating campaign status is not successful")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test15_positive_Ota_API_create_campaign(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Ota_creating_campaign")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            name = str(dict1["name"])
            type = str(dict1["type"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            releaseNotes = str(dict1["releaseNotes"])
            title = str(dict1["title"])
            briefDescription = str(dict1["briefDescription"])
            description = str(dict1["description"])
            language = str(dict1["language"])
            steps = dict1["steps"]  # Assuming steps is a list or dict
            packageId = str(dict1["packageId"])
            sequentialUpdatesRequired = dict1.get("sequentialUpdatesRequired", False)
            rollbackRequired = dict1.get("rollbackRequired", False)
            signRequired = dict1.get("signRequired", False)
            encryptionRequired = dict1.get("encryptionRequired", False)
            consent = dict1.get("consent", False)
            download = dict1.get("download", False)
            install = dict1.get("install", False)
            reboot = dict1.get("reboot", False)
            vehiclePropertie = dict1.get("vehiclePropertie", None)
            system_id = str(dict1.get("systemId", "default_system_id"))  # Get system_id from Excel or use default
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Adp"
            name = "Test Campaign"
            type = "OTA"
            startDate = "2023-01-01"
            endDate = "2023-12-31"
            releaseNotes = "Initial release"
            title = "Campaign Title"
            briefDescription = "Brief description of the campaign"
            description = "Detailed description of the campaign"
            language = "en"
            steps = []  # Default to an empty list
            packageId = "default_package_id"
            sequentialUpdatesRequired = False
            rollbackRequired = False
            signRequired = False
            encryptionRequired = False
            consent = False
            download = False
            install = False
            reboot = False
            vehiclePropertie = None
            system_id = "default_system_id"  # Default value for system_id

        print("Model: ", model)
        print("Name: ", name)
        print("Type: ", type)
        print("Start Date: ", startDate)
        print("End Date: ", endDate)
        print("Release Notes: ", releaseNotes)
        print("Title: ", title)
        print("Brief Description: ", briefDescription)
        print("Description: ", description)
        print("Language: ", language)
        print("Steps: ", steps)
        print("Package ID: ", packageId)
        print("Sequential Updates Required: ", sequentialUpdatesRequired)
        print("Rollback Required: ", rollbackRequired)
        print("Sign Required: ", signRequired)
        print("Encryption Required: ", encryptionRequired)
        print("Consent: ", consent)
        print("Download: ", download)
        print("Install: ", install)
        print("Reboot: ", reboot)
        print("Vehicle Properties: ", vehiclePropertie)
        print("System ID: ", system_id)

        # Call the function to create the campaign
        response = ota_create_campaign(self, model, name, type, startDate, endDate, releaseNotes, title,
                                         briefDescription, description, language, steps, packageId,
                                         sequentialUpdatesRequired, rollbackRequired, signRequired,
                                         encryptionRequired, consent, download, install, reboot,
                                         vehiclePropertie, "Test Case 1")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        assert response.status_code == 200, f"Response status is not as expected. Found: {response.status_code}"

        # Validate response body
        if response_body.get("message") == "Success":
            testResult(self, "passed", "Creating campaign should be successful",
                       "Creating campaign is successful")
            assert True
        else:
            testResult(self, "failed", "Creating campaign should be successful",
                       "Creating campaign is not successful")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test16_positive_ota_update_campaign(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "API_Data", "Ota_update_campaign")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            name = str(dict1["name"])
            type = str(dict1["type"])
            startDate = str(dict1["startDate"])
            endDate = str(dict1["endDate"])
            precondition = str(dict1["precondition"])
            key = str(dict1["key"])  # Assuming key is a string
            value = str(dict1["value"])  # Assuming value is a string
            releaseNotes = str(dict1["releaseNotes"])
            title = str(dict1["title"])
            briefDescription = str(dict1["briefDescription"])
            description = str(dict1["description"])
            language = str(dict1["language"])
            steps = dict1["steps"]  # Assuming steps is a list or dict
            packageId = str(dict1["packageId"])
            sequentialUpdatesRequired = dict1.get("sequentialUpdatesRequired", False)
            rollbackRequired = dict1.get("rollbackRequired", False)
            signRequired = dict1.get("signRequired", False)
            encryptionRequired = dict1.get("encryptionRequired", False)
            consent = dict1.get("consent", False)
            download = dict1.get("download", False)
            install = dict1.get("install", False)
            reboot = dict1.get("reboot", False)
            vehiclePropertie = dict1.get("vehiclePropertie", None)
            system_id = str(dict1.get("systemId", "default_system_id"))  # Get system_id from Excel or use default
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Adp"
            name = "Updated Campaign"
            type = "OTA"
            startDate = "2023-01-01"
            endDate = "2023-12-31"
            precondition = "None"
            key = "exampleKey"
            value = "exampleValue"
            releaseNotes = "Updated release"
            title = "Updated Campaign Title"
            briefDescription = "Updated brief description of the campaign"
            description = "Updated detailed description of the campaign"
            language = "en"
            steps = []  # Default to an empty list
            packageId = "default_package_id"
            sequentialUpdatesRequired = False
            rollbackRequired = False
            signRequired = False
            encryptionRequired = False
            consent = False
            download = False
            install = False
            reboot = False
            vehiclePropertie = None
            system_id = "default_system_id"  # Default value for system_id

        print("Model: ", model)
        print("Name: ", name)
        print("Type: ", type)
        print("Start Date: ", startDate)
        print("End Date: ", endDate)
        print("Precondition: ", precondition)
        print("Key: ", key)
        print("Value: ", value)
        print("Release Notes: ", releaseNotes)
        print("Title: ", title)
        print("Brief Description: ", briefDescription)
        print("Description: ", description)
        print("Language: ", language)
        print("Steps: ", steps)
        print("Package ID: ", packageId)
        print("Sequential Updates Required: ", sequentialUpdatesRequired)
        print("Rollback Required: ", rollbackRequired)
        print("Sign Required: ", signRequired)
        print("Encryption Required: ", encryptionRequired)
        print("Consent: ", consent)
        print("Download: ", download)
        print("Install: ", install)
        print("Reboot: ", reboot)
        print("Vehicle Properties: ", vehiclePropertie)
        print("System ID: ", system_id)

        # Call the function to update the campaign
        response = ota_update_campaign(self, model, name, type, startDate, endDate, precondition, key, value,
                                       releaseNotes, title, briefDescription, description, language, steps, packageId,
                                       sequentialUpdatesRequired, rollbackRequired, signRequired,
                                       encryptionRequired, consent, download, install, reboot,
                                       vehiclePropertie)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        assert response.status_code == 200, f"Response status is not as expected. Found: {response.status_code}"

        # Validate response body
        if response_body.get("message") == "Success":
            testResult(self, "passed", "Updating campaign should be successful",
                       "Updating campaign is successful")
            assert True
        else:
            testResult(self, "failed", "Updating campaign should be successful",
                       "Updating campaign is not successful")
            assert False

        print("----------------------------------------------------------")

    # Ota_API_triggering_campaign
    @pytest.mark.Smoke
    def test1_positive_ota_trigger_campaign(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_trigger_campaign")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            campaignId = str(dict1["campaignId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            campaignId = "e3699584-41ba-4210-8831-66f44e106501"

        print("campaignId: ", campaignId)

        # Verify command & control response
        response = ota_trigger_campaign(self, campaignId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "SUCCESS":
            testResult(self, "passed", "OTA Trigger Campaign should be updated successfully",
                       "OTA Trigger Campaign is updated successfully")
            assert True
        else:
            testResult(self, "failed", "OTA Trigger Campaign should be created successfully",
                       "OTA Trigger Campaign is not updated successfully")
            assert False

        print("----------------------------------------------------------")

    # Ota_API_campaign_consent_info_vehicle
    # class Test_Ota_API_campaign_consent_info_vehicle:
    @pytest.mark.Smoke
    def test2_positive_ota_get_campaign_consent_info(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_campaign_consent_info")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            campaignId = str(dict1["campaignId"])
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            campaignId = "cec1513d-6ac5-4f24-8460-86230e55c1cf"
            systemId = "7290"
            ota_get_campaign_consent_info(self, systemId, campaignId, "valid")

        print("campaignId: ", campaignId)
        print("systemId: ", systemId)

        # Verify command & control response
        response = ota_get_campaign_consent_info(self, systemId, campaignId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Consent Info Vehicle should be updated successfully",
                       "Consent Info Vehicle is updated successfully")
            assert True
        else:
            testResult(self, "failed", "Consent Info Vehicle should be created successfully",
                       "Consent Info Vehicle is not updated successfully")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test3_positive_ota_blacklists_vehicles(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_blacklists_vehicles")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            reason = str(dict1["reason"])
            date = str(dict1["date"])
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            reason = "ass"
            date = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            systemId = "7288"

        print("reason: ", reason)
        print("date: ", date)
        print("systemId: ", systemId)

        # Verify command & control response
        response = ota_blacklists_vehicles(self, systemId, reason, date, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "SUCCESS":
            testResult(self, "passed", " BlackList Vehicle  should be success",
                       "BlackList Vehicle is success")
            assert True
        else:
            testResult(self, "failed", "BlackList Vehicle should be success",
                       "BlackList Vehicle is not success")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test4_positive_ota_get_blacklists_vehicles(self):
        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_blacklists_vehicles")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            systemId = str(dict1["systemId"])
            status = str(dict1["status"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "6864"
            status = "Triggerd"

        print("systemId:", systemId)
        print("status:", status)

        # Verify command & control response
        response = ota_get_blacklists_vehicles(self, systemId, status, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

            # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Fetch BlackList Vehicle should be success",
                       "Fetch BlackList Vehicle is success")
            assert True
        else:
            testResult(self, "failed", "Fetch BlackList Vehicle should be success",
                       "Fetch BlackList Vehicle is not success")
            assert False

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test5_positive_ota_revoke_blacklists_vehicles(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_revoke_blacklists_vehicles")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            reason = str(dict1["reason"])
            date = str(dict1["date"])
            systemId = str(dict1["systemId"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            reason = "ass"
            date = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            systemId = "6864"
        print("reason: ", reason)
        print("date: ", date)
        print("systemId: ", systemId)

        # Verify command & control response
        response = ota_revoke_blacklists_vehicles(self, systemId, reason, date, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

        # Validate response body
        if response_body["message"] == "SUCCESS":
            testResult(self, "passed", "Revoke BlackList Vehicle should be success",
                       "Revoke BlackList Vehicle is success")
            assert True
        else:
            testResult(self, "failed", "Revoke BlackList Vehicle should be success",
                       "Revoke BlackList Vehicle is not success")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test6_positive_ota_get_campaign_vehicle_status(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_campaign_vehicle_status")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            campaignId = str(dict1["campaignId"])
            pageNumber = str(dict1["pageNumber"])
            pagesize = str(dict1["pagesize"])
            sort = str(dict1["sort"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            campaignId = "cec1513d-6ac5-4f24-8460-86230e55c1cf"
            pageNumber = "1"
            pagesize = "10"
            sort = "updatedTime%2Cdesc"
        print("campaignId: ", campaignId)
        print("pageNumber:", pageNumber)
        print("pagesize:", pagesize)
        print("sort:", sort)

        # Verify command & control response
        response = ota_get_campaign_vehicle_status(self, campaignId, pageNumber, pagesize, sort, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

            # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Fetch Vehicle Campaign status should be success",
                       "Fetch Vehicle Campaign status is success")
            assert True
        else:
            testResult(self, "failed", "Fetch Vehicle Campaign status should be success",
                       "Fetch Vehicle Campaign status is not success")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test7_positive_ota_get_all_campaign_info(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_all_campaign_info")
        if dict1['Flag'] == "YES":
            print("Flag is set to Yes, hence running with Excel data:")
            pageNumber = str(dict1["model"])
            pageSize = str(dict1["version"])
            sort = str(dict1["sort"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            pageNumber = "0"
            pageSize = "10"
            sort = "updatedTime%2Cdesc"

        print("pageNumber: ", pageNumber)
        print("pageSize: ", pageSize)
        print("sort: ", sort)

        # Verify command & control response
        response = ota_get_all_campaign_info(self, pageNumber, pageSize, sort, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

            # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Fetch all  vehicle campaign Info should be success",
                       "Fetch all  vehicle campaign Info is success")
            assert True
        else:
            testResult(self, "failed", "Fetch all  vehicle campaign Info should be success",
                       "Fetch all  vehicle campaign Info is not success")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test8_positive_ota_get_package_info_by_model(self):
        print("----------------------------------------------------------")

        # Read API test data from Excel sheet
        dict1 = read_api_data_from_excel(self, "OTA_API", "ota_get_package_info_by_model")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with Excel data:")
            model = str(dict1["model"])
            ecuName = str(dict1["ecuName"])
            pageNo = str(dict1["pageNo"])
            pagesize = str(dict1["pagesize"])
            sort = str(dict1["sort"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Adp"
            ecuName = "hu"
            pageNo = "1"
            pagesize = "10"
            sort = "updatedTime%2Cdesc"
        print("model: ", model)
        print("ecuName: ", ecuName)
        print("pageNo:", pageNo)
        print("pagesize:", pagesize)
        print("sort:", sort)

        # Verify command & control response
        response = ota_get_package_info_by_model(self, model, ecuName, pageNo, pagesize, sort, "valid")

        # Parse API response into JSON
        response_body = response.json()

        # Validate response status code
        if response.status_code == 200:
            assert True
        else:
            print("Response status is not as expected OR something went wrong, please check API response")
            assert False

            # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed",
                       "fetching packages by model and ECU name with pagination status should be success",
                       "fetching packages by model and ECU name with pagination status  is success")
            assert True
        else:
            testResult(self, "failed",
                       "fetching packages by model and ECU name with pagination status should be success",
                       "fetching packages by model and ECU name with pagination  status is not success")
            assert False

        print("----------------------------------------------------------")










