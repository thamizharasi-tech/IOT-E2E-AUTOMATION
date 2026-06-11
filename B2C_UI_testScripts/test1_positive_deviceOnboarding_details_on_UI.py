import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_DeviceOnboarding_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_onboarded_device_details_on_UI(self):

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

        # Step - 2

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
                testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                           "User is not navigated to / landed on Vehicle List page ")
        except:
            testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

        print("-------------------------------------------------------------------------")

        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("-------------------------------------------------------------------------")
            # Step - 3

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
            # Step - 4

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

            # Step - 5

            print("Step:5 -> Verify default package name for onboarded device on Vehicle List UI Page : ")

            # verify default package
            status = vehicleList_page.verify_default_package_name_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed", "Device should be assigned to default package",
                           "Device is assigned to default package")
            else:
                testResult(self, "failed",
                           "Device should be assigned to default package",
                           "Device is not assigned to default package")
        except:
            testResult(self, "failed",
                       "Device should be assigned to default package",
                       "Device is not assigned to default package")

        print("-------------------------------------------------------------------------")

