import time
from datetime import datetime
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, telemetry_lat_event_type
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import get_SystemId, run_paho_command_on_primary_IVI, \
    push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, pull_logs_from_IVI_device, getVIN, reboot_primary_IVI
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr_eventType
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.elementSelectors.b2c.vehicleMap import vehicleMap_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
networkType = wifi
notification_tab_name = "GEOFENCE"
notification_name = "GEOFENCE NOTIFICATION"
alert_text = 'Geofence breach'


class Test_notification:

    def test_geofence_notification_UI(self):

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        # dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Step:1 -> Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, networkType)

        # ===========================================================================================
        # Device setup for telemetry
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:2 -> Push updated conf files for telemetry test ")
        push_dmFile_on_IVI_device(self, OnboardingType, chipsetType)
        run_dm_service_on_IVI_device(self, OnboardingType, chipsetType)
        time.sleep(5)
        print("Successfully pushed Updated conf files for telemetry test ")

        # ===========================================================================================
        # Run telemetry - location stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:3 -> Run telemetry -location stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'location_geofence')
        # time.sleep(15)

        print("Telemetry-location stub run process is completed, verify logs for telemetry-location details : ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Step:4 -> Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        print("-----------------------------")
        print("Step:5 -> Device Side Validations : ")
        print("-----------------------------")

        # verify Latitude attribute in the device logs
        ls = verify_message_in_log(self, "Updated data latitude", "latitude")

        if "latitude" in str(ls[0]):
            print(f"Latitude attribute name printed in device log : ' {ls} ' ")
            testResult(self, "passed", "Latitude attribute should be present in telemetry data",
                       "Latitude attribute is present in telemetry data and device logs are updated with trip "
                       "details, pls refer device logs for"
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Latitude attribute is not present in telemetry data or device logs are not updated. pls refer device "
                "logs in detail")
            testResult(self, "verificationFailed", "Latitude attribute should be present in telemetry data ",
                       "Latitude attribute is not present in telemetry data or device logs are not updated. pls refer "
                       "device logs in detail ")

        # verify Longitude attribute in the device logs
        ls = verify_message_in_log(self, "Updated data longitude", "longitude")

        if "longitude" in str(ls[0]):
            print(f"Longitude attribute name printed in device log : ' {ls} ' ")
            testResult(self, "passed", "Longitude attribute should be present in telemetry data",
                       "Longitude attribute is present in telemetry data and device logs are updated with trip "
                       "details, pls refer device logs for"
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Longitude attribute is not present in telemetry data or device logs are not updated. pls refer "
                "device logs in detail")
            testResult(self, "verificationFailed", "Longitude attribute should be present in telemetry data ",
                       "Longitude attribute is not present in telemetry data or device logs are not updated. pls "
                       "refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Step:6 -> Cloud Side Validations : ")
        print("-----------------------------")

        # verify lat & long value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        time.sleep(60)

        response = telemetry_Curr_eventType(self, telemetry_lat_event_type, systemId, "valid")
        response_body = response.json()

        lat_value = long_value = ""

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == "LATITUDE":
                    lat_value = response_body["responseData"]["dataList"][i]["value"]
                if response_body["responseData"]["dataList"][i]["name"] == "LONGITUDE":
                    long_value = response_body["responseData"]["dataList"][i]["value"]

            print("Latitude stored in Cloud DB : ", lat_value)
            print("Longitude stored in Cloud DB : ", long_value)
        except:
            print("dataList is empty or no such attribute/parameter in api response")

        if lat_value != "0" and long_value != "0":
            testResult(self, "passed",
                       "Latitude & Longitude value should be saved in the Cloud DB. ",
                       "Latitude & Longitude value is saved in the Cloud DB. pls refer "
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "failed",
                       "Latitude & Longitude value should be saved in the Cloud DB. ",
                       "Latitude & Longitude value is not saved in the Cloud DB. pls refer "
                       "device & cloud logs for detailed info")
            # self.result.set_result(TestResults.failed)
        time.sleep(10)

        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")
        vehicleMap_page = page = ""

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

        time.sleep(60)

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

            print("Step:9 -> Verify ' System Id ' on Vehicle List UI Page : ")

            # Verify system Id in UI table
            vehicleList_page.verify_systemId_on_UI(systemId)

            print("-------------------------------------------------------------------------")

            print("Step:10 -> Verify & click on ' Notification ' image/option on Vehicle List UI Page : ")

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

            print(
                f"Step:11 -> Verify & click on '{notification_tab_name} ' tab/option on Notification window/Page : ")
            time.sleep(30)

            status = vehicleList_page.click_on_Notification_tab(notification_tab_name)
            time.sleep(5)
            status = vehicleList_page.click_on_Notification_tab(notification_tab_name)
            if status == 'present':
                testResult(self, "passed",
                           notification_tab_name + " tab/option should be displayed on Notification window/Page",
                           notification_tab_name + " tab/option is displayed on Notification window/Page")
            else:
                testResult(self, "failed",
                           notification_tab_name + " tab/option should be displayed on Notification window/Page ",
                           notification_tab_name + " tab/option is not displayed/clickable on Notification window/Page")

            print("-------------------------------------------------------------------------")

            print(f"Step:12 -> Verify {notification_name}  - Notification/Alert ")
            time.sleep(60)

            status = vehicleList_page.verify_notification(notification_name)
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " Notification/Alert should be listed on Notification window/Page",
                           notification_name + " Notification/Alert is listed on Notification window/Page")
            else:
                testResult(self, "verificationFailed",
                           notification_name + " Notification/Alert should be listed on Notification window/Page ",
                           notification_name + " Notification/Alert is not listed on Notification window/Page")

            print("-------------------------------------------------------------------------")

            print("Step:13 -> Click on View All button ")

            status = vehicleList_page.click_on_view_all_button()
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " window should open & list all the Geofence notifications",
                           notification_name + " window is opened & listed all the Geofence notifications")
            else:
                testResult(self, "failed",
                           notification_name + " window should open & list all the Geofence notifications ",
                           notification_name + " window is not opened or not listed the Geofence notifications")

            print("-------------------------------------------------------------------------")

            print(f"Step:14 -> Verify ' {notification_name} ' details' ")

            status, created_by, created_time, updated_by, updated_time, category, notification_type = vehicleList_page.verify_notification_details(
                notification_name, alert_text)
            print("Latest Notification Details :==>")
            print("Created By : ", created_by)
            print("Created Time : ", created_time)
            print("Updated By : ", updated_by)
            print("Updated Time : ", updated_time)
            print("Category : ", category)
            print("Notification Type : ", notification_type)
            time.sleep(60)
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " details should be listed on Notification window/Page",
                           notification_name + " details are listed on Notification window/Page")
            else:
                testResult(self, "failed",
                           notification_name + " details should be listed on Notification window/Page ",
                           notification_name + " details are not listed on Notification window/Page")

        except:
            print(f"{notification_name} alert is not listed yet, wait for another 60 sec")
            status, created_by, created_time, updated_by, updated_time, notification_type = vehicleList_page.verify_notification_details(
                notification_name, alert_text)
            time.sleep(60)
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " details should be listed on Notification window/Page",
                           notification_name + " details are listed on Notification window/Page")
            else:
                testResult(self, "failed",
                           notification_name + " details should be listed on Notification window/Page ",
                           notification_name + " details are not listed on Notification window/Page")
        print("-------------------------------------------------------------------------")

        try:

            print(f"Step:15 -> Click on close button : ")

            status = vehicleList_page.click_on_close_button()
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " window should be closed",
                           notification_name + " window is closed")
            else:
                testResult(self, "verificationFailed",
                           notification_name + " window should be closed ",
                           notification_name + " window is not closed")
        except:
            testResult(self, "verificationFailed",
                       notification_name + " window should be closed ",
                       notification_name + " window is not closed")

            print("-------------------------------------------------------------------------")
            reboot_primary_IVI(self, OnboardingType, chipsetType, "reboot")

