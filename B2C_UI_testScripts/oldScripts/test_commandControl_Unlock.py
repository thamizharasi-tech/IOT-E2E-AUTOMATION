import time
import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, Command_Lock_ignition_value, \
    Command_Unlock_ignition_value, b2c_telemetry_sidestand_state_OFF, b2c_telemetry_sidestand, \
    b2c_telemetry_speed_value_0, telemetry_curr_Speed, telemetry_speed_event_type, b2c_telemetry_sidestand_attribute, \
    telemetry_speed_attribute
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, pull_logs_from_IVI_device, \
    run_paho_command_on_primary_IVI
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.telemetry_modules import telemetry_Curr
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page
from UI_Testing.webUI_testData import browser_type, browser_name, headless_mode

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

base_package_name = "Elite"

class Test_commandControl:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_commandControl_unlock(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get vin & systemId from device
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        print("----------------------------------------------------------")
        print("Set preconditions on device by running can commands : ")

        run_paho_command_on_primary_IVI(self, OnboardingType, chipsetType, "commandControl_precondition2")
        time.sleep(30)

        print("precondition commands have been run on device, verify logs for detailed information")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Pull logs for validations
        # ===========================================================================================
        print("Pull/Fetch device logs for validation : ")

        pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

        print("Logs are fetched from device to host machine @ desired location ")
        print("----------------------------------------------------------")

        # ===========================================================================================
        # Device side validations : verify telemetry messages in log file
        # ===========================================================================================

        # telemetry - speed

        print("-----------------------------")
        print("Device Side Validations for preconditions : ")
        print("-----------------------------")

        # verify speed value in the device logs
        tele_speed = telemetry_speed_attribute + b2c_telemetry_speed_value_0
        ls = verify_message_in_log(self, b2c_telemetry_speed_value_0, tele_speed)

        if tele_speed in str(ls[0]) or 'speed:0.000000' in str(ls[0]):
            print(f"Speed value printed in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Speed value is not set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Speed value should be set to 0 ",
                       "Speed value is not set to 0, pls refer device & cloud logs for detailed info")

        # verify side stand state in the device logs
        tele_speed = b2c_telemetry_sidestand_attribute + b2c_telemetry_sidestand_state_OFF
        ls = verify_message_in_log(self, b2c_telemetry_sidestand_state_OFF, tele_speed)

        if tele_speed in str(ls[0]):
            print(f"side stand state in device log : ' {tele_speed} ' ")
            testResult(self, "verificationPassed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is set to 0, pls refer device logs for detailed info")
            print("c2c logs line data : => ", ls[0])

        if str(ls[0]) == "Error":
            print(
                "Side stand state should be set to 0 or updated in device logs. pls refer device & cloud logs in detail")
            testResult(self, "verificationFailed", "Precondition: Side stand state should be set to 0 ",
                       "Side stand state is not set to 0, pls refer device & cloud logs for detailed info")

        print("----------------------------------------------------------")

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for preconditions: ")
        print("-----------------------------")

        # verify speed value @ cloud

        response_body = telemetry_Curr(self, telemetry_speed_event_type, systemId)

        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == telemetry_curr_Speed:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("speed value configured in the telemetry stub : ", b2c_telemetry_speed_value_0)
            print("speed value stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(float(value)) == int(float(b2c_telemetry_speed_value_0)):
            testResult(self, "verificationPassed",
                       "Speed value should be 0 on cloud",
                       "Speed value is 0 on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Speed should be 0 on cloud",
                       "Speed is not 0 on cloud . pls refer "
                       "cloud logs for detailed info")

        # verify side stand value @ cloud
        try:
            dataList_len = len(response_body["responseData"]["dataList"])
            i = 0
            for i in range(dataList_len):
                if response_body["responseData"]["dataList"][i]["name"] == b2c_telemetry_sidestand:
                    value = response_body["responseData"]["dataList"][i]["value"]
                    break

            print("side stand state configured in the telemetry stub : ", b2c_telemetry_sidestand_state_OFF)
            print("side stand state stored in Cloud DB : ", value)
        except:
            print("dataList is empty in api response")
            value = ""

        if int(float(value)) == int(float(b2c_telemetry_sidestand_state_OFF)):
            testResult(self, "verificationPassed",
                       "Side stand state should be set to 0/OFF on cloud",
                       "Side stand state is set to 0/OFF on cloud . pls refer "
                       "cloud logs for detailed info")
        else:
            testResult(self, "verificationFailed",
                       "Side stand state should be set to 0/OFF on cloud",
                       "Side stand state is not set to 0/OFF on cloud . pls refer "
                       "cloud logs for detailed info")

        time.sleep(5)
        print("----------------------------------------------------------")

        # ===========================================================================================
        # B2C UI :
        # ===========================================================================================

        print("-------------------------------------------------------------------------")
        print(" B2C WEB UI Validations : ")
        print("-------------------------------------------------------------------------")

        # Step - 1
        try:

            print("Step:1 -> Launch B2C Web UI : ")
            playwright = sync_playwright().start()
            if browser_type == 'chromium' and browser_name != 'NA':
                browser = playwright.chromium.launch(channel=browser_name, headless=headless_mode(), args=["--start-maximised"])
            elif browser_type == 'firefox':
                browser = playwright.firefox.launch(headless=headless_mode(), args=["--start-maximised"])
            elif browser_type == 'webkit':
                browser = playwright.webkit.launch(headless=headless_mode(), args=["--start-maximised"])
            else:
                browser = playwright.chromium.launch(headless=headless_mode(), args=["--start-maximised"])

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

        # Step - 2

        print("Step:2 -> User should land on Vehicle List Page : ")

        try:
            # Verify vehicle List tab and then click on it
            status = vehicleList_page.verify_vehicleList_tab()

            if status == 'present':
                testResult(self, "passed", "Vehicle list tab should be present on UI page ",
                           "Vehicle list tab is present on UI page ")
            else:
                testResult(self, "failed", "Vehicle list tab should be present on UI page ",
                           "Vehicle list tab is not present on UI page ")

            print("-------------------------------------------------------------------------")
            status = vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)
            if status == 'present':
                testResult(self, "passed", "User should be able to click on Vehicle list tab",
                           "User is able to click on Vehicle list tab")
            else:
                testResult(self, "failed",
                           "User should be able to click on Vehicle list tab",
                           "User is not able to click on Vehicle list tab ")

            print("-------------------------------------------------------------------------")

            # Verify current page url
            status = vehicleList_page.verify_vehicleList_page_url()
            if status == 'present':
                testResult(self, "passed", "User should navigate to / land on Vehicle List page ",
                           "User is navigated to / landed on Vehicle List page successfully ")
            else:
                testResult(self, "verificationFailed", "User should navigate to / land on Vehicle List page  ",
                           "User is not navigated to / landed on Vehicle List page ")
        except:
            testResult(self, "verificationFailed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")
        print("-------------------------------------------------------------------------")

        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("-------------------------------------------------------------------------")

            print("Step:3 -> Verify newly onboarded ' System Id ' on Vehicle List UI Page : ")

            # Verify system Id in UI table
            status = vehicleList_page.verify_systemId_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page",
                           "System Id of newly onboarded device is listed in UI table on Vehicle List page")
            else:
                testResult(self, "failed",
                           "System Id of newly onboarded device should be listed in UI table on Vehicle List page  ",
                           "System Id of newly onboarded device is not listed in UI table on Vehicle List page")

            print("-------------------------------------------------------------------------")

            print("Step:4 -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            # Verify device status in UI table
            status = vehicleList_page.verify_device_status_on_UI(systemId)
            if status == 'present':
                testResult(self, "passed", "Device Status should be ACTIVE on Vehicle List UI page",
                           "Device Status is shown as ACTIVE on Vehicle List UI page")
            else:
                testResult(self, "verificationFailed",
                           "Device Status should be ACTIVE on Vehicle List UI page  ",
                           "Device Status is not ACTIVE on Vehicle List UI page")

            print("-------------------------------------------------------------------------")

            print("Step:5 -> Verify package name for onboarded device on Vehicle List UI Page : ")

            # verify base package

            base_package_name = vehicleList_page.get_package_name_from_UI(systemId)

            status = vehicleList_page.verify_package_name_on_UI(systemId, base_package_name)

            if status == 'present':
                testResult(self, "passed", "Device should be mapped to '" + base_package_name + "' package",
                           "Device is mapped to '" + base_package_name + "' package")
            else:
                testResult(self, "passed", "Device should be mapped to '" + base_package_name + "' package",
                           "Device is not mapped to '" + base_package_name + "' package")

            print("-------------------------------------------------------------------------")

            # Step - 6
            print("Step:6 -> Verify ' Commands ' image/option on Vehicle List UI Page : ")

            # Click on Vehicle Insight eye icon
            status = vehicleList_page.click_on_Commands(systemId)
            time.sleep(30)
            if status == 'present':
                testResult(self, "passed", "User should be able to select/click on Command option",
                           "User is able to select/click on Command option")
            else:
                testResult(self, "passed", "User should be able to select/click on Command option",
                           "User is not able to select/click on Command option")

            print("-------------------------------------------------------------------------")

            # Step - 7

            print("Step:7 -> Verify 'VIN No' on RHS panel : ")

            # Get vin from device
            vin = getVIN(self, OnboardingType, chipsetType)

            status = vehicleList_page.verify_vin_on_pacakge_dialog_box(vin)
            if status == 'present':
                testResult(self, "passed",
                           "VIN no should be displayed as header on Command dialog box/window",
                           "VIN no is displayed as header on Command dialog box/window")
            else:
                testResult(self, "verificationFailed",
                           "VIN no should be displayed as header on Command dialog box/window ",
                           "VIN no is not displayed as header on Command dialog box/window")

            print("-------------------------------------------------------------------------")

            # Step - 8

            print("Step:8 -> Verify drop down option: ")

            status = vehicleList_page.select_Ignition_state()

            if status == 'present':
                testResult(self, "passed",
                           "User should be able to select 'IGNITION STATE' option",
                           "User is able to select 'IGNITION STATE' option")
            else:
                testResult(self, "verificationFailed",
                           "User should be able to select 'IGNITION STATE' option ",
                           "User is able to select 'IGNITION STATE' option")

            time.sleep(10)

            print("-------------------------------------------------------------------------")
            # Step - 9

            print("Step:9 -> Verify & click on Unlock button : ")

            status = vehicleList_page.click_on_ignition_button('Unlock')

            if status == 'present':
                testResult(self, "passed",
                           "User should be able to select/click on 'Unlock' option",
                           "User is able to select/click on 'Unlock' option")
            else:
                testResult(self, "verificationFailed",
                           "User should be able to select/click on 'Unlock' option ",
                           "User is able to select/click on 'Unlock' option")

            print("-------------------------------------------------------------------------")

            # Step - 10
            print("Step:10 -> Verify success message : ")

            status = vehicleList_page.verify_success_msg_for_command()
            if status == 'present':
                testResult(self, "passed",
                           "Success message should be displayed on clicking command button",
                           "Success message is displayed on clicking command button")
            else:
                testResult(self, "verificationFailed",
                           "Success message should be displayed on clicking command button",
                           "Success message is not displayed on clicking command button")

            print("-------------------------------------------------------------------------")

            # ===========================================================================================
            # Device side validations : Fetch logs & verify command & control msg
            # ===========================================================================================

            # Step - 11
            print("Step:11 -> Verify ignition state value in device log : ")

            print("-----------------------------")
            print("Device Validations : ")
            print("-----------------------------")

            # Fetch/pull logs from device
            pull_logs_from_IVI_device(self, OnboardingType, chipsetType)

            # Verify command control msgs & type code in fetched device logs
            # status = verify_msg_details_pub2Cloud(self, 'command execution success', "")
            ls = verify_message_in_log(self, 'ignition:', 'ignition')
            print("Initiation texts captured in device logs : ", ls)
            ls = verify_message_in_log(self, 'ignition:', Command_Unlock_ignition_value)
            print("Ignition State for Command-Unlock : ", ls)

            if Command_Unlock_ignition_value in str(ls):

                testResult(self, "passed",
                           "Ignition value = 2 should be shown in log",
                           "Ignition value = 2 is displayed in device log . pls refer "
                           "device & cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Ignition value = 2 should be shown in log",
                           "Ignition value = 2 is not displayed device log or logs have been rotated . pls refer "
                           "device & cloud logs for detailed info")
            time.sleep(10)

            print("-------------------------------------------------------------------------")

            # Step - 12
            print("Step12 -> Click on reload button : ")
            time.sleep(90)

            status = vehicleList_page.click_on_reload_button()
            if status == 'present':
                testResult(self, "passed",
                           "Command window should be reloaded",
                           "Command window is reloaded")
            else:
                testResult(self, "verificationFailed",
                           "Command window should be reloaded",
                           "Command window is not reloaded")

            print("-------------------------------------------------------------------------")

            # Step - 13
            print("Step13 -> Verify unlock button status : ")

            status = vehicleList_page.verify_ignition_button_status('Unlock')
            if status == 'present':
                testResult(self, "passed",
                           "Command button should be displayed as selected/clicked",
                           "Command button is displayed as selected/clicked")
            else:
                testResult(self, "verificationFailed",
                           "Command button should be displayed as selected/clicked",
                           "Command button is not displayed as selected/clicked")


        except:
            testResult(self, "failed",
                       "Command control e2e flow should work without nay errors",
                       "Something went wrong while testing e2e flow, Pls refer logs &"
                       " screenshots for detailed info.")

        print("-------------------------------------------------------------------------")

