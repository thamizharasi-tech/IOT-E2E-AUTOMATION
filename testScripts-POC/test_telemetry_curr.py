import os
import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.telemetry_modules import telemetry_Curr_sensorValues, telemetry_Curr_sensorElements, \
    telemetry_Curr_eventType, telemetry_Curr_byVIN, telemetry_Curr_byVIN_eventType, \
    telemetry_Curr_sensorElements_eventType_name, telemetry_publisher_config, Sos_Service, telemetry_metadata_details
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

CurrentPath = os.path.realpath(__file__)
BaseName = os.path.basename(__file__)
Test_Case_No = BaseName.replace('.py', '')
print(Test_Case_No)

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Telemetry:

    # telemetry_curr
    @pytest.mark.Smoke
    def test1_positive_telmetry_curr_sensor_values(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_sensorValues")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            SystemId = str(dict1["SystemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            SystemId = get_SystemId(self, OnboardingType, chipsetType)

        # Call api reusable module
        response_body = telemetry_Curr_sensorValues(self, SystemId, testCaseName)

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

    # telemetry_curr
    @pytest.mark.Smoke
    def test2_positive_telmetry_curr_sensor_elements(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, testCaseName)

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
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
            testResult(self, "passed", "Should fetch the sensor elements data successfully",
                       "Successfully fetched the sensor elements data ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the sensor elements data successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr
    @pytest.mark.Smoke
    def test3_positive_telmetry_curr_eventType(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            event_type = 3106

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

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
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking "
                           "test case as pass")

        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry_curr
    @pytest.mark.Smoke
    def test4_positive_telmetry_curr_byVIN(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_byVIN")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)

        # Call api reusable module
        response_body = telemetry_Curr_byVIN(self, vin, testCaseName)

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
                testResult(self, "passed", "Should fetch the data/values for vin successfully",
                           "Successfully fetched the values/data for desired vin ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for vin successfully",
                           "End point is working fine, but there is no data in DB for this vin, thus marking test "
                           "case as pass")

        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for vin successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry_curr
    @pytest.mark.Smoke
    def test5_positive_telmetry_curr_vinANDeventType(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Curr_byVINandEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = getVIN(self, OnboardingType, chipsetType)
            event_type = 3106

        # Call api reusable module
        response_body = telemetry_Curr_byVIN_eventType(self, event_type, vin, testCaseName)

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
                testResult(self, "passed", "Should fetch the data/values for vin & event type successfully",
                           "Successfully fetched the values/data for desired vin & event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for vin & event type successfully",
                           "End point is working fine, but there is no data in DB for this vin & event type, "
                           "thus marking test case as pass")

        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for vin & event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry sensor elements with eventType and attribute name
    @pytest.mark.Smoke
    def test6_positive_telemetry_curr_sensor_elements_eventType_AttributeName(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements_foreventTypeandName")
        if dict1['Flag'] == "Yes":
            eventType = str(dict1["eventType"])
            name = str(dict1["name"])
        else:
            eventType = "3101"
            name = "LONGITUDE"
        # Call api reusable module
        response_body = telemetry_Curr_sensorElements_eventType_name(self, eventType, name, testCaseName)

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
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
            testResult(self, "passed", "Should fetch the sensor elements data successfully",
                       "Successfully fetched the sensor elements data ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the sensor elements data successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

        # telemetry publisher config

    @pytest.mark.Smoke
    def test7_positive_telemetry_publisher_config(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200):
            assert True
        else:
            print("response Code is not 1200. Rather found : " + str(response_body["message"]))
            assert False

        print("----------------------------------------------------------")

    # SOS-Service
    @pytest.mark.Smoke
    def test8_positive_Sos_Service(self):
        print("----------------------------------------------------------")
        testCaseName = "valid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 0
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Successfully accepted and published SoS clear action":
            assert True
            testResult(self, "passed", "sos clear action should be published successfully",
                       "sos clear action published successfully")
        else:
            print("response Code is not 1200. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # telemetry Metadata details with invalid elementId
    @pytest.mark.Sanity
    def test9_positive_telemetry_Metadata(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 5599400

        print("elementId : ", elementId)
        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Successfully fetched the sensor elements data":

            datalist_len = len(response_body["responseData"]["dataList"])
            if datalist_len >= 1:
                for i in range(datalist_len):
                    print("Id :", response_body["responseData"]["dataList"][i]["id"])
                    print("Event Type :", response_body["responseData"]["dataList"][i]["eventType"])
                    print("Name :", response_body["responseData"]["dataList"][i]["name"])
                    print("Unit :", response_body["responseData"]["dataList"][i]["unit"])
                    print(elementId, response_body["responseData"]["dataList"][i]["id"])
                    if str(elementId) == str(response_body["responseData"]["dataList"][i]["id"]):
                        testResult(self, "passed", "Should fetch the Telemetry metadata details",
                                   "Telemetry metadata details are fetched for valid elementId")
            else:
                print("datalist is empty")
                testResult(self, "verificationFailed", "Should fetch the Telemetry metadata details",
                           "Telemetry metadata details are not fetched for valid elementId : data list is empty")
        elif response_body["responseCode"] != str(1200):
            testResult(self, "failed", "Should fetch the Telemetry metadata details ",
                       "Telemetry metadata details are not fetched  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    # ---------------------------------------
    # Negative validations
    # ---------------------------------------

    # telemetry sensor elements with invalid eventType
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_eventType_AttributeName_invalideventType(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry",
                                         "Telemetry_sensorElements_foreventTypeandName_invalideventType")
        if dict1['Flag'] == "Yes":
            eventType = str(dict1["eventType"])
            name = str(dict1["name"])
        else:
            eventType = "9000"
            name = "LONGITUDE"
        # Call api reusable module
        response_body = telemetry_Curr_sensorElements_eventType_name(self, eventType, name, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == 'Successfully fetched the sensor elements data':

            if response_body["responseData"]["dataList"] == []:
                testResult(self, "passed", "Should not fetch the sensor data/values for invalid eventType ",
                           "No data present for invalid eventType ")
            else:

                testResult(self, "failed", "Should not fetch the sensor data/values for invalid eventType",
                           "Data fetched successfully for provided eventType " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != 'Successfully fetched the sensor elements data':

            testResult(self, "failed", "Should not fetch the sensor data/values for invalid eventType ",
                       "Data fetched successfully for provided eventType  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry sensor elements with empty value for param eventType
    @pytest.mark.Sanity
    def test2_negative_telemetry_curr_sensor_elements_eventType_AttributeName_emptyeventType(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry",
                                         "Telemetry_sensorElements_foreventTypeandName_emptyeventType")
        if dict1['Flag'] == "Yes":
            eventType = str(dict1["eventType"])
            name = str(dict1["name"])
        else:
            eventType = ""
            name = "LONGITUDE"
        if eventType == "None":
            eventType = ""
        # Call api reusable module
        response_body = telemetry_Curr_sensorElements_eventType_name(self, eventType, name, testCaseName)

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
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
            testResult(self, "passed", "Should fetch the sensor elements data successfully",
                       "Successfully fetched the sensor elements data ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the sensor elements data successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry sensor elements with invalid attributeName
    @pytest.mark.Sanity
    def test3_negative_telemetry_curr_sensor_elements_eventType_AttributeName_invalidName(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry",
                                         "Telemetry_sensorElements_foreventTypeandName_invalidName")
        if dict1['Flag'] == "Yes":
            eventType = str(dict1["eventType"])
            name = str(dict1["name"])
        else:
            eventType = "3101"
            name = "Fuel"
        # Call api reusable module
        response_body = telemetry_Curr_sensorElements_eventType_name(self, eventType, name, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == 'Successfully fetched the sensor elements data':

            if response_body["responseData"]["dataList"] == []:
                testResult(self, "passed", "Should not fetch the sensor data/values for invalid Attribute Name ",
                           "No data present for invalid Attribute Name ")
            else:

                testResult(self, "failed", "Should not fetch the sensor data/values for invalid Attribute Name",
                           "Data fetched successfully for provided eventType and Attribute Name" + "Reason for "
                                                                                                   "failure is : " +
                           response_body["responseData"]["message"])
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != 'Successfully fetched the sensor elements data':

            testResult(self, "failed", "Should not fetch the sensor data/values for invalid Attribute Name ",
                       "Data fetched successfully for provided eventType and Attribute Name  " + "Reason for "
                                                                                                 "failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry sensor elements with empty value for param eventType
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_eventType_AttributeName_emptyName(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry",
                                         "Telemetry_sensorElements_foreventTypeandName_emptyName")
        if dict1['Flag'] == "Yes":
            eventType = str(dict1["eventType"])
            name = str(dict1["name"])
        else:
            eventType = "3101"
            name = ""
        if name == "None":
            name = ""
        # Call api reusable module
        response_body = telemetry_Curr_sensorElements_eventType_name(self, eventType, name, testCaseName)

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
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
            testResult(self, "passed", "Should fetch the sensor elements data successfully",
                       "Successfully fetched the sensor elements data ")
        elif response_body["responseCode"] != str(1200):
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the sensor elements data successfully ",
                       "Failed to fetch the current values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # Telemetry sensor element with invalid api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_invalid_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, "invalid_apiKey")

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == "api keys are not matching. Please provide valid key":

            testResult(self, "passed", "Sensor elements data should not be fetched for invalid api-key",
                       "Sensor elements data is not fetched for invalid api-key ")
        elif response_body["responseCode"] != "api keys are not matching. Please provide valid key":

            testResult(self, "failed", "Sensor elements data should not be fetched for invalid api-key ",
                       "Fetched the current values successfully " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # Telemetry sensor element with empty api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_empty_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, "empty_apiKey")

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == "api keys are not matching. Please provide valid key":

            testResult(self, "passed", "Sensor elements data should not be fetched for empty api-key",
                       "Sensor elements data is not fetched for empty api-key ")
        elif response_body["responseCode"] != "api keys are not matching. Please provide valid key":

            testResult(self, "failed", "Sensor elements data should not be fetched for empty api-key ",
                       "Fetched the current values successfully " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # Telemetry sensor element without header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_missing_apikey(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, "no_apiKey")

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == "Required authentication headers are missing":

            testResult(self, "passed", "Sensor elements data should not be fetched for missing header api-key",
                       "Sensor elements data is not fetched for missing header api-key ")
        elif response_body["responseCode"] != "Required authentication headers are missing":

            testResult(self, "failed", "Sensor elements data should not be fetched for missing header api-key ",
                       "Fetched the current values successfully " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # Telemetry sensor element with empty x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_empty_xrequestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, "empty_x-requestor")

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == "x-requestor header cannot be blank":

            testResult(self, "passed", "Sensor elements data should not be fetched for empty header x-requestor",
                       "Sensor elements data is not fetched for empty header x-requestor")
        elif response_body["responseCode"] != "x-requestor header cannot be blank":

            testResult(self, "failed", "Sensor elements data should not be fetched for empty header x-requestor ",
                       "Fetched the current values successfully " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # Telemetry sensor element without header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_sensor_elements_missing_xrequestor(self):
        print("----------------------------------------------------------")

        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_sensorElements")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            print("No data is required")
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            print("No data is required")

        # Call api reusable module
        response_body = telemetry_Curr_sensorElements(self, "no_x-requestor")

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == "Required authentication headers are missing":

            testResult(self, "passed", "Sensor elements data should not be fetched without header x-requestor",
                       "Sensor elements data is not fetched without header x-requestor")
        elif response_body["responseCode"] != "Required authentication headers are missing":

            testResult(self, "failed", "Sensor elements data should not be fetched without header x-requestor ",
                       "Fetched the current values successfully " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry_curr By eventType and invalid systemId
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_invalidSystemId(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType_invalidSystemId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sys123"
            event_type = 3106

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == 'Successfully fetched the current values':
            # message = response_body["responseData"]["message"]
            if response_body["responseData"]["dataList"] == []:
                testResult(self, "passed", "Should not fetch the data/values for invalid SystemId ",
                           "No data present for invalid SystemId ")
            else:

                testResult(self, "failed", "Should not fetch the data/values for invalid SystemId",
                           "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != 'Successfully fetched the current values':

            testResult(self, "failed", "Should not fetch the data/values for invalid SystemId ",
                       "Data fetched successfully for provided systemId  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry_curr with invalid eventType
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_invalideventType(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType_invalideventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = 0

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 200), "Status code is not 200. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == 'Successfully fetched the current values':
            # message = response_body["responseData"]["message"]
            if response_body["responseData"]["dataList"] == []:
                testResult(self, "passed", "Should not fetch the data/values for invalid SystemId ",
                           "No data present for invalid SystemId ")
            else:

                testResult(self, "failed", "Should not fetch the data/values for invalid SystemId",
                           "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                           response_body["responseData"]["message"])
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != 'Successfully fetched the current values':

            testResult(self, "failed", "Should not fetch the data/values for invalid SystemId ",
                       "Data fetched successfully for provided systemId  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # telemetry_curr with invalid header apiKey
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_invalidapiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = 3101

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == 'api keys are not matching. Please provide valid key':

            testResult(self, "passed", "Should not fetch the telemetry data/values for invalid header apiKey ",
                       "No data present for invalid invalid headers")
        elif response_body["message"] != 'api keys are not matching. Please provide valid key':

            testResult(self, "failed", "Should not fetch the telemetry data/values for invalid header apiKey",
                       "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                       response_body["message"])

        else:
            print("Something went wrong")

        print("-------------Invalid API-KEY---------------------------------------------")

    # telemetry_curr with empty header apiKey
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_emptyapiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = 3101

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == 'api keys are not matching. Please provide valid key':

            testResult(self, "passed", "Should not fetch the telemetry data/values for empty header apiKey ",
                       "No data present for empty header apiKey")
        elif response_body["message"] != 'api keys are not matching. Please provide valid key':

            testResult(self, "failed", "Should not fetch the telemetry data/values for empty header apiKey",
                       "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                       response_body["message"])

        else:
            print("Something went wrong")

        print("-------------Empty API-KEY-----------------")

    # telemetry_curr without header apiKey
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_missing_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "no_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = '3250'

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()
        print(response_body)
        if response_body["message"] == 'Required authentication headers are missing':

            testResult(self, "passed", "Should not fetch the telemetry data/values for empty header apiKey ",
                       "No data present for empty header apiKey")
        elif response_body["message"] != 'Required authentication headers are missing':

            testResult(self, "failed", "Should not fetch the telemetry data/values for empty header apiKey",
                       "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                       response_body["message"])
        else:
            print("Something went wrong")

        print("-------------Missing header API-KEY-----------------")

    # telemetry_curr with empty header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_emptyxrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = 3101

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == 'x-requestor header cannot be blank':

            testResult(self, "passed", "Should not fetch the telemetry data/values for empty header x-requestor ",
                       "No data present for empty header x-requestor")
        elif response_body["message"] != 'x-requestor header cannot be blank':

            testResult(self, "failed", "Should not fetch the telemetry data/values for empty header x-requestor",
                       "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                       response_body["message"])

        else:
            print("Something went wrong")

        print("-------------Empty x-requestor-----------------")

    # telemetry_curr without header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_curr_eventType_missing_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "no_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_CurrForEventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["SystemId"])
            event_type = str(dict1["eventType"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            # systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sysf06ba6a4b5ec11eeba9b"
            event_type = 3101

        # Call api reusable module
        response_body = telemetry_Curr_eventType(self, event_type, systemId, testCaseName)

        # Validate response status code
        assert (response_body.status_code == 400), "Status code is not 400. Rather found : " + str(
            response_body.status_code)

        # Parse API response into JSON
        response_body = response_body.json()

        if response_body["message"] == 'Required authentication headers are missing':

            testResult(self, "passed", "Should not fetch the telemetry data/values for missing header x-requestor ",
                       "No data present when header x-requestor is missing")
        elif response_body["message"] != 'Required authentication headers are missing':

            testResult(self, "failed", "Should not fetch the telemetry data/values for missing header x-requestor",
                       "Data fetched successfully for provided systemId " + " Reason for failure is : " +
                       response_body["message"])

        else:
            print("Something went wrong")

        print("-------------Missing header x-requestor-----------------")

    # telemetry Metadata details with invalid elementId
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_invalid_elementId(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details_invalid_elementId")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 5599400

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15546) and response_body["responseData"][
            "message"] == "please provide a valid sensor element id":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details",
                       "Telemetry metadata details are not fetched for invalid elementId")
        elif response_body["responseCode"] != str(15546) and response_body["responseData"][
            "message"] != "please provide a valid sensor element id":

            testResult(self, "failed", "Should fetch the Telemetry metadata details ",
                       "Telemetry metadata details are not fetched  " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details with empty param elementId
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_empty_elementId(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_elementId"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Successfully fetched the sensor elements data":
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Area : ", response_body["responseData"]["dataList"][0]["areas"][0]["area"])
                print("AreaName : ", response_body["responseData"]["dataList"][0]["areas"][0]["areaName"])
            testResult(self, "passed", "Should fetch the Telemetry metadata details successfully",
                       "Successfully fetched the Telemetry metadata details")
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != "Successfully fetched the sensor elements data":

            testResult(self, "failed", "Should not fetch the Telemetry metadata details ",
                       "Successfully fetched the Telemetry metadata details " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details without param elementId
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_missing_elementId(self):
        print("----------------------------------------------------------")
        testCaseName = "no_elementId"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(1200) and response_body["responseData"][
            "message"] == "Successfully fetched the sensor elements data":
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("ID : ", response_body["responseData"]["dataList"][0]["id"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Name : ", response_body["responseData"]["dataList"][0]["name"])
                print("Unit : ", response_body["responseData"]["dataList"][0]["unit"])
                print("Area : ", response_body["responseData"]["dataList"][0]["areas"][0]["area"])
                print("AreaName : ", response_body["responseData"]["dataList"][0]["areas"][0]["areaName"])
            testResult(self, "passed", "Should fetch the Telemetry metadata details successfully",
                       "Successfully fetched the Telemetry metadata details")
        elif response_body["responseCode"] != str(1200) and response_body["responseData"][
            "message"] != "Successfully fetched the sensor elements data":

            testResult(self, "failed", "Should not fetch the Telemetry metadata details ",
                       "Successfully fetched the Telemetry metadata details " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details with invalid header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "api keys are not matching. Please provide valid key":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details for invalid api-Key",
                       "Telemetry metadata details are not fetched when invalid api-Key is provided")
        elif response_body["message"] != "api keys are not matching. Please provide valid key":

            testResult(self, "failed", "Should fetch the Telemetry metadata details successfully ",
                       "Telemetry metadata details are not fetched" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details with empty header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "api keys are not matching. Please provide valid key":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details for empty header api-Key",
                       "Telemetry metadata details are not fetched when empty header api-Key is provided")
        elif response_body["message"] != "api keys are not matching. Please provide valid key":

            testResult(self, "failed", "Should fetch the Telemetry metadata details successfully ",
                       "Telemetry metadata details are not fetched" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details without header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_missing_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "no_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details without header api-Key",
                       "Telemetry metadata details are not fetched without header api-Key ")
        elif response_body["message"] != "Required authentication headers are missing":

            testResult(self, "failed", "Should fetch the Telemetry metadata details successfully ",
                       "Telemetry metadata details are not fetched" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details with empty header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "x-requestor header cannot be blank":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details for empty header x-requestor",
                       "Telemetry metadata details are not fetched when empty header x-requestor is provided")
        elif response_body["message"] != "x-requestor header cannot be blank":

            testResult(self, "failed", "Should fetch the Telemetry metadata details successfully ",
                       "Telemetry metadata details are not fetched" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry Metadata details without header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_Metadata_missing_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "no_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Telemetry_Metadata_Details")
        if dict1['Flag'] == "Yes":
            elementId = str(dict1["elementId"])
        else:
            elementId = 559940097

        # Call api reusable module
        response = telemetry_metadata_details(self, elementId, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing":

            testResult(self, "passed", "Should not fetch the Telemetry metadata details without header x-requestor",
                       "Telemetry metadata details are not fetched without header x-requestor ")
        elif response_body["message"] != "Required authentication headers are missing":

            testResult(self, "failed", "Should fetch the Telemetry metadata details successfully ",
                       "Telemetry metadata details are not fetched" + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
        print("----------------------------------------------------------")

    # telemetry publisher config with invalid value for param isActive
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_invalid_isActive(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher_invalid_isActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "trueeee"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18008) and response_body["responseData"][
            "message"] == "Invalid isActive. isActive should be either true or false":
            assert True
            testResult(self, "passed", "Telemetry publisher request should not be success",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18008. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # telemetry publisher config with empty value for param isActive
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_empty_isActive(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher_empty_isActive")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = ""

        if isActive == "None":
            isActive = ""

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18008) and response_body["responseData"][
            "message"] == "Invalid isActive. isActive should be either true or false":
            assert True
            testResult(self, "passed", "Telemetry publisher request should not be success when param isActive is empty",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18008. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # telemetry publisher config without param isActive
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_missing_isActive(self):
        print("----------------------------------------------------------")
        testCaseName = "no_isActive"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18008) and response_body["responseData"][
            "message"] == "Invalid isActive. isActive should be either true or false":
            assert True
            testResult(self, "passed", "Telemetry publisher request should not be success without param isActive",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18008. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # telemetry publisher config with invalid value for param eventType
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_invalid_eventType(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher_invalid_eventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3000
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18005) and response_body["responseData"][
            "message"] == "No config data present for this eventType and x-requestor":
            assert True
            testResult(self, "passed", "Telemetry publisher request should not be success",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18005. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # telemetry publisher config without param eventType
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_missing_eventType(self):
        print("----------------------------------------------------------")
        testCaseName = "no_eventType"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18004) and response_body["responseData"][
            "message"] == "Invalid eventType":
            assert True
            testResult(self, "passed", "Telemetry publisher request should not be success without param eventType",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18004. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # telemetry publisher config with invalid header x-requestor
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_invalid_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(18005) and response_body["responseData"][
            "message"] == "No config data present for this eventType and x-requestor":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success for incorrect header x-requestor",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 18005. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

        # telemetry publisher config with invalid header x-requestor

    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(6106) and response_body["responseData"][
            "message"] == "x-requestor header cannot be blank":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success for empty header x-requestor",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 6106. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_missing_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "no_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(6106) and response_body["responseData"][
            "message"] == "Required authentication headers are missing":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success without header x-requestor",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 6106. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # Telemetry publisher with invalid header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(6106) and response_body["responseData"][
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success with invalid header api-key",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 6106. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # Telemetry publisher with empty header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(6106) and response_body["responseData"][
            "message"] == "api keys are not matching. Please provide valid key":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success for empty header api-key",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 6106. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # Telemetry publisher without header api-key
    @pytest.mark.Sanity
    def test1_negative_telemetry_publisher_config_missing_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "no_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "TelemetryPublisher", "TelemetryPublisher")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")

            eventType = str(dict1["eventType"])
            isActive = str(dict1["isActive"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            eventType = 3101
            isActive = "True"

        # Call api reusable module
        response = telemetry_publisher_config(self, eventType, isActive, testCaseName)

        # Validate response status code
        assert (response.status_code == 403), "Status code is not 403. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(6106) and response_body["responseData"][
            "message"] == "Required authentication headers are missing":
            assert True
            testResult(self, "passed",
                       "Telemetry publisher request should not be success without header api-key",
                       "Telemetry publisher request is not success ")

        else:
            print("response Code is not 6106. Rather found : " + str(response_body["responseData"]["message"]))

            testResult(self, "failed", "Telemetry publisher request should be success",
                       "Telemetry publisher request is not success ")

        print("----------------------------------------------------------")

    # SOS-Service with invalid value
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_value(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_value")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 3
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15545) and response_body["responseData"][
            "message"] == "Invalid SoS Status Value":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid value",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15545. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field value
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_value(self):
        print("----------------------------------------------------------")
        testCaseName = "no_value"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15548) and response_body["responseData"][
            "message"] == "SoS Status Value is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field value",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15548. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid area
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_area(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_area")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 3
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15543) and response_body["responseData"][
            "message"] == "Invalid SoS Status Area":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid area",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15543. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field area
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_area(self):
        print("----------------------------------------------------------")
        testCaseName = "no_area"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15549) and response_body["responseData"][
            "message"] == "SoS Status Area is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field Area",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15549. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid id
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_id(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_id")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 55574918
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15546) and response_body["responseData"][
            "message"] == "Invalid SoS Status Id":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid id",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15546. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field Id
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_id(self):
        print("----------------------------------------------------------")
        testCaseName = "no_id"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15547) and response_body["responseData"][
            "message"] == "SoS Status Id is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field Id",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15547. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field Data
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_Data(self):
        print("----------------------------------------------------------")
        testCaseName = "no_data"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15552) and response_body["responseData"][
            "message"] == "SoS telemetry datalist is required in the request body":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field Data",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15552. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid eventType
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_eventType(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_eventType")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 5000
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15538) and response_body["responseData"][
            "message"] == "Event type is not valid":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid eventType",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15538. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field evenType
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_eventType(self):
        print("----------------------------------------------------------")
        testCaseName = "no_eventType"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15550) and response_body["responseData"][
            "message"] == "SoS Event Type is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field eventType",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15550. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid reasonCode
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_reasonCode(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_reasonCode")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 20

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15539) and response_body["responseData"][
            "message"] == "Reason code is not valid":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid reasonCode",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15539. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field reasonCode
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_reasonCode(self):
        print("----------------------------------------------------------")
        testCaseName = "no_reasoncode"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15551) and response_body["responseData"][
            "message"] == "SoS reason code is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field reasonCode",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15551. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field Telemetry
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_Data(self):
        print("----------------------------------------------------------")
        testCaseName = "no_telemetry"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15553) and response_body["responseData"][
            "message"] == "SoS telemetry field is required in the request body":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field Telemetry",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15553. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid vin
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_vin(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310000"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15555) and response_body["responseData"][
            "message"] == "Vin must have length of 17 characters":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid vin",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15555. Rather found : " + str(response_body["responseData"]["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid vin(with special characters
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalidvin_specialCharacters(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalidvin_specialcharacters")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINT001SA1@"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "Special Characters present in fields" and response_body["responseData"][
            "message"] == "null":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid vin",
                       "sos clear action not published successfully")
        else:
            print("Not a valid Response . Rather found : " + str(response_body["responseData"]["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with empty  vin
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_empty_vin(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_empty_vin")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = ""
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21
        if vin == "None":
            vin = ""

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15555) and response_body["responseData"][
            "message"] == "Vin must have length of 17 characters":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully with empty vin",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15555. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without vin
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_vin(self):
        print("----------------------------------------------------------")
        testCaseName = "no_vin"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500311"
            device_id = "INT-QC-IVI-1201301"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15554) and response_body["responseData"][
            "message"] == "Vin is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field vin",
                       "sos clear action not published successfully")
        else:
            print("response Code is not 15554. Rather found : " + str(response_body["responseData"]["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid deviceId
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_deviceId(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_invalid_deviceId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-1@#"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value, event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == "Special Characters present in fields" and response_body["responseData"][
            "message"] == "null":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for invalid deviceId",
                       "sos clear action not published successfully")
        else:
            print("Sos clear action published successfully. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with empty deviceId
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_empty_deviceId(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service_empty_deviceId")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = ""
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21
        if device_id == "None":
            device_id = ""

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15557) and \
                response_body["responseData"][
                    "message"] == "Device id length must be between 3 to 19":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully for empty deviceId",
                       "sos clear action not published successfully")
        else:
            print("Reason code is not 15557. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without deviceId
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_deviceId(self):
        print("----------------------------------------------------------")
        testCaseName = "no_deviceId"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21
        if device_id == "None":
            device_id = ""

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15556) and \
                response_body["responseData"][
                    "message"] == "Device Id is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without deviceId",
                       "sos clear action not published successfully")
        else:
            print("Reason code is not 15556. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field meta
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missingfield_meta(self):
        print("----------------------------------------------------------")
        testCaseName = "no_meta"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15561) and \
                response_body["responseData"][
                    "message"] == "Meta details are required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field meta",
                       "sos clear action not published successfully")
        else:
            print("Reason code is not 15561. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without field time
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missingfield_time(self):
        print("----------------------------------------------------------")
        testCaseName = "no_time"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["responseCode"] == str(15560) and \
                response_body["responseData"][
                    "message"] == "Time field is required":
            assert True
            testResult(self, "passed", "sos clear action should not be published successfully without field time",
                       "sos clear action not published successfully")
        else:
            print("Reason code is not 15560. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with invalid header apiKey
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_invalid_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "invalid_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "api keys are not matching..please provide valid key":
            assert True
            testResult(self, "passed",
                       "sos clear action should not be published successfully for invalid header apiKey",
                       "sos clear action not published successfully")
        else:
            print("Message apiKey not matching not found. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with empty header apiKey
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_empty_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "api keys are not matching..please provide valid key":
            assert True
            testResult(self, "passed",
                       "sos clear action should not be published successfully for empty header apiKey",
                       "sos clear action not published successfully")
        else:
            print("Message apiKey not matching not found. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without header apiKey
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_apiKey(self):
        print("----------------------------------------------------------")
        testCaseName = "no_apiKey"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing..!!!!":
            assert True
            testResult(self, "passed",
                       "sos clear action should not be published successfully for missing header apiKey",
                       "sos clear action not published successfully")
        else:
            print("Message Authentication header missing not found. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service with empty header x-requestor
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_empty_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "empty_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "x-requestor header cannot be blank":
            assert True
            testResult(self, "passed",
                       "sos clear action should not be published successfully for empty header x-requestor",
                       "sos clear action not published successfully")
        else:
            print("Message x-requestor cannot be blank not found. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")

    # SOS-Service without header x-requestor
    @pytest.mark.Sanity
    def test1_negative_Sos_Service_missing_xrequestor(self):
        print("----------------------------------------------------------")
        testCaseName = "no_x-requestor"
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry", "Sos_Service")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            vin = str(dict1["vin"])
            device_id = str(dict1["device_id"])
            system_id = str(dict1["SystemId"])
            sub_system_id = str(dict1["sub_system_id"])
            time = str(dict1["time"])
            elementId = str(dict1["elementId"])
            area = str(dict1["area"])
            value = str(dict1["value"])
            event_type = str(dict1["eventType"])
            reason_code = str(dict1["reason_code"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            vin = "VINQCOMINTV500310"
            device_id = "INT-QC-IVI-12012912"
            system_id = "sysf06ba6a4b5ec11eeba9b00000"
            sub_system_id = "string-001"
            time = 1620891851
            elementId = 555749181
            area = 0
            value = 1
            event_type = 6001
            reason_code = 21

        # Call api reusable module
        response = Sos_Service(self, vin, system_id, device_id, sub_system_id, time, elementId, area, value,
                               event_type,
                               reason_code, testCaseName)

        # Validate response status code
        assert (response.status_code == 400), "Status code is not 400. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        if response_body["message"] == "Required authentication headers are missing..!!!!":
            assert True
            testResult(self, "passed",
                       "sos clear action should not be published successfully for missing header x-requestor",
                       "sos clear action not published successfully")
        else:
            print("Message Authentication header missing not found. Rather found : " + str(response_body["message"]))
            testResult(self, "failed", "sos clear action should not be published successfully",
                       "sos clear action published successfully")

        print("--------------******-------------------")
