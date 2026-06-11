import json
import random

import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.geofence import Geofence_updateGeofence
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Geofence:
    # 7 null geometry type
    def test7_negative_geofence_updateGeofence_no_geometryType(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test10_negative_geofence_updateGeofence_no_name(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test12_negative_geofence_updateGeofence_null_radius(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test13_negative_geofence_updateGeofence_no_radius(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test15_negative_geofence_updateGeofence_null_long(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test16_negative_geofence_updateGeofence_no_coordinates(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test17_negative_geofence_updateGeofence_null_lat(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test18_negative_geofence_updateGeofence_invalid_lat(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test19_negative_geofence_updateGeofence_invalid_type(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test20_negative_geofence_updateGeofence_null_type(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test21_negative_geofence_updateGeofence_no_type(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test22_negative_geofence_updateGeofence_no_IsActive(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test23_negative_geofence_updateGeofence_null_IsActive(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test24_negative_geofence_updateGeofence_invalid_IsActive(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test25_negative_geofence_updateGeofence_no_tolerance(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test26_negative_geofence_updateGeofence_null_tolerance(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test27_negative_geofence_updateGeofence_invalid_tolerance(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test28_negative_geofence_updateGeofence_no_poiFlag(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test29_negative_geofence_updateGeofence_null_poiFlag(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test30_negative_geofence_updateGeofence_invalid_poiFlag(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test31_negative_geofence_updateGeofence_no_tag(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
    def test32_negative_geofence_updateGeofence_null_tag(self):

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
        response = Geofence_updateGeofence(self, geoId, name, geometryType, radius, long, lat, isActive, tolerance, type1,
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
