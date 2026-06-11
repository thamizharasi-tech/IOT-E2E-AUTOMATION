import time

from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.webUI_testData import b2c_base_url

webElements = {
    'vehicleMap_endpoint': r'/developer-dashboard/vehicle-map',
}


class vehicleMap_Page:

    def __init__(self, page):
        self.page = page
        self.commonFunctions = common_functions(self.page)
        self.vehicleMap_url = b2c_base_url + webElements["vehicleMap_endpoint"]

    def navigate_to_vehicelMap_page(self):

        print(self.vehicleMap_url)
        self.page.goto(self.vehicleMap_url, timeout=120000)
        time.sleep(5)

    def verify_vehicleMap_page_url(self):
        # Ensures the page is navigated to the given URL.
        try:
            self.commonFunctions.verify_current_page_URL(self.vehicleMap_url)
            print("Landed on Vehicle Map page")
            status = "present"
        except:
            status = "not_present"
        return status

    def verify_vehicleMap_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle Map")
            status = "present"
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = "not_present"

        return status

    def click_on_vehicleMap_tab(self):
        try:
            self.page.get_by_role("button", name="Vehicle Map").click()
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = 'not_present'
        return status

    def select_desired_vin(self, vin):
        try:
            self.page.get_by_text("vin-Ref-101").click()
            self.page.get_by_title(vin).get_by_text(vin).click()
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = 'not_present'
        return status

    def click_on_view_button(self):
        try:
            self.page.get_by_role("button", name="VIEW", exact=True).click()
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = 'not_present'
        return status

    def expand_view_location_data(self):
        try:
            self.page.get_by_role("button", name="View Location Data").click()
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = 'not_present'
        return status

    def verify_telemetry_location_data(self):
        try:
            self.page.get_by_role("cell", name="28.61")
            self.page.get_by_role("cell", name="77.22")
            self.page.get_by_role("cell", name="28.60")
            self.page.get_by_role("cell", name="77.23")
            status = 'present'
        except:
            self.commonFunctions.screenshot("vehicleMap_page")
            status = 'not_present'
        return status
