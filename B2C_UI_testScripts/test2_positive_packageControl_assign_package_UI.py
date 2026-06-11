import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

package1 = "Essential"
package2 = "Value"
package3 = "Elite"


class Test_packageControl_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_onboarded_device_details_on_UI(self):
        vehicleList_page = assign_packageName = ""

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
            status, device_state, pacakge_name = vehicleList_page.read_packageName_from_UI(systemId)
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

            print("Step:5 -> Verify package name for onboarded device on Vehicle List UI Page : ")

            # verify package
            status = vehicleList_page.verify_default_package_name_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed", "Device should be assigned to package ",
                           "Device is assigned to package")
            else:
                testResult(self, "verificationFailed",
                           "Device should be assigned to package",
                           "Device is not assigned to package")

            print("-------------------------------------------------------------------------")

            # Step - 6

            print("Step:6 -> Click on package link for up-gradation on Vehicle List UI Page : ")

            # Click on Package link
            status = vehicleList_page.click_on_package_link(systemId)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed", "User should be able to click on package link",
                           "User is able to click on package link")
            else:
                testResult(self, "verificationFailed",
                           "User should be able to click on package link",
                           "User is not able to click on package link")

            print("-------------------------------------------------------------------------")

            # Step - 7

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
            # Step - 8

            print("Step:8 -> Verify package name : ")

            # Verify pacakge

            status = vehicleList_page.verify_selected_pacakge_tab_on_dialog_box(pacakge_name)
            if pacakge_name == package2:
                assign_packageName = package3
            elif pacakge_name == package3:
                assign_packageName = package2
            elif pacakge_name == package1:
                assign_packageName = package2
            else:
                assign_packageName = package2
            print("------------------------------------------------------")
            print("Package selected for up-gradation : ", assign_packageName)
            print("------------------------------------------------------")

            if status == 'present':
                print("Package Name :", {pacakge_name}, " is displayed")
                testResult(self, "passed",
                           pacakge_name + " Package tab should be available/displayed on package dialog box/window",
                           pacakge_name + " Package tab is available/displayed on package dialog box/window")
            else:
                testResult(self, "failed",
                           pacakge_name + " Package tab should be available/displayed on package dialog box/window",
                           pacakge_name + " Package tab is not available/displayed on package dialog box/window")

            print("-------------------------------------------------------------------------")

            # Step - 9
            print("Step:9 -> Click on", {assign_packageName}, " package tab : ")

            status = vehicleList_page.click_on_desired_pacakge_tab_on_dialog_box(assign_packageName)
            time.sleep(10)
            if status == 'present':
                testResult(self, "passed",
                           assign_packageName + " Package feature list should be displayed on clicking it",
                           assign_packageName + " Package feature list is displayed on clicking it")
            else:
                testResult(self, "failed",
                           assign_packageName + " Package feature list should be displayed on clicking it",
                           assign_packageName + " Package feature list is not displayed on clicking it")

            print("-------------------------------------------------------------------------")

            # Step - 10
            print("Step10 -> Verify & Click on Activate button for package upgrade : ")

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

            # Step - 11
            print("Step11 -> Verify Success message for package upgrade : ")

            status = vehicleList_page.verify_success_msg_for_package_update()
            if status == 'present':
                testResult(self, "passed",
                           "Success message should be displayed on clicking Activate button",
                           "Success message is displayed on clicking Activate button")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Success message should be displayed on clicking Activate button",
                           "Success message is not displayed on clicking Activate button")
                # self.result.set_result(TestResults.failed)

            # Verify current page url
            time.sleep(10)

            print("-------------------------------------------------------------------------")

            print("Step12 -> Verify assigned package name on Vehicle List UI page : ")
            for i in range(5):
                status = vehicleList_page.page_reload()
                time.sleep(5)
                status1, device_state, pacakge_name = vehicleList_page.read_packageName_from_UI(systemId)
                if pacakge_name == assign_packageName:
                    testResult(self, "passed",
                               "New package : " + assign_packageName + " should be assigned to device/vehicle",
                               "New package : " + assign_packageName + " is successfully assigned to device/vehicle")
                    # self.result.set_result(TestResults.passed)
                    break
                else:
                    time.sleep(30)
            else:

                testResult(self, "failed",
                           "New package : " + assign_packageName + " should be assigned to device/vehicle",
                           "New package : " + assign_packageName + " is not assigned to device/vehicle")
                # self.result.set_result(TestResults.failed)

        except:
            testResult(self, "failed",
                       "Package should be upgraded",
                       "Something went wrong while upgrading the package to " + assign_packageName + " , Pls refer logs &"
                       " screenshots for detailed info.")
            # self.result.set_result(TestResults.failed)

        print("-------------------------------------------------------------------------")

