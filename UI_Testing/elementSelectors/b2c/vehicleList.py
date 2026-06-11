import re
import time

from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.webUI_testData import b2c_base_url

webElements = {
    'vehicleList_endpoint': r'',
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
            print(self.vehicleList_url)
            self.commonFunctions.verify_current_page_URL(self.vehicleList_url)
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

    def read_packageName_from_UI(self, systemId):
        status, device_status, package_name = self.verify_system_id_in_table(systemId)
        return status, device_status, package_name

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
            self.page.get_by_text("IGNITION STATE").click()
            self.page.get_by_text("IGNITION STATE").nth(1).click()
            # self.page.get_by_title(base_command_name).get_by_text(base_command_name).click()
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

    def verify_success_msg_for_command(self):
        try:
            self.page.get_by_text("Command Published Successfully").click()
            self.page.get_by_text("Command could not be send to device").click()
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
            self.page.get_by_role("cell", name=attribute_name, exact=True).click()
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
            self.page.get_by_role("row", name=attribute_status, exact=True).locator("td").click()
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

    def enter_name_for_geofence(self, geofence_name):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text('Name')
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='geoName']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_role("textbox").fill(geofence_name)
            time.sleep(5)
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

    def enter_longitude_for_geofence(self, longi):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Longitude")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='lng']").fill(longi)
            time.sleep(5)
            print("Geofence longitude input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_radius_for_geofence(self, rad):
        try:
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Radius")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Create Geofence").locator("input[name='radius']").fill(rad)
            time.sleep(5)
            print("Geofence radius input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_unit_for_geofence(self, unit):
        try:
            # self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("Select Unit").click()
            self.page.get_by_role("tabpanel", name="Create Geofence").get_by_text("METER").click()
            if unit == "METER":
                self.page.get_by_text(unit).nth(4).click()
            else:
                self.page.get_by_text(unit).click()
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

    def click_on_schedulealert_button_in_geofencelist_page(self):
        try:
            self.page.locator(".ant-list-item-extra > .ant-space > div").first.click()
            time.sleep(10)
            print("Clicked on 'Schedule alert' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_alert_name_for_schedule(self, alertname):
        try:
            # self.page.get_by_role("tabpanel", name="Geofence List").get_by_text("AlertName")
            # time.sleep(5)
            # self.page.get_by_role("tabpanel", name="Geofence List").locator("input[name='alertName']").click()
            # time.sleep(10)
            self.page.locator("input[name=\"alertName\"]").click()
            self.page.locator("input[name=\"alertName\"]").fill(alertname)
            time.sleep(5)
            print("Alert Name input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_start_date_for_schedulealert(self):
        try:
            self.page.locator(".ant-picker-input").first.click()
            self.page.get_by_text("17", exact=True).click()
            time.sleep(5)
            print("Start Date input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_end_date_for_schedulealert(self):
        try:
            self.page.locator("div:nth-child(3) > .ant-picker > .ant-picker-input").first.click()
            self.page.get_by_role("cell", name="19", exact=True).click()
            time.sleep(5)
            print("End Date input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def enter_start_time_for_schedulealert(self):
        try:
            self.page.locator("div:nth-child(8) > div > .ant-picker > .ant-picker-input").first.click()
            self.page.get_by_text("Now").click()
            # self.page.get_by_text("02", exact=True).first.click()
            # self.page.get_by_text("00").nth(4).click()
            # self.page.get_by_role("button", name="Ok").click()
            time.sleep(5)
            print("Start Time input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def select_Repeat_state(self):
        try:
            # self.page.get_by_role("tabpanel", name="Geofence List").get_by_text("Repeat").click()
            self.page.get_by_text("None").click()
            self.page.get_by_title("Every Day").click()
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_savealert_button(self):
        try:
            self.page.get_by_role("button", name="Save Alert").click()
            print("Clicked on 'save alert' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_success_msg_for_savealert_button(self):
        try:
            self.page.get_by_text("Location updated Successfully for vehicle!").click()
            self.page.locator(".ant-notification-notice-close").click()
            status = "present"
            time.sleep(5)
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
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

    def verify_notification(self, alertName):
        try:
            self.page.get_by_text(alertName).first.click()
            time.sleep(20)
            print(f"{alertName} is listed/displayed on Notification window/page")
            status = "present"
        except:
            filename = 'vehicleList_page_' + alertName
            self.commonFunctions.screenshot(filename)
            status = "not_present"
        return status

    def click_on_view_all_button(self):
        try:
            self.page.get_by_role("button", name="View all").click()
            time.sleep(20)
            print("Geofence Notification window/page is displayed")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def click_on_close_button(self):
        try:
            self.page.get_by_role("button", name="Close").click()
            print("Clicked on 'close' button")
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

    def verify_geofence_notification(self):
        try:
            self.page.get_by_text("GEOFENCE NOTIFICATION").first.click()
            print("Geofence Notification is listed/displayed on Notification window/page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
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

    # ----------------------------
    # Vehicle List - Maintenance:
    # ----------------------------

    def click_on_Maintenance_tab(self, systemId):
        try:
            self.page.get_by_role("row", name=systemId).locator("img").nth(2).click(timeout=60000)
            print("Maintenance Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_vin_on_maintenance_dialog_box(self, vin):
        try:
            self.page.get_by_role("dialog", name=vin).get_by_text(vin).click(timeout=60000)
            print("Vin number is  displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_schedule_maintenance_tab(self):
        try:
            self.page.get_by_role("tab").get_by_text("Schedule Maintenance")
            print("Schedule Maintenance tab/option is displayed on Maintenance page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_Service_Date_for_Maintenance(self, service_date):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Service Date")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceDate']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceDate']").fill(
                service_date)
            time.sleep(5)
            print("service date filled  is available and selected the desired date from calender ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_service_odo(self, service_odo):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Service Odo")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceOdo']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceOdo']").fill(
                service_odo)
            time.sleep(5)
            print("Maintenance serive odo  input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_Service_Due_Date_for_Maintenance(self, service_due_date):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Select date")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator(
                "input[name='serviceDueDate']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceDueDate']").fill(
                service_due_date)
            print("service due date filled  is available and selected the desired date from calender ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_service_due_odo(self, service_due_odo):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Service Due Odo")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator(
                "input[name='serviceDueOdo']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='serviceDueOdo']").fill(
                service_due_odo)
            time.sleep(5)
            print("Maintenance serive due odo  input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_Date_Remainder_for_Maintenance(self, date_remainder):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Select date")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='dateReminder']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='dateReminder']").fill(
                date_remainder)
            time.sleep(5)
            print("Date remainder filled  is available and selected the desired date from calender ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_odo_remainder(self, odo_remainder):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Odo Remainder")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='odoReminder']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("input[name='odoReminder']").fill(
                odo_remainder)
            time.sleep(5)
            print("Maintenance odo remainder input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_Notes_for_Maintenance(self, Note):
        try:
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").get_by_text("Notes")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("textarea[name='notes']").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Schedule Maintenance").locator("textarea[name='notes']").fill(Note)
            time.sleep(5)

            print("Maintenance Notes input filed is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_submit_button_for_maintenance(self):
        try:
            self.page.get_by_role("button", name="Submit").click()
            print("Clicked on 'Submit' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    def verify_success_msg_for_schedulemaintenance(self):
        try:
            self.page.get_by_text("Data updated successfully").click()
            status = "present"
            time.sleep(5)
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_Diagnostic_tab(self):
        try:
            self.page.get_by_role("tab", name="Diagnostic").click()
            print("Diagnostic tab/option is displayed on Maintenance page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def search_dtc_code_for_diagnostic(self, dtc_code):
        try:
            self.page.get_by_role("tabpanel", name="Diagnostic").get_by_text("DTC Code")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Diagnostic").get_by_text("Search by DTC Code")
            time.sleep(5)
            self.page.get_by_role("tabpanel", name="Diagnostic").locator("img").click()
            time.sleep(10)
            self.page.get_by_role("tabpanel", name="Diagnostic").locator("img").fill("dtc_code")
            print("DTc code search tab/option is displayed on Diagnostic page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"

        return status

    # ----------------------------
    # Vehicle List - Drive Score Card:
    # ----------------------------

    def click_on_drive_score_card_tab(self, systemId):
        try:
            self.page.get_by_role("row", name=systemId).locator("img").first.click(timeout=60000)
            print("Drive Score Card Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    # ----------------------------
    # Vehicle List - Live Track Command:
    # ----------------------------

    def click_on_live_track_command_tab(self, systemId):
        try:
            self.page.get_by_role("row", name=systemId).get_by_role("img", name="radius-setting").locator("svg").click(
                timeout=60000)
            print("Live Track command Icon is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_set_frequency_for_live_track(self):
        try:
            self.page.get_by_role("tabpanel", name="Set Frequency").locator("input[@name='frequency']")
            time.sleep(10)
            print("frequncy is available and to entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_submit_button_for_frequency(self):
        try:
            self.page.get_by_role("button", name="Submit").click()
            print("Clicked on 'Submit' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_success_msg_for_set_frequency(self):
        try:
            self.page.get_by_text("Live Tracking Command Published Successfully").click()
            self.page.get_by_text("Command could not be send to device").click()
            status = "present"
            time.sleep(5)
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    # ----------------------------
    # Vehicle List - Adv Search:
    # ----------------------------

    def click_on_Adv_Search_link(self, systemId):
        try:
            self.page.get_by_role("button", name="Adv. Search").click(timeout=60000)
            print("Adv Search link is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_for_vin_number(self, vin_no):
        try:
            self.page.type('#vin', vin_no)
            print("Vin input feild is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_for_classes(self, class_value):
        try:
            self.page.type('#classes', class_value)
            print("classes input feild is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_for_style(self, style_data):
        try:
            self.page.type('#style', style_data)
            print("style input feild is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def enter_for_model(self, model):
        try:
            self.page.type('#model', model)
            print("model input feild is available and entered the desired input")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_year_for_Advsearch(self, year):
        try:
            self.page.type('#year', year)
            print("year input  feild  is available and selected the desired date from calender ")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_Search_button_from_advsearch_link(self):
        try:
            self.page.click('button[type="submit"]')
            print("Search button is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

        # ----------------------------

    # Vehicle List - Create Expression :
    # ----------------------------

    def click_on_Create_Expression_link(self):
        try:
            self.page.get_by_role("button", name="Create Expression").click(timeout=60000)
            print("Create Expression link is displayed on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_on_parameter(self):
        try:
            self.page.locator("div > .ant-select > .ant-select-selector > .ant-select-selection-item").first.click()
            print("Select parameter  is able to select on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_parameter(self):
        try:
            self.page.get_by_title("HA").get_by_text("HA").click()
            print(" parameter  is able to click on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def select_on_expression(self):
        try:
            self.page.locator(
                "div:nth-child(2) > .ant-space > div:nth-child(2) > div > .ant-select > .ant-select-selector > .ant-select-selection-item").click()
            print("Select Expression  is able to select on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_expression(self):
        try:
            self.page.get_by_text("Add", exact=True).click()
            print(" Expression  is able to click on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_Weightage(self):
        try:
            self.page.locator("input[name=\"value\"]").click()
            self.page.locator("input[name=\"value\"]").fill("23")
            print("Weightage input field ia available to enter data on Vehicle List page")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def click_on_submit_button_for_createexpression(self):
        try:
            self.page.get_by_role("button", name="Submit").click()
            print("Clicked on 'Submit' button")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def verify_success_msg_for_create_expression(self):
        try:
            self.page.get_by_text("Expression created successfully").click()
            status = "present"
            time.sleep(5)
        except:
            self.commonFunctions.screenshot("vehicleList_page")
            status = "not_present"
        return status

    def page_reload(self):
        self.page.keyboard.press('F5', delay=1000)
        self.page.reload()
