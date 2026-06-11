import time
import pytest

from C2CModules.COTA_modules import COTA_liveCommandTracking_getCurrentFrequency, \
    COTA_telemetry_getCotaDetails_by_requestId
from C2CModules.commandControl_modules import CommandControl_liveTracking, \
    get_commandCtrl_trackingId, commandControl_Tracking, verify_commandCtrl_apiResp_status
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_COTA:

    # COTA_live command tracking
    @pytest.mark.Smoke
    def test1_positive_COTA_liveCommandTracking(self):
        print("----------------------------------------------------------")
        systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call COTA reusable module
        # API operation to get current frequency value details for live tracking
        response_body = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "valid")

        # Validate response status code

        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == str('Data fetched successfully'):

            print("Live Tracking", response_body["responseData"]["liveTracking"])
            print("Current Frequency", response_body["responseData"]["currentFrequency"])

            testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                       "Successfully fetched the current values/data for desired System Id ")

        elif response_body["message"] == str('Data fetched successfully'):

            testResult(self, "failed", "Should fetch the current data/values for System id successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    def test2_CommandControl_liveCommandTracking_updateFrequency(self):

        # ===========================================================================================
        # Setup precondition on device for Command & Control request
        # ===========================================================================================

        # Get systemId from device
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        name = "LiveTracking"
        frequency = "2"
        value = "1"

        # ===========================================================================================
        # Initiate Command via API
        # ===========================================================================================
        print("-----------------------------")
        print("Initiate Command - Live Command Tracking : ")
        print("-----------------------------")

        # Read api configuration/common data
        print("Name : ", name)
        print("Frequency : ", frequency)
        print("Value : ", value)

        # Initiate command request
        # API to send context control with reduced frequency sensor data message to device
        response = CommandControl_liveTracking(self, name, systemId, frequency, value, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # ===========================================================================================
        # Cloud side validations
        # ===========================================================================================

        print("-----------------------------")
        print("Cloud Side Validations for initiated command response : ")
        print("-----------------------------")

        # ===========================================================================================
        # verify command & control status
        # ===========================================================================================
        time.sleep(30)

        try:

            # Parse API response into JSON
            response_body = response.json()

            # Verify command & control status
            if response_body["message"] == "Live Tracking Command Published Successfully":
                print("Live Tracking Command Published Successfully")
            else:
                print("Live Tracking Command is not published successfully")

            # read tracking id
            requestId = response_body["responseData"]["trackingId"]

            # Verify command & control resp

            # API Operation to get command cota Details by requestId
            response = COTA_telemetry_getCotaDetails_by_requestId(self, requestId, "valid")

            # Validate response status code
            assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
                response.status_code)

            # Parse API response into json
            response_body = response.json()

            # Verify cota details
            if response_body["message"] == "SUCCESS":
                data_len = len(response_body["response"]["responseData"])
                if data_len >= 1:
                    createdBy = response_body["response"]["responseData"][0]["createdBy"]
                    createdTime = response_body["response"]["responseData"][0]["createdTime"]
                    updatedBy = response_body["response"]["responseData"][0]["updatedBy"]
                    updatedTime = response_body["response"]["responseData"][0]["updatedTime"]
                    transId = response_body["response"]["responseData"][0]["transId"]
                    requestId = response_body["response"]["responseData"][0]["requestId"]
                    systemId = response_body["response"]["responseData"][0]["systemId"]
                    thresholdId = response_body["response"]["responseData"][0]["thresholdId"]

                    print(" Created By : ", createdBy)
                    print(" Created Time : ", createdTime)
                    print(" Updated By : ", updatedBy)
                    print(" Updated time : ", updatedTime)
                    print(" Trans Id : ", transId)
                    print(" Request Id : ", requestId)
                    print(" System Id : ", systemId)
                    print(" Threshold Id : ", thresholdId)

                testResult(self, "passed",
                           "Command execution should be completed and COTA details should be fetched successfully",
                           "Command execution is completed and COTA details also fetched successfully")
        except:
            testResult(self, "failed",
                       "Command execution should be completed and COTA details should be fetched successfully",
                       "Command execution should be completed successfully  or COTA details not fetched successfully")

        print("----------------------------------------------------------")
        # validate frequency
        # API operation to get current frequency value details for live tracking
        response = COTA_liveCommandTracking_getCurrentFrequency(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == str('Data fetched successfully'):

            liveTracking = response_body["responseData"]["liveTracking"]
            currentFrequency = response_body["responseData"]["currentFrequency"]

            print("Live Tracking", liveTracking)
            print("Current Frequency", currentFrequency)

            testResult(self, "passed", "Should fetch the current data/values for System Id successfully",
                       "Successfully fetched the current values/data for desired System Id ")

            print("----------------------------------------------------------")

            print("Frequency to be updated/configured : ", frequency)
            print("Frequency updated/configured : ", currentFrequency)

            if int(currentFrequency) == int(frequency):
                testResult(self, "passed", "Should update live tracking frequency successfully",
                           "Successfully updated live tracking frequency")
            else:
                testResult(self, "failed", "Should update live tracking frequency successfully",
                           "Failed to update live tracking frequency")

        elif response_body["message"] != str('Data fetched successfully'):

            testResult(self, "failed", "Should fetch the current data/values for System id successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])

        else:
            print("Something went wrong")
            assert False

    print("----------------------------------------------------------")
