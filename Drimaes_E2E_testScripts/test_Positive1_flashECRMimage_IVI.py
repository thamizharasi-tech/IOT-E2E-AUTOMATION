import pytest, time

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.flash_image_modules import flash_ecrm_image_on_device

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset

class Test_flashECRMimage_IVI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test1_flash_ECRMimage_IVI(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Flash HLOS image on IVI device
        # ===========================================================================================
        flash_ecrm_image_on_device(self, deviceType, chipsetType)

        print("\n================Execution Ends================")




