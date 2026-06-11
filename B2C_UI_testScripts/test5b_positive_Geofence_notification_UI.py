import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, run_paho_command_on_primary_IVI, \
    reboot_primary_IVI
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.elementSelectors.b2c.vehicleMap import vehicleMap_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_Geofence_UI:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_Geofence_notification_UI(self):
        vehicleMap_page = ""
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
            vehicleMap_page = vehicleMap_Page(page)

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
        print("Step:2 -> Navigate to Vehicle Map page : ")

        try:
            # Verify vehicle Map tab and then click on it
            vehicleMap_page.verify_vehicleMap_tab()

            print("-------------------------------------------------------------------------")
            vehicleMap_page.click_on_vehicleMap_tab()
            time.sleep(15)

            print("-------------------------------------------------------------------------")

            # Verify current page url
            vehicleMap_page.verify_vehicleMap_page_url()
        except:
            testResult(self, "failed", "User should navigate to Vehicle Map page  ",
                       "User is not navigate to Vehicle Map page ")

        print("-------------------------------------------------------------------------")

        # Step - 3
        print("Step:3 -> Select the desired VIN from dropdown list : ")

        vin = getVIN(self, OnboardingType, chipsetType)
        status = vehicleMap_page.select_desired_vin(vin)
        if status == 'present':
            testResult(self, "passed",
                       "Vin should be listed and user should be able to select it from dropdown list",
                       "Vin is listed and user is able to select it from dropdown list")
        else:
            testResult(self, "failed",
                       "Vin should be listed and user should be able to select it from dropdown list",
                       "Vin is not listed or user is not able to select it from dropdown list")
        time.sleep(10)

        print("-------------------------------------------------------------------------")

        # Step - 4
        print("Step:4-> Click on View button : ")

        status = vehicleMap_page.click_on_view_button()
        if status == 'present':
            testResult(self, "passed",
                       "'View' button should be present & clickable on Vehicle Map page",
                       "'View' button is present & clickable on Vehicle Map page")
        else:
            testResult(self, "failed",
                       "'View' button should be present & clickable on Vehicle Map page",
                       "'View' button is not present or clickable on Vehicle Map page")

        # ===========================================================================================
        # Device setup
        # ===========================================================================================

        # Step - 5
        # ===========================================================================================
        # Run location stub on device for geofence
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:5 -> Configure & Run location stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'location_geofence')

        print("Location stub start/run process is completed, verify logs & UI for telemetry-location details : ")
        # print("----------------------------------------------------------")

        time.sleep(180)

        # Step - 6
        print("Step:6-> Click on Vehicle List Tab : ")

        vehicleList_page = vehicleList_Page(page)

        # Step - 7

        print("Step:7 -> User should land on Vehicle List Page : ")

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
            # Step - 8

            print("Step:8 -> Verify ' System Id ' on Vehicle List UI Page : ")

            # Verify system Id in UI table
            vehicleList_page.verify_systemId_on_UI(systemId)

            print("-------------------------------------------------------------------------")

            # Step - 9
            print("Step:9 -> Verify & click on ' Notification ' image/option on Vehicle List UI Page : ")

            # Click on Notification icon
            status = vehicleList_page.click_on_Notifications(systemId)
            if status == 'present':
                testResult(self, "passed",
                           "Notification-bell Icon should be displayed for each onboarded device on Vehicle List page",
                           "Notification-bell Icon is displayed for newly onboarded device on Vehicle List page")
            else:
                testResult(self, "failed",
                           "Notification-bell Icon should be displayed for each onboarded device on Vehicle List page  ",
                           "Notification-bell Icon is not displayed/clickable on Vehicle List page")
            # print("-------------------------------------------------------------------------")
        except:
            testResult(self, "failed", "User should navigate to / land on Notification page  ",
                       "User is not navigated to / landed on Notification page ")

        print("-------------------------------------------------------------------------")
        try:
            # Step - 10
            print("Step:10 -> Verify & click on ' Geofence ' tab/option on Notification window/Page : ")

            # Click on Create Geofence
            status = vehicleList_page.click_on_Notification_tab("GEOFENCE")
            if status == 'present':
                testResult(self, "passed",
                           "Geofence ' tab/option should be displayed on Notification window/Page",
                           "Create Geofence ' tab/option is displayed on Notification window/Page")
            else:
                testResult(self, "failed",
                           "Geofence ' tab/option should be displayed on Notification window/Page ",
                           "Geofence ' tab/option is not displayed/clickable on Notification window/Page")

            print("-------------------------------------------------------------------------")

            # Step - 11
            print("Step:11 -> Verify ' Geofence Notification/Alert' ")

            status = vehicleList_page.verify_geofence_notification()
            if status == 'present':
                testResult(self, "passed",
                           "Geofence Notification/Alert ' should be listed on Notification window/Page",
                           "Geofence Notification/Alert ' is listed on Notification window/Page")
            else:
                testResult(self, "failed",
                           "Geofence Notification/Alert ' should be listed on Notification window/Page ",
                           "Geofence Notification/Alert ' is not listed on Notification window/Page")

            print("-------------------------------------------------------------------------")

            # Step - 12
            print("Step:12 -> Click on View All button ")

            status = vehicleList_page.click_on_view_all_button()
            if status == 'present':
                testResult(self, "passed",
                           "New 'Geofence Notifications' window should open & list all the Geofence notifications",
                           "New 'Geofence Notifications' is opened & listed all the Geofence notifications")
            else:
                testResult(self, "failed",
                           "New 'Geofence Notifications' window should open & list all the Geofence notifications ",
                           "New 'Geofence Notifications' window is not opened or not listed the Geofence notifications")

            print("-------------------------------------------------------------------------")
            # Step - 13
            print("Step:13 -> Verify ' Geofence Notification/Alert details' ")

            status = vehicleList_page.verify_geofence_notification()
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           "Geofence Notification/Alert ' details should be listed on Notification window/Page",
                           "Geofence Notification/Alert ' details are listed on Notification window/Page")
                # self.result.set_result(TestResults.passed)
            else:
                testResult(self, "failed",
                           "Geofence Notification/Alert ' details should be listed on Notification window/Page ",
                           "Geofence Notification/Alert ' details are not listed on Notification window/Page")
                # self.result.set_result(TestResults.failed)

        except:
            print("Geofence Notification alert is not listed yet, wait for another 90 sec")
            testResult(self, "failed",
                       "Geofence Notification/Alert ' should be listed on Notification window/Page ",
                       "Geofence Notification/Alert ' are not listed on Notification window/Page")
            # self.result.set_result(TestResults.failed)
            time.sleep(90)

        print("-------------------------------------------------------------------------")
        # self.result.set_result(TestResults.passed)

        reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")
