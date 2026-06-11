import time
from datetime import datetime

from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, telemetry_speed_attribute, \
    b2c_telemetry_speed_value, telemetry_speed_event_type, telemetry_curr_Speed, b2c_telemetry_speed_notification_value
from C2CModules.network_connectivity_modules import set_network_connectivity_on_device
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, run_paho_command_on_primary_IVI, \
    push_dmFile_on_IVI_device, run_dm_service_on_IVI_device, pull_logs_from_IVI_device
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.elementSelectors.b2c.vehicleMap import vehicleMap_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi
notification_tab_name = "SPEED"
notification_name = "SPEED NOTIFICATION"
alert_text = 'Speed alert'


class Test_notification:

    def test_speed_alert(self):

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
        # Run location stub on device for notification/alert
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:5 -> Configure & Run location stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, 'location_geofence')

        print("Location stub start/run process is completed, verify logs & UI for telemetry details : ")
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
            print(f"Step:10 -> Verify & click on '{notification_tab_name} ' tab/option on Notification window/Page : ")

            status = vehicleList_page.click_on_Notification_tab(self, notification_tab_name)
            if status == 'present':
                testResult(self, "passed",
                           {notification_tab_name} + " tab/option should be displayed on Notification window/Page",
                           {notification_tab_name} + " tab/option is displayed on Notification window/Page")
            else:
                testResult(self, "failed",
                           {notification_tab_name} + " tab/option should be displayed on Notification window/Page ",
                           {
                               notification_tab_name} + " tab/option is not displayed/clickable on Notification window/Page")

            print("-------------------------------------------------------------------------")

            # Step - 11
            print(f"Step:11 -> Verify {notification_name}  - Notification/Alert ")

            status = vehicleList_page.verify_notification(self, notification_name)
            if status == 'present':
                testResult(self, "passed",
                           {notification_name} + " Notification/Alert should be listed on Notification window/Page",
                           {notification_name} + " Notification/Alert is listed on Notification window/Page")
            else:
                testResult(self, "failed",
                           {notification_name} + " Notification/Alert should be listed on Notification window/Page ",
                           {notification_name} + " Notification/Alert is not listed on Notification window/Page")

            print("-------------------------------------------------------------------------")

            # Step - 12
            print("Step:12 -> Click on View All button ")

            status = vehicleList_page.click_on_view_all_button()
            if status == 'present':
                testResult(self, "passed",
                           notification_name + "New window should open & list all the Speed notifications",
                           notification_name + "New window is opened & listed all the Speed notifications")
            else:
                testResult(self, "failed",
                           notification_name + " window should open & list all the Speed notifications ",
                           notification_name + " window is not opened or not listed the Speed notifications")

            print("-------------------------------------------------------------------------")
            # Step - 13
            print(f"Step:13 -> Verify ' {notification_tab_name} ' details' ")

            status = vehicleList_page.verify_notification_details(self, notification_name)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed",
                           notification_name + " details should be listed on Notification window/Page",
                           notification_name + " details are listed on Notification window/Page")
            else:
                testResult(self, "failed",
                           notification_name + " details should be listed on Notification window/Page ",
                           notification_name + " details are not listed on Notification window/Page")

        except:
            print(f"{notification_name} alert is not listed yet, wait for another 90 sec")
            testResult(self, "failed",
                       notification_name + " should be listed on Notification window/Page ",
                       notification_name + " are not listed on Notification window/Page")
            time.sleep(90)

        print("-------------------------------------------------------------------------")

    def test_speed_notification_can(self):

        now = datetime.now()
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M_%S")
        print("Current date & time1 :", dt)

        # ===========================================================================================
        # Setup network connectivity if network is unreachable on device
        # ===========================================================================================

        print("Step:1 -> Setup network connectivity if network is unreachable on device : ")
        set_network_connectivity_on_device(self, OnboardingType, chipsetType, netwrokType)

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
        # Run telemetry stub on device for telemetry data
        # ===========================================================================================
        print("----------------------------------------------------------")
        print("Step:3 -> Run telemetry stub on device : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "telemetry_can_speed_notification")
        time.sleep(15)

        print("Telemetry stub run process is completed, verify logs for telemetry details : ")
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

        # telemetry - speed

        print("-----------------------------")
        print("Step:5 -> Device Side Validations : ")
        print("-----------------------------")

        # verify speed attribute in the device logs
        ls = verify_message_in_log(self, telemetry_speed_attribute, telemetry_speed_attribute)

        if telemetry_speed_attribute in str(ls[0]):
            print(f"Speed attribute name printed in device log : ' {telemetry_speed_attribute} ' ")
            testResult(self, "passed", "Speed attribute should be present in telemetry data",
                       "Speed attribute is present in telemetry data and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Speed attribute should be present in telemetry data ",
                       "Speed attribute is not present in telemetry data or device logs are not updated. pls refer device logs in detail ")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_notification_value
        ls = verify_message_in_log(self, b2c_telemetry_speed_notification_value, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "passed", "Speed value should be published to cloud ",
                       "Speed value is published to cloud and device logs are updated with trip details, pls refer device logs for "
                       "detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail")
            testResult(self, "verificationFailed", "Speed value should be published to cloud ",
                       "Speed value is not published to cloud or device logs are not updated. pls refer device logs in detail ")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Step:6 -> Cloud Side Validations : ")
        print("-----------------------------")

        # verify speed value @ cloud

        # Get systemId and hit telemetry request
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("Speed value configured in the telemetry stub : ", b2c_telemetry_speed_notification_value)
            print("Speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(value) == int(b2c_telemetry_speed_value):
            testResult(self, "passed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is stored in the Cloud DB and same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")
            # self.result.set_result(TestResults.passed)
        else:
            testResult(self, "passed",
                       "Speed value should be stored in the Cloud DB and same as that of configured in the telemetry stub running on device",
                       "Speed value is not stored in the Cloud DB or same as that of configured in the telemetry stub running on device . pls refer "
                       "cloud logs for detailed info")

            # self.result.set_result(TestResults.failed)
        time.sleep(60)
        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")

        try:

            print("Step:7 -> Launch B2C Web UI : ")
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

        try:
            print("Step:8 -> User should land on Vehicle List Page : ")
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
            time.sleep(120)

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
                           notification_name + " window should open & list all the Speed notifications",
                           notification_name + " window is opened & listed all the Speed notifications")
            else:
                testResult(self, "failed",
                           notification_name + " window should open & list all the Speed notifications ",
                           notification_name + " window is not opened or not listed the Speed notifications")

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
