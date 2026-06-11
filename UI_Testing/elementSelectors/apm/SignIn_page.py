import time
from playwright.sync_api import Playwright, sync_playwright, expect
from UI_Testing.webUI_testData import apm_base_url, apm_username, apm_password

webElements = {
    'UserName': '//*[@id="c2"]',
    'Password': '//*[@id="c3"]',
    'SignIn': '//form/div[4]//input',
    'SignIn_text': '//*[contains(text(), "Sign In to get unrestricted access")]'
}


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.SignIn_text = webElements["SignIn_text"]
        self.userName = webElements["UserName"]
        self.password = webElements["Password"]
        self.signIn = webElements["SignIn"]

    # Act functions/methods
    def launchWeb(self, url):
        self.page.goto(url, timeout=120000)
        title = self.page.title()
        return title

    def navigate_to_home_page(self):
        self.launchWeb(apm_base_url)
        time.sleep(10)

        # Enter valid user credentials
        self.fillUserName(apm_username)
        self.fillPassword(apm_password)

        # Click on Sign In button
        self.clickSignIn()
        time.sleep(15)

    def fillUserName(self, data):
        self.page.locator(self.userName).fill(data)

    def fillPassword(self, data):
        self.page.locator(self.password).fill(data)

    def clickSignIn(self):
        self.page.locator(self.signIn).click(timeout=60000)

    # Validation functions/methods

    def verify_text_on_SignIn_Page(self):
        text = self.page.locator(self.SignIn_text).text_content()
        return text
