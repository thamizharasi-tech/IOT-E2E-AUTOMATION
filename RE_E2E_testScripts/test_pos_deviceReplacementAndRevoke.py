import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.primary_IVI_device_modules import run_paho_command_on_primary_IVI, pull_logs_from_IVI_device, \
    read_vehicleJsonFile, run_command_on_primary_IVI_device
from C2CModules.e2e_testData import *
from C2CModules.vehicle_metadata import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
deviceSerialNo = b2c_ivi_adbSerialNo
netwrokType = wifi
TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State


class Test_EOL_Onboarding:

    def test_positive_eol_onboarding_global_replacement(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "global")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("SystemId Before Replacement: ", systemId)

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to GLOBAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to GLOBAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "GLOBAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is set to GLOBAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is not set to GLOBAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

    @pytest.mark.smoke
    def test_positive_device_rehoming_v2(self):

        print("----------------------------------------------------------")
        print("Rehome the vehicle with predefined input/data")
        print("----------------------------------------------------------")

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        print("System Id : ", systemId)
        action = "rehome"

        # Call api reusable module
        response = deviceRehoming(self, systemId, action, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

        vehicle_connection_state(self, "regional")

    def test_positive_eol_onboarding_regional_replacement(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "global")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("SystemId Before Replacement: ", systemId)

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to REGIONAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to REGIONAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is set to REGIONAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is not set to REGIONAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

    def test_positive_eol_onboarding_regional_replacement_with_attestation(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2", "QWES_ATTESTATION")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "global")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("SystemId Before Replacement: ", systemId)

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to REGIONAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to REGIONAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "regional")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is set to REGIONAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is not set to REGIONAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN_WITH_ATTESTATION")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

    def test_positive_eol_onboarding_global_replacement_of_the_replacement(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "global")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("SystemId Before Replacement: ", systemId)

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to GLOBAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to GLOBAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "GLOBAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is set to GLOBAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is not set to GLOBAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

        print("\n=============DEVICE REPLACEMENT OF THE REPLACEMENT============\n")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to GLOBAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to GLOBAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "GLOBAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is set to GLOBAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to GLOBAL_REPLACEMENT",
                           "Lifecycle state is not set to GLOBAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

    def test_positive_eol_onboarding_regional_replacement_of_the_replacement(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", + system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "global")

        systemId = read_vehicleJsonFile(self, "system_id")
        print("SystemId Before Replacement: ", systemId)

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to REGIONAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to REGIONAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "regional")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is set to REGIONAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is not set to REGIONAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failedto send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

        print("\n============REPLACEMENT OF THE REPLACEMENT=============\n")

        print("----------------------------------------------")
        print("* * * * TRIGGER DEVICE REPLACEMENT API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceReplacement(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "State updated to REPLACEMENT successfully" or response_body[
            "message"] == "State updated to REGIONAL REPLACEMENT successfully":
            testResult(self, "passed", "Device Replacement API should be triggered successfully",
                       "Successfully triggered device replacement")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "State updated to REPLACEMENT successfully" or response_body[
            "message"] != "State updated to REGIONAL REPLACEMENT successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device Replacement API should be triggered successfully",
                       "Failed to trigger device replacement API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # call vehicle metadata API reusable module
        print("\n ==>Cloud side validation \n")

        response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "regional")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":

            lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
            if lifeCycleState == "REGIONAL_REPLACEMENT":
                testResult(self, "passed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is set to REGIONAL_REPLACEMENT")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Lifecycle state should set to REGIONAL_REPLACEMENT",
                           "Lifecycle state is not set to REGIONAL_REPLACEMENT")
        elif response_body["message"] != "Data Fetched Successfully":
            assert False
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        print("---------------------------------------------------------------------------------------")
        print("* * * * * ONBOARD A DEVICE USING EXISTED ONBOARDED VIN FOR DEVICE REPLACEMENT * * * * *")
        print("---------------------------------------------------------------------------------------")
        standalone_IVI_bootstrap_device_onboarding_eol(self, onboardingType, chipsetType, "path2",
                                                       "EXISTED_ONBOARDED_VIN")
        time.sleep(10)

        reboot_primary_IVI_device(self, onboardingType, chipsetType, "path2")

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "GLOBAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in global",
                       "Device successfully onboarded in global")
        else:
            testResult(self, "failed", "Device should onboard Successfully in global",
                       "Failed to onboard a device in global" + "\n" "Reason for failure is: ", system_state)

        systemId_actual = read_vehicleJsonFile(self, "system_id")
        print("SystemId After Replacement: ", systemId)

        # call vehicle metadata API reusable module
        if systemId == systemId_actual:
            print("Before Device Replacement and After Device Replacement of the systemId is same")
            response = vehicle_get_vehicle_metadata_new(self, "1", "10", systemId, "global")
            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
            if response.status_code != 200:
                # self.result.set_result(TestResults.failed)
                assert False

            # Parse API response into JSON
            response_body = response.json()
            # Validate response body
            if response_body["message"] == "Data Fetched Successfully":

                lifeCycleState = response_body["responseData"]["vehicleDetails"][0]["lifecycleState"]
                if lifeCycleState == "GLOBAL_ACTIVE":
                    testResult(self, "passed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is set to GLOBAL_ACTIVE")
                    # self.result.set_result(TestResults.passed)
                else:
                    testResult(self, "failed", "Lifecycle state should set to GLOBAL_ACTIVE",
                               "Lifecycle state is not set to GLOBAL_ACTIVE")
            elif response_body["message"] != "Data Fetched Successfully":
                assert False
                # self.result.set_result(TestResults.failed)
            else:
                print("Something went wrong. Please check the api response for more info", response_body)
                # self.result.set_result(TestResults.failed)
                assert False

        else:
            print("Device Replacement is failed")
            assert False

        print("---------------------------------------")
        print("Rehome the device in regional partition")
        print("---------------------------------------")

        # Call api reusable module
        response = deviceRehoming(self, systemId, "rehome", "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "The device is ready to be rehomed.":
            systemId_actual = response_body["systemId"]
            if systemId == systemId_actual:
                testResult(self, "passed", "Device rehoming request should sent to device",
                           "Device rehoming request sent to device")
                # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "The device is ready to be rehomed.":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Device rehoming request should sent to device",
                       "Failed to send the rehoming request to device" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        # =======================================================================================================
        # Pull/Fetch all required files such as conf,license, logs from device post event check for validations
        # =======================================================================================================
        time.sleep(20)
        pull_files_from_primary_IVI(self, onboardingType, chipsetType, "pullFiles")
        time.sleep(10)

        # ===========================================================================================
        # Validate chipset & system state
        # ===========================================================================================
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")
        if system_state == "REGIONAL_ACTIVE" or system_state == "ACTIVE":
            testResult(self, "passed", "Device should onboard Successfully in regional cloud",
                       "Device successfully onboarded in regional cloud")
        else:
            testResult(self, "failed", "Device should onboard Successfully in regional cloud",
                       "Failed to onboard a device in regional cloud" + "\n" "Reason for failure is: ", system_state)

        validate_vehicle_metadata_by_VIN(self, onboardingType, chipsetType, "regional")

    # Device Revoke
    def test_positive_eol_onboarding_device_certificate_revoke(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        systemId = read_vehicleJsonFile(self, "system_id")

        print("SystemId Before Replacement: ", systemId)

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER CERTIFICATE REVOKE API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceRevoke(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Certificate revoked successfully":
            testResult(self, "passed", "Certificate Revoke API should be triggered successfully",
                       "Successfully triggered Certificate Revoke request")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Certificate revoked successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Certificate Revoke API should be triggered successfully",
                       "Failed to trigger certificate revoke API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False

        time.sleep(900)

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(5)

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(5)

        print("Validate telemetry after certificate revoke")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Odometer stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_odo")
        time.sleep(5)

        print("Telemetry-Odometer stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # Telemetry-Odometer

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for odometer",
                       "Device logs contains the logs for odometer, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odometer logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Odometer",
                       "Device logs doesnot contain the logs for Odometer or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odometer value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value):
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")


class Test_certificate_revoke:

    # Device Revoke
    def test_positive_eol_onboarding_device_certificate_revoke(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, onboardingType, chipsetType, netwrokType)

        systemId = read_vehicleJsonFile(self, "system_id")

        print("SystemId Before Replacement: ", systemId)

        # vehicle_connection_state(self, "global")

        print("----------------------------------------------")
        print("* * * * TRIGGER CERTIFICATE REVOKE API * * * *")
        print("----------------------------------------------")

        # Call device replacement reusable module
        response = EOL_deviceRevoke(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()
        # Validate response body
        if response_body["message"] == "Certificate revoked successfully":
            testResult(self, "passed", "Certificate Revoke API should be triggered successfully",
                       "Successfully triggered Certificate Revoke request")
            # self.result.set_result(TestResults.passed)
        elif response_body["message"] != "Certificate revoked successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Certificate Revoke API should be triggered successfully",
                       "Failed to trigger certificate revoke API" + " Reason for failure is : " +
                       response_body["message"])
            # self.result.set_result(TestResults.failed)
        else:
            print("Something went wrong. Please check the api response for more info", response_body)
            # self.result.set_result(TestResults.failed)
            assert False
        time.sleep(600)

    def test_positive_certificate_revoke_network_down_after_15_mins(self):

        time.sleep(300)

        # Command to disable Wi-Fi
        disable_network = "shell cmd -w wifi set-wifi-enabled disabled"

        # Command to enable Wi-Fi
        enable_network = "shell cmd -w wifi set-wifi-enabled enabled"

        run_command_on_primary_IVI_device(self, deviceSerialNo, disable_network)

        time.sleep(10)

        run_command_on_primary_IVI_device(self, deviceSerialNo, enable_network)

        time.sleep(10)

        # pull the files
        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        """
            Finds all occurrences of specific messages in a log file.
            Returns a dictionary where each message maps to a list of matching lines with line numbers.
            """
        log_messages = [
            "MQTTClient_connect5 failed with error: -1",
            "Cloud MQTT connect failed",
            "The certificate is still valid for day : 0 sec",
            "c2c_edge_cloud_mqtt_init failed",
            "Reconnection failed with cloud",
            "INTERNET IS DOWN ADDING TO LOCAL PRIO QUEUE"
        ]

        log_file_path = r"C:\Car2Cloud_E2ETesting\C2CtestReport\e2eExecution_Backup\c2cLogs\c2clogs.txt"
        found_messages = {msg: [] for msg in log_messages}

        try:
            with open(log_file_path, "r", encoding="latin-1", errors="replace") as log_file:
                for line_number, line in enumerate(log_file, 1):
                    for msg in log_messages:
                        if msg in line:
                            found_messages[msg].append({
                                "line_number": line_number,
                                "log_line": line.strip()
                            })

            any_found = any(found_messages[msg] for msg in log_messages)

            if any_found:
                print("\nAt least one failure message found in logs.")
                for msg, matches in found_messages.items():
                    if matches:
                        print(f"\n'==>{msg}' occurred {len(matches)} time(s):")
                        for match in matches:
                            print(f"  Line {match['line_number']}: {match['log_line']}")
            else:
                print("No failure messages were found in the log.")

        except FileNotFoundError:
            print(f"Log file not found: {log_file_path}")
        except Exception as e:
            print(f"Error reading log file: {e}")

        print("----------------------------------------------------------")

        print("Validate telemetry after certificate revoke")

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run Telemetry-Odometer stub on device : ")

        run_paho_command_on_primary_IVI(self, onboardingType, chipsetType, "telemetry_odo")
        time.sleep(5)

        print("Telemetry-Odometer stub run process is completed, verify logs for telemetry details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, onboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # Telemetry-Odometer

        print("-----------------------------")
        print("Device Side Validations : ")
        print("-----------------------------")

        # verify Odo meter attribute in the device logs
        ls = verify_message_in_log(self, telemetry_odo_attribute, telemetry_odo_attribute)

        if telemetry_odo_attribute in str(ls[0]):
            print(f"Odometer attribute name printed in device log : ' {telemetry_odo_attribute} ' ")
            testResult(self, "passed",
                       "Device logs should contain the logs for odometer",
                       "Device logs contains the logs for odometer, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Odometer logs is not present or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed",
                       "Device logs should contain the logs for Odometer",
                       "Device logs doesnot contain the logs for Odometer or failed to read the device log, pls refer device logs for "
                       "detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations : ")
        print("-----------------------------")

        # verify odometer value @ cloud

        # Get systemId and hit telemetry request
        systemId = read_vehicleJsonFile(self, "system_id")
        value = reasonCode = ""

        response = telemetry_Curr_eventType(self, telemetry_odo_event_type, systemId, "valid")

        # Parse API response into JSON
        response_body = response.json()

        try:
            dataList_len = len(response_body["responseData"]["signals"])
            for j in range(dataList_len):
                if response_body["responseData"]["signals"][j]["name"] == telemetry_curr_Odo:
                    value = response_body["responseData"]["signals"][j]["value"]
                    reasonCode = response_body["responseData"]["signals"][j]["reasonCode"]
                    break
        except:
            value = response_body["responseData"]["signals"][0]["value"]
            print("dataList is empty in api response")

        print("Odometer value configured in the stub : ", telemetry_odometer_value)
        print("Odometer value stored in Cloud DB : ", value)

        if float(value) == float(telemetry_odometer_value):
            testResult(self, "failed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is stored in the Cloud DB and same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "passed",
                       "Odometer value should be stored in the Cloud DB and same as that of configured in the stub running on device",
                       "Odometer value is not stored in the Cloud DB or same as that of configured in the stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")
