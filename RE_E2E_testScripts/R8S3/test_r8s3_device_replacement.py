import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.e2e_testData import *
from C2CModules.vehicle_metadata import *
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
deviceSerialNo = b2c_ivi_adbSerialNo
networkType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State


class Test_EOL_Onboarding:

    def test_positive_eol_onboarding_regional_replacement(self):

        print("-----------------------------------------------------------")
        print("Starting Fresh device onboarding..")
        print("-----------------------------------------------------------")

        # Step 1: Ensure network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

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
            response = EOL_Pre_Provisioning_API(self, vin, mcu, bin, vcu, model, region, country, modelDescription,
                                                plant, assemblyLine, shift, modelCode, "valid")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                #self.result.set_result(TestResults.failed)
                assert False

            response_body = response.json()
            # Validate API response body
            if response_body["message"] == "Successfully saved vehicle details":
                assert True
                testResult(self, "passed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API triggered successfully and vehicle details were saved on cloud")
                #self.result.set_result(TestResults.passed)

            else:
                testResult(self, "failed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API response is not expected. Vehicle details were not saved on cloud")
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print(f"Skipping Pre-Provisioning: cloudEnv '{cloudEnv}' not supported.")

        # reboot the device after sideloading the conf and certs
        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

        # Validate system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global onboarding validation", "Device onboarded to global cloud")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global onboarding validation", f"Failed onboarding. State: {system_state}")
                #self.result.set_result(TestResults.failed)
        else:
            if system_state in ["PRE_REGIONAL_ACTIVE"]:
                testResult(self, "passed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           "Device connected successfully to regional cloud and state transitioned to PRE_REGIONAL_ACTIVE")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "passed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           f"Device is not connected successfully to regional cloud and state is not transitioned to PRE_REGIONAL_ACTIVE. System state: {system_state}")
                #self.result.set_result(TestResults.failed)

        print("\n===========Validate Vehicle state in Global Partition============\n")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n===========Validate Vehicle state in Regional Partition==========\n")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        print("----------------------------------------------------------")
        print("Activate the vehicle in Regional Partition by calling the Activation API")
        print("----------------------------------------------------------")

        systemId_original = read_vehicleJsonFile(self, "system_id")
        print("System Id [Fresh Onboarding] : ", systemId_original)
        action = "activate"

        response = EOL_Activation_API(self, systemId_original, action, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            #self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API validation",
                       "Device activation API triggered and responded successfully")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "passed", "Activation API validation",
                       "Device activation API is not triggered and not responded successfully")
            #self.result.set_result(TestResults.failed)
            assert False

        # Pull files post activation
        time.sleep(10)
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "pullFiles")
        # time.sleep(10)

        # Final system state validation
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Regional onboarding validation",
                       "Device successfully onboarded to regional cloud")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Regional onboarding validation",
                       f"Device failed to onboard to regional cloud. System state: {system_state}")
            #self.result.set_result(TestResults.failed)

        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("Initiating Device Replacement API Call...")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId_original, "valid")

        # Validate response status code
        assert (
                    response.status_code == 200), f"Device Replacement API status code is not 200. Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] in [
            "State updated to REPLACEMENT successfully",
            "State updated to REGIONAL REPLACEMENT successfully",
            "State updated to REGIONAL_REPLACEMENT  successfully"
        ]:
            testResult(self, "passed", "Device Replacement API should trigger successfully",
                       "Device Replacement API triggered successfully and state updated.")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Device Replacement API should trigger successfully",
                       f"Device Replacement API is not triggered successfully. Message: {response_body['message']}")
            assert False
            #self.result.set_result(TestResults.failed)

        print("\n Validating cloud-side vehicle metadata...\n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_original, "global")

        assert (
                    response.status_code == 200), f"Metadata API status code is not 200. Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            assert False

        response_body = response.json()

        if response_body["message"] == "Data Fetched Successfully":
            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle State Validation",
                           "Lifecycle state correctly set to REGIONAL_REPLACEMENT.")
            else:
                testResult(self, "failed", "Lifecycle State Validation",
                           f"Lifecycle state mismatch. Found: {lifeCycleState}")
        else:
            print("Unexpected response from metadata API:", response_body)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("Starting onboarding using EXISTED ONBOARDED VIN for device replacement...")
        print("---------------------------------------------------------------------------------------")

        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Current System State: {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global Onboarding Validation",
                           "Device successfully onboarded to global cloud.")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global Onboarding Validation",
                           f"Onboarding failed. System state: {system_state}")
                #self.result.set_result(TestResults.failed)
        else:
            if system_state == "PRE_REGIONAL_ACTIVE":
                testResult(self, "passed", "Regional Onboarding Validation",
                           "Device connected to regional cloud and entered PRE_REGIONAL_ACTIVE state.")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Regional Onboarding Validation",
                           f"Device did not enter PRE_REGIONAL_ACTIVE. Found state: {system_state}")
                #self.result.set_result(TestResults.failed)

        print("\n Validating vehicle state in Global Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n Validating vehicle state in Regional Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        print("----------------------------------------------------------")
        print("Activating vehicle in Regional Partition via Activation API...")
        print("----------------------------------------------------------")

        systemId_after_replacement = read_vehicleJsonFile(self, "system_id")
        print("System ID [After Replacement]:", systemId_after_replacement)
        action = "activate"

        response = EOL_Activation_API(self, systemId_after_replacement, action, "valid")

        assert (response.status_code == 200), f"Activation API failed. Status code: {response.status_code}"
        if response.status_code != 200:
            assert False
            #self.result.set_result(TestResults.failed)

        response_body = response.json()

        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API Execution",
                       "Activation API triggered successfully and state updated.")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Activation API Execution",
                       "Activation API did not respond as expected.")
            assert False
            #self.result.set_result(TestResults.failed)

        time.sleep(10)
        pull_files_from_primary_IVI(self, OnboardingType, chipsetType, "pullFiles")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Final System State: {system_state}")

        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Final Onboarding Validation",
                       "Device successfully onboarded to regional cloud.")
            #self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Final Onboarding Validation",
                       f"Final onboarding failed. System state: {system_state}")
            #self.result.set_result(TestResults.failed)

        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        # systemId_actual = read_vehicleJsonFile(self, "system_id")
        # print("System ID After Replacement:", systemId_actual)

        if systemId_original == systemId_after_replacement:
            print("System ID is consistent before and after device replacement.")

            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_after_replacement, "regional")

            assert (
                        response.status_code == 200), f"Metadata API status code is not 200, Rather than found: Status code: {response.status_code}"
            if response.status_code != 200:
                assert False
                #self.result.set_result(TestResults.failed)

            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "REGIONAL_ACTIVE":
                    testResult(self, "passed", "Post-Replacement Lifecycle Validation",
                               "Lifecycle state correctly transitioned to REGIONAL_ACTIVE.")
                    #self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Post-Replacement Lifecycle Validation",
                               f"Unexpected lifecycle state: {lifeCycleState}")
                    #self.result.set_result(TestResults.failed)
            else:
                print("Unexpected response from metadata API:", response_body)
                assert False
                #self.result.set_result(TestResults.failed)
        else:
            print("Device Replacement failed. System ID mismatch.")
            assert False

        print("-------- Regional Device Replacement Validation Completed Successfully --------")

        print("-------------------------------------------------------------------------")

    def test_positive_eol_onboarding_regional_replacement_of_the_replacement(self):

        print("-------------------------------------------------------------------------")
        print("Checking and configuring network connectivity on device if unreachable...")
        print("-------------------------------------------------------------------------")

        # Setup network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        systemId_replacement1 = read_vehicleJsonFile(self, "system_id")
        print(f"System ID of 1st Regional Replacement: {systemId_replacement1}")

        print("\n============ INITIATING REPLACEMENT OF THE REPLACEMENT ============\n")

        print("--------------------------------------------------")
        print("Triggering Device Replacement API (Second Replacement)...")
        print("--------------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId_replacement1, "valid")

        # Validate response status code
        assert (
                    response.status_code == 200), f"Device Replacement API response status code is not 200.Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] in [
            "State updated to REPLACEMENT successfully",
            "State updated to REGIONAL REPLACEMENT successfully",
            "State updated to REGIONAL_REPLACEMENT  successfully"
        ]:
            testResult(self, "passed", "Device Replacement API Execution",
                       "Device Replacement API triggered successfully and state updated.")
            self.result.set_result(TestResults.passed)
        elif response_body["message"] not in [
            "State updated to REPLACEMENT successfully",
            "State updated to REGIONAL REPLACEMENT successfully",
            "State updated to REGIONAL_REPLACEMENT  successfully"
        ]:
            testResult(self, "failed", "Device Replacement API Execution",
                       f"Device Replacement API failed to trigger. Reason: {response_body['message']}")
            self.result.set_result(TestResults.failed)
        else:
            print("Unexpected response from Device Replacement API:", response_body)
            self.result.set_result(TestResults.failed)
            assert False

        # Cloud-side metadata validation
        print("\n Validating cloud-side metadata for replacement...\n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_replacement1, "regional")

        # Validate response status code
        assert (response.status_code == 200), f"Metadata API failed. Status code: {response.status_code}"
        if response.status_code != 200:
            self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle State Validation",
                           "Lifecycle state correctly set to REGIONAL_REPLACEMENT.")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle State Validation",
                           f"Lifecycle state mismatch. Found: {lifeCycleState}")
                self.result.set_result(TestResults.failed)
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            self.result.set_result(TestResults.failed)
        else:
            print("Unexpected response from metadata API:", response_body)
            self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("Onboarding device using EXISTED ONBOARDED VIN for replacement")
        print("Note: One replacement has already been completed")
        print("---------------------------------------------------------------------------------------")

        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Current System State: {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global Onboarding Validation",
                           "Device successfully onboarded to global cloud.")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global Onboarding Validation",
                           f"Onboarding failed. System state: {system_state}")
                self.result.set_result(TestResults.failed)
        else:
            if system_state == "PRE_REGIONAL_ACTIVE":
                testResult(self, "passed", "Regional Onboarding Validation",
                           "Device connected to regional cloud and entered PRE_REGIONAL_ACTIVE state.")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Regional Onboarding Validation",
                           f"Device did not enter PRE_REGIONAL_ACTIVE. Found state: {system_state}")
                self.result.set_result(TestResults.failed)

        print("\n Validating vehicle state in Global Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "global")

        print("\n Validating vehicle state in Regional Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        print("----------------------------------------------------------")
        print(" Activating vehicle in Regional Partition via Activation API...")
        print("----------------------------------------------------------")

        systemId_replacement2 = read_vehicleJsonFile(self, "system_id")
        print(f" System ID [Replacement of the Replacement]: {systemId_replacement2}")
        action = "activate"

        response = EOL_Activation_API(self, systemId_replacement2, action, "valid")

        assert (
                    response.status_code == 200), f"Activation API response status code is not 200.Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            assert False
            self.result.set_result(TestResults.failed)

        response_body = response.json()

        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API Execution",
                       "Activation API triggered successfully and state updated.")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Activation API Execution",
                       "Activation API did not respond as expected.")
            assert False
            self.result.set_result(TestResults.failed)

        time.sleep(10)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Final System State: {system_state}")

        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Final Onboarding Validation",
                       "Device successfully onboarded to regional cloud.")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Final Onboarding Validation",
                       f"Final onboarding failed. System state: {system_state}")
            self.result.set_result(TestResults.failed)

        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        if systemId_replacement1 == systemId_replacement2:
            print("System ID remains unchanged between the first replacement and its subsequent replacement.")

            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_replacement2, "regional")

            assert (
                        response.status_code == 200), f"Metadata API response status code is not 200.Rather than found: Status code: {response.status_code}"
            if response.status_code != 200:
                assert False
                self.result.set_result(TestResults.failed)

            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "REGIONAL_ACTIVE":
                    testResult(self, "passed", "Post-Replacement Lifecycle Validation",
                               "Lifecycle state correctly transitioned to REGIONAL_ACTIVE.")
                    self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Post-Replacement Lifecycle Validation",
                               f"Unexpected lifecycle state: {lifeCycleState}")
                    self.result.set_result(TestResults.failed)
            else:
                print("Unexpected response from metadata API:", response_body)
                assert False
                self.result.set_result(TestResults.failed)
        else:
            print("Device Replacement failed. System ID mismatch.")
            assert False

        print("Regional Replacement of the Device Replacement Validation Completed Successfully")
        print("-------------------------------------------------------------------------")

    def test_positive_eol_onboarding_qwes_regional_replacement(self):

        print("-----------------------------------------------------------")
        print("Starting Fresh device onboarding with QWES ATEESTATION..")
        print("-----------------------------------------------------------")

        # Step 1: Ensure network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # Step 2: Fresh onboarding
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "QWES_ATTESTATION")
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
            response = EOL_Pre_Provisioning_API(self, vin, mcu, bin, vcu, model, region, country, modelDescription,
                                                plant, assemblyLine, shift, modelCode, "valid")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                self.result.set_result(TestResults.failed)
                assert False

            response_body = response.json()
            # Validate API response body
            if response_body["message"] == "Successfully saved vehicle details":
                assert True
                testResult(self, "passed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API triggered successfully and vehicle details were saved on cloud")
                self.result.set_result(TestResults.passed)

            else:
                testResult(self, "failed", "Pre-Provisioning API validation",
                           "Pre-Provisioning API response is not expected. Vehicle details were not saved on cloud")
                assert False
                self.result.set_result(TestResults.failed)
        else:
            print(f"Skipping Pre-Provisioning: cloudEnv '{cloudEnv}' not supported.")

        # reboot the device after sideloading the conf and certs
        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # Validate system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global onboarding validation", "Device onboarded to global cloud")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global onboarding validation", f"Failed onboarding. State: {system_state}")
                self.result.set_result(TestResults.failed)
        else:
            if system_state in ["PRE_REGIONAL_ACTIVE"]:
                testResult(self, "passed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           "Device connected successfully to regional cloud and state transitioned to PRE_REGIONAL_ACTIVE")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "passed",
                           "Device should connects to regional cloud and should enters PRE_REGIONAL_ACTIVE state",
                           f"Device is not connected successfully to regional cloud and state is not transitioned to PRE_REGIONAL_ACTIVE. System state: {system_state}")
                self.result.set_result(TestResults.failed)

        print("\n===========Validate Vehicle state in Global Partition============\n")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "global")

        print("\n===========Validate Vehicle state in Regional Partition==========\n")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        print("----------------------------------------------------------")
        print("Activate the vehicle in Regional Partition by calling the Activation API")
        print("----------------------------------------------------------")

        systemId_original = read_vehicleJsonFile(self, "system_id")
        print("System Id [Fresh Onboarding] : ", systemId_original)
        action = "activate"

        response = EOL_Activation_API(self, systemId_original, action, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            self.result.set_result(TestResults.failed)
            assert False

        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API validation",
                       "Device activation API triggered and responded successfully")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "passed", "Activation API validation",
                       "Device activation API is not triggered and not responded successfully")
            self.result.set_result(TestResults.failed)
            assert False

        # Pull files post activation
        time.sleep(10)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        # time.sleep(10)

        # Final system state validation
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Regional onboarding validation",
                       "Device successfully onboarded to regional cloud")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Regional onboarding validation",
                       f"Device failed to onboard to regional cloud. System state: {system_state}")
            self.result.set_result(TestResults.failed)

        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("Initiating Device Replacement API Call...")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId_original, "valid")

        # Validate response status code
        assert (
                    response.status_code == 200), f"Device Replacement API status code is not 200. Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] in [
            "State updated to REPLACEMENT successfully",
            "State updated to REGIONAL REPLACEMENT successfully",
            "State updated to REGIONAL_REPLACEMENT  successfully"
        ]:
            testResult(self, "passed", "Device Replacement API should trigger successfully",
                       "Device Replacement API triggered successfully and state updated.")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Device Replacement API should trigger successfully",
                       f"Device Replacement API is not triggered successfully. Message: {response_body['message']}")
            assert False
            self.result.set_result(TestResults.failed)

        print("\n Validating cloud-side vehicle metadata...\n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_original, "global")

        assert (
                    response.status_code == 200), f"Metadata API status code is not 200. Rather than found: Status code: {response.status_code}"
        if response.status_code != 200:
            assert False

        response_body = response.json()

        if response_body["message"] == "Data Fetched Successfully":
            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle State Validation",
                           "Lifecycle state correctly set to REGIONAL_REPLACEMENT.")
            else:
                testResult(self, "failed", "Lifecycle State Validation",
                           f"Lifecycle state mismatch. Found: {lifeCycleState}")
        else:
            print("Unexpected response from metadata API:", response_body)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("Starting QWES Attestation onboarding using EXISTED ONBOARDED VIN for device replacement...")
        print("---------------------------------------------------------------------------------------")

        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN_WITH_ATTESTATION")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Current System State: {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global Onboarding Validation",
                           "Device successfully onboarded to global cloud.")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global Onboarding Validation",
                           f"Onboarding failed. System state: {system_state}")
                self.result.set_result(TestResults.failed)
        else:
            if system_state == "PRE_REGIONAL_ACTIVE":
                testResult(self, "passed", "Regional Onboarding Validation",
                           "Device connected to regional cloud and entered PRE_REGIONAL_ACTIVE state.")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Regional Onboarding Validation",
                           f"Device did not enter PRE_REGIONAL_ACTIVE. Found state: {system_state}")
                self.result.set_result(TestResults.failed)

        print("\n Validating vehicle state in Global Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "global")

        print("\n Validating vehicle state in Regional Partition...")
        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        print("----------------------------------------------------------")
        print("Activating vehicle in Regional Partition via Activation API...")
        print("----------------------------------------------------------")

        systemId_after_replacement = read_vehicleJsonFile(self, "system_id")
        print("System ID [After Replacement]:", systemId_after_replacement)
        action = "activate"

        response = EOL_Activation_API(self, systemId_after_replacement, action, "valid")

        assert (response.status_code == 200), f"Activation API failed. Status code: {response.status_code}"
        if response.status_code != 200:
            assert False
            self.result.set_result(TestResults.failed)

        response_body = response.json()

        if response_body["message"] == "State has been successfully updated and shared with device":
            testResult(self, "passed", "Activation API Execution",
                       "Activation API triggered successfully and state updated.")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Activation API Execution",
                       "Activation API did not respond as expected.")
            assert False
            self.result.set_result(TestResults.failed)

        time.sleep(10)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")

        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"Final System State: {system_state}")

        if system_state in ["ACTIVE", "REGIONAL_ACTIVE"]:
            testResult(self, "passed", "Final Onboarding Validation",
                       "Device successfully onboarded to regional cloud.")
            self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed", "Final Onboarding Validation",
                       f"Final onboarding failed. System state: {system_state}")
            self.result.set_result(TestResults.failed)

        validate_vehicle_metadata_by_VIN_v2(self, onboardingType, chipsetType, "regional")

        # systemId_actual = read_vehicleJsonFile(self, "system_id")
        # print("System ID After Replacement:", systemId_actual)

        if systemId_original == systemId_after_replacement:
            print("System ID is consistent before and after device replacement.")

            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId_after_replacement, "regional")

            assert (
                        response.status_code == 200), f"Metadata API status code is not 200, Rather than found: Status code: {response.status_code}"
            if response.status_code != 200:
                assert False
                self.result.set_result(TestResults.failed)

            response_body = response.json()

            if response_body["message"] == "Data Fetched Successfully":
                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "REGIONAL_ACTIVE":
                    testResult(self, "passed", "Post-Replacement Lifecycle Validation",
                               "Lifecycle state correctly transitioned to REGIONAL_ACTIVE.")
                    self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Post-Replacement Lifecycle Validation",
                               f"Unexpected lifecycle state: {lifeCycleState}")
                    self.result.set_result(TestResults.failed)
            else:
                print("Unexpected response from metadata API:", response_body)
                assert False
                self.result.set_result(TestResults.failed)
        else:
            print("Device Replacement failed. System ID mismatch.")
            assert False

        print("-------- Regional Device Replacement Validation Completed Successfully --------")

        print("-------------------------------------------------------------------------")



