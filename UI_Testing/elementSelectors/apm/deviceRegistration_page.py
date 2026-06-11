import time

from UI_Testing.elementSelectors.common.commonFunctions import common_functions

webElements = {
    'deviceReg_url': "https://onboard-reg.c2c-test.qualcomm.com/apiProducts/apiList/Device_Registration",
    'API_method': '//*[@id="App"]//table/tbody/tr/td[1]/span',
    'API_endpoint': '//*[@id="App"]//table/tbody/tr/td[2]/a',
    'DeviceRegApi_reqParameter': '//*[@id="App"]//div[5]//span[contains(text(), "Request Parameters")]',

    'requestId_value': '//div[7]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/span',
    'x-apiKey_value': '//div[7]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/span',
    'x-apiSecret_value': '//div[7]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div[4]/div/div/span',
    'body_value': '//div[7]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div',

    'requestId_editbox': '//*[@id="rc-tabs-0-panel-default"]//div[3]/div/div/span',
    'x-apiKey_editbox': '//*[@id="rc-tabs-0-panel-default"]//div[3]/div/div/span',
    'x-apiSecret_editbox': '//*[@id="rc-tabs-0-panel-default"]//div[3]/div/div/span',
    'body_editbox': '//*[@id="rc-tabs-0-panel-default"]//div[3]/div/div/span',
    'execute_button': '//button/span[contains(text(), "Execute")]',
    'error_text': '//span[contains(text(), "error")]',
    'resp_body_value': '//section/div/div[2]/div/div[2]/div/div/div/div'
}


class deviceReg_Page:
    def __init__(self, page):
        self.page = page
        self.deviceRegPage = webElements["deviceReg_url"]
        self.API_method = webElements["API_method"]
        self.API_endpoint = webElements["API_endpoint"]
        self.DeviceRegApi_reqParameter = webElements["DeviceRegApi_reqParameter"]
        self.commonFunctions = common_functions(self.page)
        self.read_x_api_key_locator = webElements["x-apiKey_value"]
        self.read_x_apiSecret_locator = webElements["x-apiSecret_value"]
        self.read_requestId_locator = webElements["requestId_value"]
        self.read_body_locator = webElements["body_value"]
        self.execute_button_locator = webElements["execute_button"]
        self.error_text_locator = webElements["error_text"]
        self.resp_body_value = webElements["resp_body_value"]

    # ACT functions/methods

    def read_API_details(self):
        method_type = self.page.locator(self.API_method).text_content()
        print("Method Type : ", method_type)
        api_endpoint = self.page.locator(self.API_endpoint).text_content()
        print("API Endpoint : ", api_endpoint)

    def click_on_api_endpoint(self):
        self.page.locator(self.API_endpoint).click()

    def expand_RequestParameters1(self):
        self.page.locator(self.DeviceRegApi_reqParameter).click()

    def expand_HTTPRequest1(self):
        self.page.locator(self.DeviceRegApi_reqParameter).click()

    def expand_HTTPRequest(self):
        self.page.get_by_role("button", name="right HTTP Request").click()

    def expand_PathParameters(self):
        self.page.get_by_role("button", name="right Path Parameters").click()

    def expand_QueryParameters(self):
        self.page.get_by_role("button", name="right Query Parameters").click()

    def expand_HeaderParameters(self):
        self.page.get_by_role("button", name="right Header Parameters").click()

    def expand_RequestParameters(self):
        self.page.get_by_role("button", name="right Request Parameters").click()

    def expand_ResponseTypes(self):
        self.page.get_by_role("button", name="right Response Types").click()

    def expand_SampleRequestsResponses(self):
        self.page.get_by_role("button", name="right Sample Requests/Responses").click()

    def expand_Parameters(self):
        self.page.get_by_role("button", name="right Parameters -").click()

    def expand_RequestBody(self):
        self.page.get_by_role("button", name="right Request Body -").click()

    def expand_Response(self):
        self.page.get_by_role("button", name="right Response -").click()

    def read_x_api_key_value(self):
        text = self.page.locator(self.read_x_api_key_locator).text_content()
        return text

    def read_x_api_secret_value(self):
        text = self.page.locator(self.read_x_apiSecret_locator).text_content()
        return text

    def read_requestId_value(self):
        text = self.page.locator(self.read_requestId_locator).text_content()
        return text

    def read_body_value(self):
        text = self.page.locator(self.read_body_locator).text_content()
        return text

    def fill_x_api_key(self, data):
        self.page.get_by_label("x-api-key").fill(data)

    def fill_x_api_secret(self, data):
        self.page.get_by_label("x-api-secret").fill(data)

    def fill_requestId(self, data):
        self.page.get_by_label("requestId").fill(data)

    def fill_body(self):
        reqId = self.read_requestId_value()
        payload = '{"count":1, "creator": "xreq", "requestId": ' + reqId + '}'
        # print(payload)
        self.page.get_by_placeholder("Enter body").fill(payload)

    def click_on_Execute_button(self):
        self.page.locator(self.execute_button_locator).click()
        # self.page.get_by_role("button", name="Execute").click()

    # Validation functions/methods

    def verify_deviceRegistration_page_url(self):
        # Ensures the page is navigated to the given URL.
        self.commonFunctions.verify_current_page_URL(self.deviceRegPage)

    def verify_error_text_in_api_response(self):
        self.page.locator(self.error_text_locator).click()
        self.page.get_by_text("error").click()
        time.sleep(5)
        resp_value = self.page.locator(self.error_text_locator).text_content()
        print('resp_value : ', resp_value)
        return resp_value

    def verify_Subscription_is_invalid(self):
        try:
            self.page.get_by_text(
                'root:{error:{responseCode:403responseMessage:\"Subscription is invalid or expired"').click()
        except:
            print("\n")
