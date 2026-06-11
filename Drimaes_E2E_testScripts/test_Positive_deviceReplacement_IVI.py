import pytest, time

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset, wifi
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import deviceReplacement_IVI, run_c2cServices_on_primary_IVI

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi

class Test_deviceReplacement:

    @pytest.mark.regression
    # Replace TCU .
    def test1_deviceReplacement_IVI(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Device Replacement
        # ===========================================================================================
        deviceReplacement_IVI(self, OnboardingType, chipsetType)
        time.sleep(5)

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)
        time.sleep(5)

        # ===========================================================================================
        # Run all required soft-sku & c2c services
        # ===========================================================================================
        run_c2cServices_on_primary_IVI(self, OnboardingType, chipsetType)
        time.sleep(10)

        print("================Execution Ends================")


