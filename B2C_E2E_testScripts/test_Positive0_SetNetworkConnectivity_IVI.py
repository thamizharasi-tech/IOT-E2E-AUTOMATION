import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_setNetworkConnectivity_IVI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_setNetworkConnectivity_IVI(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        print("\n================Execution Ends================")




