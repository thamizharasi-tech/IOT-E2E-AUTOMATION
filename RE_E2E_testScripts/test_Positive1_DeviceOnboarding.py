import pytest, time

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State


class Test1_DeviceOnboarding:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test1_DeviceOnboarding(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding(self, OnboardingType, chipsetType, TC)
        time.sleep(10)

        # ===========================================================================================
        # Run all required c2c services
        # ===========================================================================================
        run_c2cServices_on_primary_IVI(self, OnboardingType, chipsetType)
        time.sleep(60)

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        print("----------------------------------------------------------")
        print("Device Side Validations : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================

        validate_chipset_and_system_state_IVI(self, OnboardingType, chipsetType, deviceState)

        # ===========================================================================================
        # Save VIN no in a file
        # ===========================================================================================

        saveVIN_IVI(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Cloud Side Validations : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Validate life cycle state
        # ===========================================================================================

        validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, deviceState)

