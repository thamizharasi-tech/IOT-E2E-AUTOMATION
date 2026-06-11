from C2CModules.composite_api import *
from C2CModules.testResults import testResult
from C2CModules.e2e_testData import *
from C2CModules.primary_IVI_device_modules import *

onboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset
netwrokType = wifi

class Test_compositeAPIs_graphQL:


    def test1_vehicle_location_by_systemId(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Vehicle Location By SystemId API functionality. (positive scenario)
        :return: return test status
        Validate Vehicle Location By SystemId
        """
        print("\n------------------ VEHICLE LOCATION BY SYSTEM ID ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        systemId = read_vehicleJsonFile(self, "system_id")
        getVehicleLocationBySystemId(self, cloudEnv, systemId, "valid")


        print("\n------------------------------END------------------------------\n")

    def test2_vehicle_locations(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Vehicle Locations API functionality. (positive scenario)
        :return: return test status
        Validate Vehicle Locations
        """
        print("\n------------------ VEHICLE LOCATIONS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        regionCode = "US"
        countryCode = "India"
        engineType = "2"
        model = "ThunderX"
        year = "2022"
        variant = ""

        getVehicleLocations(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, "valid")

        print("\n------------------------------END------------------------------\n")

    def test3_active_alert_counts_for_vehicles(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the get Active Active Alert Counts For Vehicles API functionality. (positive scenario)
        :return: return test status
        Validate get Active Active Alert Counts For Vehicles
        """
        print("\n------------------ ACTIVE ALERT COUNTS FOR VEHICLES ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        regionCode = "US"
        countryCode = "India"
        engineType = "2"
        model = "ThunderX"
        year = "2022"
        variant = ""

        getActiveActiveAlertCountsForVehicles(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant,"valid")


        print("\n------------------------------END------------------------------\n")

    def test4_vehicle_counts_by_status(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the Vehicle Counts By Status API functionality. (positive scenario)
        :return: return test status
        Validate Vehicle Counts By Status
        """
        print("\n------------------ VEHICLE COUNTS BY STATUS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        regionCode = "US"
        countryCode = "India"
        engineType = "2"
        model = "ThunderX"
        year = "2022"
        variant = ""

        # Call vehicle reusable module
        getVehicleCountsByStatus(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, "valid")

        print("\n------------------------------END------------------------------\n")

    def test5_view_alert_counts(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the View Alert Counts API functionality. (positive scenario)
        :return: return test status
        Validate View Alert Counts
        """
        print("\n------------------ VIEW ALERT COUNTS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        regionCode = "US"
        countryCode = "India"
        engineType = "2"
        model = "ThunderX"
        year = "2022"
        variant = ""

        # Call vehicle reusable module
        viewAlertCounts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, "valid")

        print("\n------------------------------END------------------------------\n")

    def test6_view_nonDTC_alert_details_for_vehicle(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the ViewNonDTCAlertDetailsForVehicle API functionality. (positive scenario)
        :return: return test status
        Validate ViewNonDTCAlertDetailsForVehicle
        """
        print("\n------------------ VIEW NON-DTC ALERT DETAILS FOR VEHICLES ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)

        systemId = read_vehicleJsonFile(self, "system_id")


        viewNonDTCAlertDetailsForVehicle(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")

    def test7_view_DTC_alert_details_for_vehicle(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the ViewDTCAlertDetailsForVehicle API functionality. (positive scenario)
        :return: return test status
        Validate ViewDTCAlertDetailsForVehicle
        """
        print("\n------------------ VIEW DTC ALERT DETAILS FOR VEHICLES ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")


        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")


        viewDTCAlertDetailsForVehicle(self, cloudEnv, systemId, "valid")


        print("\n------------------------------END------------------------------\n")

    def test8_view_vehicle_details_with_alerts(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the ViewVehicleDetailsWithAlerts API functionality. (positive scenario)
        :return: return test status
        Validate ViewVehicleDetailsWithAlerts
        """
        print("\n------------------ VIEW VEHICLE DETAILS WITH ALERTS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        regionCode = "US"
        countryCode = "India"
        engineType = "2"
        model = "ThunderX"
        year = "2022"
        variant = ""

        # Call vehicle reusable module
        viewVehicleDetailsWithAlerts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, "valid")


        print("\n------------------------------END------------------------------\n")

    def test9_view_dtc_time_series_counts(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the viewDtcTimeSeriesCounts API functionality. (positive scenario)
        :return: return test status
        Validate viewDtcTimeSeriesCounts
        """
        print("\n------------------ VIEW DTC TIME SERIES COUNTS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        regionCode = "null"
        countryCode = "null"
        engineType = "null"
        model = "null"
        year = "null"
        variant = ""

        # Call vehicle reusable module
        viewDtcTimeSeriesCounts(self, cloudEnv, regionCode, countryCode, engineType, model, year, variant, "valid")

        print("\n------------------------------END------------------------------\n")

    def test10_get_trip_details(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the getTripDetails API functionality. (positive scenario)
        :return: return test status
        Validate getTripDetails
        """
        print("\n------------------ TRIP DETAILS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")


        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        getTripDetails(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")

    def test11_get_trip_replay_details_with_pagination(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the getTripReplayDetailsWithPagination API functionality. (positive scenario)
        :return: return test status
        Validate getTripReplayDetailsWithPagination
        """
        print("\n------------------ TRIP REPLAY DETAILS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")


        # Call vehicle reusable module
        getTripReplayDetailsWithPagination(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")

    def test12_get_trip_replay_details(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the getTripReplayDetails API functionality. (positive scenario)
        :return: return test status
        Validate getTripReplayDetails
        """
        print("\n------------------ TRIP REPLAY DETAILS ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        # Call vehicle reusable module
        getTripReplayDetails(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")

    def test13_delete_trip(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the delete trip API functionality. (positive scenario)
        :return: return test status
        Validate delete trip
        """
        print("\n------------------ DELETE TRIP ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")

        # Call vehicle reusable module
        deleteTrip(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")

    def test14_geofences_by_systemId(self):
        print("\n------------------------------START------------------------------\n")

        """
        This test is validating the getGeoFencesBySystemId API functionality. (positive scenario)
        :return: return test status
        Validate getGeoFencesBySystemId
        """
        print("\n------------------ GEOFENCES BY SYSTEMID ------------------\n")

        print("----------------------------------------------------------")
        utc_time = datetime.now()
        dt = utc_time.strftime("%Y-%m-%d_%H_%M")
        dt1 = utc_time.strftime("%Y-%m-%d_%H")
        print("Current date & time :", dt)
        print("----------------------------------------------------------")

        cloudEnv = read_cloud_env(self)
        systemId = read_vehicleJsonFile(self, "system_id")
        # systemId = "q58IrcZVHv9TPqzFpJc5t"

        # Call vehicle reusable module
        getGeoFencesBySystemId(self, cloudEnv, systemId, "valid")

        print("\n------------------------------END------------------------------\n")
