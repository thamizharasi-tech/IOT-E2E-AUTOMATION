
# ===================================
# Valid Test Data for web UI execution
# ===================================
import os
from C2CModules.e2e_testData import testData

path = os.path.dirname(__file__)
parent = os.path.dirname(path)
print(parent)

browser_type = testData("Web_UI", 2, 2)
browser_name = testData("Web_UI", 2, 3)
headlessMode = testData("Web_UI", 3, 2)
apm_base_url = testData("Web_UI", 4, 2)
apm_username = testData("Web_UI", 5, 2)
apm_password = testData("Web_UI", 6, 2)

b2c_base_url = testData("Web_UI", 7, 2)

webUI_ddt_file = os.path.join (parent , r'Car2Cloud_E2ETesting_Lconf\webUI_Testing_playwright\testData\WebUI_testData.xlsx')
screenshots_folderPath =r'C:\Car2Cloud_E2ETesting\C2CtestReport\UI_Screenshots' + '\\'


def headless_mode():
    if headlessMode == "True":
        x = True
    else:
        x = False
    return x