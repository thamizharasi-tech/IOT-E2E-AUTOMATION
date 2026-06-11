import json
import os
from datetime import datetime

import playwright
import pytest
import playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright

# ===============================
# Default Configuration
# ===============================


path = os.path.dirname(__file__)
parent = os.path.dirname(path)
print(parent)
        
PRJ_PATH = r'C:\Car2Cloud_E2ETesting' + '\\'
CONFIG_PATH = PRJ_PATH + r'C2CtestData\Configuration\config.json'
SUPPORTED_ENV = ["QC-QA", "QC-Int"]

# ===============================
# API Test Configuration
# ===============================

xlsx_apiTestData_file = PRJ_PATH + r'API_Testing\testData\c2c_api_test.xlsx'
payload_filepath = PRJ_PATH + r'API_Testing\testData\payloads' + '\\'
headers_filepath = PRJ_PATH + r'API_Testing\testData\headers' + '\\'
schema_filepath = PRJ_PATH + r'API_Testing\testData\schema' + '\\'
api_responseFolderPath = PRJ_PATH + r'API_Testing\testReports\api_responses' + '\\'
test_result_pass = "PASS"
test_result_fail = "FAIL"

#
# @pytest.fixture(scope='session')
# def config():
#     config_file = open(CONFIG_PATH)
#     return json.load(config_file)
#
#
# @pytest.fixture(scope="session")
# def baseURL_setup(config):
#     if "Env" not in config:
#         raise Exception('The config file does not contain "Env" option')
#     elif config["Env"] not in SUPPORTED_ENV:
#         raise Exception(f'"{config["Env"]}" is not a supported env')
#     print(config["Env"])
#     return config["Env"]
#
#
# def api_setup():
#     config_file = open(CONFIG_PATH)
#     config = json.load(config_file)
#     if config["Env"] == "QC-QA":
#         # QC-QA environment Registration URLs
#         gbl_base_url = "https://gbl.c2c-test.qualcomm.com"
#         reg_base_url = "https://reg.c2c-test.qualcomm.com"
#     elif config["Env"] == "QC-Int":
#         # QC-QA environment Registration URLs
#         gbl_base_url = "https://gbl.c2c-it.qualcomm.com"
#         reg_base_url = "https://reg.c2c-it.qualcomm.com"
#     return gbl_base_url, reg_base_url
#
#
# # ===============================
# # Web UI Test Configuration
# # ===============================
# config_file = open(CONFIG_PATH)
# config = json.load(config_file)
# apm_base_url = config["apm_base_url"]
# b2c_base_url = config["b2c_base_url"]
# headless_mode = config["headless_mode"]
# webUI_ddt_file = os.path.join (parent , r'Car2Cloud_E2ETesting_Lconf\webUI_Testing_playwright\testData\WebUI_testData.xlsx')
# screenshots_folderPath = parent + r'/Car2Cloud_E2ETesting_Lconf/UI_Testing/Screenshots' + '//'
#
# @pytest.fixture(params=["chrome"], scope="class")
# def driver_init(request, playwright: Playwright):
#     if request.param == "chrome":
#         browser = playwright.chromium.launch(headless=False, args=["--start-maximised"])
#     if request.param == "firefox":
#         browser = playwright.firefox.launch(headless=False, args=["--start-maximised"])
#     yield browser
#
# @pytest.fixture()
# def navigate_to_home_page(create_browser_context):
#     context = create_browser_context
#     page = context.new_page()
#     page.goto(apm_base_url + r'/', timeout=50000)
#     yield page
#     page.close()
#
#
# def navigate_to_home_page_b2c(create_browser_context):
#     context = create_browser_context
#     page = context.new_page()
#     page.goto(b2c_base_url , timeout=50000)
#     yield page
#     page.close()

# ===============================
# E2E Test Configuration
# ===============================
folderPath = r'C:\Car2Cloud_E2ETesting' + '\\'

xlsx_c2cTestData_file = folderPath + r'C2CtestData\c2cTestData.xlsx'

C2CtestData_batchPath = folderPath + r'C2CtestData\usr\local\C2Cbat' + '\\'
C2CtestData_jsonPath = folderPath + r'C2CtestData\usr\local\json' + '\\'
C2CtestData_c2c2Path = folderPath + r'C2CtestData\usr\local\c2c' + '\\'
C2CtestData_certsPath = folderPath + r'C2CtestData\usr\local\certs' + '\\'
C2CtestData_DepPackagePath = folderPath + r'C2CtestData\usr\local\deploymentPackages' + '\\'
C2CtestReport_exeBackupPath = folderPath + r'C2CtestReport\e2eExecution_Backup' + '\\'

# ===============================
# Test Report Configuration
# ===============================
class reportDetails:
    # Set environment for e2e testing / CTS-QA , QC-QA , PerfQC-QA , CTS-Demo , CTS-Dev, IOT-QA , QC-Demo/
    envName = "QC-Int"
    testType = "Regression"  # Smoke / E2E / Functional etc..
    deviceType = "Virtual Device"  # Real / Virtual etc..
    # devicMetabuild_TCU = "SA2150P_SA515M.LE_LE.1-3-10_2-1-10-00060-STD.INT-1"
    # devicMetabuild_IVI = "Snapdragon_Auto_Gen3_HQX.SPF.0.1-00016-STD.PROD-1"
    # deviceBinariesVerNo = "Hub version DEV_1.11.0.0 & SoftSku -> C2C_Softsku_v2.1.2"
    cloudEnvVerNo = "1.4"
    userName = "Sheela Uttarakar"
    reportTitle = "Car2Cloud TEST REPORT"
    dreportTitle = "Car2Cloud_Detailed_Test_Report"
    reportpath = "http://localhost:63342/Car2Cloud_E2ETesting_Final/Reports/" + dreportTitle + ".html"
    testSummary = "E2E Execution"


def pytest_configure(config):
    config._metadata = {"Executed By": reportDetails.userName}
    config._metadata["Executed On"] = datetime.now()
    config._metadata["Execution Type"] = reportDetails.testType
    config._metadata["Cloud Environment"] = reportDetails.envName
    config._metadata["Cloud Environment Version No"] = reportDetails.cloudEnvVerNo
    config._metadata["Device Type"] = reportDetails.deviceType
    # config._metadata["Device-1 TCU Meta-build"] = reportDetails.devicMetabuild_TCU
    # if baseTest_variables.comboDeviceOnboarding_TCUIVI == "Yes":
    # config._metadata["Device-2 IVI Meta-build"] = reportDetails.devicMetabuild_IVI
    # config._metadata["Device Binaries Version No"] = reportDetails.deviceBinariesVerNo

# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("Test Execution Summary:" + reportDetails.testSummary)])
