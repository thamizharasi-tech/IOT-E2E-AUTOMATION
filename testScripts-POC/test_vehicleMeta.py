import pytest

from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import getVIN
from C2CModules.testResults import testResult
from C2CModules.vehicle_metadata import vehicle_get_vins_byModel_v3, vehicle_get_vehicle_metadata, \
    vehicle_update_vehicle_metadata, vehicle_get_device_metadata
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_VehicleMeta:

    # Vehicle_update-vehicle-meta-data
    @pytest.mark.Smoke
    def test1_positive_vehicle_update_vehicle_metadata(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        print("VIN :", vin)

        # Call vehicle update meta reusable module
        response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                   manufacturing_location, manufacturing_plant,
                                                   manufacturing_country, vehicle_registration,
                                                   vehicle_registration_date, fleet_id, driver_id, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseMessage"] == "Vehicle data updated successfully")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False
        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert (response_body["responseMessage"] == "Success")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body))
            assert False

        print("----------------------------------------------------------")

    # vehicle_get_device_metadata
    @pytest.mark.Smoke
    def test3_positive_vehicle_get_device_metadata(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-device-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        print("VIN :", vin)

        # Call vehicle update meta reusable module
        response = vehicle_get_device_metadata(self, vin, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(13200):
            assert ("No vehicle found for the device_id" in response_body["responseMessage"])
        else:
            print("response Code is not 13200. Rather found : " + str(response_body))
            assert False

        print("----------------------------------------------------------")

    # Negative_Scenarios

    # vehicle_get_vins_byModel_v3_invalid_VIN
    @pytest.mark.Sanity
    def test1_negative_vehicle_get_vins_byModel_v3_invalid_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "vehicle_get_vinsByModel_v3_invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle_get_vins_byModel_v3 reusable module

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

        # Call vehicle_get_vins_byModel_v3 reusable module
        response = vehicle_get_vins_byModel_v3(self, vin, "valid")

        response_body = response.json()

        if response_body['responseCode'] == '13201' and response_body['responseData']['message'] == 'Vehicle does not exist.':
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "13201" and response_body["responseData"]["message"] != "Vehicle does not exist.":
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")

        print("--------------------InvalidVin--------------------------------------")

    # vehicle_get_vins_byModel_v3_empty_VIN
    @pytest.mark.Sanity
    def test2_negative_vehicle_get_vins_byModel_v3_empty_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "vehicle_get_vinsByModel_v3_invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ''
        else:
            print("Flag is not set to Yes, thus running with actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        print("VIN :", vin)

        # Call vehicle_get_vins_byModel_v3 reusable module
        response = vehicle_get_vins_byModel_v3(self, vin, "valid")
        response_body = response.json()

        if response_body['responseCode'] == '13201' and response_body['responseData']['message'] == ('Vehicle does '
                                                                                                     'not exist.'):
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "13201" and response_body["responseData"]["message"] != (
                'Vehicle does not exist.'):
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")

        print("---------------------EmptyVin-------------------------------------")

    # vehicle_get_vins_byModel_v3_without_VIN
    @pytest.mark.Sanity
    def test3_negative_vehicle_get_vins_byModel_v3_without_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "vehicle_get_vinsByModel_v3_invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == ' ':
                vin = ' '

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        print("VIN :", vin)

        # Call vehicle_get_vins_byModel_v3 reusable module
        response = vehicle_get_vins_byModel_v3(self, vin, "valid")
        print(response.status_code)
        response_body = response.json()

        if response_body['responseCode'] == '13201' and response_body['responseData']['message'] == ('Vehicle does '
                                                                                                     'not exist.'):
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "13201" and response_body["responseData"]["message"] != (
                "Vehicle does "
                "not exist."):
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")

        print("-----------------------WithoutVin-----------------------------------")

    # Vehicle_update-vehicle-meta-data_invalid_VIN
    @pytest.mark.Sanity
    def test4_negative_vehicle_update_vehicle_metadata_invalid_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update_vehicle_meta_data_invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        print("VIN :", vin)

        # Call vehicle update meta reusable module
        response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                   manufacturing_location, manufacturing_plant, manufacturing_country,
                                                   vehicle_registration, vehicle_registration_date, fleet_id, driver_id,
                                                   "valid")
        response_body = response.json()

        if response_body['responseCode'] == '1200' and response_body['responseMessage'] == 'Vehicle does not exist.':
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "1200" and response_body["responseMessage"] != "Vehicle does not exist.":
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")

        print("--------------------InvalidVin--------------------------------------")

    # Vehicle_update-vehicle-meta-data_empty_VIN
    @pytest.mark.Sanity
    def test5_negative_vehicle_update_vehicle_metadata_empty_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data_empty_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ' '
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])
        else:
            print("Flag is not set to Yes, thus running with actual device data")

            vin = ""
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        print("VIN :", vin)

        # Call vehicle update meta reusable module
        response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                   manufacturing_location, manufacturing_plant, manufacturing_country,
                                                   vehicle_registration, vehicle_registration_date, fleet_id, driver_id,
                                                   "valid")
        response_body = response.json()
        print(response_body)

        if response_body['responseCode'] == '1200' and response_body['responseMessage'] == ('Vehicle does '
                                                                                                     'not exist.'):
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "1200" and response_body["responseMessage"] != (
                "Vehicle does "
                "not exist."):
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")
        print("---------------------EmptyVin-------------------------------------")

    # Vehicle_update-vehicle-meta-data_without_VIN
    @pytest.mark.Sanity
    def test6_negative_vehicle_update_vehicle_metadata_without_VIN(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data_without_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == ' ':
                vin = ' '
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        else:
            print("Flag is not set to Yes, thus running with actual device data")
            vin = " "
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

        print("VIN :", vin)

        # Call vehicle update meta reusable module
        response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                   manufacturing_location, manufacturing_plant, manufacturing_country,
                                                   vehicle_registration, vehicle_registration_date, fleet_id, driver_id,
                                                   "valid")
        response_body = response.json()
        print(response_body)

        if response_body['responseCode'] == '1200' and response_body['responseMessage'] == ('Vehicle does '
                                                                                                     'not exist.'):
            testResult(self, "passed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details are not updated")
        elif response_body["responseCode"] != "1200" and response_body["responseMessage"] != (
                "Vehicle does "
                "not exist."):
            testResult(self, "failed", "Should not update the vehicle metadata details ",
                       "Vehicle metadata details got updated successfully")
        else:
            print("something went wrong")

        print("-----------------------WithoutVin-----------------------------------")

    # To create vehicle_update_vehicle_metadata with invalid apikey
    @pytest.mark.Smoke
    def test7_negative_vehicle_update_vehicle_metadata_invalidApikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "invalid_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "invalid_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "api keys are not matching..please provide valid key"

        print("----------------Api key mismatch------------------------------------------")

    # To create vehicle_update_vehicle_metadata with Empty apikey
    @pytest.mark.Smoke
    def test8_negative_vehicle_update_vehicle_metadata_EmptyApikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "empty_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "empty_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "api keys are not matching..please provide valid key"

        print("----------------Api key mismatch------------------------------------------")

    # To create vehicle_update_vehicle_metadata with no apikey
    @pytest.mark.Smoke
    def test9_negative_vehicle_update_vehicle_metadata_no_apiKey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "no_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "no_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "Required authentication headers are missing..!!!!"

        print("----------------Api key mismatch------------------------------------------")

    # To create vehicle_update_vehicle_metadata with empty_x-requestor
    @pytest.mark.Smoke
    def test10_negative_vehicle_update_vehicle_metadata_empty_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id,
                                                       "empty_x-requestor")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id,
                                                       "empty_x-requestor")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------X-Requestor mismatch------------------------------------------")

    # To create vehicle_update_vehicle_metadata with no_x-requestor
    @pytest.mark.Smoke
    def test11_negative_vehicle_update_vehicle_metadata_no_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_update-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "no_x-requestor")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)
            model = str(dict1["model"])
            year = str(dict1["year"])
            make = str(dict1["make"])
            engine_type = str(dict1["engine_type"])
            manufacturing_date = str(dict1["manufacturing_date"])
            manufacturing_location = str(dict1["manufacturing_location"])
            manufacturing_plant = str(dict1["manufacturing_plant"])
            manufacturing_country = str(dict1["manufacturing_country"])
            vehicle_registration = str(dict1["vehicle_registration"])
            vehicle_registration_date = str(dict1["vehicle_registration_date"])
            fleet_id = str(dict1["fleetId"])
            driver_id = str(dict1["driverId"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_update_vehicle_metadata(self, vin, model, year, make, engine_type, manufacturing_date,
                                                       manufacturing_location, manufacturing_plant,
                                                       manufacturing_country, vehicle_registration,
                                                       vehicle_registration_date, fleet_id, driver_id, "no_x-requestor")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        assert response_body["message"] == "Required authentication headers are missing..!!!!"

        print("----------------X-Requestor mismatch------------------------------------------")

    # To create Vehicle_GetVinsByModel_v3_Header_validation with invalid API key
    @pytest.mark.Smoke
    def test12_negative_Vehicle_GetVinsByModel_v3_Header_validation_invalid_apiKey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel_v3")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_get_vins_byModel_v3(self, vin, "invalid_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_get_vins_byModel_v3(self, vin, "invalid_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "api keys are not matching..please provide valid key"

        print("----------------Api key mismatch------------------------------------------")

    # To create Vehicle_GetVinsByModel_v3_Header_validation with empty API key
    @pytest.mark.Smoke
    def test13_negative_Vehicle_GetVinsByModel_v3_Header_validation_empty_apiKey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel_v3")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_get_vins_byModel_v3(self, vin, "empty_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_get_vins_byModel_v3(self, vin, "empty_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "api keys are not matching..please provide valid key"

        print("----------------Api key mismatch------------------------------------------")

    # To create Vehicle_GetVinsByModel_v3_Header_validation with no API key
    @pytest.mark.Smoke
    def test14_negative_Vehicle_GetVinsByModel_v3_Header_validation_no_apiKey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel_v3")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_get_vins_byModel_v3(self, vin, "no_apiKey")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_get_vins_byModel_v3(self, vin, "no_apiKey")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "Required authentication headers are missing..!!!!"

        print("----------------Api key mismatch------------------------------------------")

    # To create Vehicle_GetVinsByModel_v3_Header_validation with empty_x-requestor
    @pytest.mark.Smoke
    def test15_negative_Vehicle_GetVinsByModel_v3_Header_validation_empty_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel_v3")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_get_vins_byModel_v3(self, vin, "empty_x-requestor")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_get_vins_byModel_v3(self, vin, "empty_x-requestor")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "x-requestor header cannot be blank"

        print("----------------X-Requestor mismatch------------------------------------------")

    # To create Vehicle_GetVinsByModel_v3_Header_validation with no_x-requestor
    @pytest.mark.Smoke
    def test16_negative_Vehicle_GetVinsByModel_v3_Header_validation_no_x_requestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle-GetVinsByModel_v3")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            response = vehicle_get_vins_byModel_v3(self, vin, "no_x-requestor")

            print("----------------------------------------------------------")

        else:
            print("Flag is not set to Yes, thus running with actual device data")

            print("----------------------------------------------------------")

            vin = getVIN(self, OnboardingType, chipsetType)

            print("VIN :", vin)

            # Call vehicle update meta reusable module
            # response = Vehicle_update-vehicle-meta-data(self, vin, "demovehicle", "2")

            response = vehicle_get_vins_byModel_v3(self, vin, "no_x-requestor")

        print("----------------------------------------------------------")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()
        # assert response_body["responseCode"] == "10000"
        assert response_body["message"] == "Required authentication headers are missing..!!!!"

        print("----------------X-Requestor mismatch------------------------------------------")








    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_invalid_VIN(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data_invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = "vin123"

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['responseCode'] == '13201' and response_body['responseMessage'] == 'Vehicle does not exist.':
            testResult(self, "passed", "Should throw proper error code & error message for invalid vin ",
                       "Showing proper error code & error message for invalid vin ")
        elif response_body["responseCode"] != "13201" and response_body["responseMessage"] != "Vehicle does not exist.":
            testResult(self, "failed", "Should throw proper error code & error message for invalid vin  ",
                       "Not showing proper error code & error message for invalid vin ")
        else:
            print("something went wrong")

        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_empty_VIN(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data_empty_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            if vin == "None":
                vin =""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = ""

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "valid")

        # Validate response status code
        assert (response.status_code == 404), "Status code is not 404. Rather found : " + str(response.status_code)

        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_invalidApikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "invalid_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['message'] == 'api keys are not matching..please provide valid key':
            testResult(self, "passed", "Should throw proper error code & error message for invalid api key",
                       "Showing proper error code & error message for invalid api key ")
        elif response_body["message"] != "api keys are not matching..please provide valid key":
            testResult(self, "failed", "Should throw proper error code & error message for invalid api key ",
                       "Not showing proper error code & error message for invalid api key ")
        else:
            print("something went wrong")
            assert False

        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_emptyApikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "empty_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['message'] == 'api keys are not matching..please provide valid key':
            testResult(self, "passed", "Should throw proper error code & error message for empty api key",
                       "Showing proper error code & error message for empty api key ")
        elif response_body["message"] != "api keys are not matching..please provide valid key":
            testResult(self, "failed", "Should throw proper error code & error message for empty api key ",
                       "Not showing proper error code & error message for empty api key ")
        else:
            print("something went wrong")
            assert False

        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_noApikey(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "no_apiKey")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['message'] == 'Required authentication headers are missing..!!!!':
            testResult(self, "passed", "Should throw proper error code & error message for no api key parameter",
                       "Showing proper error code & error message for no api key parameter ")
        elif response_body["message"] != "Required authentication headers are missing..!!!!":
            testResult(self, "failed", "Should throw proper error code & error message for no api key parameter ",
                       "Not showing proper error code & error message for no api key parameter ")
        else:
            print("something went wrong")
            assert False

        print("----------------------------------------------------------")

# Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_empty_x_requestor (self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "empty_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['message'] == 'x-requestor header cannot be blank':
            testResult(self, "passed", "Should throw proper error code & error message for empty x-requestor key",
                       "Showing proper error code & error message for empty x-requestor key ")
        elif response_body["message"] != "x-requestor header cannot be blank":
            testResult(self, "failed", "Should throw proper error code & error message for empty x-requestor key ",
                       "Not showing proper error code & error message for empty x-requestor key ")
        else:
            print("something went wrong")
            assert False

        print("----------------------------------------------------------")

    # Vehicle_get-vehicle-meta-data
    @pytest.mark.Smoke
    def test2_positive_vehicle_get_vehicle_metadata_no_x_requestor(self):

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "VehicleMeta", "Vehicle_get-vehicle-meta-data")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            vin = getVIN(self, OnboardingType, chipsetType)

        # Call vehicle update meta reusable module
        response = vehicle_get_vehicle_metadata(self, vin, "no_x-requestor")

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body['message'] == 'Required authentication headers are missing..!!!!':
            testResult(self, "passed", "Should throw proper error code & error message for no x-requestor key parameter",
                       "Showing proper error code & error message for no x-requestor key parameter ")
        elif response_body["message"] != "Required authentication headers are missing..!!!!":
            testResult(self, "failed", "Should throw proper error code & error message for no x-requestor key parameter ",
                       "Not showing proper error code & error message for no x-requestor key parameter ")
        else:
            print("something went wrong")
            assert False

        print("----------------------------------------------------------")