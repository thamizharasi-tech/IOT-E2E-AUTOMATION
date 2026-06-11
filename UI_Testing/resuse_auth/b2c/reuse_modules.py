from playwright.sync_api import sync_playwright

from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page


def try1():
    print("-------------------------------------------------------------------------")
    print(" B2C WEB UI Validations : ")
    print("-------------------------------------------------------------------------")

    # Step - 1
    try:

        print("Step:1 -> Launch B2C Web UI : ")

        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, args=["--start-maximised"])
        context = browser.new_context()
        # Open new page
        page = context.new_page()

        # Initiating the Page Object
        vehicleList_page = vehicleList_Page(page)

        # Navigate to B2C Page
        vehicleList_page.launch_b2c_web()

        print("B2C Web UI is loaded successfully")
        testResult(self, "passed", "B2C Web UI application should be launched successfully ",
                   "B2C Web UI application is launched successfully")
    except:

        testResult(self, "failed", "B2C Web UI application should be launched successfully ",
                   "B2C Web UI application is not launched")

    print("-------------------------------------------------------------------------")