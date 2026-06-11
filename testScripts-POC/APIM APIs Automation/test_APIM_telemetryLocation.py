import json

import pytest


from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.APIM_ReusableModules import TelemetryLocation_saveVehicleLocation, TelemetryLocation_updateVehicleLocation, \
    TelemetryLocation_getVehicleLocation, TelemetryLocation_deleteVehicleLocation,Telemetry_Location_nearestPOIlocation
from C2CModules.testResults import testResult
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_smoke:

    # TelemetryLocation_saveVehicleLocation
    @pytest.mark.Smoke
    def test1_positive_TelemetryLocation_saveVehicleLocation(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "TelemetryLocation_saveVehicleLocation")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            geoId = str(dict1["geoId"])
            notification = str(dict1["notification"])
            isEdgeEnabled = str(dict1["isEdgeEnabled"])
            ruleId = str(dict1["ruleId"])
            isActive = str(dict1["isActive"])
            ruleExpression = str(dict1["ruleExpression"])
            systemId = str(dict1["systemId"])
            """if geoId == 'NA':
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["geoId"]
                print('Geofence Id : ', geoId)"""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            notification = 3
            isEdgeEnabled = 0
            ruleId = 0
            isActive = 'true'
            ruleExpression = "speed>50"

        # Call api reusable module
        response_body = TelemetryLocation_saveVehicleLocation(self, geoId, notification, isEdgeEnabled, ruleId,
                                                              isActive,
                                                              ruleExpression, systemId)

        if response_body["message"] == "Data Saved Successfully":
            vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
            # message = response_body["responseData"]["message"]
            print('Vehicle Mapping Id : ', vehicleMappingId)
            # print('Message : ', message)
            testResult(self, "passed", "Geofence should be mapped to Vehicle successfully",
                       "Geofence is mapped to Vehicle successfully ")
        elif response_body["message"] != "Location Saved Successfully for vehicle!":
            testResult(self, "failed", "Geofence should be mapped to Vehicle successfully ",
                       "Failed to mapped Geofence to Vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # TelemetryLocation_updateVehicleLocation
    @pytest.mark.Smoke
    def test2_positive_TelemetryLocation_updateVehicleLocation(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "TelemetryLocation_updateVehicleLocation")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])
            systemId = str(dict1["systemId"])
            notification = str(dict1["notification"])
            isEdgeEnabled = str(dict1["isEdgeEnabled"])
            ruleId = str(dict1["ruleId"])
            ruleExpression = str(dict1["ruleExpression"])
            name = str(dict1["name"])
            isActive = str(dict1["isActive"])

            """if geoId == 'NA':                                                                     
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet         
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")     
                api_resp = str(dict1["Actual API Response"])                                      
                # print(api_resp)                                                                 
                json_object = json.loads(api_resp)                                                
                geoId = json_object["responseData"]["geoId"]
                print('Geofence Id : ', geoId)"""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            isActive = 'true'
            notification = 0
            isEdgeEnabled = 0
            ruleId = 0
            ruleExpression = "speed>30"
            vehicleStatus = 1

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print('Geofence Id : ', geoId)

        # Call api reusable module
        response_body = TelemetryLocation_updateVehicleLocation(self, systemId, geoId, notification, isEdgeEnabled,
                                                                ruleId, isActive,
                                                                ruleExpression, name)

        if response_body["message"] == "Data Updated Successfully":
            vehicleMappingId = response_body["responseData"]["vehicleMappingId"]
            # message = response_body["responseData"]["message"]
            print('Vehicle Mapping Id : ', vehicleMappingId)
            # print('Message : ', message)
            testResult(self, "passed", "Location should be update successfully for vehicle",
                       "Location is updated successfully for vehicle ")
        elif response_body["message"] != "Location updated Successfully for vehicle!":
            testResult(self, "failed", "Location should be updated successfully for vehicle ",
                       "Failed to update location for vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # TelemetryLocation_getVehicleLocation
    @pytest.mark.Smoke
    def test3_positive_TelemetryLocation_getVehicleLocation(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "TelemetryLocation_getVehicleLocation")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call api reusable module
        response_body = TelemetryLocation_getVehicleLocation(self,systemId)

        if response_body["message"] == "Data Fetched Successfully":
            testResult(self, "passed", "Location should be fetched successfully for vehicle",
                       "Location is fetched successfully for vehicle ")
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed", "Location should be fetched successfully for vehicle ",
                       "Failed to fetch location for vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # TelemetryLocation_deleteVehicleLocation
    @pytest.mark.Smoke
    def test4_positive_TelemetryLocation_deleteVehicleLocation(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "TelemetryLocation_deleteVehicleLocation")
        vehicleMappingId = str(dict1["geoId"])
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vehicleMappingId = str(dict1["geoId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            if vehicleMappingId == 'NA':
                # Read vehicle Mapping Id from TelemetryLocation_saveVehicleLocation api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "TelemetryLocation_saveVehicleLocation")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                vehicleMappingId = json_object["responseData"]["vehicleMappingId"]
                print('Vehicle Mapping Id : ', vehicleMappingId)
                # Call api reusable module
        response_body = TelemetryLocation_deleteVehicleLocation(self, vehicleMappingId)

        if response_body["message"] == "Data Deleted Successfully":
            testResult(self, "passed", "Location should be deleted successfully for vehicle",
                       "Location is deleted successfully for vehicle ")
        elif response_body["message"] != "Success":
            testResult(self, "failed", "Location should be deleted successfully for vehicle ",
                       "Failed to delete location for vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry_Location_nearestPOIlocation
    @pytest.mark.Smoke
    def test5_positive_Telemetry_Location_nearestPOIlocation(self):

        print("----------------------------------------------------------")
        #Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "Telemetry_Location_nearestPOIlocation")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            latitude = str(dict1["coordinates-lat"])
            longitude = str(dict1["coordinates-long"])
            radius = str(dict1["radius"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            latitude = '77.23179353189641'
            longitude = '28.609184'
            radius = 2

        # Call api reusable module
        response_body = Telemetry_Location_nearestPOIlocation(self,latitude,longitude,radius,"valid")

        if response_body["message"] == "Data Fetched Successfully":
            testResult(self, "passed", "Nearest POI Location should be fectched successfully for vehicle",
                       "Nearest POI Location is fetched successfully for vehicle ")
        elif response_body["message"] != "Data Fetched Successfully":
            testResult(self, "failed", "Nearest POI Location should be fetched successfully for vehicle ",
                       "Failed to fetch Nearest POI Location for vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")





