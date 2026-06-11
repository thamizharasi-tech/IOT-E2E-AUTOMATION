import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, run_paho_command_on_primary_IVI
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

# Test data for geofence creation:
name = 'test_geo_auto'
latitude = '28.60944621041275'
longitude = '77.23101642228914'
radius = '150'
unit = 'METER'


class Test_Geofence_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_Geofence_creation_UI(self):
        vehicleList_page= ""

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
            vehicleList_page.verify_vehicleList_tab()

            print("-------------------------------------------------------------------------")
            vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)

            print("-------------------------------------------------------------------------")

            # Verify current page url
            vehicleList_page.verify_vehicleList_page_url()
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
            vehicleList_page.verify_systemId_on_UI(systemId)

            print("-------------------------------------------------------------------------")
            # Step - 4

            print("Step:3a -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            # Verify device status in UI table
            # vehicleList_page.verify_device_status_on_UI(systemId)

            print("-------------------------------------------------------------------------")

            # Step - 4
            print("Step:4 -> Verify & click on ' Geofence Config ' image/option on Vehicle List UI Page : ")

            # Click on Geofence Config icon
            status = vehicleList_page.click_on_Geofence_config(systemId)
            if status == 'present':
                testResult(self, "passed",
                           "Geofence Config Icon should be displayed for each onboarded device on Vehicle List page",
                           "Geofence Config Icon is displayed for newly onboarded device on Vehicle List page")
            else:
                testResult(self, "failed",
                           "Geofence Config Icon should be displayed for each onboarded device on Vehicle List page  ",
                           "Geofence Config Icon is not displayed/clickable on Vehicle List page")
            time.sleep(5)

            print("-------------------------------------------------------------------------")
        except:
            testResult(self, "failed", "User should navigate to / land on Geofence Config page  ",
                       "User is not navigated to / landed on Geofence Config page ")

        try:
            # Step - 5
            print("Step:5 -> Verify & click on ' Create Geofence ' tab/option on Vehicle List UI Page : ")

            # Click on Create Geofence
            status = vehicleList_page.click_on_create_geofence()
            if status == 'present':
                testResult(self, "passed",
                           "Create Geofence ' tab/option should be displayed on Geofence dialog box/window",
                           "Create Geofence ' tab/option is displayed on Geofence dialog box/window")
            else:
                testResult(self, "failed",
                           "Create Geofence ' tab/option should be displayed on Geofence dialog box/window ",
                           "Create Geofence ' tab/option is not displayed/clickable on Geofence dialog box/window")
            time.sleep(5)

            print("-------------------------------------------------------------------------")

            # Step - 6
            print("Step:6 -> Verify & enter Geofence name : ")

            # Enter geofence Name

            status = vehicleList_page.enter_name_for_geofence(name)
            if status == 'present':
                testResult(self, "passed",
                           "Create Geofence - ' Name ' field should be displayed and user should be able to enter desired input in the text field on Geofence dialog box/window",
                           "Create Geofence - ' Name ' field is displayed and user is also able to enter desired input in the text field on Geofence dialog box/window")
            else:
                testResult(self, "failed",
                           "Create Geofence - ' Name ' field should be displayed and user should be able to enter desired input in the text field on Geofence dialog box/window",
                           "Create Geofence - ' Name ' field is not displayed or user is not able to enter desired input in the text field on Geofence dialog box/window")
            time.sleep(5)

            print("-------------------------------------------------------------------------")

            # Step - 7
            print("Step:7 -> Create new geofence with valid input : ")
            print("Step:7a -> Verify each field & input valid values for geofence creation : ")

            # Create geofence with valid input
            status = vehicleList_page.create_new_geofence(latitude, longitude, radius, unit)
            if status == 'present':
                testResult(self, "passed",
                           "Create Geofence - ' User should be able to create Geofence with valid values",
                           "Create Geofence - ' User is able to create Geofence with valid values")
            else:
                testResult(self, "failed",
                           "Create Geofence - ' User should be able to create Geofence with valid values",
                           "Create Geofence - ' User is not able to create Geofence with valid values")
            time.sleep(5)

            print("-------------------------------------------------------------------------")

            # Step - 7
            print("Step:7b -> close Geofence window : ")

            # Enter latitude
            status = vehicleList_page.close_geofence_window()
            if status == 'present':
                testResult(self, "passed",
                           "Create Geofence - ' User should be able to close geofence window/dialog box",
                           "Create Geofence - ' User is able to close geofence window/dialog box")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "verificationFailed",
                           "Create Geofence - ' User should be able to close geofence window/dialog box",
                           "Create Geofence - ' User is not able to close geofence window/dialog box")
                # self.result.set_result(TestResults.failed)
            time.sleep(5)

            print("-------------------------------------------------------------------------")

        except:
            testResult(self, "failed",
                       "Create Geofence - ' User should be able to create Geofence with valid values",
                       "Create Geofence - ' User is not able to create Geofence with valid values")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")
