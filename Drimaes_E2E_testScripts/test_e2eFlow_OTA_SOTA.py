import time
import pytest

from C2CModules import c2c_modules
from C2CModules.OTA_modules_drimaes_IVI import uploadPackage, start_OTAservices_on_drimaes_IVI, createSOTAScript, \
    checkPackage
from C2CModules.OTA_reuse_modules import listPackages, listSOTAScript, triggerSOTAUpdate, listSOTAupdateSchedules
from C2CModules.device_reuse_modules import set_network_connectivity_on_device
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset, wifi

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi

class Test_SOTA_E2E_IVI:

    @pytest.mark.positive
    def test1_SOTA_IVI_uploadPackage(self):

        # ===========================================================================================
        # Upload package for desired vehicle model through API
        # ===========================================================================================
        packageId = uploadPackage(self, OnboardingType)
        print("Package Id : =>", packageId)

        # ===========================================================================================
        # Verify uploaded package details on SMP-UI through API
        # ===========================================================================================
        time.sleep(30)
        listPackages(self, packageId, OnboardingType)

    @pytest.mark.positive
    def test2_SOTA_IVI_INSTALL(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for OTA
        # ===========================================================================================
        start_OTAservices_on_drimaes_IVI(self, OnboardingType)

        # ===========================================================================================
        # Create SOTA INSTALL script for package update for desired model through API
        # ===========================================================================================

        scriptId = createSOTAScript(self, "INSTALL", OnboardingType)
        print("ScriptId : =>", scriptId)

        # ===========================================================================================
        # Verify SOTA script details on SMP-UI through API
        # ===========================================================================================
        time.sleep(60)
        refId = listSOTAScript(self, scriptId, "INSTALL", OnboardingType)  # return refId
        #print("refId : =>", refId)

        # ===========================================================================================
        # Capture Device and Cloud details before SOTA Update for validations
        # ===========================================================================================
        checkPackage(self, "beforeSOTAupdate", "INSTALL", OnboardingType)

        # ===========================================================================================
        # Trigger/Start package update campaign for desired model & script through API
        # ===========================================================================================
        time.sleep(120)
        scheduleId = triggerSOTAUpdate(self, refId, "INSTALL", OnboardingType)  # return scheduleId
        print("ScheduleId : =>", scheduleId)

        # ===========================================================================================
        # Verify Package update schedule/campaign details on SMP-UI through API
        # ===========================================================================================
        time.sleep(30)
        listSOTAupdateSchedules(self, scheduleId, "INSTALL", OnboardingType)

        # ===========================================================================================
        # Capture Device and Cloud details after SOTA Update for validations
        # ===========================================================================================
        checkPackage(self, "afterSOTAupdate", "INSTALL", OnboardingType)

    @pytest.mark.positive
    def test3_SOTAbackup_IVI(self):
        # ===========================================================================================
        # Take backup of all fetched files for debugging or reference
        # ===========================================================================================
        #c2c_modules.executionBackup(self, "OTA", "SOTA")
        checkPackage(self, "afterSOTAupdate", "INSTALL", OnboardingType)






