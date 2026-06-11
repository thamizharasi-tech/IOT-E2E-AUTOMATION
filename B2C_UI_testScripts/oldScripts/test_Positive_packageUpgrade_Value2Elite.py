import time
import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, pull_logs_from_IVI_device
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

base_package_name = "Essential"
update_package_name = "Value"


class Test_packageUpgradtion:

    @pytest.mark.regression
    # Validate package upgrade.
    def test_package_update_Value_to_Elite(self):

        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")

        try:

            print("Step:1 -> Launch B2C Web UI : ")

            playwright = sync_playwright().start()
            if browser_type == 'chromium' and browser_name != 'NA':
                browser = playwright.chromium.launch(channel=browser_name, headless=headless_mode(),
                                                     args=["--start-maximised"])
            elif browser_type == 'firefox':
                browser = playwright.firefox.launch(headless=headless_mode(), args=["--start-maximised"])
            elif browser_type == 'webkit':
                browser = playwright.webkit.launch(headless=headless_mode(), args=["--start-maximised"])
            else:
                browser = playwright.chromium.launch(headless=headless_mode(), args=["--start-maximised"])

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

        print("Step:2 -> User should land on Vehicle List Page : ")

        try:
            # Verify vehicle List tab and then click on it
            status = vehicleList_page.verify_vehicleList_tab()

            if status == 'present':
                testResult(self, "passed", "Vehicle list tab should be present on UI page ",
                           "Vehicle list tab is present on UI page ")
            else:
                testResult(self, "failed", "Vehicle list tab should be present on UI page ",
                           "Vehicle list tab is not present on UI page ")

            print("-------------------------------------------------------------------------")
            vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)
            if status == 'present':
                testResult(self, "passed", "User should be able to click on Vehicle list tab",
                           "User is able to click on Vehicle list tab")
            else:
                testResult(self, "failed",
                           "User should be able to click on Vehicle list tab",
                           "User is not able to click on Vehicle list tab ")

            print("-------------------------------------------------------------------------")

            # Verify current page url
            status = vehicleList_page.verify_vehicleList_page_url()
            if status == 'present':
                testResult(self, "passed", "User should navigate to / land on Vehicle List page ",
                           "User is navigated to / landed on Vehicle List page successfully ")
            else:
                testResult(self, "verificationFailed", "User should navigate to / land on Vehicle List page  ",
                           "User is not navigated to / landed on Vehicle List page ")
        except:
            testResult(self, "verificationFailed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

        print("-------------------------------------------------------------------------")

        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("-------------------------------------------------------------------------")

            print("Step:3 -> Verify newly onboarded ' System Id ' on Vehicle List UI Page : ")

            # Verify system Id in UI table
            status = vehicleList_page.verify_systemId_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page",
                           "System Id of newly onboarded device is listed in UI table on Vehicle List page")
            else:
                testResult(self, "failed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                           "System Id of newly onboarded device is not listed in UI table on Vehicle List page")

            print("-------------------------------------------------------------------------")

            print("Step:4 -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            # Verify device status in UI table
            status = vehicleList_page.verify_device_status_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed", "Device Status should be ACTIVE on Vehicle List UI page",
                           "Device Status is shown as ACTIVE on Vehicle List UI page")
            else:
                testResult(self, "verificationFailed",
                           "Device Status should be ACTIVE on Vehicle List UI page  ",
                           "Device Status is not ACTIVE on Vehicle List UI page")

            print("-------------------------------------------------------------------------")

            print("Step:5 -> Verify package name for onboarded device on Vehicle List UI Page : ")

            # verify base package
            status = vehicleList_page.verify_package_name_on_UI(systemId, base_package_name)
            if status == 'present':
                testResult(self, "passed", "Device should be mapped to '" + base_package_name + "' package",
                           "Device is mapped to '" + base_package_name + "' package")
            else:
                testResult(self, "passed", "Device should be mapped to '" + base_package_name + "' package",
                           "Device is not mapped to '" + base_package_name + "' package")

            print("-------------------------------------------------------------------------")

            print(f"Step:6 -> Click on {base_package_name} package link for update on Vehicle List UI Page : ")

            # Click on base Package link
            status = vehicleList_page.click_on_pacakge_link(systemId, base_package_name)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed", "User should be able to click on package update link",
                           "User is able to click on package update link")
            else:
                testResult(self, "verificationFailed",
                           "User should be able to click on package update link",
                           "User is not able to click on package update link")

            print("-------------------------------------------------------------------------")

            print("Step:7 -> Verify 'VIN No' on package dialog box : ")

            # Get vin from device
            vin = getVIN(self, OnboardingType, chipsetType)

            status = vehicleList_page.verify_vin_on_pacakge_dialog_box(vin)
            if status == 'present':
                testResult(self, "passed",
                           "VIN no should be displayed as header on package dialog box/window",
                           "VIN no is displayed as header on package dialog box/window")
            else:
                testResult(self, "verificationFailed",
                           "VIN no should be displayed as header on package dialog box/window ",
                           "VIN no is not displayed as header on package dialog box/window")

            time.sleep(30)

            print("-------------------------------------------------------------------------")

            print(f"Step:8 -> Verify selected '{base_package_name}' package : ")

            # Verify pacakge
            status = vehicleList_page.verify_selected_pacakge_tab_on_dialog_box(base_package_name)
            if status == 'present':
                testResult(self, "passed",
                           base_package_name + " Package tab should be selected on package dialog box/window",
                           base_package_name + " Package tab is selected on package dialog box/window")
            else:
                testResult(self, "failed",
                           base_package_name + " Package tab should be selected on package dialog box/window",
                           base_package_name + " Package tab is not selected on package dialog box/window")

            print("-------------------------------------------------------------------------")

            print(f"Step:9 -> Verify '{update_package_name}' package tab : ")

            # Verify pacakge
            status = vehicleList_page.verify_selected_pacakge_tab_on_dialog_box(update_package_name)
            if status == 'present':
                testResult(self, "passed",
                           update_package_name + " Package tab should be available/displayed on package dialog box/window",
                           update_package_name + " Package tab is available/displayed on package dialog box/window")
            else:
                testResult(self, "failed",
                           update_package_name + " Package tab should be available/displayed on package dialog box/window",
                           update_package_name + " Package tab is not available/displayed on package dialog box/window")

            print("-------------------------------------------------------------------------")

            print(f"Step:10 -> Click on '{update_package_name}' package tab : ")

            status = vehicleList_page.click_on_desired_pacakge_tab_on_dialog_box(update_package_name)

            time.sleep(10)
            if status == 'present':
                testResult(self, "passed",
                           update_package_name + " Package feature list should be displayed  on click/select",
                           update_package_name + " Package feature list is displayed on click/select")
            else:
                testResult(self, "failed",
                           update_package_name + " Package feature list should be displayed on click/select",
                           update_package_name + " Package feature list is not displayed on click/select")

            print("-------------------------------------------------------------------------")

            print("Step:11 -> Verify & Click on Activate button for package upgrade : ")

            status = vehicleList_page.click_on_Active_button()

            if status == 'present':
                testResult(self, "passed",
                           "User should be able to click on 'Activate' button for package upgrade",
                           "User is able to click on 'Activate' button for package upgrade")
            else:
                testResult(self, "failed",
                           "User should be able to click on 'Activate' button for package upgrade",
                           "User is not able to click on 'Activate' button for package upgrade")

            print("-------------------------------------------------------------------------")

            print("Step:12 -> Verify Success message for package update : ")
            time.sleep(5)

            status = vehicleList_page.verify_success_msg_for_package_update()
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            time.sleep(20)
            if status == 'present':
                testResult(self, "passed",
                           "Success message should be displayed on clicking Activate button",
                           "Success message is displayed on clicking Activate button")
            else:
                testResult(self, "verificationFailed",
                           "Success message should be displayed on clicking Activate button",
                           "Success message is not displayed on clicking Activate button")

        except:
            # ===========================================================================================
            # Pull logs for validations
            # ===========================================================================================
            print("Pull/Fetch device logs for validation : ")

            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            print("Logs are fetched from device to host machine @ desired location ")
            print("----------------------------------------------------------")

            testResult(self, "failed",
                       "Package should be upgraded",
                       "Something went wrong while upgrading the package from 'Essential' to 'Value', Pls refer logs &"
                       " screenshots for detailed info.")

        try:
            vehicleList_page.navigate_to_vehicelList_page()

            print("Step:13 -> Verify package name, post package update on Vehicle List UI Page : ")

            # verify base package
            status = vehicleList_page.verify_package_name_on_UI(systemId, update_package_name)
            if status == 'present':
                testResult(self, "passed", "Device should be mapped to '" + update_package_name + "' package",
                           "Device is mapped to '" + update_package_name + "' package")
            else:
                testResult(self, "failed", "Device should be mapped to '" + update_package_name + "' package",
                           "Device is not mapped to '" + update_package_name + "' package")

            print("-------------------------------------------------------------------------")

        except:
            testResult(self, "failed",
                       "Package should be upgraded",
                       "Something went wrong while upgrading the package from '" + base_package_name + "' to '" + update_package_name + "', Pls refer logs &"
                                                                                                                                        " screenshots for detailed info.")

        print("-------------------------------------------------------------------------")
