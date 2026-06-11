import pytest, time

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

class Test1_DeviceOnboarding:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test1_DeviceOnboarding(self):
        print("\n================Start Test Execution================")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding : Stop all running services on devices and replace side-loaded/conf
        # files with default ones
        # ===========================================================================================
        cleanUp_IVI_script(self, OnboardingType, chipsetType)
        time.sleep(5)

        # ===========================================================================================
        # Register new device and setup device for onboarding
        # ===========================================================================================
        standalone_IVI_device_reg_to_CldConnEstb(self, OnboardingType, chipsetType, TC)
        time.sleep(10)

        # ===========================================================================================
        # Run all required soft-sku & c2c services
        # ===========================================================================================
        run_c2cServices_on_primary_IVI(self, OnboardingType, chipsetType)
        time.sleep(10)

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "DeviceOnboarding")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================

        validate_chipset_and_system_state_IVI(self, OnboardingType, chipsetType, deviceState)

        # ===========================================================================================
        # Save VIN no in a file
        # ===========================================================================================

        saveVIN_IVI(self, OnboardingType, chipsetType)


    def test2_cleanup(self):
        # ===========================================================================================
        # Take backup of all fetched files for debugging or reference
        # ===========================================================================================
        executionBackup(self, TC, "Positive")





