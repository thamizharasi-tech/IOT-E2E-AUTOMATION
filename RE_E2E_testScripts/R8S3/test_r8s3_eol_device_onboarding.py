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

class Test_EOL_Onboarding_R8S3:

    def test_positive_eol_onboarding_r8s3(self):

        # Setup network connectivity if unreachable
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)
        #c2c_health(self, OnboardingType, chipsetType, "push_health_script")

        # Fresh onboarding
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        #Read the vin
        vin = readVIN_primary_IVI(self, OnboardingType)

        dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
        Env = str(dict["Value"])

        print("---------------------------------------------")
        print("Read the Pre Provisioning data from the sheet")
        print("---------------------------------------------")

        dict1 = read_api_data_from_excel(self, "Env_Details", Env)
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
        response = EOL_Pre_Provisioning_API(self, vin, mcu, bin, vcu, model, region, country, modelDescription, plant, assemblyLine, shift, modelCode, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        # Validate API response body
        if response_body["message"] == "Successfully saved vehicle details":
            assert True
            testResult(self, "passed", "Pre-Provisioning API validation", "Pre-Provisioning API triggered successfully and vehicle details were saved on cloud")

        else:
            testResult(self, "failed", "Pre-Provisioning API validation", "Pre-Provisioning API response is not expected. Vehicle details were not saved on cloud")
            assert False

        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

        # Validate system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state in ["GLOBAL_ACTIVE", "ACTIVE", "PRE_REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Global onboarding validation",
                       "Device successfully onboarded to global cloud")
        else:
            testResult(self, "failed", "Global onboarding validation",
                       f"Device failed to onboard to global cloud. System state: {system_state}")

        print("\n===========Validate Vehicle state in Global Partition============\n")
        validate_vehicle_metadata_by_systemId(self, OnboardingType, chipsetType, "global")

        print("\n===========Validate Vehicle state in Regional Partition==========\n")
        validate_vehicle_metadata_by_systemId(self, OnboardingType, chipsetType, "regional")

        #c2c_health(self, OnboardingType, chipsetType, "pull_health_report")

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
            testResult(self, "failed", "Activation API validation",
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

        validate_vehicle_metadata_by_systemId(self, OnboardingType, chipsetType, "regional")

    def test_try(self):

        print("Keep the device in permissive mode after reboot")

        # Command to disable Wi-Fi
        set_permissive = "shell setenforce 0"

        # Command to enable Wi-Fi
        check_status = "shell getenforce"

        set_permissive_output = run_command_on_primary_IVI_device(self, deviceSerialNo, set_permissive)

        check_status_output = run_command_on_primary_IVI_device(self, deviceSerialNo, check_status)

        if "Permissive" in check_status_output:
            print("Device is in permissive mode")
        else:
            print(f"Device is not in permissive mode. Found: {check_status_output}")
