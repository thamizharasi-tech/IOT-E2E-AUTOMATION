import pytest, time
import subprocess

from C2CModules.e2e_testData import b2c_ivi_chipset, deviceType_IVI
from C2CModules.flash_image_modules import flash_hlos_image_on_device

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset

class Test_flashHLOSimage_IVI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test1_generate_HLOSimage_IVI(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Flash HLOS image on IVI device
        # ===========================================================================================
        moba_path = "C:\Program Files (x86)\Mobatek\MobaXterm\MobaXterm.exe"
        subprocess.run((f'{moba_path} -newtab ssh my_server "mkdir test_dir"'))

        print("\n================Execution Ends================")

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test2_flash_HLOSimage_IVI(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Flash HLOS image on IVI device
        # ===========================================================================================
        flash_hlos_image_on_device(self, deviceType, chipsetType)

        print("\n================Execution Ends================")




