import time

from UI_Testing.elementSelectors.apm.apiProducts_page import APIproduct_page
from UI_Testing.elementSelectors.common.commonFunctions import common_functions
from UI_Testing.elementSelectors.apm.homePage import HomePage
from UI_Testing.webUI_testData import apm_base_url

webElements = {
    'mySubscription_url': r'/products/subscription/account',
    'mySubscription_link': '//*[@id="App"]//span[contains(text(), "My Subscription")]',
    'mySubscription_header': '//*[@id="App"]//h1[contains(text(), "My Subscription")]',
    'package_header': '//*[@id="App"]//h1[contains(text(), "Package")]',
    'essential_package': '//*[@id="App"]//span[contains(text(), "Essential")]',
    'elite_package': '//*[@id="App"]//span[contains(text(), "Elite")]',
    'essential_pacakge_desc': '//*[@id="App"]//p[contains(text(), "Essential package contains essential products")]',
    'unsubscribe_button': '//*[@id="App"]//button//span[contains(text(), "Unsubscribe")]',
    'table': '//table/tbody/tr['
}


class mySubscriptions_Page:

    def __init__(self, page):
        self.page = page
        self.commonFunctions = common_functions(self.page)
        self.mySubscription_url = apm_base_url + webElements["mySubscription_url"]

    def navigate_to_MySubscription_page(self):
        # Verify My Apps option on home Page
        homePage = HomePage(self.page)
        apiProductPage = APIproduct_page(self.page)
        commonFunctions = common_functions(self.page)
        time.sleep(5)

        # Click on API Product card
        homePage.click_on_APIportal_card()
        time.sleep(5)

        # Click on My Apps option/link on LHS
        apiProductPage.click_on_MySubscription_LHS_option()
        time.sleep(10)

    def verify_mySubscription_page_url(self):
        # Ensures the page is navigated to the given URL.
        self.commonFunctions.verify_current_page_URL(self.mySubscription_url)

    def verify_page_header_text(self):
        try:
            self.page.get_by_text("My Subscription").click()
            status = "present"
        except:
            status = "not_present"
            self.commonFunctions.screenshot("My_Subscription_page")
        return status

    def verify_unSubscribe_button_on_page(self):
        try:
            self.page.get_by_role("button", name="Unsubscribe")
            #print("Unsubscribe button is present on Products & packages page")
            status = "present"
        except:
            #print("Unsubscribe button is not present on Products & packages page")
            status = "not_present"
            self.commonFunctions.screenshot("My_Subscription_page")
        return status

    def verify_subscribed_essential_package_on_page(self):
        try:
            self.page.get_by_role("button",
                                  name="Essential Essential package contains essential products Unsubscribe").click()
            status = "present"
        except:
            status = "non_present"
            self.commonFunctions.screenshot("My_Subscription_page")
        return status

    def click_on_unSubscribe_button(self):
        #self.page.get_by_role("button", name="Unsubscribe", exact=True).click()
        #time.sleep(5)
        try:
            self.page.get_by_role("button", name="Unsubscribe", exact=True).click(timeout=120000)
        except:
            time.sleep(10)
            self.page.get_by_role("button", name="Unsubscribe", exact=True).click(timeout=180000)

    def verify_confirm_dialogBox_to_unSubscribe(self):
        try :
            self.page.get_by_text("Are you sure to unsubscribe this package?").click()
            time.sleep(5)
            status = "present"
            self.commonFunctions.screenshot("My_Subscription_page_confirmation")
        except:
            status = "not_present"
            self.commonFunctions.screenshot("My_Subscription_page_er_confirmation")
        return status

    def click_on_Yes_button(self):
        self.page.get_by_role("button", name="Yes").click()
        time.sleep(5)

    def verify_success_msg_post_unsubscribe(self):
        try:
            self.page.get_by_text("UnSubscribed Successfully").click()
            status = "present"
            self.commonFunctions.screenshot("My_Subscription_page_success_msg")
        except:
            status = "not_present"
            self.commonFunctions.screenshot("My_Subscription_page_er_msg")
        return status

    def click_on_No_button(self):
        self.page.get_by_role("button", name="No").click()
        time.sleep(5)
