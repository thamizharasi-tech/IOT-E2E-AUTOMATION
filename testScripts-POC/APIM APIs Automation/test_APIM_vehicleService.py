import pytest


from C2CModules.e2e_testData import deviceType_IVI, b2c_ivi_chipset
from C2CModules.APIM_ReusableModules import dtc_processDTC,vehicle_service_book_appointment,vehicle_service_get_dealers_available_schedule,vehicle_service_get_dealers_appointments_history,vehicle_service_get_estimate_details
from C2CModules.primary_IVI_device_modules import get_SystemId, getVIN
from C2CModules.testResults import testResult
from utils.XLUtils import read_api_data_from_excel

OnboardingType = deviceType = deviceType_IVI
chipsetType = b2c_ivi_chipset


class Test_smoke:

    # dtc trigger
    @pytest.mark.Smoke
    def test1_positive_dtc_trigger(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC",
                                         "DTC-Trigger")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            subsystemId = str(dict1["subsystemId"])
            deviceId = str(dict1["deviceId"])
            dtcCode = str(dict1["dtcCode"])
            action = str(dict1["action"])
        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            #systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sys741887956cbc11eead65"
            subsystemId = "subCm3hfdH"
            deviceId = "simD_FTBU9JjxsR2edK"
            dtcCode = "P0010"
            action = "trigger"

        print("SystemId: ",systemId)
        print("SubsystemId: ",subsystemId)
        print("DeviceId: ",deviceId)
        print("DTC Code: ",dtcCode)
        print("Action: ",action)

        # Call DTC reusable module
        response = dtc_processDTC(self, dtcCode, systemId, subsystemId, deviceId, action)

        # Parse API response into JSON
        response_body = response.json()
        message = response_body["message"]

        # validate response
        if response.status_code == 200:
            if response_body["message"] == message:
                testResult(self, "passed", "Should trigger DTC message successfully",
                                   "DTC message triggered successfully")
        else:
            testResult(self, "failed", "Should trigger DTC message successfully",
                               "Failed to trigger DTC message" +"\n"+"Reason for failure is : " +
                               response_body["message"] +"\n"+"Status code is not 200.Rather than found: " +str(response.status_code))

        print("----------------------------------------------------------")

   # book appointment
    @pytest.mark.Smoke
    def test2_positive_vehicle_service_book_dealers_appointment(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC",
                                         "vehicle-service-book-dealers-appointment")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            accountId = str(dict1["accountId"])
            territoryId = str(dict1["territoryId"])
            workTypeGroupId = str(dict1["workTypeGroupId"])
            startTime = str(dict1["startTime"])
            endTime = str(dict1["endTime"])
            quoteId = str(dict1["quoteID"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            #systemId = get_SystemId(self, OnboardingType, chipsetType)
            systemId = "sys741887956cbc11eead65"
            accountId = "001RO00000B4Ic9YAF"
            territoryId = "0HhRO00000012sO0AQ"
            workTypeGroupId = "0VSRO000000043N4AQ"
            startTime = 1692277200
            endTime = 1692280800
            quoteId = "mM1N2m74d0MRWUYDIo"

        print("SystemId: ",systemId)
        print("AccountId: ",accountId)
        print("Territory Id: ",territoryId)
        print("WordTypeGroup Id: ",workTypeGroupId)
        print("Start Time: ",startTime)
        print("End Time: ", endTime)
        print("Quote Id: ", quoteId)

        # Call DTC reusable module
        response = vehicle_service_book_appointment(self, systemId, accountId, territoryId, workTypeGroupId, startTime, endTime, quoteId)

        # Parse API response into JSON
        response_body = response.json()
        message = response_body["message"]

        # validate response
        if response.status_code == 200:
            if response_body["responseData"]["serviceAppointmentId"]:
                print("Service Appointment Id: ",response_body["responseData"]["serviceAppointmentId"])
                testResult(self, "passed", "Should book appointment successfully",
                                   "Appointment booked successfully")
        else:
            testResult(self, "failed", "Should book appointment successfully",
                               "Failed to book appointment" +"\n"+ "Reason for failure is : " +
                               response_body["message"] +"\n"+"Status code is not 200.Rather than found: "+ str(response.status_code))

        print("----------------------------------------------------------")

   # get dealers avalable schedule
    @pytest.mark.Smoke
    def test3_positive_vehicle_service_get_dealers_available_schedule(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC",
                                         "vehicle-service-get-dealers-available-schedules")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            accountId = str(dict1["accountId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            accountId = "001RO00000B4Ic9YAF"

        print("AccountId: ",accountId)


        # Call dealers available schedule reusable module
        response = vehicle_service_get_dealers_available_schedule(self, accountId)

        # Parse API response into JSON
        response_body = response.json()

        # validate response
        if response.status_code == 200:
            if response_body["responseData"]["timeSlots"]:
                print("End Time: ",response_body["responseData"]["timeSlots"][0]["endTime"])
                print("Start Time: ", response_body["responseData"]["timeSlots"][0]["startTime"])
                print("Remaining Appointments: ", response_body["responseData"]["timeSlots"][0]["remainingAppointments"])
                print("Territory Id: ", response_body["responseData"]["timeSlots"][0]["territoryId"])
                print("Account Id: ", response_body["responseData"]["timeSlots"][0]["accountId"])
                print("WorkTypeGroup Id: ", response_body["responseData"]["timeSlots"][0]["workTypeGroupId"])
                testResult(self, "passed", "Should fetch dealers available timeslots successfully",
                                   "Dealers available timeslots fetched successfully")
        else:
            testResult(self, "failed", "Should fetch dealers available timeslots successfully",
                               "Failed to fetch dealers available timeslots" + " Reason for failure is : " +
                               response_body["message"] + response.status_code)

        print("----------------------------------------------------------")

   # get dealers appointment history
    @pytest.mark.Smoke
    def test4_positive_vehicle_service_get_dealers_appointment_history(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC",
                                         "vehicle-service-get-dealers-appointment-history")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys1fd9cece6cf111eead65"

        print("SystemId: ",systemId)


        # Call dealers available schedule reusable module
        response = vehicle_service_get_dealers_appointments_history(self, systemId)

        # Parse API response into JSON
        response_body = response.json()

        # validate response
        if response.status_code == 200:
            if response_body["responseData"]["serviceAppointments"]:
                print("Service Appointments: ",response_body["responseData"]["serviceAppointments"])
                print("Upcoming Appointments: ", response_body["responseData"]["upcomingAppointments"])
                print("History Appointments: ", response_body["responseData"]["historyAppointments"])
                testResult(self, "passed", "Should fetch dealers appointment history successfully",
                                   "Dealers appointment history fetched successfully")
        else:
            testResult(self, "failed", "Should fetch dealers appointment history successfully",
                               "Failed to fetch dealers appointment history" +"\n"+"Reason for failure is : " +
                               response_body["message"] +"\n" +"Status Code is not 200.Rather than found: "+str(response.status_code))

        print("----------------------------------------------------------")

   # get service estimate details
    @pytest.mark.Smoke
    def test5_positive_vehicle_service_get_service_estimate_details(self):
        print("----------------------------------------------------------")
        # Read api test data resp from excel sheet
        dict1 = read_api_data_from_excel(self, "DTC",
                                         "vehicle-service-get-estimate-details")
        if dict1['Flag'] == "Yes":
            print("Flag is set to Yes, hence running with excel data :")
            systemId = str(dict1["systemId"])
            quoteId = str(dict1["quoteID"])

        else:
            print("Flag is not set to Yes, hence running with generic/actual device data")
            systemId = "sys1fd9cece6cf111eead65"
            quoteId = "mM1N2m74d0MRWUYDIo"

        print("SystemId: ",systemId)
        print("Quote ID: ",quoteId)

        # Call dealers available schedule reusable module
        response = vehicle_service_get_estimate_details(self,systemId,quoteId)

        # Parse API response into JSON
        response_body = response.json()

        # validate response
        if response.status_code == 200:
            if response_body["message"] == "Success":
                print("Service Parts Name: ",response_body["responseData"]["items"][0]["name"])
                print("Code: ", response_body["responseData"]["items"][0]["code"])
                print("Cost of the Part: ", response_body["responseData"]["items"][0]["costs"][0]["amount"])
                print("Labour Cost: ", response_body["responseData"]["items"][0]["costs"][1]["amount"])
                print("Tax: ", response_body["responseData"]["items"][0]["costs"][2]["amount"])
                print("Total Amount of the Parts: ", response_body["responseData"]["costs"][0]["amount"])
                print("Total Labour Cost: ", response_body["responseData"]["costs"][1]["amount"])
                print("Total Tax Amount: ", response_body["responseData"]["costs"][2]["amount"])
                print("Estimated Time: ", response_body["responseData"]["estimatedTime"])
                print("Estimated Cost: ", response_body["responseData"]["estimatedCost"])
                print("Account Id: ", response_body["responseData"]["accountId"])
                testResult(self, "passed", "Should fetch the service estimation details successfully",
                                   "Service Estimation details fetched successfully")
        else:
            testResult(self, "failed", "Should fetch the service estimation details successfully",
                               "Failed to fetch service estimation details" +"\n"+"Reason for failure is : " +
                               response_body["message"] +"\n" +"Status Code is not 200.Rather than found: "+str(response.status_code))

        print("----------------------------------------------------------")