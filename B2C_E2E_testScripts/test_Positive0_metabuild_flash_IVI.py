import pytest

from C2CModules import primary_IVI_device_modules
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_setNetworkConnectivity_IVI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_setNetworkConnectivity_IVI(self):

        # ===========================================================================================
        # Check Firmware Version
        # ===========================================================================================
        print("Metabuild Flashing on IVI device")
        primary_IVI_device_modules.checkFirmwareVer(self, deviceType, b2c_ivi_chipset)




