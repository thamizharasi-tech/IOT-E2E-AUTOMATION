import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, Command_Lock_ignition_value
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, pull_logs_from_IVI_device
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_CommandControl_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_CommandControl_Lock_UI(self):
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

            print("Step:5 -> Verify Value package name for onboarded device on Vehicle List UI Page : ")

            # verify device package
            status, device_state, pacakge_name = vehicleList_page.read_packageName_from_UI(systemId)
            if pacakge_name == 'Value' or pacakge_name == 'Elite':
                testResult(self, "passed", "Device should be assigned to 'Value/Elite' package",
                           "Device is assigned to " + pacakge_name + "package")
            else:
                testResult(self, "failed",
                           "Device should be assigned to 'Value/Elite' package",
                           "Device is not assigned to 'Value/Elite' package" + "Rather having " + pacakge_name + " package")

            print("-------------------------------------------------------------------------")

            # Step - 6
            print("Step:6 -> Verify ' Commands ' image/option on Vehicle List UI Page : ")

            # Click on Vehicle Insight eye icon
            status = vehicleList_page.click_on_Commands(systemId)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           "Commands Icon should be displayed for each onboarded device on Vehicle List page",
                           "Commands Icon is displayed for newly onboarded device on Vehicle List page")
            else:
                testResult(self, "failed",
                           "Commands Icon should be displayed for each onboarded device on Vehicle List page  ",
                           "Commands Icon is not displayed/clickable on Vehicle List page")

            print("-------------------------------------------------------------------------")

            # Step - 7

            print("Step:7 -> Verify 'VIN No' on RHS panel : ")

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

            print("-------------------------------------------------------------------------")

            # Step - 8

            print("Step:8 -> Verify 'drop down option : ")

            status = vehicleList_page.select_Ignition_state()
            if status == 'present':
                testResult(self, "passed",
                           "'IGNITION STATE' should be displayed ",
                           "'IGNITION STATE' option is displayed ")
            else:
                testResult(self, "failed",
                           "'IGNITION STATE' should be displayed ",
                           "'IGNITION STATE' option is not displayed ")

            time.sleep(30)

            print("-------------------------------------------------------------------------")
            # Step - 9

            print("Step:9 -> Verify & click on Lock button : ")

            status = vehicleList_page.click_on_ignition_button("Lock")
            if status == 'present':
                testResult(self, "passed",
                           "' IGNITION STATE - Lock ' option/button should be displayed ",
                           "' IGNITION STATE - Lock ' option/button is displayed ")
            else:
                testResult(self, "failed",
                           "' IGNITION STATE - Lock ' option/button should be displayed ",
                           "' IGNITION STATE - Lock ' option/button is not displayed ")

            print("-------------------------------------------------------------------------")

            # Step - 10
            print("Step:10 -> Verify success message : ")

            status = vehicleList_page.verify_success_msg_for_command()
            if status == 'present':
                testResult(self, "passed",
                           "Success message should be displayed on clicking command button",
                           "Success message is displayed on clicking command button")
            else:
                testResult(self, "verificationFailed",
                           "Success message should be displayed on clicking command button",
                           "Success message is not displayed on clicking command button")

            print("-------------------------------------------------------------------------")

            # ===========================================================================================
            # Device side validations : Fetch logs & verify command & control msg
            # ===========================================================================================

            # Step - 11
            print("Step:11 -> Verify ignition state value in device log : ")

            print("-----------------------------")
            print("Device Validations : ")
            print("-----------------------------")

            # Fetch/pull logs from device
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            # Verify command control msgs & type code in fetched device logs
            # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
            ls = verify_message_in_log(self, 'ignition:', 'ignition')
            print("Initiation texts captured in device logs : ", ls)
            ls = verify_message_in_log(self, 'ignition:', Command_Lock_ignition_value)
            print("Ignition State for Command-Lock: ", ls)

            if Command_Lock_ignition_value in str(ls):

                testResult(self, "passed",
                           "Ignition value = 2 should be shown in log",
                           "Ignition value = 2 is displayed in device log . pls refer "
                           "device & cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Ignition value = 2 should be shown in log",
                           "Ignition value = 2 is not displayed device log or logs have been rotated . pls refer "
                           "device & cloud logs for detailed info")
            time.sleep(10)

            print("-------------------------------------------------------------------------")

            # Step - 12
            print("Step12 -> Click on reload button : ")
            time.sleep(90)

            status = vehicleList_page.click_on_reload_button()
            if status == 'present':
                testResult(self, "passed",
                           "'Commands' RHS panel should be refreshed/reloaded on click",
                           "'Commands' RHS panel is refreshed/reloaded on click")
            else:
                testResult(self, "verificationFailed",
                           "'Commands' RHS panel should be refreshed/reloaded on click",
                           "'Commands' RHS panel is not refreshed/reloaded on click")

            print("-------------------------------------------------------------------------")

            # Step - 13
            print("Step13 -> Verify Lock button status : ")

            status = vehicleList_page.verify_ignition_button_status('Lock')
            if status == 'present':
                testResult(self, "passed",
                           "' IGNITION STATE - Lock ' option/button should be clicked ",
                           "' IGNITION STATE - Lock ' option/button is clicked ")
                #self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "' IGNITION STATE - Lock ' option/button should be clicked ",
                           "' IGNITION STATE - Lock ' option/button is not clicked ")
                # self.result.set_result(TestResults.failed)


        except:
            testResult(self, "failed",
                       "Command control e2e flow should work without any errors",
                       "Something went wrong while testing e2e flow, Pls refer logs &"
                       " screenshots for detailed info.")

        print("-------------------------------------------------------------------------")

        time.sleep(10)