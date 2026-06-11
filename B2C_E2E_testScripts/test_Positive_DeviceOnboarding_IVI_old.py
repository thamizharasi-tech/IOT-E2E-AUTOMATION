import pytest, time
from playwright.sync_api import sync_playwright

from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import *
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page

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

        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")

        # Step - 1
        try:

            print("Step:1 -> Launch B2C Web UI : ")

            playwright = sync_playwright().start()
            browser = playwright.chromium.launch(headless=False, args=["--start-maximised"])
            context = browser.new_context()
            # Open new page
            page = context.new_page()

            # Initiating the Page Object
            vehicleList_page = vehicleList_Page(page)

            # Navigate to B2C Page
            vehicleList_page.launch_b2c_web()

            print("B2C Web UI is loaded successfully")
            testResult(self, "passed", "B2C Web UI application should be launched successfully ",
                       "B2C Web UI application is launched successfully")
        except:

            testResult(self, "failed", "B2C Web UI application should be launched successfully ",
                       "B2C Web UI application is not launched")

        print("-------------------------------------------------------------------------")

        # Step - 2

        print("Step:2 -> User should land on Vehicle List Page : ")

        try:
            # Verify vehicle List tab and then click on it
            vehicleList_page.verify_vehicleList_tab()
            vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)

            # Verify current page url
            vehicleList_page.verify_vehicleList_page_url()

            print("Landed on Vehicle List page")

            testResult(self, "passed", "User should navigate to / land on Vehicle List page ",
                       "User is navigated to / landed on Vehicle List page successfully ")
        except:
            testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

        print("-------------------------------------------------------------------------")

        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            # Verify system Id in UI table
            status, device_status, package_name = vehicleList_page.verify_system_id_in_table(systemId)

            # Step - 3

            print("Step:3 -> Verify newly onboarded ' System Id ' on Vehicle List UI Page : ")

            if status == "present":
                print("System Id is listed in UI table on Vehicle List page")

                testResult(self, "passed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page",
                           "System Id of newly onboarded device is listed in UI table on Vehicle List page")
            else:
                testResult(self, "failed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                           "System Id of newly onboarded device is not listed in UI table on Vehicle List page")

            # Step - 4

            print("Step:4 -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            if device_status == "Active":
                print("Device Status is shown as ACTIVE on Vehicle List UI page")

                testResult(self, "passed", "Device Status should be ACTIVE on Vehicle List UI page",
                           "Device Status is shown as ACTIVE on Vehicle List UI page")
            else:
                testResult(self, "failed",
                           "Device Status should be ACTIVE on Vehicle List UI page  ",
                           "Device Status is not ACTIVE on Vehicle List UI page")

            # Step - 5

            print("Step:5 -> Verify newly onboarded device ' Package ' name on Vehicle List UI Page : ")

            if package_name == "Essential":
                print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
                print("By default device should have Essential package")

                testResult(self, "passed", "By default device should have 'Essential' package",
                           "By default device is having 'Essential' package")
            else:
                print(f"Package : ' {package_name} ' is shown instead of ' Essential ' on Vehicle List UI page")
                testResult(self, "failed",
                           "By default device should have 'Essential' package",
                           "By default device is not having 'Essential' package")

        except:
            testResult(self, "failed",
                       "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                       "Something went wrong, while verifying newly onboarded device details on Vehicle List Page")

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    def test2_cleanup(self):
        # ===========================================================================================
        # Take backup of all fetched files for debugging or reference
        # ===========================================================================================
        #executionBackup(self, TC, "Positive")

        # ===========================================================================================
        # Login with valid credentials
        # ===========================================================================================

        print("-------------------------------------------------------------------------")

        # Step - 1
        try:

            print("Step:1 -> Launch B2C Web UI : ")

            playwright = sync_playwright().start()
            browser = playwright.chromium.launch(headless=False, args=["--start-maximised"])
            context = browser.new_context()
            # Open new page
            page = context.new_page()

            # Initiating the Page Object
            vehicleList_page = vehicleList_Page(page)

            # Navigate to B2C Page
            vehicleList_page.launch_b2c_web()

            print("B2C Web UI is loaded successfully")
            testResult(self, "passed", "B2C Web UI application should be launched successfully ",
                       "B2C Web UI application is launched successfully")
        except:

            testResult(self, "failed", "B2C Web UI application should be launched successfully ",
                       "B2C Web UI application is not launched")

        print("-------------------------------------------------------------------------")

        # Step - 2

        print("Step:2 -> User should land on Vehicle List Page : ")

        try:
            # Verify vehicle List tab and then click on it
            vehicleList_page.verify_vehicleList_tab()
            vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)

            # Verify current page url
            vehicleList_page.verify_vehicleList_page_url()

            print("Landed on Vehicle List page")

            testResult(self, "passed", "User should navigate to / land on Vehicle List page ",
                       "User is navigated to / landed on Vehicle List page successfully ")
        except:
            testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

        print("-------------------------------------------------------------------------")



        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            # Verify system Id in UI table
            status, device_status, package_name = vehicleList_page.verify_system_id_in_table(systemId)

            # Step - 3

            print("Step:3 -> Verify newly onboarded ' System Id ' on Vehicle List UI Page : ")

            if status == "present":
                print("System Id is listed in UI table on Vehicle List page")

                testResult(self, "passed", "System Id of newly onboarded device should be listed in UI table on Vehicle List page",
                           "System Id of newly onboarded device is listed in UI table on Vehicle List page")
            else:
                testResult(self, "failed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                           "System Id of newly onboarded device is not listed in UI table on Vehicle List page")

            # Step - 4

            print("Step:4 -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            if device_status == "Active":
                print("Device Status is shown as ACTIVE on Vehicle List UI page")

                testResult(self, "passed", "Device Status should be ACTIVE on Vehicle List UI page",
                           "Device Status is shown as ACTIVE on Vehicle List UI page")
            else:
                testResult(self, "failed",
                           "Device Status should be ACTIVE on Vehicle List UI page  ",
                           "Device Status is not ACTIVE on Vehicle List UI page")

            # Step - 5

            print("Step:5 -> Verify newly onboarded device ' Package ' name on Vehicle List UI Page : ")

            if package_name == "Essential":
                print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
                print("By default device should have Essential package")

                testResult(self, "passed", "By default device should have 'Essential' package",
                           "By default device is having 'Essential' package")
            else:
                print(f"Package : ' {package_name} ' is shown instead of ' Essential ' on Vehicle List UI page")
                testResult(self, "failed",
                           "By default device should have 'Essential' package",
                           "By default device is not having 'Essential' package")

        except:
            testResult(self, "failed", "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                       "Something went wrong, while verifying newly onboarded device details on Vehicle List Page")

        print("-------------------------------------------------------------------------")

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test8_DeviceOnboarding(self):
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





