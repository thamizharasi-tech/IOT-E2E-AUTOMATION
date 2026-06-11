from datetime import datetime
import time

import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, run_paho_command_on_primary_IVI, \
    pull_logs_from_IVI_device
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.elementSelectors.b2c.vehicleMap import vehicleMap_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi


class Test_location:

    def test_telemetry_location_live_tracking(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Step:1 -> Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

        # ===========================================================================================
        # Run telemetry location stub on device for geofence
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:1 -> Configure & Run location stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'location_geofence')

        print("Telemetry Location stub start/run process is completed, verify logs & UI for telemetry-location details : ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")

        try:

            print("Step:2 -> Launch B2C Web UI : ")
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

        print("Step:3 -> Navigate to Vehicle Map page : ")

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

        print("Step:4 -> Select the desired VIN from dropdown list : ")

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

        print("Step:5-> Click on View button : ")

        status = vehicleMap_page.click_on_view_button()
        if status == 'present':
            testResult(self, "passed",
                       "'View' button should be present & clickable on Vehicle Map page",
                       "'View' button is present & clickable on Vehicle Map page")
        else:
            testResult(self, "failed",
                       "'View' button should be present & clickable on Vehicle Map page",
                       "'View' button is not present or clickable on Vehicle Map page")

        time.sleep(180)
        print("-------------------------------------------------------------------------")

        # Fetch/pull logs from device
        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("-------------------------------------------------------------------------")

        print("Step:6-> Expand View Location Data & verify telemetry latitude & longitude data : ")

        status = vehicleMap_page.expand_view_location_data()
        if status == 'present':
            testResult(self, "passed",
                       "'View Location Data ' window should be expanded",
                       "'View Location Data ' window is expanded")
        else:
            testResult(self, "failed",
                       "'View Location Data ' window should be expanded",
                       "'View Location Data ' window is not expanded")

        print("----------------------------------------------------------")

        print("Step:7-> Verify vehicle live location - telemetry latitude & longitude data : ")

        status = vehicleMap_page.verify_telemetry_location_data()
        if status == 'present':
            testResult(self, "passed",
                       "'Should list vehicle live location - telemetry latitude & longitude data",
                       "Listing vehicle vehicle live location - telemetry latitude & longitude data")
            # self.result.set_result(TestResults.passed)

            testResult(self, "passed",
                       "'Trace movement of vehicle",
                       "Vehicle live location is traced successfully at configured interval")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Should list vehicle live location - telemetry latitude & longitude data",
                       "Not listing vehicle live location - telemetry latitude & longitude data")
            # self.result.set_result(TestResults.failed)

        print("----------------------------------------------------------")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'switch_to_origin')
