import pytest


from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.APIM_ReusableModules import vehicle_get_vehicle_meta_data_by_vin,vehicle_update_vehicle_meta_data_by_vin,vehicle_get_vehicle_meta_data_vins_by_model,vehicle_get_vehicle_meta_data_by_deviceId,vehicle_getAll_vehicle_details,vehicle_get_device_meta_data,device_meta_data_update_lifecycle_state
from utils.XLUtils import read_api_data_from_excel
from C2CModules.testResults import testResult

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_VehicleMeta:

    # Vehicle_update-vehicle-meta-data-by-vin
    @pytest.mark.Smoke
    def test1_positive_Vehicle_update_vehicle_meta_data_by_vin(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data-by-vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            make = str(dict1["make"])
            brand = str(dict1["brand"])
            trim = str(dict1["trim"])
            chassis_number = str(dict1["chassis_number"])
            engine_type = str(dict1["engine_type"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])

        else:
            print("Flag is not set to Yes, thus running with actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            make = "make1"
            brand = "F"
            trim = "trim1"
            chassis_number = "chassis1"
            engine_type = "engine1"
            model = "F150"
            year = 2020
            manufacturing_plant = "Manufacturer plant"
            manufacturing_country = "Japan"
            manufacturing_date = "10-20-2022"
            manufacturing_location = "location"
            vehicle_registration = "reg1"
            vehicle_registration_date = "10-25-2022"

        print("VIN :", vin)
        print("Make: ", make)
        print("Brand: ", brand)
        print("Trim: ", trim)
        print("Chassis Number: ", chassis_number)
        print("Engine Type: ", engine_type)
        print("Manufacturing Date: ", manufacturing_date)
        print("Manufacturing Location: ", manufacturing_location)
        print("Manufacturing Plant: ", manufacturing_plant)
        print("Manufacturing Country: ", manufacturing_country)
        print("Vehicle Registration: ", vehicle_registration)
        print("Vehicle Registration Date: ", vehicle_registration_date)

        # Call vehicle update meta reusable module
        response = vehicle_update_vehicle_meta_data_by_vin(self, vin, make, brand, trim, chassis_number, engine_type, model, year, manufacturing_plant, manufacturing_country, manufacturing_date, manufacturing_location, vehicle_registration, vehicle_registration_date)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if response_body["responseMessage"] == "Vehicle data updated successfully":
                testResult(self, "passed", "Should update vehice details for given vin successfully",
                           "Successfully updated vehicle details for given vin")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            testResult(self, "failed", "Should update vehice details for given vin successfully",
                       "Failed to update the data/values " + " Reason for failure is : " +
                       response_body["responseMessage"])


        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data-by-vin
    @pytest.mark.Smoke
    def test2_positive_Vehicle_get_vehicle_meta_data_by_vin(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data-by-vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle get meta reusable module
        response = vehicle_get_vehicle_meta_data_by_vin(self, vin)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if (response_body["responseMessage"] == "Success"):
                print("Message: ",response_body["responseMessage"])
                print("SystemId: ",response_body["vehicle_information"]["system_id"])
                print("Vin: ", response_body["vehicle_information"]["vin"])
                print("Region Code: ", response_body["vehicle_information"]["region_code"])
                print("Country Code: ", response_body["vehicle_information"]["country_code"])
                print("Lifecycle State: ", response_body["vehicle_information"]["lifecycle_state"])
                print("Class: ", response_body["vehicle_information"]["class"])
                print("Style: ", response_body["vehicle_information"]["style"])
                print("Model: ", response_body["vehicle_information"]["model"])
                print("Year: ", response_body["vehicle_information"]["year"])
                print("Privacy Flag: ", response_body["vehicle_information"]["privacy_flag"])
                print("C2C-Version: ", response_body["vehicle_information"]["c2c_version"])
                print("Make: ", response_body["vehicle_information"]["make"])
                print("Brand: ", response_body["vehicle_information"]["brand"])
                print("Trim: ", response_body["vehicle_information"]["trim"])
                print("Chassis Number: ", response_body["vehicle_information"]["chassis_number"])
                print("Engine Type: ", response_body["vehicle_information"]["engine_type"])
                print("Manufacturing Date: ", response_body["vehicle_information"]["manufacturing_date"])
                print("Manufacturing Location: ", response_body["vehicle_information"]["manufacturing_location"])
                print("Manufacturing Plant: ", response_body["vehicle_information"]["manufacturing_plant"])
                print("Manufacturing Country: ", response_body["vehicle_information"]["manufacturing_country"])
                print("Vehicle Registration: ", response_body["vehicle_information"]["vehicle_registration"])
                print("Vehicle Registration Date: ", response_body["vehicle_information"]["vehicle_registration_date"])
                testResult(self, "passed", "Should fetch vehice details for given vin successfully",
                           "Successfully fetched vehicle details for given vin")
        elif response_body["responseCode"] !=str(1200):
            testResult(self, "failed", "Should fetch vehice details for given vin successfully",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseMessage"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data-vins-by-model
    @pytest.mark.Smoke
    def test3_positive_Vehicle_get_vehicle_meta_data_vins_by_model(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            model = str(dict1["model"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            model = "Tesla"

        # Call vehicle get meta reusable module
        response = vehicle_get_vehicle_meta_data_vins_by_model(self, model)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if (response_body["responseMessage"] == "Success"):
                print("Message: ",response_body["responseMessage"])
                print("Vins: ", response_body["vins"])
                testResult(self, "passed", "Should fetch the vins for given model successfully",
                           "Successfully fetched vins for given model")
        elif response_body["responseCode"] !=str(1200):
            testResult(self, "failed", "Should fetch the vins for given model successfully",
                       "Failed to fetch vins" + " Reason for failure is : " +
                       response_body["responseMessage"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data-by-deviceId
    @pytest.mark.Smoke
    def test4_positive_Vehicle_get_vehicle_meta_data_by_deviceId(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data-by-deviceId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            deviceId = str(dict1["deviceId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            deviceId = "simD_FTBU9JjxsR2edK"

        # Call vehicle get meta reusable module
        response = vehicle_get_vehicle_meta_data_by_deviceId(self, deviceId)
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            if (response_body["responseMessage"] == "Success"):
                print("Message: ", response_body["responseMessage"])
                print("SystemId: ", response_body["vehicle_information"]["system_id"])
                print("Vin: ", response_body["vehicle_information"]["vin"])
                print("Region Code: ", response_body["vehicle_information"]["region_code"])
                print("Country Code: ", response_body["vehicle_information"]["country_code"])
                print("Lifecycle State: ", response_body["vehicle_information"]["lifecycle_state"])
                print("Class: ", response_body["vehicle_information"]["class"])
                print("Style: ", response_body["vehicle_information"]["style"])
                print("Model: ", response_body["vehicle_information"]["model"])
                print("Year: ", response_body["vehicle_information"]["year"])
                print("Privacy Flag: ", response_body["vehicle_information"]["privacy_flag"])
                print("C2C-Version: ", response_body["vehicle_information"]["c2c_version"])
                print("Make: ", response_body["vehicle_information"]["make"])
                print("Brand: ", response_body["vehicle_information"]["brand"])
                print("Trim: ", response_body["vehicle_information"]["trim"])
                print("Chassis Number: ", response_body["vehicle_information"]["chassis_number"])
                print("Engine Type: ", response_body["vehicle_information"]["engine_type"])
                print("Manufacturing Date: ", response_body["vehicle_information"]["manufacturing_date"])
                print("Manufacturing Location: ", response_body["vehicle_information"]["manufacturing_location"])
                print("Manufacturing Plant: ", response_body["vehicle_information"]["manufacturing_plant"])
                print("Manufacturing Country: ", response_body["vehicle_information"]["manufacturing_country"])
                print("Vehicle Registration: ", response_body["vehicle_information"]["vehicle_registration"])
                print("Vehicle Registration Date: ", response_body["vehicle_information"]["vehicle_registration_date"])
                testResult(self, "passed", "Should fetch vehice details for given deviceId successfully",
                           "Successfully fetched vehicle details for given deviceId")
        elif response_body["responseCode"] != str(1200):
            testResult(self, "failed", "Should fetch vehice details for given deviceId successfully",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseMessage"])
        else:
            print("Something went wrong")


        print("----------------------------------------------------------")

    # vehicle_getAll_vehicle_details
    @pytest.mark.Smoke
    def test5_positive_vehicle_getAll_vehicle_details(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-get-all-vehicle")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call vehicle update meta reusable module
        response = vehicle_getAll_vehicle_details(self)
        #validate response code
        assert (response.status_code == 200),"Status code is not 200.Rather found: " + str(response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        print("Vehicle Details: ",response_body)


        print("----------------------------------------------------------")

