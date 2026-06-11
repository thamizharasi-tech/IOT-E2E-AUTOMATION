import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.testResults import testResult
from C2CModules.vehicleServices_modules import vehicleServices_getVehicleServiceDetails, \
    vehicleServices_createVehicleServiceEntry, vehicleServices_updateVehicleServiceEntry, \
    vehicleServices_getVehicleServiceHistoryList, vehicleServices_deleteVehicleServiceEntry


OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_VehicleService:

    # API to save the details of vehicle service db
    @pytest.mark.Smoke
    def test1_positive_vehicleServices_createVehicleServiceEntry(self):
        print("----------------------------------------------------------")
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        status = 2
        deviceMaintenanceFlag = bool('true')
        serviceDate = int(1688169600000)
        serviceDueDate = int(1689724800000)
        serviceOdo = int(8000)
        serviceDueOdo = int(10000)
        dateReminder = int(1689638400000)
        odoReminder = int(9500)
        notes = "Save vehicle service details"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "valid")
        # Validate response status code & success message
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Saved Successfully")
        if response_body["message"] == "Data Saved Successfully":
            testResult(self, "passed",
                       "Vehicle service data should be saved successfully",
                       "Vehicle service data is saved successfully")
        else:
            testResult(self, "failed",
                       "Vehicle service data should be saved successfully",
                       "Failed to save Vehicle service data")

        print("----------------------------------------------------------")

    # API to update the details of vehicle service db
    @pytest.mark.Smoke
    def test2_positive_vehicleServices_updateVehicleServiceEntry(self):
        print("----------------------------------------------------------")
        vin = getVIN(self, OnboardingType, chipsetType)
        systemId = get_SystemId(self, OnboardingType, chipsetType)
        status = 2
        deviceMaintenanceFlag = 'true'
        serviceDate = 1688169600000
        serviceDueDate = 1689724800000
        serviceOdo = 8000
        serviceDueOdo = 10000
        dateReminder = 1689638400000
        odoReminder = 9000
        notes = "Update vehicle service details"

        # Call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Updated Successfully")
        if response_body["message"] == "Data Updated Successfully":
            testResult(self, "passed",
                       "Vehicle service data should be updated successfully",
                       "Vehicle service data is updated successfully")
        else:
            testResult(self, "failed",
                       "Vehicle service data should be updated successfully",
                       "Failed to update Vehicle service data")
        print("----------------------------------------------------------")

    # API to get the details of vehicle service db
    @pytest.mark.Smoke
    def test3_positive_vehicleServices_getVehicleServiceDetails(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)
        print("System Id :", systemId)

        # Call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Fetched Successfully")

        if response_body["message"] == "Data Fetched Successfully":
            print("Created By : ", response_body["responseData"]["createdBy"])
            print("Created Time : ", response_body["responseData"]["createdTime"])
            print("Updated By : ", response_body["responseData"]["updatedBy"])
            print("Updated Time : ", response_body["responseData"]["updatedTime"])
            print("System Id : ", response_body["responseData"]["systemId"])
            print("Vin : ", response_body["responseData"]["vin"])
            print("Status : ", response_body["responseData"]["status"])
            print("Device Maintenance Flag : ", response_body["responseData"]["deviceMaintenanceFlag"])
            print("Service Date : ", response_body["responseData"]["serviceDate"])
            print("Service Due Date : ", response_body["responseData"]["serviceDueDate"])
            print("Service Odo : ", response_body["responseData"]["serviceOdo"])
            print("Service Due Odo : ", response_body["responseData"]["serviceDueOdo"])
            print("Date Reminder : ", response_body["responseData"]["dateReminder"])
            print("Odo Reminder : ", response_body["responseData"]["odoReminder"])
            print("Notes : ", response_body["responseData"]["notes"])
            testResult(self, "passed",
                       "Vehicle service data should be fetched successfully",
                       "Vehicle service data is fetched successfully")
        else:
            testResult(self, "failed",
                       "Vehicle service data should be fetched successfully",
                       "Failed to fetch Vehicle service data")

        print("----------------------------------------------------------")

    # Get vehicle service history api
    @pytest.mark.Smoke
    def test4_positive_vehicleServices_getVehicleServiceHistoryList(self):
        print("----------------------------------------------------------")

        systemId = get_SystemId(self, OnboardingType, chipsetType)
        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Fetched Successfully")

        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"])
            if data_len >= 1:
                data_len = int(data_len - 1)
                print("Created By : ", response_body["responseData"][data_len]["createdBy"])
                print("Created Time : ", response_body["responseData"][data_len]["createdTime"])
                print("Updated By : ", response_body["responseData"][data_len]["updatedBy"])
                print("Updated Time : ", response_body["responseData"][data_len]["updatedTime"])
                print("History Id : ", response_body["responseData"][data_len]["historyId"])
                print("System Id : ", response_body["responseData"][data_len]["systemId"])
                print("Vin : ", response_body["responseData"][data_len]["vin"])
                print("Status : ", response_body["responseData"][data_len]["status"])
                print("Device Maintenance Flag : ", response_body["responseData"][data_len]["deviceMaintenanceFlag"])
                print("Service Date : ", response_body["responseData"][data_len]["serviceDate"])
                print("Service Due Date : ", response_body["responseData"][data_len]["serviceDueDate"])
                print("Service Odo : ", response_body["responseData"][data_len]["serviceOdo"])
                print("Service Due Odo : ", response_body["responseData"][data_len]["serviceDueOdo"])
                print("Date Reminder : ", response_body["responseData"][data_len]["dateReminder"])
                print("Odo Reminder : ", response_body["responseData"][data_len]["odoReminder"])
                print("Notes : ", response_body["responseData"][data_len]["notes"])
                testResult(self, "passed",
                           "Vehicle service history should be fetched successfully",
                           "Vehicle service history is fetched successfully")
            else:
                testResult(self, "passed",
                           "Vehicle service history should be fetched successfully",
                           "Vehicle service history list is empty, but end point is working fine, thus marking test case pass")

        else:
            testResult(self, "failed",
                       "Vehicle service history should be fetched successfully",
                       "Failed to fetch Vehicle service history")

        print("----------------------------------------------------------")

    # API to delete the details of vehicle service db
    @pytest.mark.Smoke
    def test5_positive_vehicleServices_deleteVehicleServiceEntry(self):

        systemId = get_SystemId(self, OnboardingType, chipsetType)
        print("System Id :", systemId)

        # Call api reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        assert (response_body["message"] == "Data Deleted Successfully")
        if response_body["message"] == "Data Deleted Successfully":
            testResult(self, "passed",
                       "Vehicle service data should be deleted successfully",
                       "Vehicle service data is deleted successfully")
        else:
            testResult(self, "failed",
                       "Vehicle service data should be deleted successfully",
                       "Failed to delete Vehicle service data")
        print("----------------------------------------------------------")

