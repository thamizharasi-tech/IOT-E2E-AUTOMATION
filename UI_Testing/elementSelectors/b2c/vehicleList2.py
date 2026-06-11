import re
import time

from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.webUI_testData import b2c_base_url

webElements = {
    'vehicleList_endpoint': r'/developer-dashboard/vehicle-list',
    'addApp_button': '//*[@id="App"]//span[contains(text(), "Add App")]',
    'appName': '//*[@id="name"]',
    'appDescription': '//*[@id="description"]',
    'request_button': '//*[@id="App"]//td[contains(text(), "Vehicle Tracking")]',
    'save_button': '//button[3]/span[contains(text(), "Save")]',
    'table': '//table/tbody/tr[',
    'lat_text_input': "//*[@id='rc-tabs-2-panel-new']//input[@name='lat']",
    'long_text_input': "//*[@id='rc-tabs-2-panel-new']//input[@name='lng']",
    'radius_text_input': "//*[@id='rc-tabs-2-panel-new']//input[@name='radius']"
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

        # print(self.vehicleList_url)
        self.page.goto(b2c_base_url, timeout=120000)
        time.sleep(5)

    def verify_vehicleList_page_url(self):
        # Ensures the page is navigated to the given URL.
        try:
            self.commonFunctions.verify_current_page_URL(b2c_base_url)
            print("Landed on Vehicle List page")
            status = "present"
        except:
            status = "not_present"
        return status

    def verify_vehicleList_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle List")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_vehicleList_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle List").click()
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = 'not_present'
        return status

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
            # print(ui_text)
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

    def read_packageName_from_UI(self, systemId):
        status, device_status, package_name = self.verify_system_id_in_table(systemId)
        return status, device_status, package_name

    def verify_systemId_on_UI(self, systemId):
        # Verify system Id in UI table
        try:
            for i in range(1, 10):
                self.page.get_by_text(str(i), exact=True).click(timeout=30000)
                time.sleep(30)
                status, device_status, package_name = self.verify_system_id_in_table(systemId)
                if status == "present":
                    print("System Id is listed in UI table on Vehicle List page : " + str(i))
                    break
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_device_status_on_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)

        if device_status == "Active":
            print("Device Status is shown as ACTIVE on Vehicle List UI page")
            status = "present"
        else:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def get_package_name_from_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)
        print(status, device_status, package_name)
        return package_name

    def verify_default_package_name_on_UI(self, systemId):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)
        print(status, device_status, package_name)

        if package_name == "Essential":
            print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
            # print("By default device should have Essential package")
            status = "present"
        elif package_name == "Value":
            print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
            # print("By default device should have Essential package")
            status = "present"
        elif package_name == "Elite":
            print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
            # print("By default device should have Essential package")
            status = "present"
        else:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
            print(f"Package : ' {package_name} ' is shown instead of default/existing packages on Vehicle List UI page")

        return status

    def verify_package_name_on_UI(self, systemId, packageName):
        # Verify system Id in UI table
        status, device_status, package_name = self.verify_system_id_in_table(systemId)

        if packageName == "Value":
            if package_name == packageName:
                print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
                status = "present"
            else:
                print(f"Package : ' {package_name} ' is shown instead of ' Value ' on Vehicle List UI page")
                self.commonFunctions.screenshot("vehicleList_page")
                status = "not_present"
        elif packageName == "Elite":
            if package_name == packageName:
                print(f"Package : ' {package_name} ' is shown on Vehicle List UI page")
                status = "present"
            else:
                print(f"Package : ' {package_name} ' is shown instead of ' Elite ' on Vehicle List UI page")
                self.commonFunctions.screenshot("vehicleList_page")
                status = "not_present"
        return status

    def click_on_package_link(self, systemId):
        status, device_status, packageName = self.verify_system_id_in_table(systemId)
        try:
            self.page.get_by_role("row", name=systemId).get_by_text(packageName).click(timeout=60000)
            print("Vehicle Insight Icon is displayed on Vehicle List page")
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    # ----------------------------
    # Vehicle List - Package Window:
    # ----------------------------

    def verify_selected_pacakge_tab_on_dialog_box(self, packageName):
        try:
            self.page.get_by_role("tab", name=packageName)
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_desired_pacakge_tab_on_dialog_box(self, packageName):
        try:
            self.page.get_by_role("tab", name=packageName).click()
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_vin_on_pacakge_dialog_box(self, vin):
        try:
            self.page.get_by_role("dialog", name=vin).get_by_text(vin).click(timeout=60000)
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_Active_button(self):
        try:
            self.page.get_by_role("button", name="Activate").click()
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_success_msg_for_package_update(self):
        try:
            time.sleep(5)
            self.page.get_by_text("Package mapping requested successfully").click()
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    # ----------------------------
    # Vehicle List - Commands:
    # ----------------------------

    def click_on_Commands(self, systemId):
        # self.page.locator('//table/tbody/tr[2]/td[5]/div/div[3]/span').click(timeout=600000)
        try:
            self.page.get_by_role("row", name=systemId).locator("img").first.click(
                timeout=60000)
            print("Commands Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_Ignition_state(self):
        try:
            self.page.get_by_text("IGNITION STATE")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

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
            print(f" {text} button is displayed on UI ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg")
            # self.page.get_by_role("img", name="reload").locator("svg").click()
            self.page.get_by_role("img", name="reload").locator("svg").click(click_count=2)
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

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

            status = "present"

        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_success_msg_for_command(self):
        try:
            self.page.get_by_text("Command Published Successfully").click()
            status = "present"
            self.page.get_by_role("button", name="Close").click()
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    # ----------------------------
    # Vehicle List - Vehicle Insight:
    # ----------------------------

    def click_on_vehicle_insight(self, systemId):
        # self.page.locator('//table/tbody/tr[2]/td[5]/div/div[3]/span').click(timeout=600000)
        try:
            self.page.get_by_role("row", name=systemId).get_by_role("img", name="eye").locator("svg").click(
                timeout=60000)
            print("Vehicle Insight Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_more_option(self):
        try:
            self.page.get_by_role("button", name="down More").click()
            print("'More' option is present on Vehicle Insight RHS panel")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_reload_button(self):
        try:
            self.page.get_by_role("img", name="reload").locator("svg").click()
            status = "present"
        except:

            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_vehicle_telemetry_attribute_name(self, attribute_name):
        try:
            self.page.get_by_role("cell", name=attribute_name).click()
            print(
                f" => Vehicle Insight : '{attribute_name}' option/attribute is listed/shown under Vehicle Insight RHS "
                f"panel ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_vehicle_telemetry_attribute_status(self, attribute_name, status):
        attribute_status = attribute_name + ' ' + status
        print(attribute_status)
        try:
            self.page.get_by_role("row", name=attribute_status).locator("td").click()
            print(
                f" => Vehicle Insight : '{attribute_status}' option/attribute is listed/shown under Vehicle Insight RHS "
                f"panel ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_vehicle_telemetry_attribute_value(self, attribute_value):
        try:
            self.page.get_by_role("cell", name=attribute_value, exact=True).click()
            print(f" => Vehicle Insight : '{attribute_value}' value is listed/shown under Vehicle Insight RHS "
                  f"panel ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

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
                # print(veh_attribute_name, veh_attribute_value)
                # break

            else:
                ui_attribute_name = "not_present"
                ui_attribute_value = "not_present"
        return ui_attribute_name, ui_attribute_value

    # ----------------------------
    # Vehicle List - Geofence:
    # ----------------------------

    def click_on_Geofence_config(self, systemId):
        try:
            # self.page.get_by_role("row", name=systemId).get_by_role("img", name="radius-setting").locator("svg").click(
            # timeout=60000)
            self.page.get_by_role("row", name=systemId).locator("img").nth(1).click()
            print("Geofence Config Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_create_geofence(self):
        try:
            self.page.get_by_role("tab", name="Create Geofence").click()
            print("Create Geofence tab/option is displayed on Geofence Config page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_name_for_geofence(self, data):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text('Name')
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_role("textbox").fill(data)
            print("Geofence Name input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_latitude_for_geofence(self, lat):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Latitude")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lat']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lat']").fill(lat)
            time.sleep(5)
            print("Geofence latitude input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_longitude_for_geofence(self, data):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Longitude")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").fill(data)
            time.sleep(5)
            print("Geofence longitude input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_radius_for_geofence(self, data):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Radius")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").fill(data)
            time.sleep(5)
            print("Geofence radius input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_unit_for_geofence(self, data):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Select Unit").click()
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("METER").click()
            if data == "METER":
                self.page.get_by_text(data).nth(4).click()
            else:
                self.page.get_by_text(data).click()
            time.sleep(5)
            print("Geofence unit filed is available and selected the desired unit from drop down box")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_submit_button_for_geofence(self):
        try:
            self.page.get_by_role("button", name="Submit").click()
            print("Clicked on 'Submit' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_success_msg_for_geofenceCreation(self):
        try:
            self.page.get_by_text("Location Saved Successfully!").click()
            self.page.get_by_text("Location Saved Successfully for vehicle!").click()
            status = "present"
            time.sleep(5)
            # self.page.get_by_role("button", name="Close").click()
            # self.page.get_by_role("button", name="Close").click()
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def navigate_to_geofence_list(self):
        try:
            self.page.get_by_role("tab", name="Geofence List").click()
            print("Clicked on 'Geofence List' tab")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_geofence_list(self):
        try:
            self.page.get_by_label("Geofence List").get_by_role("listitem").click()
            print("Geofence List is displayed")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_geofence_delete_button(self):
        try:
            self.page.get_by_label("delete").locator("svg")
            print("Geofence Delete button is displayed")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_geofence_delete_button(self):
        try:
            self.page.get_by_label("delete").locator("svg").click()
            print("Geofence Delete button is clicked")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_geofence_delete_confirmation_message(self):
        try:
            self.page.get_by_text("Are you sure to delete this geofence?").click()
            print("Geofence delete confirmation message is displayed")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_geofence_delete_yes_button(self):
        try:
            self.page.get_by_role("button", name="Yes", exact=True).click()
            print("Successfully clicked on Geofence delete confirmation - Yes button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def close_geofence_window(self):
        try:
            self.page.get_by_role("button", name="Close").click()
            print("Clicked on 'close' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def create_new_geofence(self, lat, lng, rad, unit):
        try:
            self.enter_latitude_for_geofence(lat)
            time.sleep(15)
            self.enter_longitude_for_geofence(lng)
            time.sleep(15)
            self.enter_radius_for_geofence(rad)
            time.sleep(15)
            self.select_unit_for_geofence(unit)
            time.sleep(10)
            self.click_on_submit_button_for_geofence()
            self.verify_success_msg_for_geofenceCreation()
            time.sleep(15)
            self.navigate_to_geofence_list()
            time.sleep(20)
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def Create_new_geofence1(self, lat, lng, rad, unit):
        # try:
        self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Latitude")
        time.sleep(5)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lat']").click()
        time.sleep(10)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lat']").fill(lat)
        time.sleep(15)
        self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Longitude")
        time.sleep(5)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").click()
        time.sleep(10)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").fill(lng)
        time.sleep(15)
        self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Radius")
        time.sleep(5)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").click()
        time.sleep(10)
        self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").fill(rad)
        time.sleep(15)
        self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Select Unit").click()
        time.sleep(5)
        self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("METER").click()
        time.sleep(5)
        if unit == "METER":
            self.page.get_by_text(unit).nth(4).click()
        else:
            self.page.get_by_text(unit).click()
        time.sleep(10)
        self.page.get_by_role("button", name="Submit").click()
        self.verify_success_msg_for_geofenceCreation()
        time.sleep(15)
        self.navigate_to_geofence_list()
        time.sleep(20)
        status = "present"
        # except:
        # self.commonFunctions.screenshot("vehicleList_page")
        # status = "not_present"
        return status

    # ----------------------------
    # Vehicle List - Notification:
    # ----------------------------

    def click_on_Notifications(self, systemId):
        try:
            self.page.get_by_role("row", name=systemId).get_by_role("img", name="bell").locator("svg").click(
                timeout=60000)
            print("Notification Bell Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_Geofence_tab(self):
        # self.page.get_by_role("tab", name="GEOFENCE").click()
        # self.page.locator("div").filter(has_text=re.compile(r"^GEOFENCE$")).first.click()
        # self.page.locator("//*[@id='rc-tabs-5-tab-GEOFENCE NOTIFICATION']").click(6000)
        try:
            self.page.get_by_role("tab", name="GEOFENCE").click()
            print("Geofence Tab is selected on Notification window/page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "present"

        return status

    def verify_geofence_notification(self):
        try:
            self.page.get_by_text("GEOFENCE NOTIFICATION").first.click()
            print("Geofence Notification is listed/displayed on Notification window/page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_view_all_button(self):
        try:
            self.page.get_by_role("button", name="View all").click()
            print("Geofence Notification window/page is displayed")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_geofence_details(self):
        try:
            self.page.locator(".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td").first.click()
            self.page.get_by_text("Geofence breach for vin ").click()
            self.page.get_by_role("button", name="Close").click()
            print("Geofence Notification is listed/displayed on Notification window/page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_Notification_tab(self, tabName):

        try:
            self.page.get_by_role("tab", name=tabName).click()
            print(f"{tabName} tab is selected on Notification window/page")
            status = "present"
        except:
            filename = 'vehicleList_page_' + tabName
            self.commonFunctions.screenshot(filename)
            status = "present"

        return status

    def verify_notification(self, alertName):
        try:
            self.page.get_by_text(alertName).first.click()
            print(f"{alertName} is listed/displayed on Notification window/page")
            status = "present"
        except:
            filename = 'vehicleList_page_' + alertName
            self.commonFunctions.screenshot(filename)
            status = "not_present"
        return status

    def verify_notification_details(self, alertName, alertText):
        created_by = created_time = updated_by = updated_time = category = notification_type = ''
        try:
            self.page.locator(".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td").first.click()
            # text = self.page.locator(".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td").first.text_content()
            created_by = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(1)").text_content()
            created_time = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(2)").text_content()
            updated_by = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(3)").text_content()
            updated_time = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(4)").text_content()
            category = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(5)").text_content()
            notification_type = self.page.locator(
                ".ant-table-body > table > .ant-table-tbody > tr:nth-child(2) > td:nth-child(6)").text_content()
            print(created_by, created_time, updated_by, updated_time, category, notification_type)
            self.page.get_by_text(alertText).click()
            # self.page.get_by_role("button", name="Close").click()
            print(f"{alertName} is listed/displayed on Notification window/page")
            status = "present"
        except:
            filename = 'vehicleList_page_details_' + alertName
            self.commonFunctions.screenshot(filename)
            status = "not_present"

        return status, created_by, created_time, updated_by, updated_time, category, notification_type

    def click_on_close_button(self):
        try:
            self.page.get_by_role("button", name="Close").click()
            print("Clicked on 'close' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def page_reload(self):
        self.page.keyboard.press('F5', delay=1000)
        self.page.reload()
