import time

from C2CModules.contextControl_modules import context_Control_for_telemetry_location
from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId, run_paho_command_on_primary_IVI

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
networkType = wifi


class Test_notification:

    def test1_switch_to_hybrid_stub(self):
        # ===========================================================================================
        # Run telemetry - location stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:1 -> Switch to hybrid stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'switch_to_hybrid_stub')
        # time.sleep(15)

        print("Switching to hybrid_stub process is completed, verify logs for telemetry-location details ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Hit context control api with required payload
        # ===========================================================================================

        print("Step:2 -> Hit context control api for publishing telemetry data @ configured frequency : ")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call context control reusable module
        response_body = context_Control_for_telemetry_location(self, systemId)

        assert (response_body["responseCode"] == "1200")

        print("----------------------------------------------------------")

    def test2_switch_to_paho_stub(self):
        # ===========================================================================================
        # Run telemetry - location stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:1 -> Switch to paho stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'switch_to_paho_stub')
        # time.sleep(15)

        print("Switching to paho stub process is completed, verify logs")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Hit context control api with required payload
        # ===========================================================================================

        print("Step:2 -> Hit context control api for publishing telemetry data @ configured frequency : ")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call context control reusable module
        response_body = context_Control_for_telemetry_location(self, systemId)

        assert (response_body["responseCode"] == "1200")

        print("----------------------------------------------------------")

    def test3_switch_to_can_stub(self):
        # ===========================================================================================
        # Run telemetry - location stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:1 -> Switch to can stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'switch_to_can_stub')
        # time.sleep(15)

        print("Switching to can stub process is completed, verify logs")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Hit context control api with required payload
        # ===========================================================================================

        print("Step:2 -> Hit context control api for publishing telemetry data @ configured frequency : ")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call context control reusable module
        response_body = context_Control_for_telemetry_location(self, systemId)

        assert (response_body["responseCode"] == "1200")

        print("----------------------------------------------------------")

    def test4_switch_to_origin(self):
        # ===========================================================================================
        # Run telemetry - location stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:1 -> Switch to origin stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'switch_to_origin')
        # time.sleep(15)

        print("Switching to origin stub process is completed, verify logs")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Hit context control api with required payload
        # ===========================================================================================

        print("Step:2 -> Hit context control api for publishing telemetry data @ configured frequency : ")

        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call context control reusable module
        response_body = context_Control_for_telemetry_location(self, systemId)

        assert (response_body["responseCode"] == "1200")

        print("----------------------------------------------------------")

