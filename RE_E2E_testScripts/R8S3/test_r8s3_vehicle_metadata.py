import pytest
import random
import time

from C2CModules.vehicle_metadata import vehicle_get_vehicle_metadata
from C2CModules.primary_IVI_device_modules import *
from C2CModules.testResults import testResult
from C2CModules.api_modules import verify_api_response_for_invalid_header
from utils.XLUtils import read_api_data_from_excel


class Test:

    def test_positive_get_vehicle_metadata(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        dict = read_api_data_from_excel(self, "API_Common_Data", "Test Env Name")
        Env = str(dict["Value"])

        dict1 = read_api_data_from_excel(self, "Env_Details", Env)

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        pageNo = "1"
        pageSize = "100"
        model = "suv"
        year = "2022"
        lifeCycleState = "REGIONAL_ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        if cloudEnv in ["GCP-QA3", "RE-DEV"]:
            model = str(dict1["model"])
            year = "2022"
            lifeCycleState = "REGIONAL_ACTIVE"
            regionCode = str(dict1["region"])

        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_systemId(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "REGIONAL_ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_systemId")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_make(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_make")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["vehicleDetails"])
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            if data_len >= 1:
                for i in range(data_len):
                    systemId = response_body["responseData"]["vehicleDetails"][i]["systemId"]
                    regionCode = response_body["responseData"]["vehicleDetails"][i]["regionCode"]
                    countryCode = response_body["responseData"]["vehicleDetails"][i]["countryCode"]
                    lifeCycleState = response_body["responseData"]["vehicleDetails"][i]["lifecycleState"]
                    class1 = response_body["responseData"]["vehicleDetails"][i]["class"]
                    style = response_body["responseData"]["vehicleDetails"][i]["style"]
                    model = response_body["responseData"]["vehicleDetails"][i]["model"]
                    year = response_body["responseData"]["vehicleDetails"][i]["year"]
                    privacyFlag = response_body["responseData"]["vehicleDetails"][i]["privacyFlag"]
                    c2cVersion = response_body["responseData"]["vehicleDetails"][i]["c2cVersion"]
                    make_actual = response_body["responseData"]["vehicleDetails"][i]["make"]
                    brand = response_body["responseData"]["vehicleDetails"][i]["brand"]
                    engineType = response_body["responseData"]["vehicleDetails"][i]["engineType"]
                    manufacturingDate = response_body["responseData"]["vehicleDetails"][i]["manufacturingDate"]
                    manufacturingLocation = response_body["responseData"]["vehicleDetails"][i]["manufacturingLocation"]
                    manufacturingPlant = response_body["responseData"]["vehicleDetails"][i]["manufacturingPlant"]
                    manufacturingCountry = response_body["responseData"]["vehicleDetails"][i]["manufacturingCountry"]
                    hw_version = response_body["responseData"]["vehicleDetails"][i]["hw_version"]
                    sw_version = response_body["responseData"]["vehicleDetails"][i]["sw_version"]
                    vehicleFuelType1 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][0]
                    vehicleFuelType2 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][1]
                    provisionedTime = response_body["responseData"]["vehicleDetails"][i]["provisionedTime"]
                    deviceImei = response_body["responseData"]["vehicleDetails"][i]["deviceImei"]
                    iccid = response_body["responseData"]["vehicleDetails"][i]["iccid"]
                    if make_actual == make:
                        break
            else:
                print("No data available")

            print("System Id: ", systemId)
            print("Region Code: ", regionCode)
            print("Country Code: ", countryCode)
            print("LifeCycleState: ", lifeCycleState)
            print("Class: ", class1)
            print("Style: ", style)
            print("Model: ", model)
            print("Year: ", year)
            print("PrivacyFlag: ", privacyFlag)
            print("c2cVersion: ", c2cVersion)
            print("Make: ", make_actual)
            print("Brand: ", brand)
            print("EngineType: ", engineType)
            print("ManufacturingDate: ", manufacturingDate)
            print("ManufacturingLocation: ", manufacturingLocation)
            print("ManufacturingPlant: ", manufacturingPlant)
            print("ManufacturingCountry: ", manufacturingCountry)
            print("hw_version: ", hw_version)
            print("sw_version: ", sw_version)
            print("vehicleFuelType1: ", vehicleFuelType1)
            print("vehicleFuelType2: ", vehicleFuelType2)
            print("provisionedTime: ", provisionedTime)
            print("deviceImei: ", deviceImei)
            print("iccid: ", iccid)
            print("offset: ", offset)
            print("limit: ", limit)
            print("Total Records: ", totalRecords)

            testResult(self, "passed", "Vehicle Metadata should be fetched successfully",
                       "Vehicle Metadata is fetched successfully ")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Vehicle Metadata should be fetched successfully ",
                       "Failed to fetch Vehicle Metadata " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_model(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "ThunderX"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        cloudEnv = read_cloud_env(self)
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_model")

        # Validate response status code
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_year(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "50"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_year")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_regionCode(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "50"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "US"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_regionCode")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_systemId_lifeCycleState(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "REGIONAL_ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState,
                                                "vehicle_meta_by_systemId_lifeCycleState")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_systemId_lifeCycleState_model(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "ThunderX"
        year = "2022"
        lifeCycleState = "REGIONAL_ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState,
                                                "vehicle_meta_by_systemId_lifeCycleState_model")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_systemId_lifeCycleState_model_make(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState,
                                                "vehicle_meta_by_systemId_lifeCycleState_model_make")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["vehicleDetails"])
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            if data_len >= 1:
                for i in range(data_len):
                    systemId_actual = response_body["responseData"]["vehicleDetails"][i]["systemId"]
                    regionCode = response_body["responseData"]["vehicleDetails"][i]["regionCode"]
                    countryCode = response_body["responseData"]["vehicleDetails"][i]["countryCode"]
                    lifeCycleState_actual = response_body["responseData"]["vehicleDetails"][i]["lifecycleState"]
                    class1 = response_body["responseData"]["vehicleDetails"][i]["class"]
                    style = response_body["responseData"]["vehicleDetails"][i]["style"]
                    model_actual = response_body["responseData"]["vehicleDetails"][i]["model"]
                    year = response_body["responseData"]["vehicleDetails"][i]["year"]
                    privacyFlag = response_body["responseData"]["vehicleDetails"][i]["privacyFlag"]
                    c2cVersion = response_body["responseData"]["vehicleDetails"][i]["c2cVersion"]
                    make_actual = response_body["responseData"]["vehicleDetails"][i]["make"]
                    brand = response_body["responseData"]["vehicleDetails"][i]["brand"]
                    engineType = response_body["responseData"]["vehicleDetails"][i]["engineType"]
                    manufacturingDate = response_body["responseData"]["vehicleDetails"][i]["manufacturingDate"]
                    manufacturingLocation = response_body["responseData"]["vehicleDetails"][i]["manufacturingLocation"]
                    manufacturingPlant = response_body["responseData"]["vehicleDetails"][i]["manufacturingPlant"]
                    manufacturingCountry = response_body["responseData"]["vehicleDetails"][i]["manufacturingCountry"]
                    hw_version = response_body["responseData"]["vehicleDetails"][i]["hw_version"]
                    sw_version = response_body["responseData"]["vehicleDetails"][i]["sw_version"]
                    vehicleFuelType1 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][0]
                    vehicleFuelType2 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][1]
                    provisionedTime = response_body["responseData"]["vehicleDetails"][i]["provisionedTime"]
                    deviceImei = response_body["responseData"]["vehicleDetails"][i]["deviceImei"]
                    iccid = response_body["responseData"]["vehicleDetails"][i]["iccid"]
                    if systemId_actual == systemId and lifeCycleState_actual == lifeCycleState and model_actual == model and make_actual == make:
                        break
            else:
                print("No data available")

            print("System Id: ", systemId_actual)
            print("Region Code: ", regionCode)
            print("Country Code: ", countryCode)
            print("LifeCycleState: ", lifeCycleState_actual)
            print("Class: ", class1)
            print("Style: ", style)
            print("Model: ", model_actual)
            print("Year: ", year)
            print("PrivacyFlag: ", privacyFlag)
            print("c2cVersion: ", c2cVersion)
            print("Make: ", make_actual)
            print("Brand: ", brand)
            print("EngineType: ", engineType)
            print("ManufacturingDate: ", manufacturingDate)
            print("ManufacturingLocation: ", manufacturingLocation)
            print("ManufacturingPlant: ", manufacturingPlant)
            print("ManufacturingCountry: ", manufacturingCountry)
            print("hw_version: ", hw_version)
            print("sw_version: ", sw_version)
            print("vehicleFuelType1: ", vehicleFuelType1)
            print("vehicleFuelType2: ", vehicleFuelType2)
            print("provisionedTime: ", provisionedTime)
            print("deviceImei: ", deviceImei)
            print("iccid: ", iccid)
            print("offset: ", offset)
            print("limit: ", limit)
            print("Total Records: ", totalRecords)

            testResult(self, "passed", "Vehicle Metadata should be fetched successfully",
                       "Vehicle Metadata is fetched successfully ")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Vehicle Metadata should be fetched successfully ",
                       "Failed to fetch Vehicle Metadata " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_by_systemId_lifeCycleState_model_make_style(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState,
                                                "vehicle_meta_by_systemId_lifeCycleState_model_make_style")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)
        if response.status_code != 200:
            # self.result.set_result(TestResults.failed)
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Data Fetched Successfully":
            data_len = len(response_body["responseData"]["vehicleDetails"])
            offset = response_body["responseData"]["offset"]
            limit = response_body["responseData"]["limit"]
            totalRecords = response_body["responseData"]["totalRecords"]
            if data_len >= 1:
                for i in range(data_len):
                    systemId_actual = response_body["responseData"]["vehicleDetails"][i]["systemId"]
                    regionCode = response_body["responseData"]["vehicleDetails"][i]["regionCode"]
                    countryCode = response_body["responseData"]["vehicleDetails"][i]["countryCode"]
                    lifeCycleState_actual = response_body["responseData"]["vehicleDetails"][i]["lifecycleState"]
                    class1 = response_body["responseData"]["vehicleDetails"][i]["class"]
                    style_actual = response_body["responseData"]["vehicleDetails"][i]["style"]
                    model_actual = response_body["responseData"]["vehicleDetails"][i]["model"]
                    year = response_body["responseData"]["vehicleDetails"][i]["year"]
                    privacyFlag = response_body["responseData"]["vehicleDetails"][i]["privacyFlag"]
                    c2cVersion = response_body["responseData"]["vehicleDetails"][i]["c2cVersion"]
                    make_actual = response_body["responseData"]["vehicleDetails"][i]["make"]
                    brand = response_body["responseData"]["vehicleDetails"][i]["brand"]
                    engineType = response_body["responseData"]["vehicleDetails"][i]["engineType"]
                    manufacturingDate = response_body["responseData"]["vehicleDetails"][i]["manufacturingDate"]
                    manufacturingLocation = response_body["responseData"]["vehicleDetails"][i]["manufacturingLocation"]
                    manufacturingPlant = response_body["responseData"]["vehicleDetails"][i]["manufacturingPlant"]
                    manufacturingCountry = response_body["responseData"]["vehicleDetails"][i]["manufacturingCountry"]
                    hw_version = response_body["responseData"]["vehicleDetails"][i]["hw_version"]
                    sw_version = response_body["responseData"]["vehicleDetails"][i]["sw_version"]
                    vehicleFuelType1 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][0]
                    vehicleFuelType2 = response_body["responseData"]["vehicleDetails"][i]["vehicleFuelType"][1]
                    provisionedTime = response_body["responseData"]["vehicleDetails"][i]["provisionedTime"]
                    deviceImei = response_body["responseData"]["vehicleDetails"][i]["deviceImei"]
                    iccid = response_body["responseData"]["vehicleDetails"][i]["iccid"]
                    if systemId_actual == systemId and lifeCycleState_actual == lifeCycleState and model_actual == model and make_actual == make and style_actual == style:
                        break
            else:
                print("No data available")

            print("System Id: ", systemId_actual)
            print("Region Code: ", regionCode)
            print("Country Code: ", countryCode)
            print("LifeCycleState: ", lifeCycleState_actual)
            print("Class: ", class1)
            print("Style: ", style)
            print("Model: ", model)
            print("Year: ", year)
            print("PrivacyFlag: ", privacyFlag)
            print("c2cVersion: ", c2cVersion)
            print("Make: ", make)
            print("Brand: ", brand)
            print("EngineType: ", engineType)
            print("ManufacturingDate: ", manufacturingDate)
            print("ManufacturingLocation: ", manufacturingLocation)
            print("ManufacturingPlant: ", manufacturingPlant)
            print("ManufacturingCountry: ", manufacturingCountry)
            print("hw_version: ", hw_version)
            print("sw_version: ", sw_version)
            print("vehicleFuelType1: ", vehicleFuelType1)
            print("vehicleFuelType2: ", vehicleFuelType2)
            print("provisionedTime: ", provisionedTime)
            print("deviceImei: ", deviceImei)
            print("iccid: ", iccid)
            print("offset: ", offset)
            print("limit: ", limit)
            print("Total Records: ", totalRecords)

            testResult(self, "passed", "Vehicle Metadata should be fetched successfully",
                       "Vehicle Metadata is fetched successfully ")
        elif response_body["message"] != "Data Fetched Successfully":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Vehicle Metadata should be fetched successfully ",
                       "Failed to fetch Vehicle Metadata " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_pageNo_0(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "0"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "valid")

        # Validate response status code
        if response.status_code == 400 or response.status_code == str(400):
            # self.result.set_result(TestResults.failed)
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13211" and response_body["errors"][0][
            "message"] == "Page number should not be 0 or negative":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_pageSize_0(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "0"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "valid")

        # Validate response status code
        if response.status_code == 400 or response.status_code == str(400):
            # self.result.set_result(TestResults.failed)
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        response_body = response.json()

        if response_body["errors"][0]["errorCode"] == "13212" and response_body["errors"][0][
            "message"] == "Page size must not be less than one":
            assert True
        else:
            assert False
        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_positive_get_vehicle_metadata_pageSize_greater_totalRecords(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "1000"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "6429"
        cloudEnv = read_cloud_env(self)

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        issuedTime = ""
        if response_body["message"] == "Data Fetched Successfully":
            dtc_len = len(response_body["responseData"]["vehicleDetails"])
            if dtc_len >= 1:
                valid_vehicle_found = False

                for i in range(dtc_len):
                    vehicle = response_body["responseData"]["vehicleDetails"][i]
                    lifecycleState_actual = vehicle.get("lifecycleState", "")

                    if lifecycleState_actual == 'REGIONAL_ACTIVE' or "ACTIVE" in lifecycleState_actual:
                        valid_vehicle_found = True

                        actual_systemId = vehicle.get("systemId", "")
                        regionCode = vehicle.get("regionCode", "")
                        countryCode = vehicle.get("countryCode", "")
                        vehicle_class = vehicle.get("class", "")
                        style = vehicle.get("style", "")
                        model = vehicle.get("model", "")
                        year = vehicle.get("year", "")
                        privacyFlag = vehicle.get("privacyFlag", "")
                        c2cVersion = vehicle.get("c2cVersion", "")
                        hw_version = vehicle.get("hw_version", "")
                        sw_version = vehicle.get("sw_version", "")
                        provisionedTime = vehicle.get("provisionedTime", "")

                        if cloudEnv not in ["GCP-QA3"]:
                            make = vehicle.get("make", "")
                            engineType = vehicle.get("engineType", "")
                            manufacturingDate = vehicle.get("manufacturingDate", "")
                            manufacturingLocation = vehicle.get("manufacturingLocation", "")
                            manufacturingPlant = vehicle.get("manufacturingPlant", "")
                            vehicleFuelType = vehicle.get("vehicleFuelType", "")
                            manufacturingCountry = vehicle.get("manufacturingCountry", "")
                            brand = vehicle.get("brand", "")

                        if cloudEnv == "GCP_QA3":
                            vin = vehicle.get("vin", "")

                        break  # ✅ Exit loop once valid vehicle is found

                if not valid_vehicle_found:
                    testResult(self, "failed",
                               "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                               "Vehicle metadata details is retrieved for desired systemId with all the required parameters, but life cycle statuts is not ACTIVE/REHOMED ")
                    assert False

                print("----------------------------------------------------------")
                print('System Id : ', systemId)
                print('Region Code : ', regionCode)
                print('Country Code : ', countryCode)
                print('Life cycle State : ', lifecycleState_actual)
                print('Class : ', vehicle_class)
                print('Style : ', style)
                print('model : ', model)
                print('Year : ', year)
                print('Privacy Flag : ', privacyFlag)
                print('c2cVersion : ', c2cVersion)
                if cloudEnv not in ["GCP-QA3"]:
                    print('make : ', make)
                    print('engineType : ', engineType)
                    print('manufacturingDate : ', manufacturingDate)
                    print('manufacturingLocation : ', manufacturingLocation)
                    print('manufacturingPlant : ', manufacturingPlant)
                    print('brand : ', brand)
                    print('manufacturingCountry : ', manufacturingCountry)
                    print('vehicleFuelType : ', vehicleFuelType)
                print('hw_version : ', hw_version)
                print('sw_version : ', sw_version)
                print('provisionedTime : ', provisionedTime)
                if cloudEnv == "GCP_QA3":
                    print('VIN : ', vin)
                print("----------------------------------------------------------")
                testResult(self, "passed",
                           "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                           "Vehicle metadata details is retrieved for desired systemId with all the required parameters ")
            else:
                print("No vehicle metadata record exists in cloud DB")
                assert False
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed",
                       "Vehicle metadata details should be retrieved for desired systemId with all the required parameters",
                       "Failed to retrieve vehicle metadata details for desired systemId " + " Reason for failure is : " +
                       str(response_body))
            assert False
        else:
            print("Something went wrong")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_invalid_systemId(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = "wew232cd"
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "vehicle_meta_by_systemId")

        # Validate response status code
        if response.status_code == 204 or response.status_code == str(204):
            # self.result.set_result(TestResults.failed)
            assert True
        else:
            print("Status code is not 200. Rather found : " + str(response.status_code))
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_invalid_apikey(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "invalid_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "invalid_apiKey")

        testResult(self, "passed",
                   "Vehicle Metadata API should throw appropriate error message for invalid apikey.",
                   "Vehicle Metadata API showing/throwing appropriate error message for invalid apikey.")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_empty_apikey(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "empty_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_apiKey")

        testResult(self, "passed",
                   "Vehicle Metadata API should throw appropriate error message for empty apikey.",
                   "Vehicle Metadata API showing/throwing appropriate error message for empty apikey.")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_no_apikey(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "no_apiKey")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_apiKey")

        testResult(self, "passed",
                   "Vehicle Metadata API should throw appropriate error message for no apikey.",
                   "Vehicle Metadata API showing/throwing appropriate error message for no apikey.")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_empty_xrequestor(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "empty_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "empty_x-requestor")

        testResult(self, "passed",
                   "Vehicle Metadata API should throw appropriate error message for empty x-requestor.",
                   "Vehicle Metadata API showing/throwing appropriate error message for empty x-requestor.")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")

    @pytest.mark.smoke
    def test_negative_get_vehicle_metadata_no_xrequestor(self):

        print("----------------------------------------------------------")
        print("Get Vehicle Metadata with predefined input/data")
        print("----------------------------------------------------------")

        pageNo = "1"
        pageSize = "10"
        model = "suv"
        year = "2022"
        lifeCycleState = "ACTIVE"
        regionCode = "NA"
        make = "toyota"
        style = "suv"
        operationalState = "NA"
        # Read system id from c2c_vehicle.json file
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "0000"

        # Call api reusable module
        response = vehicle_get_vehicle_metadata(self, pageNo, pageSize, model, year, lifeCycleState, regionCode, make,
                                                systemId, style, operationalState, "no_x-requestor")

        # Validate api status & response
        verify_api_response_for_invalid_header(response, "no_x-requestor")

        testResult(self, "passed",
                   "Vehicle Metadata API should throw appropriate error message for no x-requestor.",
                   "Vehicle Metadata API showing/throwing appropriate error message for no x-requestor.")
        # self.result.set_result(TestResults.passed)

        print("----------------------------------------------------------")