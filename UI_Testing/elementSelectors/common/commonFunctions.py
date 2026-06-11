from playwright.sync_api import expect

from UI_Testing.webUI_testData import screenshots_folderPath

webElements = {
    'empty_image': "//div[@class='ant-empty-description']",
    'error_form': '//*[@id="form-errors"]'
}


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "test_action: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")


class common_functions:
    def __init__(self, page):
        self.page = page
        self.empty_table_img = webElements["empty_image"]

    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def verify_current_page_URL(self, current_url):
        # Ensures the page is navigated to the given URL.
        expect(self.page).to_have_url(current_url)

    def verify_page_title(self, pageTitle):
        title = self.page.title()
        print('title', title)
        expect(self.page.title()).to_have_title(pageTitle)
        return

    def click_on_card(self, cardName):
        self.page.get_by_role("heading", name=cardName).click()

    def verify_locator_text(self, elementLocator, expectedText):
        text = elementLocator.text_content()
        expect(elementLocator).to_have_text(expectedText)
        return text

    def verify_locator_tobe_checked(self, elementLocator):
        expect(elementLocator).to_be_checked()

    def verify_locator_tobe_visible(self, elementLocator):
        expect(elementLocator).to_be_visible()

    def verify_locator_tobe_disable(self, elementLocator):
        expect(elementLocator).to_be_disabled()

    def screenshot(self, filename):
        self.page.screenshot(path=screenshots_folderPath + filename + ".png", full_page=True)

    def verify_cell_locator_on_page(self, locator_name):
        try:
            self.page.get_by_role("cell", name=locator_name).click()
            status = "present"
        except:
            status = "non_present"
            self.commonFunctions.screenshot("vehicleList_page")
        return status

    def verify_message(self, expected_message):
        elementLocator = self.page.get_by_text(expected_message)
        expect(elementLocator).to_have_text(expected_message)

    def verify_table_cell_value(self, condition, value):
        elementLocator = self.page.get_by_text(value)
        if condition == "containText":
            expect(elementLocator).to_contain_text(value)
        elif condition == "notContainText":
            expect(elementLocator).not_to_contain_text(value)

    def read_table_value(self, cell_value, cell_value_1):
        value1 = value2 = value3 = ''
        value = self.page.locator('//table/tbody').text_content()
        # print('empty value', value)
        if "No Data" in value:
            print('table is empty')
            value1 = value2 = value3 = value
        else:
            try:
                for i in range(2, 5):
                    ls1 = '//table/tbody/tr[' + str(i) + ']'
                    ls = ls1 + '/td[1]'
                    value1 = self.page.locator(ls).text_content()
                    ls = ls1 + '/td[2]'
                    value2 = self.page.locator(ls).text_content()
                    ls = ls1 + '/td[3]'
                    value3 = self.page.locator(ls).text_content()
                    if value2 == cell_value:
                        break
            except:
                # Else read first row values
                ls = '//table/tbody/tr[' + str(2) + ']/td[1]'
                value1 = self.page.locator(ls).text_content()
                ls1 = '//table/tbody/tr[' + str(2) + ']/td[2]'
                value2 = self.page.locator(ls1).text_content()
                ls2 = '//table/tbody/tr[' + str(2) + ']/td[3]'
                value3 = self.page.locator(ls2).text_content()

        return value1, value2, value3

    def empty_table(self):
        text = self.page.locator(self.empty_table_img).text_content()
        self.page.get_by_text("No Data").click()
        print("### Table is empty ###", text)

    def page_refresh(self):
        self.page.reload()
        print("### Page is refreshed/reloaded ###")

    def verify_error_form_text(self):
        text = self.page.locator(webElements["error_form"]).text_content()
        # print("Error form text", text)
        return text
