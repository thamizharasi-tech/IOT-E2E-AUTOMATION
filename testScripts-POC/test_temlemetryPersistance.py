import pytest
from datetime import datetime, timezone

from C2CModules.api_modules import verify_api_response
from C2CModules.e2e_testData import deviceType_IVI, drimaes_ivi_chipset
from C2CModules.primary_IVI_device_modules import get_SystemId
from C2CModules.telemetry_persistance import Telemetry_Persistence
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel
from C2CModules.primary_IVI_device_modules import getVIN

OnboardingType = deviceType = deviceType_IVI
chipsetType = drimaes_ivi_chipset


class Test_telemetryPersistence:

    # Telemetry persistance API to fetch history details
    @pytest.mark.Smoke
    def test1_positive_telemetry_persistance_history(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)

        # Parse API response into JSON
        response_body = response.json()

        # Validate response body

        assert response_body["responseCode"] == 15500
        dataList_len = len(response_body["responseData"]["dataList"])
        if dataList_len <= 0:
            print("No data available/There is no datas in database for given inputs")
        else:
            print("Telemetry datas fetched successfully")

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test2_positive_telemetry_persistance_for_event_SoS(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test3_positive_telemetry_persistance_for_event_Sidestand(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test4_positive_telmetry_persistance_for_event_Speed(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test5_positive_telmetry_persistance_for_event_batteryLevel(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test6_positive_telmetry_persistance_for_event_Fuellevel(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test7_positive_telmetry_persistance_for_event_fuelLevel_low(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test8_positive_telmetry_persistance_for_event_odometer(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test9_positive_telmetry_persistance_for_event_GPS(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
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
    def test10_positive_telmetry_persistance_for_event_Ignition(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response_body = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "valid")

        # Parse API response into JSON
        response_body = response_body.json()

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
                testResult(self, "verificationFailed", "Should fetch the data/values for event type successfully",
                           "End point is working fine, but there is no data in DB for this event type, thus marking test case as pass")
        elif response_body["responseCode"] != 15500:
            # print(response_body["responseData"]["message"])
            testResult(self, "failed", "Should fetch the data/values for event type successfully ",
                       "Failed to fetch the data/values " + " Reason for failure is : " +
                       response_body["responseData"]["message"])
        else:
            print("Something went wrong")

        print("----------------------------------------------------------")

    # ---------------------------------------------------------------------------------
    # Telemetry-Persistence : Negative header validations
    # ---------------------------------------------------------------------------------
    # invalid apikey
    @pytest.mark.Smoke
    def test1_negative_telemetry_persistance_history_invalidapikey(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")

        print("----------------------------------------------------------")

    # empty apikey
    @pytest.mark.Smoke
    def test2_negative_telemetry_persistance_history_emptyapikey(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    # no apikey
    @pytest.mark.Smoke
    def test3_negative_telemetry_persistance_history_noapikey(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    # empty x-requestor
    @pytest.mark.Smoke
    def test4_negative_telemetry_persistance_history_emptyxrequestor(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")

        print("----------------------------------------------------------")

    # no x-requestor
    @pytest.mark.Smoke
    def test5_negative_telemetry_persistance_history_noxrequestor(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")

        print("----------------------------------------------------------")

    # -----------------------------------------------------------------------------------------
    # Telemetry Persistance : Negative-Testdata validations
    # -----------------------------------------------------------------------------------------
    # invalid systemId
    @pytest.mark.Smoke
    def test6_negative_telemetry_persistance_history_invalidsystemId(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_invalidSystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys123"
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_systemId")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # empty systemId
    @pytest.mark.Smoke
    def test7_negative_telemetry_persistance_history_emptysystemId(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_emptySystemId")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            if systemId == "None":
                systemId = ""
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_systemId")
        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15545)
        assert (response_body["responseData"]["message"] == "Missing system Id from request")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # no systemId
    @pytest.mark.Smoke
    def test8_negative_telemetry_persistance_history_nosystemId(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = ""
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_systemId")
        # Validate response status code
        assert (response.status_code == 202), "Status code is not 202. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15545)
        assert (response_body["responseData"]["message"] == "Missing system Id from request")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # invalid vin
    @pytest.mark.Smoke
    def test9_negative_telemetry_persistance_history_invalidvin(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_invalidVin")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = "vin123"
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_vin")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # empty vin
    @pytest.mark.Smoke
    def test10_negative_telemetry_persistance_history_emptyVin(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_emptyVin")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            if vin == "None":
                vin = ""
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = " "
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_vin")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15545 or response_body["responseCode"] == 15500)
        if response_body["responseCode"] == 15545:
            assert (response_body["responseData"]["message"] == "Missing vin from request")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # no vin
    @pytest.mark.Smoke
    def test11_negative_telemetry_persistance_history_noVin(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = " "
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_vin")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0, "There is no data in database for given filter"

        print("----------------------------------------------------------")

    # invalid eventType
    @pytest.mark.Smoke
    def test12_negative_telemetry_persistance_history_invalidEventType(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_invalidEventType")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = dict1["eventType"]
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 31019023
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_eventType")
        # Validate response status code
        assert (response.status_code == 400 or response.status_code == 200), "Status code is not 400 or 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response.status_code == 200:
            assert (response_body["responseCode"] == 15500)
            assert (response_body["responseData"]["message"] == "No data available")
            assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # empty eventType
    @pytest.mark.Smoke
    def test13_negative_telemetry_persistance_history_emptyeventType(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_emptyEventType")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = dict1["eventType"]
            if eventType == "None":
                eventType = ""
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = ""
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_eventType")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # no eventType
    @pytest.mark.Smoke
    def test14_negative_telemetry_persistance_history_noEventType(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_eventType")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # invalid start
    @pytest.mark.Smoke
    def test15_negative_telemetry_persistance_history_invalidStart(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_invalidStart")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = dict1["start"]
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = "01234567845"
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_start")
        # Validate response status code
        assert (response.status_code == 400 or response.status_code == 200 ), "Status code is not 200 or 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response.status_code == 200:
            assert (response_body["responseCode"] == 15500)
            assert (response_body["responseData"]["message"] == "No data available")
            assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # empty start
    @pytest.mark.Smoke
    def test16_negative_telemetry_persistance_history_emptyStart(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_emptyStart")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = dict1["start"]
            if start == "None":
                start = ""
            stop = int(dict1["stop"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = ""
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_start")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        if response_body["responseData"]["message"] == "SUCCESS":
            print("Data fetched successfully for Start = None, this is expected behaviour as per design")
        else:
            assert (response_body["responseData"]["message"] == "No data available")
            assert len(response_body["responseData"]["dataList"]) == 0
        print("----------------------------------------------------------")

    # no start
    @pytest.mark.Smoke
    def test17_negative_telemetry_persistance_history_noStart(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_start")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # invalid stop
    @pytest.mark.Smoke
    def test18_negative_telemetry_persistance_history_invalidstop(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_invalidStop")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = dict1["stop"]


        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = "27312783672"
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_stop")
        # Validate response status code
        assert (response.status_code == 200 or response.status_code == 400), "Status code is not 200 or 400. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        if response.status_code == 200:
            assert (response_body["responseCode"] == 15500)
            assert (response_body["responseData"]["message"] == "No data available")
            assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")

    # empty stop
    @pytest.mark.Smoke
    def test19_negative_telemetry_persistance_history_emptyStop(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history_emptyStop")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = dict1["stop"]
            if stop == "None":
                stop = ""
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = ""
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_stop")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        if response_body["responseData"]["message"] == "SUCCESS":
            print("Data fetched successfully for Stop = None, this is expected behaviour as per design")
        else:
            assert (response_body["responseData"]["message"] == "No data available")
            assert len(response_body["responseData"]["dataList"]) == 0
        print("----------------------------------------------------------")

    # no stop
    @pytest.mark.Smoke
    def test20_negative_telemetry_persistance_history_noStop(self):
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_history")

        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            vin = str(dict1["vin"])
            eventType = int(dict1["eventType"])
            start = int(dict1["start"])
            stop = int(dict1["stop"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = get_SystemId(self, OnboardingType, chipsetType)
            vin = getVIN(self, OnboardingType, chipsetType)
            eventType = 3101
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # call vehicle service reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_stop")
        # Validate response status code
        assert (response.status_code == 200), "Status code is not 200. Rather found : " + str(
            response.status_code)
        # Parse API response into JSON
        response_body = response.json()
        assert (response_body["responseCode"] == 15500)
        assert (response_body["responseData"]["message"] == "No data available")
        assert len(response_body["responseData"]["dataList"]) == 0

        print("----------------------------------------------------------")



    @pytest.mark.Smoke
    def test21_negative_telmetry_persistance_for_event_Sidestand_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test22_negative_telmetry_persistance_for_event_Sidestand_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test23_negative_telmetry_persistance_for_event_Sidestand_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test24_negative_telmetry_persistance_for_event_Sidestand_empty_Xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test25_negative_telmetry_persistance_for_event_Sidestand_without_Xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_sidestand")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test26_positive_telmetry_persistance_for_event_Speed_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test27_positive_telmetry_persistance_for_event_Speed_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test28_positive_telmetry_persistance_for_event_Speed_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test29_positive_telmetry_persistance_for_event_Speed_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test30_positive_telmetry_persistance_for_event_Speed_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_speed")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test31_positive_telmetry_persistance_for_event_batteryLevel_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test32_positive_telmetry_persistance_for_event_batteryLevel_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test33_positive_telmetry_persistance_for_event_batteryLevel_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test34_positive_telmetry_persistance_for_event_batteryLevel_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test35_positive_telmetry_persistance_for_event_batteryLevel_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence",
                                         "TelemetryPersistence_for_event_batteryLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test36_positive_telmetry_persistance_for_event_Fuellevel_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test37_positive_telmetry_persistance_for_event_Fuellevel_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test38_positive_telmetry_persistance_for_event_Fuellevel_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test39_positive_telmetry_persistance_for_event_Fuellevel_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test40_positive_telmetry_persistance_for_event_Fuellevel_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_fuelLevel")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test41_positive_telmetry_persistance_for_event_fuelLevel_low_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test42_positive_telmetry_persistance_for_event_fuelLevel_low_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test43_positive_telmetry_persistance_for_event_fuelLevel_low_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test44_positive_telmetry_persistance_for_event_fuelLevel_low_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test45_positive_telmetry_persistance_for_event_fuelLevel_low_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_event_fuelLevel_low")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test46_positive_telmetry_persistance_for_event_odometer_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test47_positive_telmetry_persistance_for_event_odometer_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test48_positive_telmetry_persistance_for_event_odometer_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test49_positive_telmetry_persistance_for_event_odometer_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test50_positive_telmetry_persistance_for_event_odometer_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_odometer")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")


    @pytest.mark.Smoke
    def test51_positive_telmetry_persistance_for_event_GPS_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test52_positive_telmetry_persistance_for_event_GPS_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test53_positive_telmetry_persistance_for_event_GPS_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test54_positive_telmetry_persistance_for_event_GPS_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test55_positive_telmetry_persistance_for_event_GPS_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_GPS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test56_positive_telmetry_persistance_for_event_Ignition_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test57_positive_telmetry_persistance_for_event_Ignition_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test58_positive_telmetry_persistance_for_event_Ignition_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test59_positive_telmetry_persistance_for_event_Ignition_empty_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test60_positive_telmetry_persistance_for_event_Ignition_no_xRequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_Ignition")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")
        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test61_positive_telmetry_persistance_for_event_SoS_invalid_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "invalid_apiKey")

        # Verify api response
        verify_api_response(response, "invalid_apiKey")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test62_positive_telmetry_persistance_for_event_SoS_empty_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_apiKey")

        # Verify api response
        verify_api_response(response, "empty_apiKey")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test63_positive_telmetry_persistance_for_event_SoS_no_apiKey(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_apiKey")

        # Verify api response
        verify_api_response(response, "no_apiKey")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test64_positive_telmetry_persistance_for_event_SoS_empty_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "empty_x-requestor")

        # Verify api response
        verify_api_response(response, "empty_x-requestor")

        print("----------------------------------------------------------")

    @pytest.mark.Smoke
    def test65_positive_telmetry_persistance_for_event_SoS_no_xrequestor(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "Telemetry_Persistence", "TelemetryPersistence_for_event_SoS")
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
            startDate = int(0)
            print("Start Date : ", startDate)
            endDate = int(datetime.now(tz=timezone.utc).timestamp()) * 1000 + 100000000
            print("End Date : ", endDate)
            start = startDate
            stop = endDate

        # Call api reusable module
        response = Telemetry_Persistence(self, systemId, vin, eventType, start, stop, "no_x-requestor")

        # Verify api response
        verify_api_response(response, "no_x-requestor")

        print("----------------------------------------------------------")
