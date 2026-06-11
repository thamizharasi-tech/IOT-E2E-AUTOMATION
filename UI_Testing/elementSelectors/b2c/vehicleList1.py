import re
import time

from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.webUI_testData import b2c_base_url

webElements = {
    'vehicleList_endpoint': r'/developer-dashboard/vehicle-list',
    'addApp_button': '//*[@id="App"]//span[contains(text(), "Add App")]',
    'appName': '//*[@id="name"]',
    'appDescription': '//*[@id="description"]',
    'request_button': '//*[@id="App"]//td[contains(text(), "Vehicle Tracking")]',
    'save_button': '//button[3]/span[contains(text(), "Save")]',
    'table': '//table/tbody/tr['
}


class vehicleList_Page:
    def __init__(self, page):
        self.page = page
        self.commonFunctions = common_functions(self.page)
        self.vehicleList_url = b2c_base_url + webElements["vehicleList_endpoint"]

    def launch_b2c_web(self):
        self.page.goto(b2c_base_url, timeout=120000)
        time.sleep(5)

    def navigate_to_vehicelList_page(self):

        print(self.vehicleList_url)
        self.page.goto(self.vehicleList_url, timeout=120000)
        time.sleep(5)

    def verify_vehicleList_page_url(self):
        # Ensures the page is navigated to the given URL.
        try:
            self.commonFunctions.verify_current_page_URL(self.vehicleList_url)
            print("Landed on Vehicle List page")

            testResult(self, "passed", "User should navigate to / land on Vehicle List page ",
                       "User is navigated to / landed on Vehicle List page successfully ")

        except:
            testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

    def verify_vehicleList_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle List")
            testResult(self, "passed", "Vehicle list tab should be present on UI page ",
                       "Vehicle list tab is present on UI page ")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed", "Vehicle list tab should be present on UI page ",
                       "Vehicle list tab is not present on UI page ")

    def click_on_vehicleList_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle List").click()
            testResult(self, "passed", "User should be able to click on Vehicle list tab",
                       "User is able to click on Vehicle list tab")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "User should be able to click on Vehicle list tab",
                       "User is not able to click on Vehicle list tab ")

    # ----------------------------
    # Vehicle List page:
    # ----------------------------

    def verify_systemId_cloumnName(self):
        status = self.commonFunctions.verify_cell_locator_on_page(self, "System ID")
        return status

    def verify_model_cloumnName(self):
        status = self.commonFunctions.verify_cell_locator_on_page(self, "Model")
        return status

    def verify_state_cloumnName(self):
        status = self.commonFunctions.verify_cell_locator_on_page(self, "State")
        return status

    def verify_Package_cloumnName(self):
        status = self.commonFunctions.verify_cell_locator_on_page(self, "Package")
        return status

    def verify_vehicleData_cloumnName(self):
        status = self.commonFunctions.verify_cell_locator_on_page(self, "Vehicle Data")
        return status

    def verify_system_id_in_table(self, systemId):
        for i in range(2, 12):
            ls1 = webElements["table"] + str(i) + ']'
            sysId_col = ls1 + '/td[1]'
            ui_text = self.page.locator(sysId_col).text_content()
            #print(ui_text)
            if ui_text == systemId:
                status_col = ls1 + '/td[3]'
                package_col = ls1 + '/td[4]'
                status = "present"
                device_state = self.page.locator(status_col).text_content()
                pacakge_name = self.page.locator(package_col).text_content()
                # print(device_state)
                break
            else:
                status = "not_present"
                device_state = "not_present"
                pacakge_name = "not_present"
        return status, device_state, pacakge_name

    def verify_systemId_on_UI(self, systemId):
        # Verify system Id in UI table
        try:
            for i in range(1, 10):
                self.page.get_by_text(str(i), exact=True).click(timeout=30000)
                time.sleep(30)
                status, device_status, package_name = self.verify_system_id_in_table(systemId)
                if status == "present":
                    print("System Id is listed in UI table on Vehicle List page : " + str(i))

                    testResult(self, "passed",
                               "System Id of newly onboarded device should be listed in UI table on Vehicle List page",
                               "System Id of newly onboarded device is listed in UI table on Vehicle List page")
                    break
        except:
            testResult(self, "failed",
                       "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                       "System Id of newly onboarded device is not listed in UI table on Vehicle List page")


    def verify_device_status_on_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)

        if device_status == "Active":
            print("Device Status is shown as ACTIVE on Vehicle List UI page")

            testResult(self, "passed", "Device Status should be ACTIVE on Vehicle List UI page",
                       "Device Status is shown as ACTIVE on Vehicle List UI page")
        else:
            testResult(self, "failed",
                       "Device Status should be ACTIVE on Vehicle List UI page  ",
                       "Device Status is not ACTIVE on Vehicle List UI page")

    def verify_package_name_on_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)

        if package_name == "Essential":
            print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
            print("By default device should have Essential package")

            testResult(self, "passed", "By default device should have 'Essential' package",
                       "By default device is having 'Essential' package")
        else:
            print(f"Package : ' {package_name} ' is shown instead of ' Essential ' on Vehicle List UI page")
            testResult(self, "failed",
                       "By default device should have 'Essential' package",
                       "By default device is not having 'Essential' package")

    def verify_value_package_name_on_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)

        if package_name == "Value":
            print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")

            testResult(self, "passed", "Device should have 'Value' package",
                       "Device is having 'Value' package")
        else:
            print(f"Package : ' {package_name} ' is shown instead of ' Value ' on Vehicle List UI page")
            testResult(self, "failed",
                       "Device should have 'Value' package",
                       "Device is not having 'Value' package")

    def click_on_pacakge_link(self, systemId):
        try:
            self.page.get_by_role("row", name=systemId).get_by_text("Essential").click(timeout=60000)
            print("Vehicle Insight Icon is displayed on Vehicle List page")

            testResult(self, "passed",
                       "Package Link should be present for each onboarded device on Vehicle List page",
                       "Package Link is present for newly onboarded device on Vehicle List page")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "Package Link should be present for each onboarded device on Vehicle List page  ",
                       "Package Link is not present/clickable on Vehicle List page")

    # ----------------------------
    # Vehicle List - Package Window:
    # ----------------------------


    def verify_value_pacakge_tab_on_dialog_box(self):
        try:
            self.page.get_by_role("tab", name="Value")

            testResult(self, "passed",
                       "Value Package tab should be available/displayed on package dialog box/window",
                       "Value Package tab is available/displayed on package dialog box/window")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "Value Package tab should be available/displayed on package dialog box/window",
                       "Value Package tab is not available/displayed on package dialog box/window")

    def click_on_value_pacakge_tab_on_dialog_box(self):
        try:
            self.page.get_by_role("tab", name="Value").click()

            testResult(self, "passed",
                       "Value Package feature list should be displayed on clicking it",
                       "Value Package feature list is displayed on clicking it")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "Value Package feature list should be displayed on clicking it",
                       "Value Package feature list is not displayed on clicking it")

    def verify_vin_on_pacakge_dialog_box(self, vin):
        try:

            self.page.get_by_role("dialog", name=vin).get_by_text(vin).click(timeout=60000)

            testResult(self, "passed",
                       "VIN no should be displayed as header on package dialog box/window",
                       "VIN no is displayed as header on package dialog box/window")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "verificationFailed",
                       "VIN no should be displayed as header on package dialog box/window ",
                       "VIN no is not displayed as header on package dialog box/window")

    def click_on_Active_button(self):
        try:
            self.page.get_by_role("button", name="Activate").click()

            testResult(self, "passed",
                       "User should be able to click on 'Activate' button for package upgrade",
                       "User is able to click on 'Activate' button for package upgrade")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "User should be able to click on 'Activate' button for package upgrade",
                       "User is not able to click on 'Activate' button for package upgrade")

    def verify_success_msg_for_package_upgrade(self):
        try:
            self.page.get_by_text("Package mapping requested successfully").click()

            testResult(self, "passed",
                       "Success message should be displayed on clicking Activate button",
                       "Success message is displayed on clicking Activate button")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "VerificationFailed",
                       "Success message should be displayed on clicking Activate button",
                       "Success message is not displayed on clicking Activate button")

    # ----------------------------
    # Vehicle List - Commands:
    # ----------------------------

    def click_on_Commands(self, systemId):
        # self.page.locator('//table/tbody/tr[2]/td[5]/div/div[3]/span').click(timeout=600000)
        try:
            self.page.get_by_role("row", name=systemId).locator("img").first.click(
                timeout=60000)
            print("Commands Icon is displayed on Vehicle List page")

            testResult(self, "passed",
                       "Commands Icon should be displayed for each onboarded device on Vehicle List page",
                       "Commands Icon is displayed for newly onboarded device on Vehicle List page")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "Commands Icon should be displayed for each onboarded device on Vehicle List page  ",
                       "Commands Icon is not displayed/clickable on Vehicle List page")

    def select_Ignition_state(self):
        try:
            self.page.get_by_text("IGNITION STATE")

            testResult(self, "passed",
                       "'IGNITION STATE' should be displayed ",
                       "'IGNITION STATE' option is displayed ")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "'IGNITION STATE' should be displayed ",
                       "'IGNITION STATE' option is not displayed ")

    def click_on_ignition_button(self, buttonName):
        try:
            if buttonName == "Lock":
                i = int(1)
            elif buttonName == "Unlock":
                i = int(2)
            elif buttonName == "Acc":
                i = int(3)
            elif buttonName == "ON":
                i = int(4)
            self.page.get_by_role("complementary").get_by_role("button").nth(i).click()

            text = "' IGNITION STATE - " + buttonName + " '"

            testResult(self, "passed",
                       text + " option/button should be displayed ",
                       text + " option/button is displayed ")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       text + " option/button should be displayed ",
                       text + " option/button is not displayed ")

    def click_on_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg")
            #self.page.get_by_role("img", name="reload").locator("svg").click()
            self.page.get_by_role("img", name="reload").locator("svg").click(click_count=2)

            testResult(self, "passed",
                       "'Reload' option/button should be displayed ",
                       "'Relaod' option/button is displayed ")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "'Reload' option/button should be displayed ",
                       "'Reload' option/button is not displayed ")

    def verify_ignition_button_status(self, buttonName):
        try:
            if buttonName == "Lock":
                i = int(1)
            elif buttonName == "Unlock":
                i = int(2)
            elif buttonName == "Acc":
                i = int(3)
            elif buttonName == "ON":
                i = int(4)

            self.page.locator("div").filter(has_text=re.compile(r"^IGNITION STATE$")).nth(1).click()

            text = "' IGNITION STATE - " + buttonName + " '"

            testResult(self, "passed",
                       text + "option/button should be clicked ",
                       text + " option/button is clicked ")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       text + "option/button should be clicked ",
                       text + "option/button is not clicked ")


    def verify_success_msg_for_command(self):
        try:
            self.page.get_by_text("Command Published Successfully").click()
            testResult(self, "passed",
                       "Success message should be displayed on clicking command button",
                       "Success message is displayed on clicking command button")
            self.page.get_by_role("button", name="Close").click()
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "VerificationFailed",
                       "Success message should be displayed on clicking command button",
                       "Success message is not displayed on clicking command button")

    # ----------------------------
    # Vehicle List - Vehicle Insight:
    # ----------------------------

    def click_on_vehicle_insight(self, systemId):
        # self.page.locator('//table/tbody/tr[2]/td[5]/div/div[3]/span').click(timeout=600000)
        try:
            self.page.get_by_role("row", name=systemId).get_by_role("img", name="eye").locator("svg").click(
                timeout=60000)
            print("Vehicle Insight Icon is displayed on Vehicle List page")

            testResult(self, "passed",
                       "Vehicle Insight Icon should be displayed for each onboarded device on Vehicle List page",
                       "Vehicle Insight Icon is displayed for newly onboarded device on Vehicle List page")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "Vehicle Insight Icon should be displayed for each onboarded device on Vehicle List page  ",
                       "Vehicle Insight Icon is not displayed/clickable on Vehicle List page")


    def click_on_more_option(self):
        try:
            self.page.get_by_role("button", name="down More").click()
            print("'More' option is present on Vehicle Insight RHS panel")
            testResult(self, "passed",
                       "'More' option should be present to expand the list on Vehicle Insight RHS panel",
                       "'More' option is present and on click, expanded the list on Vehicle Insight RHS panel")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "verificationFailed",
                       "'More' option should be present to expand the list on Vehicle Insight RHS panel",
                       "'More' option is not present/clickable on Vehicle Insight RHS panel")

    def verify_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg")
            testResult(self, "passed",
                       "'Page Reload' option/image should be present to refresh Vehicle Insight RHS panel",
                       "'Page Reload' option/image is present to refresh Vehicle Insight RHS panel")
        except:

            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "'Page Reload' option/image should be present to refresh Vehicle Insight RHS panel",
                       "'Page Reload' option/image is not present on Vehicle Insight RHS panel")

    def click_on_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg").click()
            testResult(self, "passed",
                       "'Vehicle Insight' RHS panel should be refreshed/reloaded on click",
                       "'Vehicle Insight' RHS panel is refreshed/reloaded on click")
        except:

            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "passed",
                       "'Vehicle Insight' RHS panel should be refreshed/reloaded on click",
                       "'Vehicle Insight' RHS panel is not refreshed/reloaded on click")

    def verify_vehicle_speed_option(self):
        try:
            self.page.get_by_role("cell", name="Perf Vehicle Speed").click()
            print(f" => Vehicle Insight : ' Perf Vehicle Speed ' option is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed", "'Perf Vehicle Speed ' should be listed under Vehicle Insight RHS panel",
                       "'Perf Vehicle Speed ' is listed under Vehicle Insight RHS panel")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed", "'Perf Vehicle Speed ' should be listed under Vehicle Insight RHS panel",
                       "'Perf Vehicle Speed ' is not listed under Vehicle Insight RHS panel")

    def verify_vehicle_speed_value(self):
        try:
            self.page.get_by_role("cell", name="32 km/hr").click()
            print(
                f" => Vehicle Insight : ' Perf Vehicle Speed - 32 km/hr ' is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed",
                       "' Perf Vehicle Speed value ' should be same as that of configured telemetry stub on device",
                       "' Perf Vehicle Speed value ' is same as that of configured telemetry stub on device")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "' Perf Vehicle Speed value ' should be same as that of configured telemetry stub on device",
                       "' Perf Vehicle Speed value ' is not shown or same as that of configured telemetry stub on device")

    def verify_perf_odometer_option(self):
        try:
            self.page.get_by_role("cell", name="Perf Odometer").click()
            print(f" => Vehicle Insight : ' Perf Odometer ' option is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed", "' Perf Odometer ' should be listed under Vehicle Insight RHS panel",
                       "' Perf Odometer ' is listed under Vehicle Insight RHS panel")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed", "' Perf Odometer ' should be listed under Vehicle Insight RHS panel",
                       "' Perf Odometer ' is not listed under Vehicle Insight RHS panel")

    def verify_perf_odometer_value(self):
        try:
            self.page.get_by_role("cell", name="12031 km").click()
            print(
                f" => Vehicle Insight : ' Perf Odometer - 12031 km ' is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed",
                       "' Perf Odometer value ' should be same as that of configured telemetry stub on device",
                       "' Perf Odometer ' is same as that of configured telemetry stub on device")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "' Perf Odometer ' should be same as that of configured telemetry stub on device",
                       "' Perf Odometer ' is not shown or same as that of configured telemetry stub on device")

    def verify_fuel_level_option(self):
        try:
            self.page.get_by_role("cell", name="Fuel Level", exact=True).click()
            print(f" => Vehicle Insight : ' Fuel Level ' option is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed", "' Fuel Level ' should be listed under Vehicle Insight RHS panel",
                       "' Fuel Level ' is listed under Vehicle Insight RHS panel")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed", "' Fuel Level ' should be listed under Vehicle Insight RHS panel",
                       "' Fuel Level ' is not listed under Vehicle Insight RHS panel")

    def verify_fuel_level_value(self):
        try:
            self.page.get_by_role("cell", name="8192 ml").click()
            print(
                f" => Vehicle Insight : ' Fuel Level - 8192 ml ' is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed",
                       "' Fuel Level value ' should be same as that of configured telemetry stub on device",
                       "' Fuel Level value ' is same as that of configured telemetry stub on device")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "' Fuel Level value ' should be same as that of configured telemetry stub on device",
                       "' Fuel Level value ' is not shown or same as that of configured telemetry stub on device")

    def verify_battery_level_option(self):
        try:
            self.page.get_by_role("cell", name="Ev Battery Level", exact=True).click()
            print(f" => Vehicle Insight : ' Ev Battery Level ' option is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed", "' Ev Battery Level ' should be listed under Vehicle Insight RHS panel",
                       "' Ev Battery Level ' is listed under Vehicle Insight RHS panel")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed", "' Ev Battery Level ' should be listed under Vehicle Insight RHS panel",
                       "' Ev Battery Level ' is not listed under Vehicle Insight RHS panel")

    def verify_battery_level_value(self):
        try:
            self.page.get_by_role("cell", name="128 wh").click()
            print(
                f" => Vehicle Insight : ' Fuel Level - 128 wh ' is listed/shown under Vehicle Insight RHS panel ")
            testResult(self, "passed",
                       "' Ev Battery Level value ' should be same as that of configured telemetry stub on device",
                       "' Ev Battery Level value ' is same as that of configured telemetry stub on device")
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            testResult(self, "failed",
                       "' Ev Battery Level value ' should be same as that of configured telemetry stub on device",
                       "' Ev Battery Level value ' is not shown or same as that of configured telemetry stub on device")

    def verify_vehicle_insight_table(self, attribute_name):
        for i in range(2, 13):
            # //table/tbody/tr[2]/th
            tab = '//*[@id="app"]//main[2]//div[2]/div/table/tbody/tr[' + str(i) + ']'
            veh_attribute_name = tab + '/th'
            veh_attribute_value = tab + '/td'
            # print(veh_attribute_name, veh_attribute_value)
            ui_attribute_name = self.page.locator(veh_attribute_name).text_content()
            if ui_attribute_name == attribute_name:
                ui_attribute_value = self.page.locator(veh_attribute_value).text_content()
                #print(veh_attribute_name, veh_attribute_value)
                # break

            else:
                ui_attribute_name = "not_present"
                ui_attribute_value = "not_present"
        return ui_attribute_name, ui_attribute_value
