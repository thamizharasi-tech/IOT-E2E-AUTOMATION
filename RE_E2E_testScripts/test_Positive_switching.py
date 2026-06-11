import pytest

from C2CModules.primary_IVI_device_modules import *

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test1_switching:

    @pytest.mark.regression
    def test1_switch_to_stub(self):
        # ===========================================================================================
        # Switch to paho commands
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run trip start stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "switch_to_stub")
        time.sleep(15)

        print("Switch to stub process is completed, verify device logs: ")
        print("----------------------------------------------------------")

    @pytest.mark.regression
    # Validate telemetry functionality.
    def test1_switch_to_origin(self):
        # ===========================================================================================
        # Switch to origin for can commands
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run trip start stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "switch_to_orig")
        time.sleep(15)

        print("Switch to stub process is completed, verify device logs: ")
        print("----------------------------------------------------------")