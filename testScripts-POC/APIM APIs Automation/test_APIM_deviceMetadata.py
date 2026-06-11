import pytest
import json

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.APIM_ReusableModules import vehicle_get_device_meta_data,device_meta_data_update_lifecycle_state
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_DeviceMetadata:

    #get devices.
    @pytest.mark.Smoke
    def test1_positive_get_device_metadata_device_details(self):

        print("----------------------------------------------------------")
        testcaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "device-meta-data-all-devices")
        if dict1['Flag'] == "Yes":
            deviceId = str(dict1["deviceId"])
            print("Flag is set to Yes, hence running with excel data :")
        else:
            deviceId = ""
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call vehicle update meta reusable module
        response = vehicle_get_device_meta_data(self,deviceId,testcaseName)
        #validate response code
        assert (response.status_code == 200),"Status code is not 200.Rather found: " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        print("Device Details: ",response_body)


        print("----------------------------------------------------------")

   #get devices by deviceId
    @pytest.mark.Smoke
    def test2_positive_get_device_metadata_by_deviceId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "get-device-meta-data-by-deviceId")
        if dict1['Flag'] == "Yes":
            deviceId = str(dict1["deviceId"])
            print("Flag is set to Yes, hence running with excel data :")
        else:
            deviceId = "simD_FTBU9JjxsR2edK"
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call vehicle update meta reusable module
        response = vehicle_get_device_meta_data(self,deviceId,"getDevicesBydeviceId")
        #validate response code
        assert (response.status_code == 200),"Status code is not 200.Rather found: " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if (response_body["responseMessage"] == "Success"):
                print("Message: ", response_body["responseMessage"])
                print("Created By: ", response_body["responseObj"]["createdBy"])
                print("Updated By: ", response_body["responseObj"]["updatedBy"])
                print("Created Time: ", response_body["responseObj"]["createdTime"])
                print("Updated Time: ", response_body["responseObj"]["updatedTime"])
                print("Id: ", response_body["responseObj"]["id"])
                print("Device Id: ", response_body["responseObj"]["deviceId"])
                print("System Id: ", response_body["responseObj"]["systemId"])
                print("Subsystem Id: ", response_body["responseObj"]["subsystemId"])
                print("Vin: ", response_body["responseObj"]["vin"])
                print("Is Primary: ", response_body["responseObj"]["isPrimary"])
                print("Make: ", response_body["responseObj"]["make"])
                print("Model: ", response_body["responseObj"]["model"])
                print("Manufacturer: ", response_body["responseObj"]["manufacturer"])
                print("ECU Type: ", response_body["responseObj"]["ecuType"])
                print("Attestation Mechanism: ", response_body["responseObj"]["attestationMechanism"])
                print("State: ", response_body["responseObj"]["state"])
                print("Error Message: ", response_body["responseObj"]["errorMessage"])
                testResult(self, "passed", "Should fetch device details for given deviceId successfully",
                           "Successfully fetched device details for given deviceId")
        elif response_body["responseCode"] != str(1200):
            testResult(self, "failed", "Should fetch device details for given deviceId successfully",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseMessage"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

    #update device lifecycle state
#Note :  This allows updates from a lower state to a higher state only. The order of (positive) state is PROVISION -> ACTIVE.
    @pytest.mark.Smoke
    def test3_positive_device_metadata_update_lifycycle_state(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "device-meta-data-update-lifecycle-state")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            deviceId = str(dict1["deviceId"])
            lifecycleState = str(dict1["lifecycleState"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            deviceId = "simD_FTBU9JjxsR2edK"
            lifecycleState = "ACTIVE"

        print("Device Id: ", deviceId)
        print("Lifecycle State: ", lifecycleState)

        # Call vehicle update meta reusable module
        response = device_meta_data_update_lifecycle_state(self, deviceId, lifecycleState)
        #validate response code
        assert (response.status_code == 200),"Status code is not 200.Rather found: " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if (response_body["responseMessage"] == "Success"):
                print("Message: ", response_body["responseMessage"])
                testResult(self, "passed", "Should update device lifecycle state for given deviceId successfully",
                           "Successfully updated device lifecycle state for given deviceId")
        elif response_body["responseCode"] != str(1200):
            testResult(self, "failed", "Should update device lifecycle state for given deviceId successfully",
                       "Failed to update "+"\n"+"Note : This allows updates from a lower state to a higher state only. The order of (positive) state is PROVISION -> ACTIVE." +"\n"+ "Reason for failure is : " +
                       response_body["responseMessage"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

