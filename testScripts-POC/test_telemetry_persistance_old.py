import os
from datetime import datetime, timezone

import pytest
import requests
import json

from C2CModules.e2e_testData import telemetry_fuel_level_event_type, testData, deviceType_IVI, b2c_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.resuse_modules import save_api_resp_into_file
from C2CModules.telemetry_modules import telemetry_Curr_sensorValues, telemetry_Curr_sensorElements
from C2CModules.telemetry_persistance_old import Telemetry_Persistence
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

CurrentPath = os.path.realpath(__file__)
BaseName = os.path.basename(__file__)
Test_Case_No = BaseName.replace('.py', '')
print(Test_Case_No)

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_Smoke:

    # telemetry_curr
    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_SoS(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 6001
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >=1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_Sidestand(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3106
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >=1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")
    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_Speed(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 4001
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_batteryLevel(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 1001
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_Fuellevel(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3250
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @ pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_fuelLevel_low(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3251
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_odometer(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 2005
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_GPS(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test1_positive_telmetry_persistance_for_event_Ignition(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = str(dict1["eventType"])
            start = str(dict1["start"])
            stop = str(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 2003
            startDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop)

        if response_body["responseCode"] == str(15500) or response_body["responseCode"] == 15500:
            message = response_body["responseData"]["message"]
            print('Message : ', message)
            if len(response_body["responseData"]["dataList"]) >= 1:
                print("SystemId : ", response_body["responseData"]["dataList"][0]["systemId"])
                print("Event Type : ", response_body["responseData"]["dataList"][0]["eventType"])
                print("Time : ", response_body["responseData"]["dataList"][0]["time"])
                print("VIN : ", response_body["responseData"]["dataList"][0]["vin"])
                print("Reason Code : ", response_body["responseData"]["dataList"][0]["reasonCode"])

                print("Vin : ", response_body["responseData"]["dataList"][0]["meta"]["vin"])
                print("Device Id : ", response_body["responseData"]["dataList"][0]["meta"]["device_id"])
                print("System Id : ", response_body["responseData"]["dataList"][0]["meta"]["system_id"])

                print("ID : ", response_body["responseData"]["dataList"][0]["data"][0]["id"])
                print("Name : ", response_body["responseData"]["dataList"][0]["data"][0]["name"])
                print("Area : ", response_body["responseData"]["dataList"][0]["data"][0]["area"])
                print("Area Name : ", response_body["responseData"]["dataList"][0]["data"][0]["area_name"])
                print("Value : ", response_body["responseData"]["dataList"][0]["data"][0]["value"])
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "Successfully fetched the values/data for desired event type ")
            else:
                print(" => datalist is empty")
                testResult(self, "passed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

    print("----------------------------------------------------------")