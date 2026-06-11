import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.e2e_testData import *
from C2CModules.vehicle_state import *
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.telemetry_modules import telemetry_Curr
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State
deviceSerialNo = b2c_ivi_adbSerialNo

class Test_EOL_Onboarding_R8S4:

    def test_positive_eol_onboarding_r8s4(self):
        print("-----------------------------------------------------------")
        print("Starting device onboarding...")
        print("-----------------------------------------------------------")

        # Step 1: Ensure network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType,
                                           netwrokType)  # fixed typo: netwrokType → networkType

        # Step 2: Fresh onboarding
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        # Step 3: Read VIN and cloud environment
        vin = readVIN_primary_IVI(self, OnboardingType)
        cloudEnv = read_cloud_env(self)

        # Step 4: Pre-Provisioning for regional environments
        if cloudEnv in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            print("\n--- Reading Pre-Provisioning Data ---")
            print("---------------------------------------------")
            print("Read the Pre Provisioning data from the sheet")
            print("---------------------------------------------")

            dict1 = read_api_data_from_excel(self, "Env_Details", cloudEnv)
            mcu = str(dict1["mcu"])
            bin = str(dict1["bin"])
            vcu = str(dict1["vcu"])
            model = str(dict1["model"])
            region = str(dict1["region"])
            country = str(dict1["country"])
            modelDescription = str(dict1["modelDescription"])
            plant = str(dict1["plant"])
            assemblyLine = str(dict1["assemblyLine"])
            shift = str(dict1["shift"])
            modelCode = str(dict1["modelCode"])

            print("Vin: ", vin)
            print("mcu: ", mcu)
            print("bin: ", bin)
            print("vcu: ", vcu)
            print("model: ", model)
            print("region: ", region)
            print("country: ", country)
            print("modelDescription: ", modelDescription)
            print("plant: ", plant)
            print("assemblyLine: ", assemblyLine)
            print("shift: ", shift)
            print("modelCode: ", modelCode)

            # Pre-Provisioning API
            response = EOL_Pre_Provisioning_API(self, vin, mcu, bin, vcu, model, region, country,
                                                modelDescription, plant, assemblyLine, shift, modelCode, "valid")

            # Validate response status code
            assert response.status_code == 200, "Status code is not 200. Rather found : " + str(response.status_code)
            response_body = response.json()

            # Validate API response body
            if response_body["message"] == "Successfully saved vehicle details":
                testResult(self, "passed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API triggered successfully and vehicle details were saved on cloud")
            else:
                testResult(self, "failed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API response is not expected. Vehicle details were not saved on cloud")
                assert False
        else:
            print(f"Skipping Pre-Provisioning: cloudEnv '{cloudEnv}' not supported.")

        # Step 5: Reboot and stub onboarding
        path = "path2"

        try:
            run_command_on_device(self, deviceSerialNo, "reboot")
            for i in range(5):
                outputer = run_command_on_device(self, deviceSerialNo, "root")
                if 'not found' in outputer:
                    print("Device is not up yet post reboot, wait for 60s")
                    time.sleep(60)
                else:
                    break
            print(f"=> command response : {outputer}")

            if is_device_connected(self, deviceSerialNo):
                print("Device is connected after reboot.")
            else:
                print("Device is not connected after reboot.")

            # Command to push file
            push_file = "push C:\\Car2Cloud_E2ETesting\\C2CtestData\\VinNo.txt /data"
            run_command_on_primary_IVI_device(self, deviceSerialNo, push_file)
            time.sleep(5)

            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")
            print("Run Onboarding vin stub on device : ")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * * ")

            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'onboarding_vin_stub')
            time.sleep(15)

            print("Onboarding Vin stub start/run process is completed, verify logs for trip & telemetry details : ")

            # Continuously pull files until the device state is ACTIVE or timeout
            timeout = 180
            interval = 30
            increase_time = 0

            while increase_time <= timeout:
                if is_device_active(self):
                    print("Device is ACTIVE after reboot.")
                    break
                else:
                    print("Device is not ACTIVE yet, pulling files...")
                    if path == "path1":
                        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "DeviceOnboarding")
                    elif path == "path2":
                        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "pullFiles")
                    time.sleep(interval)
                    increase_time += interval
            else:
                print("Device did not become ACTIVE after reboot. Timeout reached.")
        except OSError:
            print("Something went wrong while reading command response")
            outputer = None
        except Exception as e:
            print(f"Something went wrong while rebooting device: {e}")

        # Step 6: Validate chipset & system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global onboarding validation",
                           "Device onboarded to global cloud")
            else:
                testResult(self, "failed", "Global onboarding validation",
                           f"Failed onboarding. State: {system_state}")
        else:
            if system_state in ["PRE_REGIONAL_ACTIVE"]:
                testResult(self, "passed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           "Device connected successfully to regional cloud and state transitioned to PRE_REGIONAL_ACTIVE")
            else:
                testResult(self, "failed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           f"Device is not connected successfully to regional cloud and state is not transitioned to PRE_REGIONAL_ACTIVE. System state: {system_state}")

        # Step 7: Validate metadata
        print("\n=== Validate Vehicle State in Global Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n=== Validate Vehicle State in Regional Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

    def test_positive_activation_API(self):

        print("----------------------------------------------------------")
        print("\nActive the vehicle in Regional Partition be calling the Activation API\n")
        print("----------------------------------------------------------")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)
        action = "activate"

        response = EOL_Activation_API(self, systemId, action, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API validation",
                       "Device activation API triggered and responded successfully")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "passed", "Activation API validation",
                       "Device activation API is not triggered and not responded successfully")
            # self.result.set_result(TestResults.failed)
            assert False

        # Pull files post activation
        time.sleep(10)
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "pullFiles")
        #time.sleep(10)

        # Final system state validation
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Regional onboarding validation",
                       "Device successfully onboarded to regional cloud")
        else:
            testResult(self, "failed", "Regional onboarding validation",
                       f"Device failed to onboard to regional cloud. System state: {system_state}")

        validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, "regional")

