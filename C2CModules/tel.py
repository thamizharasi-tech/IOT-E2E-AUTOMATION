import os
import random
import string

import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.telemetry_modules import telemetry_Curr_sensorValues, telemetry_Curr_sensorValues_VIN, \
    telemetry_Curr_sensorValues_systemIDAndVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

CurrentPath = os.path.realpath(__file__)
BaseName = os.path.basename(__file__)
Test_Case_No = BaseName.replace('.py', '')
print(Test_Case_No)

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Telemetry:

    @pytest.mark.Smoke
    def test1_positive_telmetry_curr_sensor_values_systemID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200):
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Value : ", response_body["responseData"]["dataList"][0]["value"])
            testResult(self, "passed", "Should fetch the current values successfully",
                       "Successfully fetched the current values ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the current values successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr_InvalidsystemID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_InvalidsystemID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_InvalidsystemID")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sy'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200):
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Value : ", response_body["responseData"]["dataList"][0]["value"])
            testResult(self, "passed", "Should fetch the current values successfully",
                       "Successfully fetched the current values ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the current values successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr_NullsystemID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_NullsystemID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_NullsystemID")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            if SystemId == "None":
                SystemId = ''
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = ''
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200):
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Value : ", response_body["responseData"]["dataList"][0]["value"])
            testResult(self, "passed", "Should fetch the current values successfully",
                       "Successfully fetched the current values ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the current values successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr_mismatchingeventtype&ID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_mismatchingeventTypeAndID(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_mismatchingeventtype&ID")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 291504903
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200):
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Value : ", response_body["responseData"]["dataList"][0]["value"])
            testResult(self, "passed", "Should fetch the current values successfully",
                       "Successfully fetched the current values ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the current values successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr_mismatchingeventtype&Name
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_mismatchingeventTypeAndName(self):
        print("----------------------------------------------------------")
        testCaseName = "delid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_mismatching event TypeAndName")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'abc576'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(15548):
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            assert message == "Given names are not valid"
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr_empty_xrequestor
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,"empty_x-requestor")
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["message"] == "x-requestor header cannot be blank"

    # telemetry_curr_no_xrequestor
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,"no_x-requestor")
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["message"] == "Required authentication headers are missing"

    # telemetry_curr_Invalid_APIKey
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_Invalid_APIKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,"invalid_apiKey")
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

    # telemetry_curr_Empty_APIKey
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_Empty_APIKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,"empty_apiKey")
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["message"] == "api keys are not matching. Please provide valid key"

    # telemetry_curr_Without_APIKey
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_Without_APIKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,"no_apiKey")
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["message"] == "Required authentication headers are missing"

    # telemetry_curr_idmorethan15
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_idmorethan15(self):
        print("----------------------------------------------------------")
        testCaseName = "id15"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = [random.randint(111111111, 999999999) for _ in range(16)]
            print(id)
            print('\n')

            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 557847377, 291504901, 559940097, 559940098, 559943685, 559942149, 291504904, 291504903, 291504644, 559940100, 320865540, 373295872, 291504647, 322964416, 320867268, 289408009, 339739916
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        assert response_body["responseData"]["message"] == "Element Id size should not be more than 15"

    # telemetry_curr_withoutSystemID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_WithoutSystemID(self):
        print("----------------------------------------------------------")
        testCaseName = "no_SystemId"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "SystemId or VIN is mandatory"

    # telemetry_curr_only eventtype
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_onlyEventType(self):
        print("----------------------------------------------------------")
        testCaseName = "EventType"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_only eventtype null
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_onlyEventType_null(self):
        print("----------------------------------------------------------")
        testCaseName = "EventType"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_nullEventtype")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            if eventType == "None":
                eventType = ''
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = ''
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_only eventtype INVALID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_onlyEventType_Invalid(self):
        print("----------------------------------------------------------")
        testCaseName = "EventType"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_InvalidEventtype")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 1
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_Valid eventtype and null ID
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_ValideventTypeAndNullId(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_Valid event TypeAndNull ID")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            if id == "None":
                id = ''
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = ''
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_Valid eventtype and null Name
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_ValideventTypeAndNullname(self):
        print("----------------------------------------------------------")
        testCaseName = "delid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_Valid event TypeAndNullName")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])
            if name == "None":
                name = ''


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = '559940097'
            name = ''

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_mismatching eventtype and Name
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_MismatchingeventTypeAndname(self):
        print("----------------------------------------------------------")
        testCaseName = "delid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_mismatching event TypeAndName")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = '559940097'
            name = 'abc'

        # Call api reusable module
        response = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Given names are not valid"

    # telemetry_curr_withvin
    @pytest.mark.Smoke
    def test1_positive_telmetry_curr_sensor_values_WithVIN(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = 'VINQCOMIVI0001848'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues_VIN(self, vin, eventType, id, name, testCaseName)
        response_body = response.json()

        assert (response.status_code == 200), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Successfully fetched the current values"

    # telemetry_curr_Invalid_vin
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_Invalid_VIN(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_Invalid_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = 'VINQCOMIVI000'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues_VIN(self, vin, eventType, id, name, testCaseName)
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Given vin is not valid"

    # telemetry_curr_Null_vin
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_Null_VIN(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_Null_VIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            vin = str(dict1["vin"])
            if vin == "None":
                vin = ''
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = ''
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues_VIN(self, vin, eventType, id, name, testCaseName)
        response_body = response.json()

        assert (response.status_code == 500), "Status code is not 500. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"] == None

    # telemetry_curr_IDs&Name_Together
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_IDsAndNameTogether(self):
        print("----------------------------------------------------------")
        testCaseName = "IDAndName"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_ID&NameTogether")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = 'VINQCOMIVI0001848'
            eventType = 3101
            id = 559940097
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues_VIN(self, vin, eventType, id, name, testCaseName)
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "Element ids and element names cannot be given together"

    # telemetry_curr_ VIN & System ID
    @pytest.mark.Smoke
    def test1_positive_telmetry_curr_sensor_values_VINaNDSystemID(self):
        print("----------------------------------------------------------")
        testCaseName = "abc"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues_VIN&SystemIDTogether")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            name = str(dict1["name"])



        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            vin = 'VINQCOMIVI0001848'
            eventType = 3101
            id = '559940097'
            name = 'latitude'

        # Call api reusable module
        response = telemetry_Curr_sensorValues_systemIDAndVIN(self, SystemId, vin, eventType, id, name,testCaseName)
        response_body = response.json()

        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        assert response_body["responseData"]["message"] == "SystemId and VIN cannot be given together"

    # telemetry_curr_namemorethan15
    @pytest.mark.Smoke
    def test1_negative_telmetry_curr_sensor_values_namemorethan15(self):
        print("----------------------------------------------------------")
        testCaseName = "name15"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])
            eventType = str(dict1["eventType"])
            id = str(dict1["elementId"])
            print(id)
            print('\n')

            chars = string.ascii_lowercase
            name = [random.choice(chars) for _ in range(16)]


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = 'sys19581604a96811eeba9b'
            eventType = 3101
            id = 557847377, 291504901, 559940097, 559940098, 559943685, 559942149, 291504904, 291504903, 291504644, 559940100, 320865540, 373295872, 291504647, 322964416, 320867268, 289408009, 339739916
            name = 'latitude'

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, eventType, id, name,testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        assert response_body["responseData"]["message"] == "Element Name size should not be more than 15"
