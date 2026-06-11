import os
import pytest

from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.telemetry_modules import telemetry_Curr_sensorValues, telemetry_Curr_sensorElements, \
    telemetry_Curr_eventType, telemetry_Curr_byVIN, telemetry_Curr_byVIN_eventType, \
    telemetry_publisher_config, Sos_Service, telemetry_metadata_details
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

CurrentPath = os.path.realpath(__file__)
BaseName = os.path.basename(__file__)
Test_Case_No = BaseName.replace('.py', '')
print(Test_Case_No)

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Telemetry:
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

