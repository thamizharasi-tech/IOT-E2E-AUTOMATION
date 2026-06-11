import json
import random

import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.geofence import Geofence_createGeofence, Geofence_updateGeofence, Geofence_deleteGeofence, \
    Geofence_getGeofences
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Geofence:

    # geofence_createGeofence
    @pytest.mark.Smoke
    def test1_positive_geofence_createGeofence(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Location Saved Successfully!":
            geoId = response_body["responseData"]["geoId"]
            # message = response_body["responseData"]["message"]
            print('Geofence Id : ', geoId)
            # print('Message : ', message)
            testResult(self, "passed", "New geofence should be created successfully",
                       "New geofence is created successfully ")
        elif response_body["message"] != "Location Saved Successfully!":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "New geofence should be created successfully ",
                       "New geofence is not created " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # geofence_createGeofence
    @pytest.mark.Smoke
    def test2_positive_geofence_updateGeofence(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])
            if geoId == "NA":
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["geoId"]
                print('Geofence Id : ', geoId)


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1, poiFlag, tag, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Location updated Successfully!":
            geoId = response_body["responseData"]["geoId"]
            # message = response_body["responseData"]["message"]
            print('Geofence Id : ', geoId)
            # print('Message : ', message)
            testResult(self, "passed", "Geofence should be updated successfully",
                       "Geofence is updated successfully ")
        elif response_body["message"] != "Location updated Successfully!":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Geofence should be updated successfully ",
                       "Failed to update geofence " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Geofence_deleteGeofence
    @pytest.mark.Smoke
    def test3_positive_geofence_deleteGeofence(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])
            if geoId:
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["geoId"]
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

            # Call api reusable module
            response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "valid")

            # Parse API response into JSON
            response_body = response.json()

            # Validate response body
            if response_body["message"] == "Location Saved Successfully!":
                geoId = response_body["responseData"]["geoId"]
            else:
                # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
                dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
                api_resp = str(dict1["Actual API Response"])
                # print(api_resp)
                json_object = json.loads(api_resp)
                geoId = json_object["responseData"]["geoId"]

        print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Geofence should be deleted successfully",
                       "Geofence is deleted successfully ")
        elif response_body["message"] != "Success":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Geofence should be deleted successfully ",
                       "Failed to delete the geofence " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Geofence_getGeofenceList
    @pytest.mark.Smoke
    def test4_positive_geofence_getGeofenceList(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Success":
            testResult(self, "passed", "Geofence list should be fetched successfully",
                       "Geofence list is fetched successfully ")
        elif response_body["message"] != "Success":
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Geofence list should be fetched successfully ",
                       "Failed to fetch the geofence list " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # New Test Scripts
    #   5 - invalid geometry type
    @pytest.mark.Smoke
    def test5_negative_geofence_createGeofence_invalid_geometryType(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_geo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15512" and response_body["message"] == "Geometry type is not valid":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 6 null geometry type
    def test6_negative_geofence_createGeofence_null_geometryType(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_null_geo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            if geometryType == "None":
                geometryType = ' '
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15503" and response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 7 null geometry type
    def test7_negative_geofence_createGeofence_no_geometryType(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_null_geo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_geometryType")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15503" and response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 8 null name
    def test8_negative_geofence_createGeofence_null_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_null_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            if name == "None":
                name = ''
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15502" and response_body[
            "responsemessage"] == "Name cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 9 invalid name with special characters
    def test9_negative_geofence_createGeofence_invalid_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15528" and response_body[
            "responsemessage"] == "Name contains special characters":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 10 invalid name with special characters

    def test10_negative_geofence_createGeofence_no_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15502" and response_body[
            "responsemessage"] == "Name cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 11   invalid radius change from 50 -5000
    def test11_negative_geofence_createGeofence_invalid_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_radius")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            if lat == "None":
                lat = ''
            long = str(77.22751858264235)
            if long == "None":
                long = ''
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15540" and response_body[
            "message"] == "Radius must be in the range 50m to 50000m":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 12   null radius

    def test12_negative_geofence_createGeofence_null_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = ""
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = ""
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15513" and response_body[
            "message"] == "Radius is mandatory for circle":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 13   without radius

    def test13_negative_geofence_createGeofence_no_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = ""
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_radius")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15513" and response_body[
            "message"] == "Radius is mandatory for circle":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 14  invalid longitude
    def test14_negative_geofence_createGeofence_invalid_long(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(776367362)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15511" and response_body[
            "message"] == "the long must be between -180 to 180 degrees":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 15  null longitude
    def test15_negative_geofence_createGeofence_null_long(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = ""
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15509" and response_body[
            "message"] == "long cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 16  no longitude
    def test16_negative_geofence_createGeofence_no_coordinates(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = ""
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_coordinates")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15504" and response_body[
            "responsemessage"] == "coordinates array should not be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 17  null longitude
    def test17_negative_geofence_createGeofence_null_lat(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            long = str(dict1["coordinates-long"])
            lat = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = ""
            long = str(28.61370736476138)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15508" and response_body[
            "message"] == "lat cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    ##print(response.status_code)

    # 18 invalid longitude
    def test18_negative_geofence_createGeofence_invalid_lat(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_lat")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = 2861370736476138
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15510" and response_body[
            "message"] == "the lat must be between -90 to 90 degrees":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    #   19 - invalid geometry type
    @pytest.mark.Smoke
    def test19_negative_geofence_createGeofence_invalid_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_type")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circlet"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = '%^%Y'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if "errorCode" in str(response_body):
            if response_body["errorCode"] == "15527" and response_body[
                "message"] == "Invalid value for type field":
                assert True
        elif "responseCode" in str(response_body):
            if response_body["responseCode"] == "15530" and response_body[
                "responsemessage"] == "Tag contains special characters":
                assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    #   20 - invalid geometry type
    @pytest.mark.Smoke
    def test20_negative_geofence_createGeofence_null_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = ""
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = ""
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15503" and response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

        #   21 - invalid geometry type

    @pytest.mark.Smoke
    def test21_negative_geofence_createGeofence_no_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_type")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = ""
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = ""
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_type")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if "15503" in response_body["responseCode"] and "Geometry type cannot be null or empty" in response_body[
            "responsemessage"]:
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test22_negative_geofence_createGeofence_no_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_IsActive")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15505" and response_body["responsemessage"] == "isActive cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test23_negative_geofence_createGeofence_null_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = ""
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = ''
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15505" and response_body["responsemessage"] == "isActive cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test24_negative_geofence_createGeofence_invalid_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test25_negative_geofence_createGeofence_no_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_tolerance")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test26_negative_geofence_createGeofence_null_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = ""
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test27_negative_geofence_createGeofence_invalid_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_tolerance")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("A")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test28_negative_geofence_createGeofence_no_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_poiFlag")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test29_negative_geofence_createGeofence_null_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = ""
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = ''
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Skip
    def test30_negative_geofence_createGeofence_invalid_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_poiFlag")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("A")
            type1 = 'PERSONAL'
            poiFlag = 'False1'
            tag = 'office'

        poiFlag = '%^1'
        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test31_negative_geofence_createGeofence_no_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_tag")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test32_negative_geofence_createGeofence_null_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = ''

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test33_negative_geofence_createGeofence_invalid_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence_invalid_tag")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("A")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = '$% ^&'

        tag = '$% ^&'
        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15530" and response_body[
            "responsemessage"] == "Tag contains special characters":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    #  13 geofence invalid header
    @pytest.mark.Smoke
    def test34_negative_geofence_createGeofence_invalid_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "invalid_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    #  14 geofence null api key header
    @pytest.mark.Smoke
    def test35_negative_geofence_createGeofence_empty_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "empty_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 15 geofence no api key header
    @pytest.mark.Smoke
    def test36_negative_geofence_createGeofence_no_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_apiKey")

        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 16 geofence empty_x-requestor key header
    @pytest.mark.Smoke
    def test37_negative_geofence_createGeofence_empty_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "empty_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False
        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "x-requestor header cannot be blank"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    #  17 geofence no_x-requestor key header
    @pytest.mark.Smoke
    def test38_negative_geofence_createGeofence_no_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_createGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'

        # Call api reusable module
        response = Geofence_createGeofence(self, name, geometryType, radius, long, lat, isActive, tolerance, type1,
                                           poiFlag, tag, "no_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)
        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    ################     UPDATE API  #########################

    #  18 geofence invalid header
    @pytest.mark.Smoke
    def test39_negative_geofence_updateGeofence_invalid_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive,
                                           tolerance, type1, poiFlag, tag, "invalid_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    #  19 geofence null api key header
    @pytest.mark.Smoke
    def test40_negative_geofence_updateGeofence_empty_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, name, geoId, geometryType, radius, long, lat, isActive,
                                           tolerance, type, poiFlag, tag, "empty_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 20 geofence no api key header
    @pytest.mark.Smoke
    def test41_negative_geofence_updateGeofence_no_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive,
                                           tolerance, type, poiFlag, tag, "no_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 21 geofence empty_x-requestor key header
    @pytest.mark.Smoke
    def test42_negative_geofence_updateGeofence_empty_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive,
                                           tolerance, type, poiFlag, tag, "empty_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "x-requestor header cannot be blank"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 22 geofence no_x-requestor key header
    @pytest.mark.Smoke
    def test43_negative_geofence_updateGeofence_no_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive,
                                           tolerance, type, poiFlag, tag, "no_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

    print("----------------------------------------------------------")

    # 23 geofence_updateGeofence with invalid name
    @pytest.mark.Smoke
    def test44_negative_geofence_updateGeofence_invalid_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)
        response_body = response.json()
        if response.status_code != 400:
            assert False
        if response_body["responseCode"] == str(15528) or response_body[
            "responsemessage"] == "Name contains special characters":
            assert True
        else:
            assert False

    print("----------------------------------------------------------")

    # 24 geofence_updateGeofence with null name
    @pytest.mark.Smoke
    def test45_negative_geofence_updateGeofence_null_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_null_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            if name == "None":
                name = ' '
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)
        response_body = response.json()
        if response.status_code != 400:
            assert False
        if response_body["responseCode"] == str(15502) or response_body[
            "responsemessage"] == "Name cannot be null or empty":
            assert True
        else:
            assert False

    print("----------------------------------------------------------")

    # 25 geofence_updateGeofence with  invalid geometry type
    @pytest.mark.Smoke
    def test46_negative_geofence_updateGeofence_invalid_geo(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_geo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False

        response_body = response.json()

        if response_body["errorCode"] == str(15512) or response_body["message"] == "Geometry type is not valid":
            assert True
        else:
            assert False

    print("----------------------------------------------------------")

    # 26 geofence_updateGeofence with null geometry type
    @pytest.mark.Smoke
    def test47_negative_geofence_updateGeofence_null_geo(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_null_geo")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            if geometryType == "None":
                geometryType = ' '
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False

        response_body = response.json()

        if response_body["responseCode"] == str(15503) or response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            assert False

    print("----------------------------------------------------------")

    # 27 geofence_updateGeofence with invalid radius
    @pytest.mark.Smoke
    def test48_negative_geofence_updateGeofence_invalid_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_radius")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False

        response_body = response.json()

        if response_body["errorCode"] == str(15540) or response_body[
            "message"] == "Radius must be in the range 50m to 50000m":
            assert True
        else:
            assert False

        print("----------------------------------------------------------")

    # 10  invalid longitude
    def test49_negative_geofence_updateGeofence_invalid_long(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(87234238483274823)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        print(geoId)
        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15511" and response_body[
            "message"] == "the long must be between -180 to 180 degrees":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 29 geofence_updateGeofence with invalid type feild
    @pytest.mark.Smoke
    def test50_negative_geofence_updateGeofence_invalid_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_type")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            long = str(dict1["coordinates-long"])
            if long == "None":
                long = ' '
            lat = str(dict1["coordinates-lat"])
            if lat == "None":
                lat = ''
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False

        response_body = response.json()

        if response_body["errorCode"] == str(15527) or response_body["message"] == "Invalid value for type field":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 30 geofence_updateGeofence with tag feild with special chracters
    @pytest.mark.Smoke
    def test51_negative_geofence_updateGeofence_invalid_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_tag")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            long = str(dict1["coordinates-long"])
            if long == "None":
                long = ' '
            lat = str(dict1["coordinates-lat"])
            if lat == "None":
                lat = ''
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = 500
            lat = 28.61370736476138
            long = 77.22751858264235
            isActive = 'True'
            tolerance = 0
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'home'

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1, poiFlag, tag, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False
        response_body = response.json()
        if response_body["responseCode"] == str(15530) or response_body[
            "responsemessage"] == "Tag contains special characters":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 7 null geometry type
    def test52_negative_geofence_updateGeofence_no_geometryType(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_geometryType")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15503" and response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 10 invalid name with special characters
    def test53_negative_geofence_updateGeofence_no_name(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_name")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15502" and response_body[
            "responsemessage"] == "Name cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 12   null radius
    def test54_negative_geofence_updateGeofence_null_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = ""
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = ""
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15513" and response_body[
            "message"] == "Radius is mandatory for circle":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 13   without radius
    def test55_negative_geofence_updateGeofence_no_radius(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = ""
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_radius")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15513" and response_body[
            "message"] == "Radius is mandatory for circle":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 15  null longitude
    def test56_negative_geofence_updateGeofence_null_long(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = ""
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15509" and response_body[
            "message"] == "long cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 16  no longitude
    def test57_negative_geofence_updateGeofence_no_coordinates(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = ""
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_coordinates")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15504" and response_body[
            "responsemessage"] == "coordinates array should not be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 17  null longitude
    def test58_negative_geofence_updateGeofence_null_lat(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_long")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            long = str(dict1["coordinates-long"])
            lat = ""
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = ""
            long = str(28.61370736476138)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")
        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15508" and response_body[
            "message"] == "lat cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 18 invalid longitude
    def test59_negative_geofence_updateGeofence_invalid_lat(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_lat")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = 2861370736476138
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["errorCode"] == "15510" and response_body[
            "message"] == "the lat must be between -90 to 90 degrees":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    #   19 - invalid geometry type
    @pytest.mark.Smoke
    def test60_negative_geofence_updateGeofence_invalid_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_type")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circlet"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = '%^%Y'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if "errorCode" in str(response_body):
            if response_body["errorCode"] == "15527" and response_body[
                "message"] == "Invalid value for type field":
                assert True
        elif "responseCode" in str(response_body):
            if response_body["responseCode"] == "15530" and response_body[
                "responsemessage"] == "Tag contains special characters":
                assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    #   20 - invalid geometry type
    @pytest.mark.Smoke
    def test61_negative_geofence_updateGeofence_null_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = ""
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = ""
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15503" and response_body[
            "responsemessage"] == "Geometry type cannot be null or empty":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

        #   21 - invalid geometry type

    @pytest.mark.Smoke
    def test62_negative_geofence_updateGeofence_no_type(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_type")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = ""
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = ""
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_type")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if "15503" in response_body["responseCode"] and "Geometry type cannot be null or empty" in response_body[
            "responsemessage"]:
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test63_negative_geofence_updateGeofence_no_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_IsActive")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15505" and response_body["responsemessage"] == "isActive cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test64_negative_geofence_updateGeofence_null_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = ""
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = ''
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["responseCode"] == "15505" and response_body["responsemessage"] == "isActive cannot be null":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test65_negative_geofence_updateGeofence_invalid_IsActive(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str(0)
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test66_negative_geofence_updateGeofence_no_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_tolerance")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test67_negative_geofence_updateGeofence_null_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = ""
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test68_negative_geofence_updateGeofence_invalid_tolerance(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_tolerance")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("A")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test69_negative_geofence_updateGeofence_no_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_poiFlag")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test70_negative_geofence_updateGeofence_null_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = ""
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = ''
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Skip
    def test71_negative_geofence_updateGeofence_invalid_poiFlag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_poiFlag")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("A")
            type1 = 'PERSONAL'
            poiFlag = 'False1'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        poiFlag = '%^1'
        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test72_negative_geofence_updateGeofence_no_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = str(dict1["tag"])
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = str("0")
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = 'office'
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "no_tag")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test73_negative_geofence_updateGeofence_null_tag(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_updateGeofence_invalid_IsActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            name = str(dict1["GeofenceName"])
            geometryType = str(dict1["geometryType"])
            radius = str(dict1["radius"])
            lat = str(dict1["coordinates-lat"])
            long = str(dict1["coordinates-long"])
            isActive = str(dict1["isActive"])
            tolerance = str(dict1["tolerance"])
            type1 = str(dict1["type"])
            poiFlag = str(dict1["poiFlag"])
            tag = ""
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            msg_id = ' '.join([str(random.randint(10, 9999)).zfill(6) for _ in range(1)])
            name = 'Geofence' + str(msg_id)
            geometryType = "circle"
            radius = str(150)
            lat = str(28.61370736476138)
            long = str(77.22751858264235)
            isActive = 'True1'
            tolerance = ""
            type1 = 'PERSONAL'
            poiFlag = 'False'
            tag = ''
            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance,
                                           type1,
                                           poiFlag, tag, "invalid")

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(response.status_code)

        if response.status_code != 400:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body
        if response_body["message"] == "Json Parse Error":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # DELETE API HEADERS###################

    #  31 geofence invalid header
    @pytest.mark.Smoke
    def test74_negative_geofence_delete_Geofence_invalid_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "invalid_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    #  32 geofence null api key header
    @pytest.mark.Smoke
    def test75_negative_geofence_deleteGeofence_empty_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "empty_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 33 geofence no api key header
    @pytest.mark.Smoke
    def test76_negative_geofence_deleteGeofence_no_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "no_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 34 geofence empty_x-requestor key header
    @pytest.mark.Smoke
    def test77_negative_geofence_deleteGeofence_empty_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "empty_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "x-requestor header cannot be blank"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 35 geofence no_x-requestor key header
    @pytest.mark.Smoke
    def test78_positive_geofence_deleteGeofence_no_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

            # Read geofence Id from Geofence_createGeofence api resp from Excel sheet
            dict1 = read_api_data_from_excel(self, "API_Data", "Geofence_createGeofence")
            api_resp = str(dict1["Actual API Response"])
            # print(api_resp)
            json_object = json.loads(api_resp)
            geoId = json_object["responseData"]["geoId"]
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "no_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 36 geofence_deleteGeofence with invalid name
    @pytest.mark.Smoke
    def test79_negative_geofence_deleteGeofence_invalid_geoId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence_invalid_name")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = str(dict1["geoId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            geoId = "65$7"
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "invalid")

        assert response.status_code == 400, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 400:
            assert False

        response_body = response.json()

        if response_body["errorCode"] == str(15514) or response_body[
            "responsemessage"] == "Given geoid is not present in the database":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    # 36 geofence_deleteGeofence with invalid name
    @pytest.mark.Smoke
    def test80_negative_geofence_deleteGeofence_null_geoId(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_deleteGeofence")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            geoId = ""

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            geoId = ""
            print('Geofence Id : ', geoId)

        # Call api reusable module
        response = Geofence_deleteGeofence(self, geoId, "invalid")

        assert response.status_code == 405, "Status code is not 400. rather found" + str(response.status_code)

        if response.status_code != 405:
            assert False

        response_body = response.json()

        if response_body["status"] == str(405) or response_body[
            "error"] == "Method Not Allowed":
            assert True
        else:
            print("Something went wrong or response/error code & message is not as expected")
            assert False

        print("----------------------------------------------------------")

    ##################      GET API HEADERS###################
    # 37 get geofence

    @pytest.mark.Smoke
    def test81_negative_geofence_get_Geofence_invalid_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "invalid_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    #  38 geofence null api key header
    @pytest.mark.Smoke
    def test82_negative_geofence_getGeofence_empty_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "empty_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 39 geofence no api key header
    @pytest.mark.Smoke
    def test83_negative_geofence_getGeofence_no_apikey(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "no_apiKey")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 40 geofence empty_x-requestor key header
    @pytest.mark.Smoke
    def test84_negative_geofence_deleteGeofence_empty_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "empty_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "x-requestor header cannot be blank"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")

    # 40 geofence n without x-requestor key header
    @pytest.mark.Smoke
    def test85_negative_geofence_deleteGeofence_no_x(self):

        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Geofence", "Geofence_getGeofences")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")

        # Call api reusable module
        response = Geofence_getGeofences(self, "no_x-requestor")
        response_body = response.json()
        # Validate response status code
        assert (
                response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        if response.status_code != 403:
            assert False

        # Parse API response into JSON
        response_body = response.json()

        assert response_body["message"] == "Required authentication headers are missing"

        ##print("----------------Api key mismatch------------------------------------------")

        print("----------------------------------------------------------")
