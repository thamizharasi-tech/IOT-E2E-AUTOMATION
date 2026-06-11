import time
from playwright.sync_api import Playwright, sync_playwright, expect

from UI_Testing.webUI_testData import apm_base_url

webElements = {
    'homePage_url': "/",
    'SignOut': '//p[contains(text(), "Sign Out")]',
    'APIportal_card': '//*[@id="App"]//span[contains(text(), "API Portal")]',
    'APIDocumentation_card': '//*[@id="App"]//span[contains(text(), "API Documentation")]',
    'DevelopApps_card': '//*[@id="App"]//span[contains(text(), "Develop Apps")]',
    'Toolkit_card': '//*[@id="App"]//span[contains(text(), "Toolkit")]',
    'MarketPlace_card': '//*[@id="App"]//span[contains(text(), "Market Place")]'
}


class HomePage:
    def __init__(self, page):
        self.page = page
        self.homePage_url = apm_base_url + webElements["homePage_url"]
        self.signOut = webElements["SignOut"]
        self.apiProduct_card = webElements["APIportal_card"]
        self.apiDocumentation_card = webElements["APIDocumentation_card"]
        self.developApps_card = webElements["DevelopApps_card"]
        self.toolkit_card = webElements["Toolkit_card"]
        self.marketPlace_card = webElements["MarketPlace_card"]

    # ACT functions/methods

    def navigate_to_home_page(self):
        self.page.goto(self.homePage_url, timeout=120000)

    def click_on_APIportal_card(self):
        self.page.locator(self.apiProduct_card).click()

    def click_on_APIDocumentation_card(self):
        self.page.locator(self.apiDocumentation_card).click()

    def click_on_DevelopApps_card(self):
        self.page.locator(self.developApps_card).click()

    def click_on_Toolkit_card(self):
        self.page.locator(self.toolkit_card).click()

    def click_on_MarketPlace_card(self):
        self.page.locator(self.marketPlace_card).click()

    def click_on_SignOut(self):
        self.page.locator(self.signOut).click()

    # Validation functions/methods

    def verify_text_of_APIproduct_card(self):
        text = self.page.locator(webElements["APIportalCard"]).text_content()
        print(text)
        return text

    def verify_logout_option(self):
        self.page.get_by_text("Sign Out")




