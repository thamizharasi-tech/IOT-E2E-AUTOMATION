import time
from playwright.sync_api import expect

from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.elementSelectors.apm.homePage import HomePage
from UI_Testing.webUI_testData import apm_base_url

webElements = {
    'myApps_LHS_option': '//*[@id="App"]//span[contains(text(), "My Apps")]',
    'Reports_LHS_option': '//*[@id="App"]//span[contains(text(), "Reports")]',
    'myProducts_LHS_option': '//*[@id="App"]//span[contains(text(), "My Products")]',
    'deviceRegistration_card': '//*[@id="App"]//span[contains(text(), "Device Registration")]',
    'myProducts_url': r'/products'

}


class APIproduct_page:
    def __init__(self, page):
        self.page = page
        self.deviceRegistration_card = webElements["deviceRegistration_card"]
        self.apiProduct_page_url = apm_base_url + webElements["myProducts_url"]
        self.myProducts_option = webElements["myProducts_LHS_option"]
        self.myApps_option = webElements["myApps_LHS_option"]
        self.commonFunctions = common_functions(self.page)

    # Act functions/methods

    def navigate_to_APIproduct_page(self):
        # Verify My Apps option on home Page
        hPage = HomePage(self.page)
        time.sleep(5)

        # Click on API Product card
        hPage.click_on_APIportal_card()
        time.sleep(5)

        self.verify_apiProduct_page_url()

    def click_on_MyProducts_LHS_option(self):
        self.page.locator(self.myProducts_option).click()

    def click_on_MySubscription_LHS_option(self):
        self.page.get_by_text("My Subscription").click()

    def click_on_ProductsPackages_LHS_option(self):
        # self.page.get_by_text("Products & Packages").click()
        self.page.get_by_role("menuitem", name="Products & Packages").click()

    def click_on_Reports_LHS_option(self):
        self.page.get_by_text("Reports").click()

    def click_on_MyApps_LHS_option(self):
        self.page.locator(self.myApps_option).click()

    def click_on_deviceRegistration_card(self):
        text = self.page.locator(self.deviceRegistration_card).text_content()
        print("Product header text : ", text)
        self.page.locator(self.deviceRegistration_card).click()

    # Validation functions/methods

    def verify_apiProduct_page_url(self):
        # Ensures the page is navigated to the given URL.
        self.commonFunctions.verify_current_page_URL(self.apiProduct_page_url)

    def verify_MyProducts_url(self, url):
        myApps = self.page.get_by_url()
        expect(self.page).to_have_url(self.apiProduct_page_url)
        print(myApps)
        return myApps






