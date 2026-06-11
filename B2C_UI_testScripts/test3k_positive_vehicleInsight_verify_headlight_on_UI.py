import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, \
    b2c_on_status_ui, b2c_telemetry_headlight_attribute_ui
from C2CModules.primary_IVI_device_modules import get_SystemId, run_paho_command_on_primary_IVI
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_DeviceOnboarding_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_telemetry_headlight_on_UI(self):
        vehicleList_page = ""

        # ===========================================================================================
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType,
                                        "telemetry_can_headlight_ON")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
        # print("----------------------------------------------------------")

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

            print("Step:5 -> Verify ' Vehicle Insight ' option on Vehicle List UI Page : ")

            # Click on Vehicle Insight eye icon
            status = vehicleList_page.click_on_vehicle_insight(systemId)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           "Vehicle Insight Icon should be displayed for each onboarded device on Vehicle List page",
                           "Vehicle Insight Icon is displayed for newly onboarded device on Vehicle List page")
            else:
                testResult(self, "failed",
                           "Vehicle Insight Icon should be displayed for each onboarded device on Vehicle List page  ",
                           "Vehicle Insight Icon is not displayed/clickable on Vehicle List page")

            print("-------------------------------------------------------------------------")
            # Step - 6

            print("Step:6 -> Verify ' More ' option on Vehicle-Insight RHS panel : ")

            # Click on Vehicle Insight eye icon
            status = vehicleList_page.click_on_more_option()
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           "'More' option should be present to expand the list on Vehicle Insight RHS panel",
                           "'More' option is present and on click, expanded the list on Vehicle Insight RHS panel")
            else:
                testResult(self, "verificationFailed",
                           "'More' option should be present to expand the list on Vehicle Insight RHS panel",
                           "'More' option is not present/clickable on Vehicle Insight RHS panel")

            print("-------------------------------------------------------------------------")
            # Step - 7

            print(
                "Step:7 -> Verify ' Vehicle Insight - Headlight' option & value on Vehicle List UI Page : ")

            # Verify Headlight option & value on UI
            status = vehicleList_page.verify_vehicle_telemetry_attribute_name(b2c_telemetry_headlight_attribute_ui)
            if status == 'present':
                testResult(self, "passed",
                           b2c_telemetry_headlight_attribute_ui + " should be listed under Vehicle Insight RHS panel",
                           b2c_telemetry_headlight_attribute_ui + " is listed under Vehicle Insight RHS panel")
            else:
                testResult(self, "failed",
                           b2c_telemetry_headlight_attribute_ui + " should be listed under Vehicle Insight RHS panel",
                           b2c_telemetry_headlight_attribute_ui + " is not listed under Vehicle Insight RHS panel")

            status = vehicleList_page.verify_vehicle_telemetry_attribute_status(b2c_telemetry_headlight_attribute_ui,
                                                                                b2c_on_status_ui)
            if status == 'present':
                testResult(self, "passed",
                           b2c_telemetry_headlight_attribute_ui + " status should be same as that of configured telemetry stub on device",
                           b2c_telemetry_headlight_attribute_ui + ' : ' + b2c_on_status_ui + " => status is same as that of configured telemetry stub on device")
            else:
                status = vehicleList_page.verify_vehicle_telemetry_attribute_value(b2c_on_status_ui)
                if status == 'present':
                    testResult(self, "passed",
                               b2c_telemetry_headlight_attribute_ui + " status should be same as that of configured telemetry stub on device",
                               b2c_telemetry_headlight_attribute_ui + ' : ' + b2c_on_status_ui + "  => status is same as that of configured telemetry stub on device")
                else:
                    testResult(self, "failed",
                               b2c_telemetry_headlight_attribute_ui + " status should be same as that of configured telemetry stub on device",
                               b2c_telemetry_headlight_attribute_ui + " is not shown or same as that of configured telemetry stub on device")
        except:
            testResult(self, "failed",
                       "Vehicle Insight window should show device Headlight status",
                       "Something went wrong while validating Headlight status on vehicle insight window")

        print("-------------------------------------------------------------------------")
