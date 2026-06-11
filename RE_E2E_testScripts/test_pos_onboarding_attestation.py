import pytest

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from C2CModules.deviceRegistration_modules import *
from C2CModules.e2e_testData import *
from C2CModules.resuse_modules import verify_message_in_log, search_text_in_file

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
networkType = wifi
deviceSerialNo = b2c_ivi_adbSerialNo

TC = "DeviceOnboarding_validData"
deviceState = ACTIVE_State

class Test_EOL_Onboarding_Attestation:

    def test_positive_eol_onboarding(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "valid")
        time.sleep(10)

        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

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

        validate_vehicle_metadata_by_VIN(self, OnboardingType, chipsetType, "global")

        vehicle_connection_state(self, "global")

    def test_positive_eol_onboarding_qwes_attestation(self):

        print("-----------------------------------------------------------")
        print("Starting device onboarding with QWES ATTESTATION enabled...")
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

        # Step 5: Reboot device
        reboot_primary_IVI_device(self, OnboardingType, chipsetType, "path2")

        # Step 6: Validate system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"\nSystem State: {system_state}")

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

        # Step 7: Validate metadata
        print("\n=== Validate Vehicle State in Global Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n=== Validate Vehicle State in Regional Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        print("\n--- Onboarding Process Completed with QWES ATTESTATION---")

    def test1_supplier_feed_for_mno(self):

        print("\n------------------------------START------------------------------\n")

        """

        This test is validating the Supplier Feed functionality. (positive scenario)

        :return: return test status

        Validate Supplier Feed

        """
        #print("=========GENERATE AND UPDATE IMEI AND ICCID IN CSV========")
        imei = "IMEI" + str(random.randint(1, 1000))
        iccid = "ICCID" + str(random.randint(1, 1000))

        #print("IMEI: ", imei)
        #print("ICCID: ", iccid)

        write_to_csv(self, imei, iccid)

        print("\n------------------SUPPLIER FEED------------------\n")


        response = supplier_feed(self, "valid")

        # Parse API response into JSON

        response_body = response.json()

        # Validate response status code

        if response.status_code == 200:

            # Validate response body

            if response_body["message"] == "Supplier feed Saved Successfully":
                if "supplierFeed" in response_body:
                    if response_body["supplierFeed"][0]["iccid"]:
                        if response_body["supplierFeed"][0]["mnoStatus"] == "Success":
                            trackingId = response_body["supplierFeed"][0]["trackingId"]
                            #testResult(self, "passed",
                             #          "Validate that Supplier feed saved successfully",
                              #         "Supplier feed saved successfully, pls refer api response for detailed info")
                            # verify supplier feed status on the cloud side
                            response = supplier_feed_status(self, trackingId, "valid")
                            # Validate response status code
                            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                                response.status_code)
                            if response.status_code != 200:
                                # self.result.set_result(TestResults.failed)
                                assert False

                            # Parse API response into JSON
                            response_body = response.json()
                            # Validate response body
                            if response_body["message"] == "Data fetched successfully":
                                if response_body["supplierFeed"][0]["mnoStatus"] == "Success" and \
                                        response_body["supplierFeed"][0]["iccid"]:
                                    trackingId_actual = response_body["supplierFeed"][0]["trackingId"]
                                    if trackingId == trackingId_actual:
                                        testResult(self, "passed", "Supplier Feed data should be saved successfully",
                                                   "Supplier Feed data saved successfully")
                                    # self.result.set_result(TestResults.passed)
                            elif response_body["message"] != "Data fetched successfully":
                                # print(response_body["responseData"]["message"])
                                testResult(self, "failed", "Supplier Feed data should be saved successfully",
                                           "Supplier Feed data failed to save" + " Reason for failure is : " +
                                           response_body["message"])
                                # self.result.set_result(TestResults.failed)
                            else:
                                print("Something went wrong. Please check the api response for more info", response_body)
                                # self.result.set_result(TestResults.failed)
                                assert False

                else:
                    testResult(self, "passed",

                               "Validate that Supplier feed saved successfully",

                               "Supplier feed data already saved on the database")
            else:

                testResult(self, "failed",

                       "Validate that Supplier feed is saved successfully",

                       "Supplier feed is not saved, pls refer api response for detailed info")

        elif response.status_code == 400:

            # Validate response body

            if response_body["errors"][0]["message"] == "device imei is already exits":

                testResult(self, "passed",

                       "Validate that Supplier feed is saved or already exists in DB",

                       "Supplier feed is already exits, pls refer api response for detailed info")

            else:

                testResult(self, "failed",

                       "Validate that Supplier feed is saved successfully",

                       "Supplier feed is not saved or does not exits, pls refer api response for detailed info")

        else:

            testResult(self, "failed",

                   "Validate that Supplier feed is saved successfully",

                   "Supplier data is not saved, pls refer api response for detailed info")

    def test_positive_eol_onboarding_mno_attestation(self):

        print("-----------------------------------------------------------")
        print("Starting device onboarding with MNO ATTESTATION enabled...")
        print("-----------------------------------------------------------")

        # Step 1: Ensure network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # Step 2: Fresh onboarding
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "MNO_ATTESTATION")
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
            pass

        # Reboot and stub onboarding
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

            print("Run stub to onboard a device with mno attestation on device : ")
            print("----------------------------------------------------------")

            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "attestation_stub")
            print("Attestation - stub run process is completed, verify logs for details : ")
            print("----------------------------------------------------------")

            # Continuously pull files until the device state is ACTIVE or timeout
            timeout = 300
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

        # Validate chipset & system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global onboarding validation",
                           "Device onboarded to global cloud")
                self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global onboarding validation",
                           f"Failed onboarding. State: {system_state}")
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

        # Step 7: Validate metadata
        print("\n=== Validate Vehicle State in Global Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n=== Validate Vehicle State in Regional Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        print("\n--- Onboarding Process Completed with MNO ATTESTATION ---")
        print("-------------------------------------------------------------------------")

    def test_positive_eol_onboarding_qwes_mno_attestation(self):

        print("-----------------------------------------------------------")
        print("Starting device onboarding with MNO ATTESTATION enabled...")
        print("-----------------------------------------------------------")

        # Step 1: Ensure network connectivity
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # Step 2: Fresh onboarding
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2",
                                                       "QWES_MNO_ATTESTATION")
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
            pass

        # Reboot and stub onboarding
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

            print("Run stub to onboard a device with mno attestation on device : ")
            print("----------------------------------------------------------")

            run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "attestation_stub")
            print("Attestation - stub run process is completed, verify logs for details : ")
            print("----------------------------------------------------------")

            # Continuously pull files until the device state is ACTIVE or timeout
            timeout = 300
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

        # Validate chipset & system state
        system_state = read_vehicleJsonFile(self, "system_state")
        print(f"System State : {system_state}")

        if cloudEnv not in ["GCP-QA3", "RE-DEV", "RE-DM1"]:
            if system_state in ["GLOBAL_ACTIVE", "ACTIVE"]:
                testResult(self, "passed", "Global onboarding validation",
                           "Device onboarded to global cloud")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed", "Global onboarding validation",
                           f"Failed onboarding. State: {system_state}")
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

        # Step 7: Validate metadata
        print("\n=== Validate Vehicle State in Global Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "global")

        print("\n=== Validate Vehicle State in Regional Partition ===")
        validate_vehicle_metadata_by_VIN_v2(self, OnboardingType, chipsetType, "regional")

        print("\n--- Onboarding Process Completed with QWES and MNO ATTESTATION ---")
        print("-------------------------------------------------------------------------")

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

class Test_Onboarding_invalidData:

    ##Before running the script need to update the c2ctestdata

    def test_positive_eol_onboarding_duplicate_deviceId(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "DUPLICATE_DEVICEID")
        time.sleep(10)

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

            # Check if the device is connected
            if is_device_connected(self, deviceSerialNo):
                print("Device is connected after reboot.")
            else:
                print("Device is not connected after reboot.")
        except OSError:
            print("Something went wrong while reading command response")
            outputer = None
        except Exception as e:
            print(f"Something went wrong while rebooting device: {e}")

        time.sleep(20)

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(10)

    def test_try(self):

        # duplicate vehicle onboarding
        log_file_path = C2CtestReport_c2cLogsPath + 'c2clogs.txt'
        pqr_message_type = "Message type: 3 : Encoding type : 2"
        duplicate_vehicle_errorCode = "error : 13140 received in property bag"

        # Check if log file exists
        if not os.path.exists(log_file_path):
            print(f"=> Log file not found: {log_file_path}")
            testResult(
                self, "failed",
                "Validate if the device throws an error when trying to onboard a duplicate device",
                "Log file missing. Unable to validate duplicate onboarding."
            )
        else:
            try:
                with open(log_file_path, "r", encoding="utf-8", errors="ignore") as log_file:
                    log_content = log_file.readlines()

                found_error = False
                for log_entry in log_content:
                    if duplicate_vehicle_errorCode in log_entry.strip():
                        print("=> Error encountered: Device attempted to onboard as a duplicate")
                        testResult(
                            self, "passed",  # Pass if error found
                            "Validate if the device throws an error when trying to onboard a duplicate device",
                            "Device attempted to onboard as a duplicate. Error was detected correctly."
                        )
                        print("C2C logs line data: =>", log_entry.strip())
                        found_error = True
                        break  # Stop searching once found

                if not found_error:
                    print("=> Error message not found in the log file.")
                    testResult(
                        self, "failed",  # Fail if error not found
                        "Validate if the device throws an error when trying to onboard a duplicate device",
                        "Error message not found in logs. The device did not register a duplicate onboarding attempt correctly."
                    )

            except FileNotFoundError:
                print(f"=> Log file not found: {log_file_path}")
                testResult(self, "failed", "Log File Error", "Log file is missing.")
            except PermissionError:
                print(f"=> Permission denied: Unable to access {log_file_path}")
                testResult(self, "failed", "Log File Error", "Permission denied while accessing log file.")
            except UnicodeDecodeError as e:
                print(f"=> Encoding error while reading log file: {e}")
                testResult(self, "failed", "Log File Error", f"Encoding issue: {e}")


    def test_positive_eol_onboarding_duplicate_deviceId_vin(self):
        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # ===========================================================================================
        # Device setup for fresh onboarding
        # ===========================================================================================
        standalone_IVI_bootstrap_device_onboarding_eol(self, OnboardingType, chipsetType, "path2", "DUPLICATE_DEVICEID_VIN")
        time.sleep(10)

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

            # Check if the device is connected
            if is_device_connected(self, deviceSerialNo):
                print("Device is connected after reboot.")
            else:
                print("Device is not connected after reboot.")
        except OSError:
            print("Something went wrong while reading command response")
            outputer = None
        except Exception as e:
            print(f"Something went wrong while rebooting device: {e}")

        time.sleep(15)

        logs_data = pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        # Pull logs and validate message type

        # Validation check
        if logs_data["status"] == "success":
            for log in logs_data["logs"]:
                if '"message_type": 3' in log:
                    print("Valid Message Type Found: 3")
                if '"error": "13140"' in log:
                    print("Error Code 13140 Detected!")
        else:
            print(f"Log retrieval failed: {logs_data['message']}")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

