import time

from UI_Testing.elementSelectors.apm.apiProducts_page import APIproduct_page
from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.elementSelectors.apm.homePage import HomePage
from UI_Testing.elementSelectors.apm.myAppsPage import myapps_Page
from UI_Testing.webUI_testData import apm_base_url

webElements = {
    'productsPackages_url': r'/products/subscription'

}


class productPackages_page:

    def __init__(self, page):
        self.page = page
        self.productsPackages_page_url = apm_base_url + webElements["productsPackages_url"]
        # self.error_msg = page.get_by_text("App with name newApp1 already exists")
        self.success_msg = page.get_by_text("Package Subscribed Successfully")
        self.commonFunctions = common_functions(self.page)

    # Act functions/methods

    def navigate_to_productPackages_page(self):
        # Verify My Apps option on home Page
        homePage = HomePage(self.page)
        apiProductPage = APIproduct_page(self.page)
        commonFunctions = common_functions(self.page)
        time.sleep(5)

        # Click on API Product card
        homePage.click_on_APIportal_card()
        time.sleep(5)

        # Click on My Apps option/link on LHS
        apiProductPage.click_on_ProductsPackages_LHS_option()
        self.page.goto(self.productsPackages_page_url, timeout=90000)
        time.sleep(10)

        # Verify current url post clicking My Apps link
        appsPage = myapps_Page(self.page)

    # ACT / Validation functions/methods

    def verify_productsPackages_page_url(self):
        # Ensures the page is navigated to the given URL.
        self.commonFunctions.verify_current_page_URL(self.productsPackages_page_url)

    def verify_page_header_text(self):
        try:
            self.page.get_by_text("Products & Packages").first
            status = "present"
        except:
            print("\n")
            status = "non_present"
        self.commonFunctions.screenshot("My_ProductsPackages_page")
        return status

    def verify_productsPackages_url(self):
        url = self.page.get_by_url()
        expect(self.page).to_have_url(self.productsPackages_page_url)
        print(url)
        return url

    def verify_essential_package_card(self):
        try:
            self.page.get_by_text("Essential", exact=True).click()
            status = "present"
        except:
            status = "not_present"
            self.commonFunctions.screenshot("My_ProductsPackages_page")
        return status

    def verify_value_package_card(self):
        self.page.get_by_text("Value", exact=True).click()

    def verify_elite_package_card(self):
        self.page.get_by_text("Elite", exact=True).click()

    def click_on_essential_package_request_button(self):
        self.page.locator(".sc-kUGxgu").first.click(timeout=60000)
        time.sleep(5)

    def click_on_value_package_request_button(self):
        self.page.locator("div:nth-child(2) > .sc-fmEDhd > .sc-kUGxgu").click(timeout=60000)

    def click_on_elite_package_request_button(self):
        self.page.locator("div:nth-child(3) > .sc-fmEDhd > .sc-kUGxgu").click(timeout=60000)

    def verify_package_subscribed_success_msg(self):
        try:
            self.page.get_by_text("Package Subscribed Successfully").click()
            self.page.get_by_text("Subscribed").first
            status = "present"
            self.commonFunctions.screenshot("My_ProductsPackages_page_success_msg")
        except:
            status = "present"
            self.commonFunctions.screenshot("My_ProductsPackages_page_er_msg")
        return status
