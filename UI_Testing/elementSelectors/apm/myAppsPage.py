import time

from UI_Testing.elementSelectors.apm.apiProducts_page import APIproduct_page
from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.elementSelectors.apm.homePage import HomePage
from UI_Testing.webUI_testData import apm_base_url

webElements = {
    'myApps_url': r'/products/apps',
    'addApp_button': '//*[@id="App"]//span[contains(text(), "Add App")]',
    'appName': '//*[@id="name"]',
    'appDescription':'//*[@id="description"]',
    'request_button': '//*[@id="App"]//td[contains(text(), "Vehicle Tracking")]',
    'save_button': '//button[3]/span[contains(text(), "Save")]',
    'table': '//table/tbody/tr['
}


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "test_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")


class myapps_Page:
    def __init__(self, page):
        self.page = page
        self.add_button = page.get_by_role("button", name="plus-circle Add App")
        self.error_msg = page.get_by_text("App with name newApp1 already exists")
        self.success_msg = page.get_by_text("App with name newApp1 already exists")
        self.commonFunctions = common_functions(self.page)
        self.myapps_url = apm_base_url + webElements["myApps_url"]

    def navigate_to_MyApps_page(self):

        # Verify My Apps option on home Page
        homePage = HomePage(self.page)
        apiProductPage = APIproduct_page(self.page)
        commonFunctions = common_functions(self.page)
        time.sleep(5)

        # Click on API Product card
        homePage.click_on_APIportal_card()
        time.sleep(5)

        # Click on My Apps option/link on LHS
        apiProductPage.click_on_MyApps_LHS_option()
        time.sleep(10)

        # Verify current url post clicking My Apps link
        appsPage = myapps_Page(self.page)

        # Verify current URL
        #self.commonFunctions.verify_current_page_URL(self.myapps_url)

    def verify_myApps_page_url(self):
        # Ensures the page is navigated to the given URL.
        self.commonFunctions.verify_current_page_URL(self.myapps_url)

    def verifyAddApp_button(self):
        addAppButton = self.add_button.text_content()
        return addAppButton

    def clickAddApp_button(self):
        #self.page.locator(webElements["addApp_button"]).click()
        self.page.get_by_role("button", name="plus-circle Add App").click()

    def fillAppName(self, data):
        self.page.get_by_placeholder("*Name").click()
        self.page.get_by_placeholder("*Name").fill(data)
        #self.page.locator(webElements["appName"]).fill(data)

    def fillAppDescription(self, data):
        self.page.locator(webElements["appDescription"]).fill(data)

    def selectAPIs(self):
        for i in range(2,13):
            ls1 = webElements["table"] + str(i)+']'
            #ls1 = "//table/tbody/tr["+str(i)+']'
            ls = ls1 + '/td[1]/span'
            #print(ls)
            api_text = self.page.locator(ls).text_content()
            #print(api_text)
            if api_text == " Device Registration" or api_text == "Device Registration":
                ls = ls1 + '/td[3]/span'
                api_text1 = self.page.locator(ls).text_content()
                #print(ls, api_text1)
                ls = ls1 + '/td[4]/button'
                #print(ls)
                api_text = self.page.locator(ls).click()

    def selectDeviceRegistrationAPIs(self):
        self.page.get_by_role("row", name="lock Device Registration Device Registration APIS - Request").get_by_role(
            "button", name="Request").click()

    def select_battery_heating_request(self):
        self.page.get_by_text("Battery Heating", exact=True).click()
        self.page.get_by_role("row", name="lock Battery Heating Battery heating data apis - Request").get_by_role("button", name="Request").click()
        time.sleep(5)
        self.page.get_by_text("Save to Enable").click()

    def select_vehicle_tracking_request(self):
        self.page.get_by_text("Vehicle Tracking").click()
        self.page.get_by_role("cell", name="Gives data of vehicle location").click()
        self.page.get_by_role("row", name="lock Vehicle Tracking Gives data of vehicle location - Request").get_by_role(
            "button", name="Request").click()
        time.sleep(5)
        self.page.get_by_text("Save to Enable").click()

    def select_battery_status_check_request(self):
        self.page.get_by_text("Battery Status Check", exact=True).click()
        self.page.get_by_role("cell", name="Gives battery status check Data").click()
        self.page.get_by_role("row", name="lock Battery Status Check Gives battery status check Data - Request").get_by_role("button", name="Request").click()
        time.sleep(5)
        self.page.get_by_text("Save to Enable").click()

    def selectTelemetryV3APIs(self):
        self.page.get_by_role("row", name="lock Telemetry V3 Newly Added telemetry APIS - Request").get_by_role("button", name="Request").click()


    def click_on_Save_button(self):
        #self.page.locator(webElements["save_button"]).click()
        #self.page.get_by_role("button", name="Enable").to_be_enabled()
        self.page.get_by_role("button", name="Save").click()

    def select_app_to_delete(self, cell_value1, cell_value2):
        commonFunctions = common_functions(self.page)
        app = commonFunctions.read_table_value(cell_value1, cell_value2)
        print(app)
        appId = str(app[0])
        self.page.get_by_text(appId).click()

    def click_on_Delete_button(self):
        self.page.get_by_role("button", name="Delete").click()










