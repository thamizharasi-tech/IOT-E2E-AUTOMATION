import pytest
import json

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.testResults import testResult
from C2CModules.vehicleServices_modules import vehicleServices_getVehicleServiceDetails, \
    vehicleServices_createVehicleServiceEntry, vehicleServices_updateVehicleServiceEntry, \
    vehicleServices_getVehicleServiceHistoryList, vehicleServices_deleteVehicleServiceEntry

from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_VehicleService:

    # API to save the details of vehicle service db
    @pytest.mark.Smoke
    def test1_positive_vehicleServices_createVehicleServiceEntry(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
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
    def test1_positive_vehicleServices_updateVehicleServiceEntry(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_updateVehicleServiceEntry")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = 'true'
            serviceDate = 1688169600000
            serviceDueDate = 1689724800000
            serviceOdo = 123
            serviceDueOdo = 5123
            dateReminder = 1689638400000
            odoReminder = 4623
            notes = "string"

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
    def test1_positive_vehicleServices_getVehicleServiceDetails(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            print("System Id :", systemId)
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            print("System Id :", systemId)
        # Call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

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
    def test1_positive_vehicleServices_getVehicleServiceHistoryList(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            print("System Id :", systemId)

            print("---------------------------------------")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["message"] == "Data Fetched Successfully")

        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"])
            if data_len >=1:
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
    def test1_positive_vehicleServices_deleteVehicleServiceEntry(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            print("System Id :", systemId)

            print("---------------------------------------")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            print("System Id :", systemId)

        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "valid")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
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

    # -------------------------------------------------------------------------------
    # Negative Testdata validations
    # -------------------------------------------------------------------------------
    # Negative
    # invalid systemId
    @pytest.mark.Smoke
    def test1_negative_get_vehicle_service_invalidSystemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_getVehicleServiceDetails_invalidSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # null systemId
    @pytest.mark.Smoke
    def test1_negative_get_vehicle_service_empty_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_getVehicleServiceDetails_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = " "
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""

        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Negative
    # invalid systemId
    @pytest.mark.Smoke
    def test1_negative_update_vehicle_service_invalid_systemId(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_updateVehicleServiceEntry_invalidSystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = str(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = str(dict1["serviceDate"])
            serviceDueDate = str(dict1["serviceDueDate"])
            serviceOdo = str(dict1["serviceOdo"])
            serviceDueOdo = str(dict1["serviceDueOdo"])
            dateReminder = str(dict1["dateReminder"])
            odoReminder = str(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = "sysc943bdfe252d11eeaed6"
            status = 2
            deviceMaintenanceFlag = 'true'
            serviceDate = 1688169600000
            serviceDueDate = 1689724800000
            serviceOdo = 123
            serviceDueOdo = 5123
            dateReminder = 1689638400000
            odoReminder = 4623
            notes = "string"

        print("System Id : ", systemId)

        # Call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")
        print("----------------------------------------------------------")

    # empty systemId
    @pytest.mark.Smoke
    def test1_negative_update_vehicle_service_empty_systemId(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_updateVehicleServiceEntry_emptySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = " "
            vin = str(dict1["vin"])
            status = str(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = str(dict1["serviceDate"])
            serviceDueDate = str(dict1["serviceDueDate"])
            serviceOdo = str(dict1["serviceOdo"])
            serviceDueOdo = str(dict1["serviceDueOdo"])
            dateReminder = str(dict1["dateReminder"])
            odoReminder = str(dict1["odoReminder"])
            notes = str(dict1["notes"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = ""
            status = 2
            deviceMaintenanceFlag = 'true'
            serviceDate = 1688169600000
            serviceDueDate = 1689724800000
            serviceOdo = 123
            serviceDueOdo = 5123
            dateReminder = 1689638400000
            odoReminder = 4623
            notes = "string"

        print("System Id :", systemId)

        # Call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Get vehicle service history api
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_invalid_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_getVehicleServiceHistoryList_invalidSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        print("System Id :", systemId)

        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # Get vehicle service history api
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_empty_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_getVehicleServiceHistoryList_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = " "
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")
        print("----------------------------------------------------------")

    # invalid systemId
    @pytest.mark.Smoke
    def test1_negative_delete_vehicle_service_invalid_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_deleteVehicleServiceEntry_invalidSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"

        print("System Id :", systemId)

        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # null systemid
    @pytest.mark.Smoke
    def test1_negative_delete_vehicle_service_empty_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_deleteVehicleServiceEntry_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = " "
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""

        print("System Id :", systemId)

        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # invalid systemId
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_invalid_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_createVehicleServiceEntry_invalidSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = "sys123"
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # null systemid
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_empty_systemId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = ""
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = ""
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("System Id :", systemId)

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # invalid vin
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_invalid_vin(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry_invalidVin")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "vin123"
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("VIN :", vin)

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # null vin
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_empty_vin(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_createVehicleServiceEntry_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ""
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = ""
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("VIN :", vin)

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # invalid vin
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_invalid_vin(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_updateVehicleServiceEntry_invalidVin")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "vin123"
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("VIN :", vin)
        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # null vin
    @pytest.mark.Smoke
    def test1_negative_update_vehicle_service_empty_vin(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService",
                                         "vehicleServices_updateVehicleServiceEntry_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ""
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = ""
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        print("VIN :", vin)
        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["errors"][0]["errorCode"] == str(6112))
        assert (response_body["errors"][0]["message"] == "Given System id/VIN is not valid or empty")

        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------
    # Negative scripts for headers validation
    # ---------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_invalidapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_emptyapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_noapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_empty_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_createVehicleServiceEntry_no_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_createVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_invalidapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_updateVehicleServiceEntry")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_emptyapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_noapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_empty_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_updateVehicleServiceEntry_no_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_createVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            status = int(dict1["status"])
            deviceMaintenanceFlag = str(dict1["deviceMaintenanceFlag"])
            serviceDate = int(dict1["serviceDate"])
            serviceDueDate = int(dict1["serviceDueDate"])
            serviceOdo = int(dict1["serviceOdo"])
            serviceDueOdo = int(dict1["serviceDueOdo"])
            dateReminder = int(dict1["dateReminder"])
            odoReminder = int(dict1["odoReminder"])
            notes = str(dict1["notes"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            status = 2
            deviceMaintenanceFlag = bool('true')
            serviceDate = int(1688169600000)
            serviceDueDate = int(1689724800000)
            serviceOdo = int(123)
            serviceDueOdo = int(5123)
            dateReminder = int(1689638400000)
            odoReminder = int(4623)
            notes = "string"

        # call vehicle service reusable module
        response = vehicleServices_updateVehicleServiceEntry(self, systemId, vin, status, deviceMaintenanceFlag,
                                                             serviceDate,
                                                             serviceDueDate, serviceOdo, serviceDueOdo, dateReminder,
                                                             odoReminder,
                                                             notes, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceDetails_invalidapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceDetails_emptyapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceDetails_noapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceDetails_empty_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceDetails_no_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceDetails")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceDetails(self, systemId, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # --------------------------------------------------------------------
    # --------------------------------------------------------------------

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_invalidapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_emptyapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_noapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_empty_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_getVehicleServiceHistoryList_no_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_getVehicleServiceHistoryList")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_getVehicleServiceHistoryList(self, systemId, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # --------------------------------------------------------------------
    # --------------------------------------------------------------------

    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_deleteVehicleServiceEntry_invalidapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "invalid_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_deleteVehicleServiceEntry_emptyapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "empty_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "api keys are not matching. Please provide valid key")

        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_deleteVehicleServiceEntry_noapikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
        # call vehicle service reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "no_apiKey")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_deleteVehicleServiceEntry_empty_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "empty_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "x-requestor header cannot be blank")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test1_negative_vehicleServices_deleteVehicleServiceEntry_no_xrequestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleService", "vehicleServices_deleteVehicleServiceEntry")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # call vehicle service reusable module
        response = vehicleServices_deleteVehicleServiceEntry(self, systemId, "no_x-requestor")
        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["message"] == "Required authentication headers are missing")

        print("----------------------------------------------------------")

# --------------------------------------------------------------------

