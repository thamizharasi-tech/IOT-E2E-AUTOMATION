import time
import pytest

from C2CModules import c2c_modules
from C2CModules.OTA_modules_b2c_IVI import uploadFirmware, createFirmwareScript, start_OTAservices_on_b2c_IVI, \
    check_FirwareVer_b2c_IVI
from C2CModules.OTA_reuse_modules import listFirmware, listFirmwareScript, triggerFirmwareUpdate, listFirmwareSchedules
from C2CModules.e2e_testData import deviceType_IVI, wifi, b2c_ivi_chipset
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_FOTA_IVI:

    @pytest.mark.positive
    def test1_FOTA_IVI_uploadBaseFirmware(self):

        # ===========================================================================================
        # Upload Base Firmware package for desired vehicle model through API
        # ===========================================================================================

        firmwareId_b = uploadFirmware(self, "baseFirmware", OnboardingType, chipsetType)
        print("Base Firmware Package firmwareId : =>", firmwareId_b)

        # ===========================================================================================
        # Verify uploaded base firmware package details on SMP-UI through API
        # ===========================================================================================

        listFirmware(self, firmwareId_b, OnboardingType, chipsetType)

    @pytest.mark.positive
    def test2_FOTA_IVI_uploadDiffFirmware(self):

        # ===========================================================================================
        # Upload Update/diff Firmware package for desired vehicle model through API
        # ===========================================================================================

        firmwareId_u = uploadFirmware(self, "updateFirmware", OnboardingType, chipsetType)
        print("Update/DiffImage Firmware Package firmwareId : =>", firmwareId_u)

        # ===========================================================================================
        # Verify uploaded Update/diff firmware package details on SMP-UI through API
        # ===========================================================================================

        listFirmware(self, firmwareId_u, OnboardingType, chipsetType)

    @pytest.mark.positive
    def test3_FOTA_IVI_createScript(self):

        # ===========================================================================================
        # Create FOTA script for firmware update for desired model through API
        # ===========================================================================================

        scriptId = createFirmwareScript(self, OnboardingType, chipsetType)

        # ===========================================================================================
        # Verify firmware script details on SMP-UI through API
        # ===========================================================================================

        refId = listFirmwareScript(self, scriptId, OnboardingType, chipsetType)

    @pytest.mark.positive
    def test3_FOTA_IVI_triggerFOTA(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for OTA
        # ===========================================================================================
        start_OTAservices_on_b2c_IVI(self, OnboardingType, chipsetType)

        # ===========================================================================================
        # Capture Device and Cloud details before FOTA Update for validations
        # ===========================================================================================
        check_FirwareVer_b2c_IVI(self, "beforeFOTAupdate", OnboardingType,chipsetType)

        # ===========================================================================================
        # Trigger/Start Firmware update campaign for desired model & script through API
        # ===========================================================================================

        scheduleId = triggerFirmwareUpdate(self, OnboardingType, chipsetType)
        time.sleep(180)

        # ===========================================================================================
        # Verify firmware schedule/campaign details on SMP-UI through API
        # ===========================================================================================

        listFirmwareSchedules(self, scheduleId, OnboardingType, chipsetType)
        time.sleep(180)

        # ===========================================================================================
        # Capture Device and Cloud details after FOTA Update for validations
        # ===========================================================================================
        check_FirwareVer_b2c_IVI(self, "afterFOTAupdate", OnboardingType, chipsetType)

    def test4_FOTAbackup_IVI(self):
        # ===========================================================================================
        # Take backup of all fetched files for debugging or reference
        # ===========================================================================================
        c2c_modules.executionBackup(self, "OTA", "FOTA")










