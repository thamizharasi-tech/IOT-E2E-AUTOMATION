import json

import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.telemetry_location import TelemetryLocation_assignGeofenceToVehicle, Telemetry_Location_bySystemId, \
    Telemetry_Location_byGeofenceId, Telemetry_Location_byGeoIdGefoNameIsActive, \
    Telemetry_Location_updateLocationForVehicle, Telemetry_Location_nearestPOIlocation
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_TelemetryLocation:

    # TelemetryLocation_assignGeofenceToVehicle
    @pytest.mark.Smoke
    def test1_positive_TelemetryLocation_assignGeofenceToVehicle(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "TelemetryLocation_assignGeofenceToVehicle")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            geoId = str(dict1["geoId"])
            notification = str(dict1["notification"])
            isEdgeEnabled = str(dict1["isEdgeEnabled"])
            ruleId = str(dict1["ruleId"])
            isActive = str(dict1["isActive"])
            ruleExpression = str(dict1["ruleExpression"])
            systemId = str(dict1["systemId"])
            if geoId == 'NA':
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["id"]
                print('Geofence Id : ', geoId)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["id"]
            print('Geofence Id : ', geoId)

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            notification = 3
            isEdgeEnabled = 0
            ruleId = 0
            isActive = 'true'
            ruleExpression = "speed>50"

        # Call api reusable module
        response_body = TelemetryLocation_assignGeofenceToVehicle(self, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                              ruleExpression, systemId, "valid")

        if response_body["message"] == "Success":
            geoId = response_body["responseData"]["id"]
            message = response_body["responseData"]["message"]
            print('Geofence Id : ', geoId)
            print('Message : ', message)
            testResult(self, "passed", "Geofence should be mapped to Vehicle successfully",
                       "Geofence is mapped to Vehicle successfully ")
        elif response_body["message"] != "Success":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Geofence should be mapped to Vehicle successfully ",
                       "Failed to mapped Geofence to Vehicle " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry_Location_bySystemId
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Location_bySystemId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "Telemetry_Location_bySystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)


        # Call api reusable module
        response_body = Telemetry_Location_bySystemId(self, systemId,"valid")

        if response_body["message"] == 'Success':
            testResult(self, "passed", "Geofence should be listed successfully",
                       "Geofence is listed successfully ")
        elif response_body["message"] != 'Success':
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Geofence should be listed successfully ",
                       "Failed to list geofence " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry_Location_byGeofenceId
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Location_byGeofenceId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "Telemetry_Location_byGeofenceId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])
            if geoId == 'NA':
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["id"]
                print('Geofence Id : ', geoId)

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["id"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response_body = Telemetry_Location_byGeofenceId(self, geoId, "valid")

        # if response_body["responseCode"] == str(1200):
        #     geoId = response_body["responseData"]["id"]
        #     message = response_body["responseData"]["message"]
        #     print('Geofence Id : ', geoId)
        #     print('Message : ', message)
        #     testResult(self, "passed", "Geofence should be deleted successfully",
        #                "Geofence is deleted successfully ")
        # elif response_body["responseCode"] != str(1200):
        #     # print(response_body["responseData"]["message"])
        #     testResult(self, "failed", "Geofence should be deleted successfully ",
        #                "Failed to delete the geofence " + " Reason for failure is : " +
        #                response_body["responseData"]["message"])
        # else:
        #     print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry_Location_byGeoIdGefoNameIsActive
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Location_byGeoIdGefoNameIsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "Telemetry_Location_byGeoIdGefoNameIsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])
            geoName = str(dict1["GeofenceName"])
            isActive = str(dict1["isActive"])

            if geoId == 'NA':
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["id"]
                print('Geofence Id : ', geoId)
        
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["id"]
            geoName = str(dict1["GeofenceName"])
            isActive = 'true'
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response_body = Telemetry_Location_byGeoIdGefoNameIsActive(self, geoId, geoName, isActive,"valid")

        # if response_body["responseCode"] == str(1200):
        #     geoId = response_body["responseData"]["id"]
        #     message = response_body["responseData"]["message"]
        #     print('Geofence Id : ', geoId)
        #     print('Message : ', message)
        #     testResult(self, "passed", "Geofence should be deleted successfully",
        #                "Geofence is deleted successfully ")
        # elif response_body["responseCode"] != str(1200):
        #     # print(response_body["responseData"]["message"])
        #     testResult(self, "failed", "Geofence should be deleted successfully ",
        #                "Failed to delete the geofence " + " Reason for failure is : " +
        #                response_body["responseData"]["message"])
        # else:
        #     print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry_Location_updateLocationForVehicle
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Location_updateLocationForVehicle(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Location", "Telemetry_Location_updateLocationForVehicle")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])
            systemId = str(dict1["systemId"])
            notification = str(dict1["notification"])
            isEdgeEnabled = str(dict1["isEdgeEnabled"])
            ruleId = str(dict1["ruleId"])
            ruleExpression = str(dict1["ruleExpression"])
            vehicleStatus = str(dict1["vehicleStatus"])
            isActive = str(dict1["isActive"])

            if geoId == 'NA':                                                                     
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet         
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")     
                api_resp = str(dict1["Actual API Response"])                                      
                # print(api_resp)                                                                 
                json_object = json.loads(api_resp)                                                
                geoId = json_object["responseData"]["id"]                                         
                print('Geofence Id : ', geoId)                                                    
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["id"]
            isActive = 'true'
            notification = 0
            isEdgeEnabled = 0
            ruleId = 0
            ruleExpression = "speed>30"
            vehicleStatus =1

            systemId = get_SystemId(self, OnboardingType, chipsetType)

            print('Geofence Id : ', geoId)

        # Call api reusable module
        response_body = Telemetry_Location_updateLocationForVehicle(self, systemId, geoId, notification, isEdgeEnabled, ruleId, isActive,
                                                ruleExpression, vehicleStatus, "valid")

        # if response_body["responseCode"] == str(1200):
        #     geoId = response_body["responseData"]["id"]
        #     message = response_body["responseData"]["message"]
        #     print('Geofence Id : ', geoId)
        #     print('Message : ', message)
        #     testResult(self, "passed", "Geofence should be deleted successfully",
        #                "Geofence is deleted successfully ")
        # elif response_body["responseCode"] != str(1200):
        #     # print(response_body["responseData"]["message"])
        #     testResult(self, "failed", "Geofence should be deleted successfully ",
        #                "Failed to delete the geofence " + " Reason for failure is : " +
        #                response_body["responseData"]["message"])
        # else:
        #     print("Something went wrong")

    print("----------------------------------------------------------")

    # Telemetry_Location_nearestPOIlocation
    @pytest.mark.Smoke
    def test1_positive_Telemetry_Location_nearestPOIlocation(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
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
        response_body = Telemetry_Location_nearestPOIlocation(self, latitude, longitude, radius)

        # if response_body["responseCode"] == str(1200):
        #     geoId = response_body["responseData"]["id"]
        #     message = response_body["responseData"]["message"]
        #     print('Geofence Id : ', geoId)
        #     print('Message : ', message)
        #     testResult(self, "passed", "Geofence should be deleted successfully",
        #                "Geofence is deleted successfully ")
        # elif response_body["responseCode"] != str(1200):
        #     # print(response_body["responseData"]["message"])
        #     testResult(self, "failed", "Geofence should be deleted successfully ",
        #                "Failed to delete the geofence " + " Reason for failure is : " +
        #                response_body["responseData"]["message"])
        # else:
        #     print("Something went wrong")

    print("----------------------------------------------------------")