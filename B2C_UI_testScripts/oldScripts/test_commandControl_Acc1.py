import time
import pytest
from playwright.sync_api import sync_playwright

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset, wifi, Command_Lock_ignition_value, \
    Command_Unlock_ignition_value, Command_Acc_ignition_value
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN, pull_logs_from_IVI_device
from C2CModules.resuse_modules import verify_message_in_log
from C2CModules.testResults import testResult
from UI_Testing.elementSelectors.b2c.vehicleList import vehicleList_Page

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

command_button_name = "Acc"


class Test_commandControl:

    @pytest.mark.regression
    # Validate device on-boarding functionality.
    def test_commandControl_Acc1(self):

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

        # Step - 2

        print("Step:2 -> User should land on Vehicle List Page : ")

        try:
            # Verify vehicle List tab and then click on it
            vehicleList_page.verify_vehicleList_tab()

            print("-------------------------------------------------------------------------")
            vehicleList_page.click_on_vehicleList_tab()
            time.sleep(15)

            print("-------------------------------------------------------------------------")

            # Verify current page url
            vehicleList_page.verify_vehicleList_page_url()
        except:
            testResult(self, "failed", "User should navigate to / land on Vehicle List page  ",
                       "User is not navigated to / landed on Vehicle List page ")

        print("-------------------------------------------------------------------------")

        print(" => Verify newly onboarded details on Vehicle List UI Page : ")

        try:
            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print("-------------------------------------------------------------------------")
            # Step - 3

            print("Step:3 -> Verify newly onboarded ' System Id ' on Vehicle List UI Page : ")

            # Verify system Id in UI table
            vehicleList_page.verify_systemId_on_UI(systemId)

            print("-------------------------------------------------------------------------")
            # Step - 4

            print("Step:4 -> Verify newly onboarded device ' Status ' on Vehicle List UI Page : ")

            # Verify device status in UI table
            vehicleList_page.verify_device_status_on_UI(systemId)

            print("-------------------------------------------------------------------------")

            # Step - 5

            print("Step:5 -> Verify package name for onboarded device on Vehicle List UI Page : ")

            # verify Essential package
            # vehicleList_page.verify_value_package_name_on_UI(systemId)

            print("-------------------------------------------------------------------------")

            # Step - 6
            print("Step:6 -> Verify ' Commands ' image/option on Vehicle List UI Page : ")

            # Click on Vehicle Insight eye icon
            status = vehicleList_page.click_on_Commands(systemId)
            time.sleep(30)

            print("-------------------------------------------------------------------------")

            # Step - 7

            print("Step:7 -> Verify 'VIN No' on RHS panel : ")

            # Get vin from device
            vin = getVIN(self, OnboardingType, chipsetType)

            vehicleList_page.verify_vin_on_pacakge_dialog_box(vin)

            print("-------------------------------------------------------------------------")

            # Step - 8

            print("Step:8 -> Verify 'drop down option : ")

            vehicleList_page.select_Ignition_state()

            time.sleep(30)

            print("-------------------------------------------------------------------------")
            # Step - 9

            print("Step:9 -> Verify & click on Command button : ", command_button_name)

            vehicleList_page.click_on_ignition_button(command_button_name)

            print("-------------------------------------------------------------------------")

            # Step - 10
            print("Step:10 -> Verify success message : ")

            vehicleList_page.verify_success_msg_for_command()

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
            ls = verify_message_in_log(self, 'ignition:', Command_Acc_ignition_value)
            print("Ignition State for Command-Acc : ", ls)

            if Command_Unlock_ignition_value in str(ls):

                testResult(self, "passed",
                           "Ignition value = 3 should be shown in log",
                           "Ignition value = 3 is displayed in device log . pls refer "
                           "device & cloud logs for detailed info")
            else:
                testResult(self, "verificationFailed",
                           "Ignition value = 3 should be shown in log",
                           "Ignition value = 3 is not displayed device log or logs have been rotated . pls refer "
                           "device & cloud logs for detailed info")
            time.sleep(10)

            print("-------------------------------------------------------------------------")

            # Step - 12
            print("Step12 -> Click on reload button : ")
            time.sleep(90)

            vehicleList_page.click_on_reload_button()

            print("-------------------------------------------------------------------------")

            # Step - 13
            print("Step13 -> Verify unlock button status : ")

            vehicleList_page.verify_ignition_button_status(command_button_name)


        except:
            testResult(self, "failed",
                       "Command control e2e flow should work without nay errors",
                       "Something went wrong while testing e2e flow, Pls refer logs &"
                       " screenshots for detailed info.")

        print("-------------------------------------------------------------------------")
