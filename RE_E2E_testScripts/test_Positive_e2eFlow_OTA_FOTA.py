import random
import time
from datetime import datetime, timezone

import pytest

from C2CModules.OTA_modules_re_IVI import create_package, verify_uploaded_package_details, read_ecu_details_of_vehicle, \
    read_pacakgeId_from_file, create_campaign, verify_campaign_details, approve_campaign, \
    verify_campaign_vehicle_status, verify_device_cloud_status
from C2CModules.e2e_testData import deviceType_IVI, wifi, b2c_ivi_chipset, testData, otaPackagePath
from C2CModules.primary_IVI_device_modules import read_vehicleJsonFile

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

# Test Data
otaPackagePath_flag = testData("FotaData_RE_IVI", 2, 2)
otaPackagePath_new = testData("FotaData_RE_IVI", 2, 3)
source_fileName = testData("FotaData_RE_IVI", 3, 3)
target_fileName = testData("FotaData_RE_IVI", 4, 3)
otaPackageId_flag = testData("FotaData_RE_IVI", 5, 2)
otaPackageId_new = testData("FotaData_RE_IVI", 5, 3)


class Test_FOTA_IVI:

    @pytest.mark.positive
    def test1_FOTA_IVI_uploadFirmwarePackage(self):

        # ===========================================================================================
        # Upload Base/Source Firmware package for desired vehicle model through API
        # ===========================================================================================
        tc = "target_firmware"

        if otaPackagePath_flag == "No":
            if tc == "source_firmware":
                fileName = source_fileName
                file = otaPackagePath + source_fileName
            else:
                fileName = target_fileName
                file = otaPackagePath + target_fileName
        else:
            if tc == "source_firmware":
                fileName = source_fileName
                file = otaPackagePath_new + source_fileName
            else:
                fileName = target_fileName
                file = otaPackagePath_new + target_fileName

        targetId = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        packageName = str(fileName).replace('.zip', '')
        model = read_ecu_details_of_vehicle(self, systemId, "model")
        ecuName = "hu"
        packageType = "pp"
        sourceVersion = "*"
        targetVersion = 'v' + str(targetId)

        print("--------------------------------------------------------")
        print("systemId : ", systemId)
        print("packageName : ", packageName)
        print("File Name : ", fileName)
        print("File : ", file)
        print("model : ", model)
        print("ecuName : ", ecuName)
        print("packageType : ", packageType)
        print("sourceVersion : ", sourceVersion)
        print("targetVersion : ", targetVersion)
        print("--------------------------------------------------------")

        packageId = create_package(self, packageName, model, ecuName, packageType, sourceVersion, targetVersion,
                                   fileName, file, tc)
        print("Package Id : =>", packageId)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Verify uploaded firmware package details through API
        # ===========================================================================================

        verify_uploaded_package_details(self, packageId, packageName, model, ecuName, packageType, sourceVersion,
                                        targetVersion, fileName, tc)

        print("--------------------------------------------------------")

    @pytest.mark.positive
    def test1_FOTA_IVI_createCampaign(self):

        # ===========================================================================================
        # Create campaign for uploaded firmware package for desired vehicle model/systemId through API
        # ===========================================================================================
        tc = "valid"
        targetId = ' '.join([str(random.randint(10, 9999)).zfill(2) for _ in range(1)])

        if otaPackageId_flag == "No":
            packageId = otaPackageId_new
        else:
            packageId = read_pacakgeId_from_file(self)

        name = "campaign_" + str(targetId)
        type1 = "fota"
        startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
        endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")

        # Read model
        model = read_ecu_details_of_vehicle(self, systemId, "model")

        print("--------------------------------------------------------")
        print("packageId : ", packageId)
        print("name : ", name)
        print("model : ", model)
        print("type : ", type1)
        print("startDate : ", startDate)
        print("endDate : ", endDate)
        print("systemId : ", systemId)

        print("--------------------------------------------------------")

        # call create campaign reusable module
        campaignId = create_campaign(self, name, model, packageId, type1, startDate, endDate, systemId, tc)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Verify newly created campaign details through API
        # ===========================================================================================

        time.sleep(10)
        campaignStatus = "NEW"
        verify_campaign_details(self, campaignId, packageId, name, model, type1, startDate, endDate, systemId,
                                campaignStatus, tc)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Capture Device and Cloud details before FOTA Update for validations
        # ===========================================================================================
        option = "beforeFOTAupdate"
        verify_device_cloud_status(self, option, systemId, campaignId, tc)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Approve newly created campaign details through API
        # ===========================================================================================

        action = "APPROVED"
        approve_campaign(self, campaignId, action, tc)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Verify Approved campaign details through API
        # ===========================================================================================

        time.sleep(10)
        campaignStatus = "APPROVED"
        verify_campaign_details(self, campaignId, packageId, name, model, type1, startDate, endDate, systemId,
                                campaignStatus, tc)

        print("--------------------------------------------------------")

        # ===========================================================================================
        # Capture & Validate Device and Cloud details after FOTA Update
        # ===========================================================================================
        option = "afterFOTAupdate"
        verify_device_cloud_status(self, option, systemId, campaignId, tc)

        print("--------------------------------------------------------")


    def test3_verify_campaign_vehicle_status(self):
        systemId= "7082"
        campaignId = "8135fd66-4e69-45d1-951d-e14aca19d2a7"
        pageNumber = 0
        pageSize = 10
        sort = "updatedTime%2Cdesc"
        tc= "valid"
        verify_campaign_vehicle_status(self, systemId, campaignId, pageNumber, pageSize, sort, tc)

    def test4_verify_device_cloud_status(self):
        # ===========================================================================================
        # Capture Device and Cloud details before FOTA Update for validations
        # ===========================================================================================
        systemId = "6874"
        campaignId = "a9dbb40d-cd50-4456-b5f7-58042ae862a3"
        tc ="valid"
        option = "beforeFOTAupdate"
        verify_device_cloud_status(self, option, systemId, campaignId, tc)

        option = "afterFOTAupdate"
        verify_device_cloud_status(self, option, systemId, campaignId, tc)
